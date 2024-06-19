#Write a python program that checks if a substring is present in a given string.
string=raw_input("Enter string:")
sub_str=raw_input("Enter word:")
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")
