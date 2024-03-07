#############################################
################# QUESTÃO 1 #################
################### SOMA ####################
#############################################

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma) ### REPOSTA: 91

#############################################
################# QUESTÃO 2 #################
########## SEQUÊNCIA DE FIBONACCI ###########
#############################################

numero_desejado = int(input('Insira um numero para testar: '))

var1 = 0
var2 = 1
soma_fibonacci = 0
sequencia_fibonacci = []

while soma_fibonacci <= numero_desejado:
    soma_fibonacci = var2 + var1
    sequencia_fibonacci.append(soma_fibonacci)
    var1 = var2
    var2 = soma_fibonacci

if numero_desejado in sequencia_fibonacci:
    print(f'O numero {numero_desejado} pertence a sequencia de Fibonacci!')
else:
    print(f'O numero {numero_desejado} nao pertence a sequencia de Fibonacci!')

#############################################
################# QUESTÃO 3 #################
################## PADRÕES ##################
#############################################

### LETRA A)
    ### Progressão Aritmética de razão = 2 começando em 1
    ### RESPOSTA: 9

### LETRA B)
    ### Progressão Geométrica de razão = 2 começando em 2
    ### RESPOSTA: 128

### LETRA C)
    ### Progressão Aritmética de Segunda Ordem, com razão 2 começando em 1
    ### PA de Primeira Ordem: [0,1,4,9,16,25,36]
    ### PA de Segunda Ordem: [1,3,5,7,9,11,13]
    ### RESPOSTA: 36 + 13 = 49

### LETRA D)
    ### Progressão Aritmética de Segunda Ordem, com razão 8 começando em 12
    ### PA de Primeira Ordem: [4,16,36,64]
    ### PA de Segunda Ordem: [12,20,28,36]
    ### RESPOSTA: 64 + 36 = 100

### LETRA E)
    ### Sequência de Fibonacci: [1,1,2,3,5,8,13,21,34,...]
    ### Questão anterior.
    ### RESPOSTA: 13

### LETRA F)
    ### [2,10,12,16,17,18,19]
    ### Sem lógica matemática
    ### Todos começam com D (??????)
    ### RESPOSTA: 200 (???)

#############################################
################# QUESTÃO 4 #################
################## PADRÕES ##################
#############################################

    ### RESPOSTA: Usar a temperatura das lâmpadas. 
    ### Liga Interruptor 1, deixa aquecer (alguns minutos, sei lá), desliga e liga o interruptor 2. 
    ### Vai na sala ver qual está desligada e quente (Interruptor 1)
    ### A lâmpada acesa é do Interruptor 2
    ### A fria e apagada é do interruptor 3
    ### Apenas uma ida a sala.

#############################################
################# QUESTÃO 5 #################
########### INVERSÃO DE STRING ##############
#############################################
    
texto_desejado = input('Insira a string da Questão 5: ')
texto_desejado_invertido = texto_desejado[::-1]
print(texto_desejado_invertido)