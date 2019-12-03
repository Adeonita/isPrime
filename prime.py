
def isPrime():
    number = int(input("Digite um numero: "))
    prime = None

    if( number == 2 ):
        print(f"{number} é primo")
    elif(number % 2 == 0 or number == 1): #Já elimino os numeros pares e o número 1, pois o único par primo é 2
        print("Não é primo")
    else:
        temp =  number -1 #Pego o numero como sendo ele mesmo -1 pois n%n = 0
        while(temp > 1): #Percorro até maior que 1 , pois n%1 = 0
            resto = number % temp #Pego o resto da divisão de number por ele mesmo até 1
            print(f"O resto da divisão de {number} por {temp} é {resto}")
            if(resto != 0):
                print("é primo")
            else:
                print("Não é primo")
                return #Na primeiro ocorrencia de uma divisão exata retorno que não é primo
            temp = temp - 1

            
i = -1
while( i < 10):
    isPrime()
    i = i + 1