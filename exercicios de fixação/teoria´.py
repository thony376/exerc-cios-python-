numero = 0


while numero < 5:
    numero += 1
    
    if numero == 3:
        print("Vamos pular a interação para", numero)
        continue
    
    print("Numero:", numero)
    
print("Fim do loop")


while True:
    resposta = input("Deseja sair? (s/n): ")
    if resposta.lower() == 's':
        print("Saindo do loop.")
        break
    print("Continuando o loop...")
    print(" ")
    
    
    
    
    
    
