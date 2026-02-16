import pandas as pd
import numpy as np

def encode_seq(seq):


def main():
    df_names = pd.read_csv("names_dataset.csv",
                           index_col=False,
                           encoding='utf-8')

    # number of possible valid sequences of two letters - 31 * 30 + 1 (including '.')
    trigram_matrix_male = np.zeros(shape=(31 * 30 + 1, 31))
    trigram_matrix_female = np.zeros(shape=(31 * 30 + 1, 31))

    for name, gender in zip(df_names["name"], df_names["gender"]):
        if gender == 'M':
            matrix = trigram_matrix_male
        elif gender == 'F':
            matrix = trigram_matrix_female

        first_char_code = ord(name[i]) - ord('а') + 1
        matrix[0, first_char_code] = matrix[0, first_char_code] + 1
        
        for i in range(len(name) - 1):
            seq_row = encode_seq(name, i)
    return


if __name__ == "__main__":
    main()
