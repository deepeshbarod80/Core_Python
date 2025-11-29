# Python String Functions Examples

# ============ Case Conversion Functions ============

print("=== CASE CONVERSION FUNCTIONS ===\n")

# str.upper()
text = "hello world"
print(f"upper(): '{text}' -> '{text.upper()}'")

# str.lower()
text = "HELLO WORLD"
print(f"lower(): '{text}' -> '{text.lower()}'")

# str.capitalize()
text = "hello world"
print(f"capitalize(): '{text}' -> '{text.capitalize()}'")

# str.title()
text = "hello world python"
print(f"title(): '{text}' -> '{text.title()}'")

# str.swapcase()
text = "Hello World"
print(f"swapcase(): '{text}' -> '{text.swapcase()}'")

# str.casefold()
text = "HELLO"
print(f"casefold(): '{text}' -> '{text.casefold()}'")

"""
Expected Output:
=== CASE CONVERSION FUNCTIONS ===

upper(): 'hello world' -> 'HELLO WORLD'
lower(): 'HELLO WORLD' -> 'hello world'
capitalize(): 'hello world' -> 'Hello world'
title(): 'hello world python' -> 'Hello World Python'
swapcase(): 'Hello World' -> 'hELLO wORLD'
casefold(): 'HELLO' -> 'hello'
"""

# ============ String Testing Functions ============

print("\n=== STRING TESTING FUNCTIONS ===\n")

# str.isalpha()
print(f"isalpha(): 'Hello' -> {'Hello'.isalpha()}")
print(f"isalpha(): 'Hello123' -> {'Hello123'.isalpha()}")

# str.isdigit()
print(f"isdigit(): '12345' -> {'12345'.isdigit()}")
print(f"isdigit(): '123a5' -> {'123a5'.isdigit()}")

# str.isalnum()
print(f"isalnum(): 'Hello123' -> {'Hello123'.isalnum()}")
print(f"isalnum(): 'Hello 123' -> {'Hello 123'.isalnum()}")

# str.isspace()
print(f"isspace(): '   ' -> {'   '.isspace()}")
print(f"isspace(): ' a ' -> {' a '.isspace()}")

# str.islower()
print(f"islower(): 'hello' -> {'hello'.islower()}")
print(f"islower(): 'Hello' -> {'Hello'.islower()}")

# str.isupper()
print(f"isupper(): 'HELLO' -> {'HELLO'.isupper()}")
print(f"isupper(): 'Hello' -> {'Hello'.isupper()}")

# str.istitle()
print(f"istitle(): 'Hello World' -> {'Hello World'.istitle()}")
print(f"istitle(): 'hello world' -> {'hello world'.istitle()}")

# str.isidentifier()
print(f"isidentifier(): 'variable_name' -> {'variable_name'.isidentifier()}")
print(f"isidentifier(): '123variable' -> {'123variable'.isidentifier()}")

# str.isprintable()
print(f"isprintable(): 'Hello World' -> {'Hello World'.isprintable()}")
print(f"isprintable(): 'Hello\\nWorld' -> {'Hello\nWorld'.isprintable()}")

# str.isdecimal()
print(f"isdecimal(): '12345' -> {'12345'.isdecimal()}")
print(f"isdecimal(): '123.45' -> {'123.45'.isdecimal()}")

# str.isnumeric()
print(f"isnumeric(): '12345' -> {'12345'.isnumeric()}")
print(f"isnumeric(): '½' -> {'½'.isnumeric()}")

"""
Expected Output:
=== STRING TESTING FUNCTIONS ===

isalpha(): 'Hello' -> True
isalpha(): 'Hello123' -> False
isdigit(): '12345' -> True
isdigit(): '123a5' -> False
isalnum(): 'Hello123' -> True
isalnum(): 'Hello 123' -> False
isspace(): '   ' -> True
isspace(): ' a ' -> False
islower(): 'hello' -> True
islower(): 'Hello' -> False
isupper(): 'HELLO' -> True
isupper(): 'Hello' -> False
istitle(): 'Hello World' -> True
istitle(): 'hello world' -> False
isidentifier(): 'variable_name' -> True
isidentifier(): '123variable' -> False
isprintable(): 'Hello World' -> True
isprintable(): 'Hello\nWorld' -> False
isdecimal(): '12345' -> True
isdecimal(): '123.45' -> False
isnumeric(): '12345' -> True
isnumeric(): '½' -> True
"""

