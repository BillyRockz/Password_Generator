import random

x = random.randint(0,9)
dict_alpha = ["A", random.randint(0,9), "B", random.randint(0,9), "C", random.randint(0,9), "D", random.randint(0,9), "E", random.randint(0,9), "F", random.randint(0,9), "G", random.randint(0,9), "H", random.randint(0,9), "I", random.randint(0,9), "J", random.randint(0,9), "K", random.randint(0,9), "L", random.randint(0,9), "M", random.randint(0,9), "N",
              random.randint(0,9), "O", random.randint(0,9), "P", random.randint(0,9), "Q", random.randint(0,9), "R", random.randint(0,9), "S", random.randint(0,9), "T", random.randint(0,9), "U", random.randint(0,9), "V", random.randint(0,9), "W", random.randint(0,9), "X", random.randint(0,9), "Y", random.randint(0,9), "Z", random.randint(0,9)]

password = input("Input a password: ").upper()
number_pass = []
for letter in password:
    for i in range(0, len(dict_alpha)):
        if letter == dict_alpha[i]:
            number_pass.append(dict_alpha[i+1])

print(number_pass)

for number in number_pass:
 lista = []
 for i in range(0, len(dict_alpha)):
  if number == dict_alpha[i]:
      lista.append(dict_alpha[i-1])

 print(lista)


print(f"Random values are: \n "
       f"{dict_alpha}")
