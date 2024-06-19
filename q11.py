#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

print(lines)
