from distutils import text_file

with open('./text_file/Input/Letters/starting_letter.txt') as letter:
    contents = letter.read()

with open('./text_file/Input/Names/invited_names.txt') as names:
    name = names.read().split('\n')
    names_list = []
    names_list.append(name)
    # print(names_list[0])
    names.close()

for invited_person in names_list[0]:
    with open(f'./text_file/Output/ReadyToSend/to_{invited_person}.txt', mode = 'w') as new_letter:
        new_letter.write(contents.replace('[name]', invited_person))

