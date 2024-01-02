import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$_&-+()/*"':;!?~`|•√π÷×§∆£¢€¥^°={}\%©®™✓[]<>'

l = int(input("Enter your length that you want:"))
password = ""

for a in range (l):
    password += random.choice(chars)

print(password)