#!/usr/bin/env python3.11

# print string "Hello, World!"
print("Hello, World!")

# print string in lower case
print("Hello, World!".lower())

# print type of bollean value
print(type(True)); print(type(False))
print(bool({})); print(bool("")); print(bool(0)); print(bool(0.0)); print(bool(None))

# print looping 4 times
count = 4
while count > 0:
    print(f"while looping {count}")
    count -= 1

for i in range(4):
    print(f"for looping {i}")