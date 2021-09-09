dict_alpha = {"A":2, "B":1, "C":3, "D":7,"E":7, "F":0, "G":6, "H":4, "I":3, "J":5, "K":7, "L":5, "M":0, "N":9, "O":1, "P":6, "Q":1, "R":4, "S":6, "T":6, "U":8, "V":5, "W":4, "X":2, "Y":8, "Z":2}

password = input("Input a password: ").upper()
number_pass = ""
for letter in password:
    number_pass += str(dict_alpha.get(letter))

print(number_pass)
