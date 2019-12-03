
def isPrime():
    number = int(input("Digite um numero: "))

    if( number == 2 ):
        print(f"{number} é primo")
    else:
        temp = number -1
        prime = False
        while number >= 1 and temp > 1:
            result = number % temp
            print(f"{number} % {temp} = {result}")
            if(number % temp == 0):
                prime = False
                return
            else:
                prime = True
               # print(f"{number} is Prime")
                

            temp = temp - 1
    

            


isPrime()