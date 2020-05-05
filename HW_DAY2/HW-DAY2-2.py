
for x in range(5):
    number = int(input(" please Enter the number : "))
    if number > 0 :
        if number <= 20:
            if number % number == 0 and number % 1 == 0:
                print(" the number is the prime number ")
            else:
                print("sorry, this is not prime number")
        else:
            print("the number must be between 1 and 20")
    else:
        print("must be positive number")
