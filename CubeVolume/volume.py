#This program calculates the volume of a cube

import math

def Volume(d):
    v = d * d * d

    print("The volume of the cube is %.2f units squared." %v)

def main():
    dimension = input("Enter the size of one side of a cube: ")
    try:
        float(dimension)
        is_float = True
    except:
        is_float = False
        print("The dimension you entered cannot be calculated into a volume.")
    
    if(is_float == True):
        d = float(dimension)
        if(d > 0):
            Volume(d)
        else:
            print("Cannot get a volume of a negative dimension.")
        

if __name__ == "__main__":
    main()