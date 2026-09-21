# skip_counter.py

def main():
    # Even numbers from 0 to 20 inclusive
    print("Even numbers:")
    for num in range(0, 21, 2):
        print(num, end=" " if num < 20 else "\n")
    
    print("\n" + "=" * 20 + "\n")

    # Countdown from 10 down to 0 inclusive
    print("Countdown:")
    for count in range(10, -1, -1):
        print(count, end=" " if count > 0 else "\n")

if __name__ == "__main__":
    main()