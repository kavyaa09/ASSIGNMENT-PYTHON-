#Write a program in python that converts a string into a list of its characters.
import re
string = "Hello,World"
list = re.split(r',', string)
print(list)
