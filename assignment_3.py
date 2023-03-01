db = []

while True:
    command = int(input("Enter a number between 1 and 10 (or 0 to exit): "))
    if 10 < command or command < 0:
        print("Sorry, if the number is not between 0 and 10 it's toohard for me.")
    elif command == 0:
        break
    else:
        db.append(command)
        print(f'The sum of all your number is: {sum(db)} ')

print(f'The program is finished, the final sum is: {sum(db)} ')
