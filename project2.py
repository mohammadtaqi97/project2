print("===== Welcome to Logic Box! =====")
print("1. Pattern type")
print("2. Number analysis")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    rows = int(input("Enter number of rows: "))

    if rows <=0:
        print("Error!, Invalid number")
        print("Enter a positive number!")

    else:
        print("Pattern: ")
        for i in range(1,rows+1):
            for j in range(i):
                print("*",end = " ")
            print()

elif choice == 2:
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    if end <= start:
        print("Error!")
        print("Start should be lesser than end")
    else:
        print("\nEven number = ")
        for i in range(start,end+1):
            if i%2 == 0:
                print(i,end = " ")
        print("\nOdd numbers = ")
        for i in range(start,end+1):
                if i %2!=0:
                    print(i,end = " ")
    n = end-start+1
    total = n*(start+end)//2
    print("\n\nSum = 2",total)

    
elif choice == 3:
    print("Thank you for using Logic Box.")
    print("Program Ended.")
    

else:
    print("Invalid choice!,please try again")