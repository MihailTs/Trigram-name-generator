import pandas as pd
import numpy as np

EOS = '.'
CYRILIC_FIRST = 'а'
ALPHABET_LENGTH = 30
BULGARIAN_ALPHABET_DICT = {
    'а': 0,
    'б': 1,
    'в': 2,
    'г': 3,
    'д': 4,
    'е': 5,
    'ж': 6,
    'з': 7,
    'и': 8,
    'й': 9,
    'к': 10,
    'л': 11,
    'м': 12,
    'н': 13,
    'о': 14,
    'п': 15,
    'р': 16,
    'с': 17,
    'т': 18,
    'у': 19,
    'ф': 20,
    'х': 21,
    'ч': 22,
    'ц': 23,
    'ш': 24,
    'щ': 25,
    'ъ': 26,
    'ь': 27,
    'ю': 28,
    'я': 29,
    '.': 30
}

def encode_seq(first, second):
    first_code = BULGARIAN_ALPHABET_DICT[first]
    second_code = BULGARIAN_ALPHABET_DICT[second]

    return first_code * 30 + second_code

def main():
    df_names = pd.read_csv("names_dataset.csv",
                           index_col=False,
                           encoding='utf-8')

    # number of possible valid sequences of two letters - 31 * 30 + 1 (including '.')
    trigram_matrix_male = np.zeros(shape=(31 * 30 + 1, 31))
    trigram_matrix_female = np.zeros(shape=(31 * 30 + 1, 31))

    for name, gender in zip(df_names["name"], df_names["gender"]):
        name = name.lower()

        if gender == 'M':
            matrix = trigram_matrix_male
        elif gender == 'F':
            matrix = trigram_matrix_female
        else:
            continue

        # tackling the cases for the initial token '.'
        first_char_code = BULGARIAN_ALPHABET_DICT[name[0]]
        matrix[encode_seq('.', '.'), first_char_code] += 1

        first_in_seq = EOS
        second_in_seq = name[0]

        for i in range(1, len(name)):
            seq_row = encode_seq(first_in_seq, second_in_seq)
            next_char_code = BULGARIAN_ALPHABET_DICT[name[i]]
            matrix[seq_row, next_char_code] += 1

            first_in_seq = second_in_seq
            second_in_seq = name[i]

        seq_row = encode_seq(first_in_seq, second_in_seq)
        matrix[seq_row, BULGARIAN_ALPHABET_DICT[EOS]] += 1

    row_sums = trigram_matrix_female.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    trigram_matrix_female = trigram_matrix_female / row_sums

    row_sums = trigram_matrix_male.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    trigram_matrix_male = trigram_matrix_male / row_sums

    np.save("trigram_male.npy", trigram_matrix_male)
    np.save("trigram_female.npy", trigram_matrix_female)


if __name__ == "__main__":
    main()
