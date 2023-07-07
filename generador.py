import random

lista_mayusculas = [chr(65 + i) for i in range(26)]
lista_minusculas = [chr(97 + i) for i in range(26)]
lista_numeros = [1,2,3,4,5,6,7,8,9]

stoker = lista_numeros
password = []
def Generador():
    global password
    for i in range(1,29):
        
        jul1 = random.choice(lista_numeros)
        password.append(jul1)
        jul2 = random.choice(lista_minusculas)
        password.append(jul2)
        jul3 = random.choice(lista_mayusculas)
        password.append(jul3)

def main():
    Generador()
    cadena = ''.join(str(elements) for elements in password)
    print(cadena)

if __name__ == '__main__':
    main()

