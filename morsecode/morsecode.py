from international import Morsecode

morsecode_data = Morsecode()
morse = morsecode_data.codes()

keep_going = True
answer_list = []
while keep_going:
    english_words = input('Type some words that you want to translate to morse code, please.').upper()
    # print(type(english_words))
    for word in english_words:
        # print(morse)
        code = morse[word] # list
        code_string = ''.join(code) # string
        answer_list.append(code_string) # list
        keep_going = False
    # print(answer_list)
    answer_string = ' '.join(answer_list) #string
print(f'{english_words} is to be "{answer_string}"')