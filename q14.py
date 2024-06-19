# Write a program in python that converts a given string to title case (first letter of each word capitalized).
def cap_sentence(s):
    return ''.join( (c.upper() if i == 0 or s[i-1] == ' ' else c)  for i, c in enumerate(s) )