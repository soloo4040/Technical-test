#write a program that prints the numbers from 1 t0 100. For multiples of 3 , print "Fizz"; 
#for multiples of 5, print"Buzz"; and for numbers that are multiples of both 3 and 5, print"FizzBuzz

for number in range(1,101):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")

    elif (number % 3 == 0):
        print("Fizz")

    elif (number % 5 == 0):
        print("Buzz")
    
    else:
        print(number)

#write a program to genearte the finonacci sequence up to 100 
    
    def fib (n):
        sequence = []
        
        x=0
        y=1

        while x < n: 
            sequence.append(x)

            x, y = y, x=y
            
        return sequence    

    fib_100 = fib(100)
    print(fib_100)



#write a program that accept string as  input, capitalizes the first letter of each word in a string  and then return the result string
#examples
#"hi" returns "Hi" 
#"i love programming" returns "I Love Programming"
    
    text = input("Enter a string: ")
    print(text.title()) 


#write a program that takes an integer as input and returns an integer with reversed digit ordering.
#example for input -500, the program should return 5
# for input -56, the prn ogram should return -65
# for input  -90, the program should return  -9
# for input 91, the program should return 19

    number =int(input(" Enter number: "))
    reversedvalue = 0
    while (number > 0):
        digit = number % 10
        reversedvalue = reversedvalue * 10 + digit

        number = number // 10

    print("Reverse of the number is: ", reversedvalue)    


#write a program that counts the number of vowels in a sentence
# e. g " Hello world " returns 2
    
    text = input(" Enter a text: ")
    count = 0

    for char in text: 
        if (char in "AaEeIiOoUu"):
            count += 1

    print("count: ", count)


#write a program that takes an integer as input and returns true if the input is a power of two
# e. g 8 returns true
# e. g 6 returns false

 
    def isPowerofTwo(n):
        if ( n == 0):
            return False
        
        while (n != 1):
            if (n % 2 != 0 ):
                return False
            n = n // 2

        return True
    number =  int(input(" Enter a number: "))  
    print(isPowerofTwo(number))

    



        
