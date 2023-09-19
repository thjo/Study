## Define variables ===================
# print("Hello World!")
# greeting = "Hello World!!"
# print(greeting)


## Naming Convention ===================


## Data Type ===================
## 1. Strings
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

## upper # lower
# city = "   seoul  "
# city = city.upper()     #city = city.lower()
# print(city)

## city.rstrip()  # city.lstrip() # city.strip()
# city = city.strip() 
# print(city)
# message = "Hello!\nIt's nice to meet you.\nHow are you?"
# print(message)

## removeprefix #removesuffix
# score1 = "Score: 90"
# print(score1.removeprefix("Score: "))
# score2 = "80 score"
# print(score2.removesuffix(" score"))

## replace
# city = "Milpitas, CA"
# print(city.replace("CA", "California"))

## f - String
# city1 = "Milpitas"
# state1 = "California"
# addr1 = f"{city1}, {state1}, USA"
# city2 = "Little Ferry"
# state2 = "New Jersey"
# addr2 = f"{city2}, {state2}, USA"
# print(f"{addr1}\n{addr2}")


## Numbers =================== 
# a = 2
# b = 3
# ## add # minus # multify # divide
# #  +     -        *         /
# print(a ** b)  # 2의 3승 값 
# ## 몫
# print(a//b) # 몫
# print(a%b)  # 나머지

# ## Float ===================
# x = 2.0
# y = 0.3
# z = 1
# print(f"{x+y}\t{x-y}\t{x*y}\t{x/y}")
# print(f"{x+z}\t{x-z}\t{x*z}\t{x/z}")

# ## 큰 숫자에 자리수 별 구분을 줄 수 있는 tip
# price = 12_349_000_000_000
# print(price)

## Constants - 상수로 표시하는 키워드 미 존재 하여 대문자로 표기하여 constant임을 알려줌 ===================
# PI = 3.141592


## Convert between String and Number ===================
# num_ten = 10
# str_ten = "10"

# ## convert number to string
# str_new = str(num_ten)
# ## convert string to number
# num_new = int(str_ten)  # float(str_ten)


## Bool, Boolean ===================
# True, False *** Start with upper case ***
# print(3 > 2)
# print(3 == 3.0)     # 같은 값
# print(3 is 3.0)     # 같은 값과 타입까지 확인



## Prompt ===================
## std input 
str_input_data = input("Please input your name: ")
print(str_input_data)

## comments 
## - single line - #
## multiple lines - """


