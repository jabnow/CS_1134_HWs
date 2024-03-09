"""
CS1134 LAB 1 SOLUTIONS
Fall 2023
"""

# QUESTION 1

"""
Problem - Given a word and a list of letters, determine if the word can be created using the letters.

Solution - Iterate (loop) through each letter in the word and check if there are enough of that letter in the letters.

  - Build up a "letter bank" by counting the number of times each letter appears in letters
  - Loop through the word using letters from the bank
    - If not enough letters in the bank, return False
    - Else, decrement the count of the letter in the bank
  - If we get through the whole word, return True

Letter bank:
  - Mimic a dictionary using a list
    - Each index represents a letter
    - Each value represents the count of that letter
    - How to convert a letter to an index? Ascii values
      - Each letter has a unique ascii value (a = 97, b = 98, etc.)
      - We can use ord() to get the ascii value of a letter (ord("a") = 97)

  - e.g.
    - letters = "apples"
    - [1, 0, 0, ..., 2, 0, 0, ..., 0] list of letter count
    -  a, b, c, ..., p, q, r, ..., z  letter represented

Some other possible approaches:
  - Just sort and compare the word and letters: return sorted(word) == sorted(letters) - but this only checks for exact letters.
  - Call .count() for each letter in the word and compare to the count in letters - but this is inefficient.
  - Loop through word and .remove() each letter from letters - but this is also inefficient.
"""

def can_construct(word, letters):
    letter_bank = [0] * 26 # Create a letter bank using a list with a length of 26 with each index representing one letter
    a = ord("a") # Get the ascii value of "a" to use as an offset to convert letters to indices
    for char in letters:
        letter_bank[ord(char)-a] += 1

    for char in word:
        if letter_bank[ord(char)-a] < 1: # Not enough of the same letters for the word
            return False
        letter_bank[ord(char)-a] -= 1 # Character is in the word so we "use" it by reducing the count by 1
    return True # Confirmed that each the letters are enough to create the word


# QUESTION 2

class Complex:
    # a + bi
    def __init__(self, a, b):
        self.a = a # constant
        self.b = b # coefficient for i

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other): # FOIL Method
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
    
    def __repr__(self):
        sign = " + " if self.b >= 0 else " - "
        return f"{self.a} {sign} {abs(self.b)}i"
    
    def __iadd__(self, other):
        """The += operator is shorthand for cplx1 = cplx1 + cplx2"""
        self = self + other
        return self # Need to return self or won't work!

# TEST CODE
# constructor, output
cplx1 = Complex(5, 2)
print(cplx1)          # 5 + 2i
cplx2 = Complex(3, 3)
print(cplx2)          # 3 + 3i

# addition
print(cplx1 + cplx2)  # 8 + 5i

# subtraction
print(cplx1 - cplx2)  # 2 - 1i

# multiplication
print(cplx1 * cplx2)  # 9 + 21i

# original objects remain unchanged
print(cplx1)          # 5 + 2i
print(cplx2)          # 3 + 3i

# iadd
print(cplx1)          # 5 + 2i
cplx1 += cplx2
print(cplx1)          # 8 + 5i



# QUESTION 3

import random

# Part A
# decreases the given number by 1 each loop and places it at a random index in the list. 
# Guarantees the numbers in the list are not repeated.

def create_permutation(n):
    perm = [-1] * n # -1 is used to signify that the spot has not been taken
    counter = n - 1
    while counter >= 0:
        index = random.randint(0, n-1)
        if perm[index] == -1:
            perm[index] = counter
            counter -= 1
            
    return perm



# Part B
# Calls the create_permutation function which returns a list. 
# Uses the values of the list to index the letters in the word and places them in the list. 

def scramble_word(word):
    lst = create_permutation(len(word))
    for i in range(len(lst)):
        lst[i] = word[lst[i]]
    return " ".join(lst)


# Part C
word_bank = ["Pokemon", "Digimon"]

def choose_word(words):
    return words[random.randint(0, len(word_bank)-1)]

def guessing_game(word):
    print("Unscramble the word " + scramble_word(word))
    tries = 3
    correct_guess = False

    while tries and not correct_guess:
        guess = input("Try #" + str(4 - tries) +":" )
        if word == guess:
            correct_guess = True
        else:
            print("Wrong!")
            tries -= 1

    if tries:
        print("Yay you got it!")
    else:
        print("Out of tries!")


pick = choose_word(word_bank)

guessing_game(pick)



#QUESTION 1 
def add_bin(bin_num1, bin_num2):
    result = ""
    carry = 0

    max_length = max(len(bin_num1), len(bin_num2)) 
    
    #sign extension so both will have same length
    b1 = (max_length - len(bin_num1))*'0' + bin_num1
    b2 = (max_length - len(bin_num2))*'0' + bin_num2


    for i in range(1, max_length + 1): 
        #we will use the negative indices since we evaluate from right to left
        sum_bits = int(b1[-i]) + int(b2[-i]) + carry
        result = str(sum_bits % 2) + result

        #carry = sum_bits >= 2  #can shorten the following if/else like with this line via implicit bool conversion
        if sum_bits < 2: 
            carry = 0
        else:
            carry = 1 #if sum of the bits + carry >= 2, then carry = 1

    return carry*'1' + result
