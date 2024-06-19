#Write a python program that counts the occurrences of a specific element in a list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
count = 0  
for item in my_list:  
if(item == 5):  
count += 1  
print(count)  