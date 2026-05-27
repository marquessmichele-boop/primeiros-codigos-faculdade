# Exercícios de Lógica Básica em Python
# Este arquivo reúne exemplos simples de operações, condições e laços.

# 1️⃣ Soma de dois números
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print("A soma é:", soma)

# 2️⃣ Verificação de número par ou ímpar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# 3️⃣ Cálculo de média e situação do aluno
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3

if media >= 7:
    print("APROVADO")
elif media >= 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")

# 4️⃣ Contagem de 1 a 10
for i in range(1, 11):
    print(i)

# 5️⃣ Tabuada do número 3
num = 3
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
