# Python String Functions Reference

# Case Conversion Functions
str.upper()          # Convert to uppercase
str.lower()          # Convert to lowercase
str.capitalize()     # Capitalize first character
str.title()          # Title case (capitalize each word)
str.swapcase()       # Swap case of all characters
str.casefold()       # Aggressive lowercase for comparisons

# String Testing Functions
str.isalpha()        # Check if all characters are alphabetic
str.isdigit()        # Check if all characters are digits
str.isalnum()        # Check if all characters are alphanumeric
str.isspace()        # Check if all characters are whitespace
str.islower()        # Check if all characters are lowercase
str.isupper()        # Check if all characters are uppercase
str.istitle()        # Check if string is in title case
str.isidentifier()   # Check if string is valid identifier
str.isprintable()    # Check if all characters are printable
str.isdecimal()      # Check if all characters are decimal
str.isnumeric()      # Check if all characters are numeric

# Search and Replace Functions
str.find()           # Find substring (returns index or -1)
str.rfind()          # Find substring from right
str.index()          # Find substring (raises exception if not found)
str.rindex()         # Find substring from right (raises exception)
str.count()          # Count occurrences of substring
str.startswith()     # Check if string starts with substring
str.endswith()       # Check if string ends with substring
str.replace()        # Replace occurrences of substring

# Splitting and Joining Functions
str.split()          # Split string into list
str.rsplit()         # Split string from right
str.splitlines()     # Split string at line breaks
str.partition()      # Split into 3 parts at first occurrence
str.rpartition()     # Split into 3 parts at last occurrence
str.join()           # Join list elements with string as separator

# Formatting and Alignment Functions
str.center()         # Center string in given width
str.ljust()          # Left justify string
str.rjust()          # Right justify string
str.zfill()          # Pad string with zeros
str.format()         # Format string with placeholders
str.format_map()     # Format string with mapping

# Trimming Functions
str.strip()          # Remove whitespace from both ends
str.lstrip()         # Remove whitespace from left
str.rstrip()         # Remove whitespace from right
str.removeprefix()   # Remove prefix (Python 3.9+)
str.removesuffix()   # Remove suffix (Python 3.9+)

# Encoding/Decoding Functions
str.encode()         # Encode string to bytes
str.expandtabs()     # Expand tabs to spaces
str.translate()      # Translate characters using translation table
str.maketrans()      # Create translation table (static method)

# Other Utility Functions
len()                # Get string length
ord()                # Get Unicode code point of character
chr()                # Get character from Unicode code point
str()                # Convert object to string
repr()               # Get string representation of object