"""
Atividade 04
*** Criar um programa que faça uma a computação da máquina de estados do autômato  do binário divisível por 4.
"""

"""
** * REGRA DE ESTÁGIOS DO AUTÔMATO = [0, 1, 0, 1]

        0                                    1
    _________                             ________
    |       v                             v      |
     < -  ( 0 ) - > ( 1 ) - > ( 0 ) - > ( 1 ) - > 
            ^                   |
            |___________________|        
                      0            

"""

def muda_estado(valor, estado_atual):
    estados =   [0, 1, 2, 3]

    ## Percorre o vetor de estados 
    ## para cada condição é considerada o estado atual, informado no parâmetro da função, e o valor do binário
    ## Considerando a regra de estágio do autômato ele atribui um valor para os estágio atual
    for estado in estados:
        if estado_atual == estado: 
            if valor == 0 and estado_atual == 0: 
                estado_atual = 0
                break
            if valor == 1 and estado_atual == 0:
                estado_atual = 1
                break
            if valor == 1 and estado_atual == 1:
                estado_atual = 1
                break
            if valor == 0 and estado_atual == 1:
                estado_atual = 2
                break
            if valor == 0 and estado_atual == 2:
                estado_atual = 0
                break 
            if valor == 1 and estado_atual == 2:
                estado_atual = 3
                break 
            if valor == 1 and estado_atual == 3:
                estado_atual = 3
                break 
            if valor == 0 and estado_atual == 3:
                estado_atual = 2
                break
    return estado_atual


## Recebe a entrada pelo teclado
inteiro=int(input('Informe o decimal para avaliação: '))
 
copia_inteiro=inteiro

## Vetor para armazenar os restos das divisões
binario_invertido=[]


while (inteiro>0):
    ## Enquanto o interio não for zero, ele continuará fazendo a divisão por 2
    ## Armazena o resto da divisão 
    resto=int(float(inteiro%2))
    ## adiciona esse resto em um vetor 
    binario_invertido.append(resto)
    ## Decremente o inteiro para uma nova divisão
    inteiro=(inteiro-resto)/2
binario_invertido.append(0)

binario = []
binario_string = ''

## Inverte a sequência de restos para formar o binário 
for a in binario_invertido[::-1]:
    binario_string=binario_string+str(a)
    binario.append(a)

print('O valor convertido para binário de %d é %s'%(copia_inteiro, binario_string))

# Nesse caso, considera o index do primeiro elemento do vertor "automato" que é igual a zero
estado_final = 0
estado_atual = 0
    
for valor in binario:
    estado_atual = muda_estado(valor, estado_atual)
    print('ESTADO ATUAL = ' + str(estado_atual))

if estado_atual == estado_final:
    print('O binário %s é multiplo de 4' % binario_string)
else:
    print('O binário %s não é multiplo de 4' % binario_string)
