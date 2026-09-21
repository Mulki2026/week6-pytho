# times_table.py

def main():
    try:
        number = int(input("Enter a number to generate its times table: "))
        print(f"\nTimes Table for {number}:")
        print("-" * 20)
        # range(1, 11) includes 1 through 10
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()