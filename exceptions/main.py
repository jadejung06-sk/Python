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

## IndexError
fruit_list = ["Apple", "Banana", "Pear"]
try:
    fruit = fruit_list[2]
except IndexError:
    print("Fruit pie")
else:
    print(fruit + " pie")

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
