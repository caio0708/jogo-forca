from random import choice
import os

def imprime(ponto, certas, erradas, palavra):
    os.system('cls')
    print("*************** Forca ***************")
    print("\n\nPalavra secreta: " + palavra + "\n\n")
    if(ponto == 0):
        print("=======[_] \n|| | \n|| \n|| \n|| \n||\nHHHHHHHHHHHH")
    elif(ponto == 1):
        print("=======[_] \n|| | \n|| o \n|| \n|| \n||\nHHHHHHHHHHHH")
    elif(ponto == 2):
        print("=======[_] \n|| | \n|| o \n|| | \n|| \n||\nHHHHHHHHHHHH")
    elif(ponto == 3):
        print("=======[_] \n|| | \n|| o \n|| /| \n|| \n||\nHHHHHHHHHHHH")
    elif(ponto == 4):
        print("=======[_] \n|| | \n|| o \n|| /|\ \n|| \n||\nHHHHHHHHHHHH")
    elif(ponto == 5):
        print("=======[_] \n|| | \n|| o \n|| /|\ \n|| / \n|| \nHHHHHHHHHHHH")
    elif(ponto == 6):
        print("=======[_] \n|| | \n|| o \n|| /|\ \n|| / \ \n||\nHHHHHHHHHHHH")
        
    print("\nLetras erradas:",erradas)
    print("Letras corretas:",certas)
    
def iniciaPalavra(tamanho):
    return '*'*tamanho
    
def sorteia():
    return choice(['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa',        'elefante', 'pirata', 'rato','arara', 'arame', 'familia', 'camisa', 'fazenda', 'cama', 'mesa', 'garfo','sapato', 'formiga', 'martelo','lagarto', 'lanche', 'copo', 'corpo', 'humano', 'laranja', 'pera','melancia', 'manteiga', 'sofa'])

def revelar_palavra(palavra, letras_descobertas):
    secreta = ''
    for letra in palavra:
        if letra in letras_descobertas:
            secreta += letra
        else:
            secreta += '*'
    return secreta

def main():
        x = sorteia()
        print(x) # VER GABARITO 
        secreta = iniciaPalavra(len(x))
        certas = []
        erradas = []  
        imprime(0, certas, erradas, secreta ) 
        
        i = 0
        while i <= 5 :
            letra = input('Digite uma letra: ')          
            palavra = list(x)                   
            
            if letra in palavra:
                certas.append(letra)
                palavra_revelada = revelar_palavra(x, certas)           
                imprime( i , certas, erradas, palavra_revelada )    
                
                if palavra_revelada == x:
                    print('\nParabéns!! Você Ganhou o jogo')
                    break
                          
            else:
                erradas.append(letra)
                imprime( i+1, certas, erradas, secreta )
                i+=1
            
            
main()


