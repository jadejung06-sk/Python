# import os
# print(os.getcwd())

### read
with open('./text_file/my_file.txt', mode = 'r') as file:
    contents = file.read()
    print(contents)
file.close() # resource ★

### write
with open('./text_file/my_file.txt', mode = 'w') as file:
    file.write("\nNew text.")

file.close() # resource ★


### append
with open('./text_file/new_file.txt', mode = 'a') as file:
    file.write("\nNew text.")

file.close() # resource ★