depositos =[]
saques = []
valor_deposito = 0
saldo = 0
valor_saque = 0
numeros_saque = 0
calculo_saques = 0

LIMITE_SAQUES = 3


menu = """

    (a) depositar
    (b) sacar
    (c) extrato
    (x) sair

"""

while True:
    opcao = input(menu)
    if opcao == "a":
        valor_deposito = int(input("Digite o valor que deseja depositar: \n"))
        if valor_deposito > 0:
            depositos.append(valor_deposito)
            saldo += valor_deposito
            print(f"O seu saldo atual é {saldo}")
            print(depositos)
        else:
            print("Nao podemos depositar esse valor!")
            
        
    if opcao == "b":
        if numeros_saque == 3:
            print("Numero de saques excedido, por favor tente novamente amanha")
        
        else:
            valor_saque = int(input("Digite o valor que deseja sacar: \n" ))
            if valor_saque > 500:
                print("Voce só pode realizar saques até 500 reais!")
                
            elif valor_saque > saldo:
                print("Voce nao possui saldo o suficiente")
                
            else:
                saldo -= valor_saque
                print(f"Saque no valor de {valor_saque} realizado, seu novo saldo é de {saldo}")
                saques.append(valor_saque)
                numeros_saque += 1
                calculo_saques = LIMITE_SAQUES - numeros_saque
                print(f"Voce só pode realizar mais {calculo_saques} saques hoje")
                print(saques)
                
        