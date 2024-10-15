import string


let = input("Write letters: ")

first_let = let[0]
end_let = let[-1]

letters = string.ascii_letters

start = letters.index(first_let)
end = letters.index(end_let)

result = letters[start:end + 1]

print(result)


