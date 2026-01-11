class Arithmetic:
    def operators(self):
        print("Enter the first number:")
        a = float(input())

        print("Enter the second number:")
        b = float(input())

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print("Sum:", a + b)

        elif choice == 2:
            print("Subtraction:", a - b)

        elif choice == 3:
            print("Multiplication:", a * b)

        elif choice == 4:
            if b == 0:
                print("Division not possible (cannot divide by zero)")
            else:
                print("Division:", a / b)

        else:
            print("Invalid choice")


c = Arithmetic()
c.operators()

if __name__ == "main":
    operator()


