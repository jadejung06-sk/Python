# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import os


data = pandas.read_csv("./NATO/NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
## method 1
# keep_going = True
# while keep_going:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print(f"Sorry, only letters in the alphabet please.")
#     else:
#         print(output_list)
#         keep_going = False

## method 2
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print(f"Sorry, only letters in the alphabet please.")
        generate_phonetic() # ★
    else:
        print(output_list)

generate_phonetic()
