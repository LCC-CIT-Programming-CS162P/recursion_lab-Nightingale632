def main():
    '''Lab 2, Problem 2: Fibonacci'''
    print("The fibonacci sequence up to the nth output\n")

    n = int(input("Enter a whole number to start the sequence:"))
    n1 = 0
    n2 = 1
    next_number = n2
    count = 1
    while count <= n:
        print(next_number, end=" ")
        count += 1
        n1, n2 = n2, next_number
        next_number = n1 + n2
    print()


main()