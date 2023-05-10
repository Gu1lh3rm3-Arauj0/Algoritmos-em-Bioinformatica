def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
resultado = fatorial(numero)
print("O fatorial de", numero, "é", resultado)

def maxnum(*numeros):
    if len(numeros) == 0:
        print("Nenhum número fornecido.")
        return None
    else:
        maximo = numeros[0]
        for numero in numeros:
            if numero > maximo:
                maximo = numero
        return maximo

# Exemplo de uso da função
resultado = maxnum(7, 2, 9, 4, 1)
print("O maior número é:", resultado)

def verifica_multiplo(num1, num2):
    if num2 != 0 and num1 % num2 == 0:
        return True
    else:
        return False

# Exemplo de uso da função
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = verifica_multiplo(numero1, numero2)
print(resultado)

def calcular_media(peso1, peso2, *notas):
    total_pesos = peso1 + peso2
    soma_ponderada = peso1 * notas[0] + peso2 * notas[1]
    media = soma_ponderada / total_pesos
    return media

# Exemplo de uso da função
peso1 = 0.4
peso2 = 0.6
resultado = calcular_media(peso1, peso2, 8, 7)
print(resultado)  # Saída: 7.4

def concatenar_strings(*strings):
    resultado = ""
    for s in strings:
        resultado += s
    return resultado

# Exemplo de uso da função
nomes = ["João", "Maria", "Pedro"]
resultado = concatenar_strings(*nomes)
print(resultado)  # Saída: JoãoMariaPedro
