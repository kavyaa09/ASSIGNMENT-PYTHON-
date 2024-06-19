#Write a program that reads data from a CSV file and prints it to the console.
import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)