import random
import string

print("Hello,welcome to password generator!")


length = int(input("\nEnter the length of password: "))

lower = string.ascii_lowercase

upper = string.ascii_uppercase

print(lower)
print(upper)

num = string.digits
Symbols = string.punctuation
print(lower)
print(Symbols)

all = lower + upper + num + Symbols

temp = random.sample(all,length)
password = "".join(temp)
print(password)