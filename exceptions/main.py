
age: int
name: str
height: float
is_humna: bool
def police_check(age: int):
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check():
    print("You may pass.")
else:
    print("Pay a fine.")



### keyword
# try
# except
# else
# finally
# raise

## FileNotFoundError
# try:
#     file = open("./exceptions/a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["safefe"])
# except FileNotFoundError:
#     file = open("./exceptions/a_file.txt", "w") # ★
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.") # ★ KeyError: 'safefe'
# else: # ★
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")
    # file.close()
    # print("file was closed.")

## KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes'] # ★
#     except KeyError:
#         total_likes += 0
#         # pass
# print(total_likes)



## IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# try:
#     fruit = fruit_list[2]
# except IndexError:
#     print("Fruit pie")
# else:
#     print(fruit + " pie")

## TypeError
# text = "abc"
# print(text + 5)

## ValueError
# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3: 
    # raise ValueError("Human Height should not be over 3 meters")
# bmi = weight / height ** 2
# print(bmi)
