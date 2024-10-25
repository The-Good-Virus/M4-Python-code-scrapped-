# Lela Parks
# Oct 22,2024

#Code is suppose to print a number of options 
#presented to the user and allow the user to 
#select an option from the list

attempts = 0

if attempts < 1:
    print("Please choose an option from the list below:")
    print("1. Learn Python")
    print("2. Learn Java")
    print("3. Go swimming")
    print("4. Have dinner")
    print("5. Go to bed")

    choice = input("Enter the number of your choice (1-5): ")

    if choice == '1':
        print("You selected Learn Python.")
        attempts += 1
    elif choice == '2':
        print("You selected Learn Java.")
        attempts += 1
    elif choice == '3':
        print("You selected Go swimming.")
        attempts += 1
    elif choice == '4':
        print("You selected Have dinner.")
        attempts += 1
    elif choice == '5':
        print("You selected Go to bed.")
        attempts += 1
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