# ============ Search and Replace Functions ============

print("\n=== SEARCH AND REPLACE FUNCTIONS ===\n")

text = "Hello World Python"

# str.find()
print(f"find(): '{text}'.find('World') -> {text.find('World')}")
print(f"find(): '{text}'.find('Java') -> {text.find('Java')}")

# str.rfind()
text2 = "Hello World World"
print(f"rfind(): '{text2}'.rfind('World') -> {text2.rfind('World')}")

# str.index()
print(f"index(): '{text}'.index('World') -> {text.index('World')}")

# str.count()
print(f"count(): '{text2}'.count('World') -> {text2.count('World')}")

# str.startswith()
print(f"startswith(): '{text}'.startswith('Hello') -> {text.startswith('Hello')}")
print(f"startswith(): '{text}'.startswith('Hi') -> {text.startswith('Hi')}")

# str.endswith()
print(f"endswith(): '{text}'.endswith('Python') -> {text.endswith('Python')}")
print(f"endswith(): '{text}'.endswith('Java') -> {text.endswith('Java')}")

# str.replace()
print(f"replace(): '{text}'.replace('World', 'Universe') -> '{text.replace('World', 'Universe')}'")

"""
Expected Output:
=== SEARCH AND REPLACE FUNCTIONS ===

find(): 'Hello World Python'.find('World') -> 6
find(): 'Hello World Python'.find('Java') -> -1
rfind(): 'Hello World World'.rfind('World') -> 12
index(): 'Hello World Python'.index('World') -> 6
count(): 'Hello World World'.count('World') -> 2
startswith(): 'Hello World Python'.startswith('Hello') -> True
startswith(): 'Hello World Python'.startswith('Hi') -> False
endswith(): 'Hello World Python'.endswith('Python') -> True
endswith(): 'Hello World Python'.endswith('Java') -> False
replace(): 'Hello World Python'.replace('World', 'Universe') -> 'Hello Universe Python'
"""

# ============ Splitting and Joining Functions ============

print("\n=== SPLITTING AND JOINING FUNCTIONS ===\n")

text = "apple,banana,cherry"

# str.split()
print(f"split(): '{text}'.split(',') -> {text.split(',')}")

# str.rsplit()
text2 = "a.b.c.d"
print(f"rsplit(): '{text2}'.rsplit('.', 2) -> {text2.rsplit('.', 2)}")

# str.splitlines()
text3 = "Line 1\nLine 2\nLine 3"
print(f"splitlines(): multiline text -> {text3.splitlines()}")

# str.partition()
text4 = "name@domain.com"
print(f"partition(): '{text4}'.partition('@') -> {text4.partition('@')}")

# str.rpartition()
print(f"rpartition(): '{text4}'.rpartition('.') -> {text4.rpartition('.')}")

# str.join()
words = ['Hello', 'World', 'Python']
print(f"join(): ' '.join({words}) -> '{' '.join(words)}'")

"""
Expected Output:
=== SPLITTING AND JOINING FUNCTIONS ===

split(): 'apple,banana,cherry'.split(',') -> ['apple', 'banana', 'cherry']
rsplit(): 'a.b.c.d'.rsplit('.', 2) -> ['a.b', 'c', 'd']
splitlines(): multiline text -> ['Line 1', 'Line 2', 'Line 3']
partition(): 'name@domain.com'.partition('@') -> ('name', '@', 'domain.com')
rpartition(): 'name@domain.com'.rpartition('.') -> ('name@domain', '.', 'com')
join(): ' '.join(['Hello', 'World', 'Python']) -> 'Hello World Python'
"""

# ============ Formatting and Alignment Functions ============

print("\n=== FORMATTING AND ALIGNMENT FUNCTIONS ===\n")

text = "Python"

# str.center()
print(f"center(): '{text}'.center(20, '*') -> '{text.center(20, '*')}'")

# str.ljust()
print(f"ljust(): '{text}'.ljust(15, '-') -> '{text.ljust(15, '-')}'")

# str.rjust()
print(f"rjust(): '{text}'.rjust(15, '-') -> '{text.rjust(15, '-')}'")

