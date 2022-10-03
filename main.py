#Brayden Challoner
import random
import string

print(
  "Optional:\n - Use this tool offline\n - Store the keys encrypted"
)
length = int(input('\nKey Length: '))
amount = int(input('\nNumber of Keys: '))
print("")
count = 1
while count <= amount:
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  num = string.digits
  symbols = string.punctuation
  all = lower + upper + num + symbols
  temp = random.sample(all, length)
  password = "".join(temp)
  print(password)
  count = count + 1