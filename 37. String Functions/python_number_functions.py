# Python Number Functions Reference

# Basic Arithmetic Functions
abs()                # Absolute value
pow()                # Power (x**y or pow(x,y,z) for modular)
round()              # Round to nearest integer or decimal places
divmod()             # Return quotient and remainder
sum()                # Sum of iterable numbers

# Type Conversion Functions
int()                # Convert to integer
float()              # Convert to float
complex()            # Convert to complex number
bool()               # Convert to boolean

# Mathematical Functions (import math)
math.ceil()          # Round up to nearest integer
math.floor()         # Round down to nearest integer
math.trunc()         # Truncate decimal part
math.sqrt()          # Square root
math.log()           # Natural logarithm
math.log10()         # Base-10 logarithm
math.exp()           # e raised to power
math.factorial()     # Factorial
math.gcd()           # Greatest common divisor
math.lcm()           # Least common multiple (Python 3.9+)

# Trigonometric Functions (import math)
math.sin()           # Sine
math.cos()           # Cosine
math.tan()           # Tangent
math.asin()          # Arc sine
math.acos()          # Arc cosine
math.atan()          # Arc tangent
math.degrees()       # Convert radians to degrees
math.radians()       # Convert degrees to radians

# Number Testing Functions
isinstance(x, int)   # Check if integer
isinstance(x, float) # Check if float
math.isnan()         # Check if NaN
math.isinf()         # Check if infinite
math.isfinite()      # Check if finite

# Float Methods
float.is_integer()   # Check if float is whole number
float.hex()          # Hexadecimal representation
float.fromhex()      # Create float from hex (class method)

# Integer Methods
int.bit_length()     # Number of bits needed to represent
int.to_bytes()       # Convert to bytes
int.from_bytes()     # Create int from bytes (class method)

# Random Number Functions (import random)
random.random()      # Random float between 0 and 1
random.randint()     # Random integer in range
random.uniform()     # Random float in range
random.choice()      # Random element from sequence
random.shuffle()     # Shuffle list in place
random.sample()      # Random sample without replacement

# Constants (import math)
math.pi              # Pi constant
math.e               # Euler's number
math.tau             # Tau (2*pi)
math.inf             # Positive infinity
math.nan             # Not a Number

# Decimal Module Functions (import decimal)
decimal.Decimal()    # Precise decimal arithmetic
decimal.getcontext() # Get current decimal context
decimal.localcontext() # Temporary decimal context

# Fraction Module Functions (import fractions)
fractions.Fraction() # Rational number representation

# Built-in Number Functions
min()                # Minimum value
max()                # Maximum value
bin()                # Binary representation
oct()                # Octal representation
hex()                # Hexadecimal representation