# str.zfill()
number = "42"
print(f"zfill(): '{number}'.zfill(5) -> '{number.zfill(5)}'")

# str.format()
template = "Hello {}, welcome to {}"
print(f"format(): '{template}'.format('John', 'Python') -> '{template.format('John', 'Python')}'")

# str.format_map()
data = {'name': 'Alice', 'lang': 'Python'}
template2 = "Hello {name}, welcome to {lang}"
print(f"format_map(): with dict -> '{template2.format_map(data)}'")

"""
Expected Output:
=== FORMATTING AND ALIGNMENT FUNCTIONS ===

center(): 'Python'.center(20, '*') -> '*******Python*******'
ljust(): 'Python'.ljust(15, '-') -> 'Python---------'
rjust(): 'Python'.rjust(15, '-') -> '---------Python'
zfill(): '42'.zfill(5) -> '00042'
format(): 'Hello {}, welcome to {}'.format('John', 'Python') -> 'Hello John, welcome to Python'
format_map(): with dict -> 'Hello Alice, welcome to Python'
"""

# ============ Trimming Functions ============

print("\n=== TRIMMING FUNCTIONS ===\n")

text = "   Hello World   "

# str.strip()
print(f"strip(): '{text}' -> '{text.strip()}'")

# str.lstrip()
print(f"lstrip(): '{text}' -> '{text.lstrip()}'")

# str.rstrip()
print(f"rstrip(): '{text}' -> '{text.rstrip()}'")

# str.removeprefix() (Python 3.9+)
text2 = "HelloWorld"
print(f"removeprefix(): '{text2}'.removeprefix('Hello') -> '{text2.removeprefix('Hello')}'")

# str.removesuffix() (Python 3.9+)
print(f"removesuffix(): '{text2}'.removesuffix('World') -> '{text2.removesuffix('World')}'")

"""
Expected Output:
=== TRIMMING FUNCTIONS ===

strip(): '   Hello World   ' -> 'Hello World'
lstrip(): '   Hello World   ' -> 'Hello World   '
rstrip(): '   Hello World   ' -> '   Hello World'
removeprefix(): 'HelloWorld'.removeprefix('Hello') -> 'World'
removesuffix(): 'HelloWorld'.removesuffix('World') -> 'Hello'
"""

# ============ Encoding/Decoding Functions ============

print("\n=== ENCODING/DECODING FUNCTIONS ===\n")

text = "Hello"

# str.encode()
encoded = text.encode('utf-8')
print(f"encode(): '{text}'.encode('utf-8') -> {encoded}")

# str.expandtabs()
text_with_tabs = "Hello\tWorld\tPython"
print(f"expandtabs(): '{text_with_tabs}'.expandtabs(4) -> '{text_with_tabs.expandtabs(4)}'")

# str.translate() and str.maketrans()
translation_table = str.maketrans('aeiou', '12345')
text3 = "Hello World"
print(f"translate(): '{text3}'.translate(table) -> '{text3.translate(translation_table)}'")

"""
Expected Output:
=== ENCODING/DECODING FUNCTIONS ===

encode(): 'Hello'.encode('utf-8') -> b'Hello'
expandtabs(): 'Hello\tWorld\tPython'.expandtabs(4) -> 'Hello   World   Python'
translate(): 'Hello World'.translate(table) -> 'H2ll4 W4rld'
"""

# ============ Other Utility Functions ============

print("\n=== OTHER UTILITY FUNCTIONS ===\n")

text = "Hello"

# len()
print(f"len(): len('{text}') -> {len(text)}")

# ord()
char = 'A'
print(f"ord(): ord('{char}') -> {ord(char)}")

# chr()
code = 65
print(f"chr(): chr({code}) -> '{chr(code)}'")

# str()
number = 123
print(f"str(): str({number}) -> '{str(number)}'")

# repr()
text4 = "Hello\nWorld"
print(f"repr(): repr('{text4}') -> {repr(text4)}")

"""
Expected Output:
=== OTHER UTILITY FUNCTIONS ===

len(): len('Hello') -> 5
ord(): ord('A') -> 65
chr(): chr(65) -> 'A'
str(): str(123) -> '123'
repr(): repr('Hello\nWorld') -> 'Hello\\nWorld'
"""

print("\n=== END OF EXAMPLES ===")