# Definindo os produtos
arroz = 1
feijao = 2
cafe = 3
produtos = 0

print("Bem vindo ao supermercado!")
print('---'*15)
print(f" {arroz} - Arroz R$18.00\n {feijao} - Feijão R$7.00\n {cafe} - Café R$5.00")

while True:
    # Escolha do usuário
    us = int(input("Escolha os produtos que deseja comprar pela numeração: "))

    if us == arroz:
        produtos += 18
        print(f'Total da compra é R$ {produtos:.2f}')
    elif us == feijao:
        produtos += 7
        print(f'Total da compra é R$ {produtos:.2f}')
    elif us == cafe:
        produtos += 5
        print(f'Total da compra é R$ {produtos:.2f}')
    else:
        print("Produto inválido, tente novamente.")

    # Pergunta se o usuário quer adicionar mais um produto
    us = input('Deseja adicionar mais um produto? (s/n): ').strip().lower()
    if us == 'n':
        print(f'Compra finalizada. Total: R$ {produtos:.2f}')
        print('Obrigada pela compra!')
        break