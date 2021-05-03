#This program generates a full name when you provide it with a first and last name

def validate(name):
    bool = name.isalpha()
    if(bool == True):
        return bool
    else:
        print("Name contains something other than alphabetical characters.")
        return bool

def putTogether(name1, name2):
    Name = name1 + " " + name2
    print("Your full name is: %s" %Name)

def main():
    first = input("Enter your first name: ")
    validate(first)
    if(True):
        last = input("Enter your last name: ")
        validate(last)
        if(True):
            putTogether(first, last)

if __name__ == "__main__":
    main()