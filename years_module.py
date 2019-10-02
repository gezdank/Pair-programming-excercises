import datetime

name = str(input('Name: '))
c = int(input('Age: '))

e = int(input("Number: "))

def years(age):
    d = datetime.date.today().year
    a = d+(100-c)
    
    for i in range(e):
        print("You're gonna be 100 yrs old the year:", a)
    return(a)

def main():
    return

if __name__ == '__main__':
    main()

years(c)


"""
name = input("Enter you name: ")
age = int(input("Enter your age: "))

x = 100 - age # user will be 100 year old in x years
y = 2019 + x # user will be 100 years old in this year

print(name + " You will turn 100 in " + str(y))
"""