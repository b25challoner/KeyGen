# Brayden Challoner

# Created: Fri, Sep 30, 2022

# Teacher: Mr. Heid

# Hour: 1

# This program generates random strings or "keys", and outputs them to the console or a text file that will be created or overwritten within the same directory as "main.py". Each key outputted will be seperated via a new line. These keys can be used as passwords or really anything, but cannot used as encryption/decryption keys that are 128-bit or above, as the modules limit the length of the newly created keys


# Imports the modules required for the program
import random
import string

# To the console, this writes the optional steps to take
print("Optional:\n - Use this tool offline\n - Store the keys encrypted")

# Makes the user input the length of each key
length = int(input('\nKey Length (Max 94): '))

# Makes the user input the number of keys
amount = int(input('\nNumber of Keys: '))

# To the console, this writes a new line to correct current formatting mistakes
print("")

# Resets the count variable
count = 1

# 1 Creates or overwites a text file, 2 repeats the script until the "amount" value reached, 3 defines the variables; "lower,upper,num,symbols,all,temp,key" to determine the used characters and to scramble them, 4 to the text file "keys.txt", each individual key gets written, 5 adds "1" value to the count variable
with open("keys.txt", "w") as f:
  while count <= amount:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all, length)
    key = "".join(temp)
    print(key, file=f)
    count = count + 1

# Opens the "keys.txt" in read only mode
f = open('keys.txt', 'r')

# Defines the "file_contents" variable to read it
file_contents = f.read()

# Prints all of the read contents of the file
print(file_contents)

# Closes "keys.txt"
f.close()

# To the console, this writes an announcement saying that the generated keys have been saved to "keys.txt"
print('Generated keys saved to "keys.txt"')