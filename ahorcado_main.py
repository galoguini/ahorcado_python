import random #importo la libreria random para poder usar la funcion randint
import os #importo la libreria os para poder usar la funcion cls
os.system("cls") #limpio todo lo q este puesto antes en la consola

#declaro las variables
palabras = ["agua", "barro"]
palabra_aleatoria = palabras[random.randint(0, len(palabras) - 1)] #selecciono una palabra aleatoria de la lista palabras y la cargo en una variable
gano = False
intentos = 0
letras_adivinadas = []
letras_ingresadas = []

def muñequito_ASCII(etapa): #funcion para mostrar el muñequito en ASCII segun los intentos
    if etapa == 1:
        muñeco = '''
        +-------+
        |       |
        |      😢
        |      
        |         
        |       
        ===========
        '''
    elif etapa == 2:
        muñeco = '''
        +-------+
        |       |
        |      😢
        |       |
        |          
        |       
        ===========
        '''
    elif etapa == 3:
        muñeco = '''
        +-------+
        |       |
        |      😢
        |       |
        |      /    
        |       
        ===========
        '''
    elif etapa == 4:
        muñeco = '''
        +-------+
        |       |
        |      😢
        |       |
        |      / \   
        |       
        ===========
        '''
    elif etapa == 5:
        muñeco = '''
        +-------+
        |       |
        |      😢
        |      /|
        |      / \   
        |       
        ===========
        '''
    elif etapa == 6: #no se llega a imprimir, pensa que hacer con esto
        muñeco = '''
        +-------+
        |       |
        |      💀
        |      /|\ 
        |      / \   
        |       
        ===========
        '''
    else:
        muñeco = '''
        +-------+
        |       |
        |      
        |      
        |         
        |       
        ===========
        '''
    return muñeco

def mostrar_palabra(palabra_aleatoria, letras_adivinadas): #funcion para mostrar la palabra con guiones bajos mientras no se adivinen las letras
    resultado = ''
    for letra in palabra_aleatoria:
        if letra in letras_adivinadas:
            resultado += letra + ' ' #agrega la letra adivinada en el lugar donde estaba el guion
        else:
            resultado += '_ ' #agrega un guion bajo en el lugar donde no se adivino la letra
    return resultado.strip()

def estadisticas_jugador(): #funcion para mostrar las estadisticas del jugador
    print("Estadísticas del jugador: ")
    print(f"Intentos fallidos: {intentos}")
    print("Letras ingresadas: ", letras_ingresadas)
    print(f"Lalabra secreta es: {palabra_aleatoria}\n\n")

while intentos < 6:
    print(muñequito_ASCII(intentos)) #llamo a la funcion q muestra el muñequito segun los intentos
    print(mostrar_palabra(palabra_aleatoria, letras_adivinadas)) #llamo a la funcion q muestra la palabra con guiones bajos y letras adivinadas
    print("Intentos anteriores: ")
    for letras in letras_ingresadas: #muestra el historial de letras ingresadas
        print(letras, end=" ")

    # El usuario ingresa una letra
    letra = input("\n\nIngresa una letra o la palabra secreta: ").lower() #pido al usuario q ingrese una letra o la palabra secreta y la paso a minuscula
    letras_ingresadas.append(letra) # agrega la letra ingresada a la lista de letras ingresadas

    os.system("cls")  # Limpia la consola

    # Verificamos si la letra ya fue adivinada
    if letra in letras_adivinadas:
        intentos += 1 # Incrementa los intentos si la letra ya fue adivinada
        print("⚠️ Ya adivinaste esa letra, intenta otra vez. ⚠️")
        continue

    # Verificamos si la letra está en la palabra
    if len(letra) == 1: #verifico que la letra ingresada sea solo 1 ya que si ingresa mas de 1 el programa funciona de formas no predecibles ni deseadas
        if letra in palabra_aleatoria:
            print("🟢 ¡Correcto! 🟢")
            letras_adivinadas.append(letra)
            
        else:
            intentos += 1  # Incrementa los intentos si la letra es incorrecta
            print("🚫 Letra incorrecta. Intenta nuevamente. 🚫")
    else:
        intentos += 1 # Incrementa los intentos si me ingrea mas de 1 letra
        print("⚠️ Ingrese unicamente 1 letra o la palabra secreta ⚠️")

    # Verificamos si se adivinaron todas las letras
    if len(letra) == 1: #verifico que la letra ingresada sea solo 1 ya que si ingresa mas de 1 el programa funciona de formas no predecibles ni deseadas
        if set(letras_adivinadas) == set(palabra_aleatoria): #aca transformo la lista en set y verifico que las letras ingresadas coincidan con las de la palabra secreta
            gano = True #si las letras ingresadas coinciden con las de la palabra secreta, gana
            break
    elif len(letra) == len(palabra_aleatoria): #aca verifico que la longitud de la palabra ingresada sea la misma que la palabra secreta 
        if letra == palabra_aleatoria:
            gano = True #si la palabra coincide con la secreta, gana
            break

#if else para mostrar si gano o perdio la partida, junto a sus estadisticas
if gano:
    os.system("cls")
    msjVictoria = '''
=====================
|      GANASTE      | 
|  ¡Adivinaste la   |
|      palabra!     |       
=====================
        '''
    print(msjVictoria)
    estadisticas_jugador()
else: 
    os.system("cls")
    msjDerrota = '''
=====================
|     PERDISTE      | 
|  ¡No adivinaste   |
|    la palabra!    |       
=====================
        '''
    print(msjDerrota)
    estadisticas_jugador()