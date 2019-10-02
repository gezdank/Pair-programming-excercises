def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return("FizzBuzz")
    elif number % 3 == 0:
        return('Fizz')  
    elif number % 5 == 0:
        return('Buzz')
    else: 
        return(number) 
    


def main():
    #for i in range(1, 101):
    #    if i % 3 == 0 and i % 5 == 0:
    #        print("FizzBuzz")
    #    elif i % 3 == 0:
    #        print('Fizz')  
    #    elif i % 5 == 0:
    #        print('Buzz')
    #    else: 
    #        print(i)  
    return

if __name__ == '__main__':
    main()