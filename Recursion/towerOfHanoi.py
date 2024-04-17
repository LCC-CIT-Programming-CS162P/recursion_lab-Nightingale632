def towerPlay(n, towerStart, towerFinal, towerExtra):
    if n == 1:
        print("Disk " +str(n) + ": " + towerStart + "-->" + towerFinal)
    else:
        towerPlay(n - 1, towerStart, towerExtra, towerFinal)
        print("Disk " + str(n) + ": " + towerStart + "-->" + towerFinal)
        towerPlay(n - 1, towerExtra, towerFinal, towerStart)

def main():
    '''Lab 2, Problem 4: Tower of Hanoi'''
    print("The Tower of Hanoi\n")
    print("This program will challenge the computer to solve the Tower of Hanoi\n")
    diskCount = int(input("Provide a positive whole number of disks to give to the computer: "))
    print("The computer will now attempt to solve the Tower of Hanoi with " +str(diskCount) + " Disks:")
    towerPlay(diskCount, "left", "right", "middle")


main()