#Data science bootcamp -- section 1 hw -- 2/27/2024

# 1. Write a function  count_vowels(word) that takes a
# word as an argument and returns the number of vowels in the word
def count_vowels(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for chara in word:
        if chara in vowels:
            count += 1
    return count

#alt solution to question 1 with list comprehension if can't use .count()
def count_vowels_altsol(word):
    count = len(list(chara for chara in word if chara in "AaEeIiOoUu"))
    return count


# 2. Iterate through the following list of animals and print each one in all caps.
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
animals_cap = [ele.upper() for ele in animals]
print(animals_cap)


# 3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
for i in range(1,21):
    if i%2 != 0:
        print(str(i)+' odd')
    else:
        print(str(i)+' even')


# 4. Write a function sum_of_integers(a, b) that takes two integers as input from the user
# and returns their sum.
def add_ints():
    a = input('type your first integer \n')
    b = input('type your second integer \n')
    sum = int(a) + int(b)
    return sum

print(add_ints())
