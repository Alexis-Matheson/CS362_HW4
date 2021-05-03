#This program calculates the average of the elements in a list

import math
import random

def createList(num):
    arr = []
    if(num == 0):
        print(arr)
        print("The list is empty.")
    else:
        for i in range(num):
            arr.append(random.randint(0,100))
        print(arr)
        average(arr)

def average(arr):
    count = 0
    for i in arr:
        count += i
    avg = count/len(arr)
    print("The average of the list is: %.2f" %avg)

def main():
    l = input("Enter the size of a list: ")
    try:
        int(l)
        is_int = True
    except:
        is_int = False
        print("The number/character you selected cannot create a list")
    
    if(is_int == True):
        num = int(l)
        if(num >= 0):
            createList(num)
        else:
            print("Cannot create a list with negative number of elements.")

if __name__ == "__main__":
    main()