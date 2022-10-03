#Brayden Challoner
import random
import string

print("Optional:\n - Use this tool offline\n - Store the keys encrypted")
length = int(input('\nKey Length: '))
amount = int(input('\nNumber of Keys: '))
print("")
count = 1
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
f = open('keys.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
print('Generated keys saved to "keys.txt"')