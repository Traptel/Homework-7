import random

# Завдання 1
print("Завдання 1")
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

# Завдання 2
print("\nЗавдання 2")
dictionary_random = {f"num_{i}": random.randint(1, 10) for i in range(1, 21)}

result = 1
for value in dictionary_random.values():
    result *= value

print("Результат множення чисел:", result)
print(dictionary_random)

# Завдання 3
print("\nЗавдання 3")
dictionary_cube = {i: i**3 for i in range(1, 11)}
print(dictionary_cube)

# Завдання 4
print("\nЗавдання 4")
list_1 = ["A", "B", "C", "D", "E"]
list_2 = ["12", "34", "56", "78", "90"]

result_dict = {list_1[i]: list_2[i] for i in range(len(list_1))}
print(result_dict)

# Завдання 5
print("\nЗавдання 5")
text = "Python is good language to learn and in same time we like to tell that it is cool expereance for us"

letter_number = {}
for letter in text:
    if letter.isalpha():
        letter = letter.lower()
        letter_number[letter] = letter_number.get(letter, 0) + 1

print(letter_number)

# Завдання 6
print("\nЗавдання 6")
text = """
Любіть Україну , як сонце , любіть ,
як вітер , і трави , і води …
В годину щасливу і в радості мить ,
любіть у годину негоди .
Любіть Україну у сні й наяву ,
вишневу свою Україну ,
красу її , вічно живу і нову ,
і мову її солов’їну . 
Між братніх народів , мов садом рясним ,
сіяє вона над віками …
Любіть Україну всім серцем своїм
і всіми своїми ділами .
Для нас вона в світі єдина , одна
в просторів солодкому чарі …
Вона у зірках , і у вербах вона ,
і в кожному серця ударі ,
у квітці, в пташині , в електровогнях,
у пісні у кожній , у думі ,
в дитячий усмішці , в дівочих очах
і в стягів багряному шумі …
"""
punctuation = ['.', ',', '"', '“', '”', '…', '!',  '—' ';' ':']
for sing in punctuation:
    text = text.replace(sing, '')

text_l = text.lower()
text_lst = text_l.split()

dct = {}
for word in text_lst:
    dct.setdefault(word, 0)
    dct[word] += 1

print(dct)
most_word = None
least_word = None

for word, count in dct.items():
    if most_word is None or count > dct[most_word]:
        most_word = word
    if least_word is None or count < dct[least_word]:
        least_word = word

print(f"Найбільше зустрічається слово: {most_word} ({dct[most_word]} разів)")
print(f"Найменше зустрічається слово: {least_word} ({dct[least_word]} разів)")
