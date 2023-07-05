ultimo = 10
fila = list (range(1, ultimo +1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila Atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operaçao = input("Operação (F, A ou S): ")
    if operaçao == "A":
        if len(fila) >0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila vazia! Ninguem para Atender.")
    elif operaçao == "F":
        ultimo += 1 #incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operaçao == "S":
        break
    else:
        print("Operação Inválida! Digite apenas F, A ou S!")