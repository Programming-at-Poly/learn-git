#
# Decription: This program will analize the upper and lower case content of
# a given string.
#



sampleString = ("We the People of the United States, in Order+ to form a more perfect Union,"
" establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare,"
" and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution"
" for the United States of America.")


# 1) Start by counting the number of upper, lower, and other characters in the provided string. Print your results.

# 2) Next, invert the case of all of the text in the sample string. Print the resulting string.

# 3) Place all vowels in one list. 

# 4) Place all consonant in another list. 

# 5) Find the decimal value of each character and place all characters that are multiples of 3 in another list.

lowers = 0
uppers = 0
not_letters = 0

vowel_list = []
consonant_list = []

new_string = ""

for char in sampleString:
    if char.islower():
        new_string += char.upper()
        lowers += 1
    elif char.isupper():
        new_string += char.lower()
        uppers += 1
    else:
        new_string += char
        not_letters += 1

    if char.lower() in "aeiouy":
        vowel_list.append(char)
    elif char.isalpha():
        consonant_list.append(char)
   
        

print(lowers, uppers, not_letters)
print()
print(new_string)
print()
print(vowel_list)
print()
print(consonant_list)
print()
print([ord(c) for c in sampleString if ord(c)%3==0])






    
