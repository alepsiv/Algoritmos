def palindromo(numero):
    numero1 = numero
    numero2 = 0
    
    if numero >= 1 and numero <= 10000:
        while numero1 > 0:
            digito = numero1 % 10
            numero2 = numero2*10+digito
            numero1 = numero1//10
            
        if numero != numero2:
            return False
        else:
            return True
    else:
        return False


numero = 1
print(f"{palindromo(numero)}")

numero = 545
print(f"{palindromo(numero)}")

numero = -11
print(f"{palindromo(numero)}")

numero = 4567
print(f"{palindromo(numero)}")
