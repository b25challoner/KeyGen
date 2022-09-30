#Brayden Challoner
import random
import string

print(
  "WARNING FOR BEST USE:\nOnly use this program without internet access, and store \nthese keys on a local encrypted password manager!"
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
  print(password + "\n")
  count = count + 1
