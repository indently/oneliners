phrase: str = 'Hello, Bob!'

# Easy reversing
print(phrase[::-1])

# You can also do:
print(''.join(reversed(phrase)))
# Not really recommended though because reversed creates a memory efficient object
# and is pretty much a waste if you flatten it immediately
