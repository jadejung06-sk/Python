#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd
letter_data = pd.read_csv('./NATO/NATO-alphabet-start/nato_phonetic_alphabet.csv')
phonetic_words = {row.letter : row.code for index, row in letter_data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print([phonetic_words[word] for word in input("what's your name?").upper()])
