#Write a python program that takes a list of numbers and returns their sum.
total = 0 
 
list1 = [ 5, 17, 18, 23] 
 
for ele in range(0, len(list1)): 
	total = total + list1[ele] 
 
print("Sum of all elements in a given list: ", total) 