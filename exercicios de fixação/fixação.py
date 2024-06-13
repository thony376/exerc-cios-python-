#desafio temperatura


# for i in range(1, 100):
#     print(i)
    
 
 #desafio extra 1
for i in range(1,100,2):
     print(i)
     

#desafio extra 2
for i in range(10):
    valor = int(input(f"Digite o valor {i+1}"))
    

#desafio extra 3
qnt_analisadas= int(input("Quantas pessoas deseja analisar? "))
fim= qnt_analisadas+1
somatoria= 0

print(" ")
for i in range(1,fim):
        print(i)
        temperatura= float(input("Digite a temperatura: (celsius)"))
        somatoria= somatoria+temperatura
        
        print(f"paciente {i}: ")
        if temperatura<=37.2:
            print("Temperatura Normal")
        elif temperatura>37.2 and temperatura<=38:
            print("Em estado febril")
        elif temperatura>38 and temperatura<=39:
            print("Está com febre")
        else:
            print("Está com febre alta")
            
            
print("----------------------------------")

media= somatoria/qnt_analisadas
print(f"Média de temperatura de {qnt_analisadas} pessoas = {media} celsius")