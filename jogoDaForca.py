import random

def sorteio():
    return random.choice(["amarelo", "amiga", "azul", "girafa", "foto", "cama", "garfo"])

def forca(vidas):
    if vidas == 0:
        print('''
    +---+
    |   |
    0   |
   /|\  | 
   / \  |                 
        |
===========            
''')
    elif vidas == 1:
        print('''
    +---+
    |   |
    0   |
   /|\  | 
   /    |                     
        |
===========            
''')
    elif vidas == 2:
        print('''
    +---+
    |   |
    0   |
   /|\  | 
        |                 
        |
===========            
''')
    elif vidas == 3:
        print('''
    +---+
    |   |
    0   |
   /|   | 
        |                 
        |
===========            
''')   
    elif vidas == 4:
        print('''
    +---+
    |   |
    0   |
    |   | 
        |                 
        |
===========            
''')   
    elif vidas == 5:
        print('''
    +---+
    |   |
    0   |
        | 
        |                 
        |
===========            
''')   
    elif vidas == 6:
        print('''
    +---+
    |   |
        |
        | 
        |                 
        |
===========            
''')  
        
#Sorteia palavra
palavra = sorteio()

#Gera palavra com _
tamanho = len(palavra)
adivinhada = "_" * tamanho
vidas = 6
letras = '' #LETRAS ESCOLHIDAS

jogoAtivo = True
#Jogo ativo
while jogoAtivo:
    
    #Estado do jogo
    forca(vidas)
    print(adivinhada)
    print(f"Letras já escolhidas: {letras.upper()}")

    #Valida letra 
    valida = False
    while not valida:
        letra = input("Escolha uma letra: ")
        if letra not in letras:
            valida = True
        else: print("Letra já foi escolhida!")
    letras += letra 

    #verifica se a letra ta na palavra
    if letra in palavra:
        #Troca os _
        for pos in range(tamanho):
            if letra == palavra[pos]:
              adivinhada = adivinhada[:pos] + letra + adivinhada[pos+1:]
    else:
        print("Esta letra não está na palavra")
        vidas -= 1
        if vidas == 0:
            forca(vidas)
            print(f'Você perdeu...')
            jogoAtivo = False

    if "_" not in adivinhada:
        print("Parabéns você ganhou! ")
        jogoAtivo = False

print(f"A palavra sorteada era {palavra.upper()}")