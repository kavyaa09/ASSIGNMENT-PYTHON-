#Write a python program that returns the minimum and maximum values in a list of numbers.
l=eval(input("Enter a list of numbers"))
larg = l[0] 
small =l[0] 

for num in l:
    if num > larg:
        larg = num
    if num < small:
        smallest = num

print("Largest:", larg)
print("Smallest:", small)