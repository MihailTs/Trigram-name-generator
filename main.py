import pandas as pd
import numpy as np
import random
import model_training as mt

NAME_LIMIT = 20
GENERATED_COUNT = 10

def main():
    name = ''

    trigram_matrix_male = np.load("trigram_male.npy")
    trigram_matrix_female = np.load("trigram_female.npy")

    gender = input("Gender of for name generation (M/F): ")

    for k in range(GENERATED_COUNT):
        name = ''

        first_in_seq = '.'
        second_in_seq = '.'
        for i in range(NAME_LIMIT):
            rnd = random.random()
            seq_code = mt.encode_seq(first_in_seq, second_in_seq)
            curr_sum = 0

            # just male for now
            if gender == 'M':
                matrix = trigram_matrix_male
            elif gender == 'F':
                matrix = trigram_matrix_female
            else:
                print("Invalid gender format")
                return
            
            for j in range(matrix.shape[1]):
                curr_sum += matrix[seq_code, j]
                if rnd <= curr_sum:
                    first_in_seq = second_in_seq
                    second_in_seq = [key for key, val in mt.BULGARIAN_ALPHABET_DICT.items() if val == j][0]
                    break
            
            if second_in_seq == mt.EOS:
                break
            name += second_in_seq.upper() if i == 0 else second_in_seq
        print(name)


if __name__ == "__main__":
    main()