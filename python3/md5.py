"""md5 encoding of a string"""

import hashlib

str = '16557022'
# encoding using md5 hash
# function
result = hashlib.md5(b'16557022')

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result.digest())

# encoding using encode()
# then sending to md5()
result = hashlib.md5(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())