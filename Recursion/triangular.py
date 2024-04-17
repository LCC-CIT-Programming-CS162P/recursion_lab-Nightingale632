def triangle(n):
    '''basecase'''
    if n == 1:
        return 1
    else:
        return n + triangle(n - 1)

def trianglePrint(n, nMax):
    '''fn to define a border and triangle pattern from oftedahld'''
    borderExtra = nMax - n
    line = (borderExtra * '-') + ((('-' + '\u25b2') * n) + '-') + (borderExtra * '-')
    print(line)
    if n == 1:
        return 1
    else:
        return n + trianglePrint(n - 1, nMax)

def main():
    '''Lab 2, problem 1: Triangles'''
    print("This program allows the user to request the nth triangle number they decide to use\n")
    max = int(input("Provide a positive whole number to convert to triangles: "))
    triNum = triangle(max)
    print("The " + str(max) + "th triangle number is " + str(triNum) + ".")
    print()
    for n in range(1, max + 1):
        border = ('=' * ((n * 2) + 1))
        print(border)
        print("Triangle " + str(n) + " = " + str(triNum))
        print(border)
        triNum = trianglePrint(n, n)
        print(border)
        print()

    print()


main()