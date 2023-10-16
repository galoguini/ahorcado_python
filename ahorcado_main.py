import random #importo la librería random para poder usar la función randint
import os #importo la librería os para poder usar la función cls
os.system("cls") #limpio todo lo que esté puesto antes en la consola

#region listas hardcodeadas
palabras = ["casa", "perro", "gato", "auto", "computadora", "celular", "teclado", "mouse", "auriculares", "monitor", "ventana", "puerta", "silla", "mesa", "cama"]
letras_abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
#endregion

#declaro variables y listas:
palabra_aleatoria = palabras[random.randint(0, len(palabras) - 1)] #selecciono una palabra aleatoria de la lista palabras y la cargo en una variable
gano = False
juego = True
intentos = 0
letras_adivinadas = []
letras_ingresadas = []
letras_ingresadas_no_validas = []

#region Mensajes
msjBienvenida = '''

 █████  ██   ██  ██████  ██████   ██████  █████  ██████   ██████  
██   ██ ██   ██ ██    ██ ██   ██ ██      ██   ██ ██   ██ ██    ██ 
███████ ███████ ██    ██ ██████  ██      ███████ ██   ██ ██    ██ 
██   ██ ██   ██ ██    ██ ██   ██ ██      ██   ██ ██   ██ ██    ██ 
██   ██ ██   ██  ██████  ██   ██  ██████ ██   ██ ██████   ██████  

            ¡Bienvenido al juego del ahorcado! 
'''
msjReglas = '''
Reglas del juego:

Este juego consiste en adivinar la palabra secreta 🤫

Para adivinarla tenés 6 intentos en los que ingresás 
una letra por vez. ¡Ojo! Sólo letras sin acentuaciones, tampoco 
ingreses caracteres especiales o números. A medida que ingreses 
cada letra éstas se posicionarán en el lugar que les corresponden 
para que puedas adivinar la palabra más fácilmente.

Si te quedás sin intentos... 😵  ¡AHORCADO! 😵 

Así que pensá bien antes de ingresar una letra o 
intentar adivinar la palabra.

Nota: escribi "$salir" para salir cuando estas jugando
'''
msjVictoria = '''
🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢
        GANASTE     
    ¡Adivinaste la  
        palabra!           
🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢
        '''
msjDerrota = '''
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
      PERDISTE     
   ¡No adivinaste  
     la palabra!          
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
        '''
msjDespedida = ''' 
¡Muchas gracias por jugar al ahorcado! 
¡Espero que te hayas divertido!
'''
msjMenu = '''
\nPresioná 1 para jugar.
Presioná 2 para ver las reglas.
Presioná 3 para salir.\n
'''
#endregion

def muñequito_ASCII(etapa): #función para mostrar el muñequito en ASCII según los intentos
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
    elif etapa == 6:
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

def mostrar_palabra(palabra_aleatoria, letras_adivinadas): #función para mostrar la palabra con guiones bajos mientras no se adivinen las letras
    resultado = ''
    for letra in palabra_aleatoria:
        if letra in letras_adivinadas:
            resultado += letra + ' ' #agrega la letra adivinada en el lugar donde estaba el guión
        else:
            resultado += '_ ' #agrega un guión bajo en el lugar donde no se adivinó la letra
    return resultado.strip()

def estadisticas_jugador(gano): #función para mostrar si ganó o no, junto a las estadísticas del jugador
    if gano:
        print(msjVictoria)
    else: 
        print(msjDerrota)
    print("Estadísticas del jugador: ")
    print(f"Intentos fallidos: {intentos}")
    print("Letras ingresadas: ", letras_ingresadas)
    print("Letras ingresadas no validas: ", letras_ingresadas_no_validas)
    print(f"La palabra secreta era: {palabra_aleatoria}\n\n")

print(msjBienvenida) #mensaje de bienvenida
while True: #loop infinito para que el juego comience solo si hace lo que el programa le pide
    ojito = input("\n🤐 Presiona ENTER para continuar...🤐 ")
    if len(ojito) == 0:
        break
    else:
        os.system("cls")
        print(msjBienvenida)
        print("\n🤬 DEJA DE HACERTE EL VIVO Y PRESIONA ENTER 🤬")
os.system("cls") #se limpia la bienvenida

print(msjBienvenida + msjMenu) #mensaje de bienvenida + opciones para jugar
while True: #loop infinito para que el usuario ingrese una opcion válida
    menu = input("Ingrese una opción: ") 
    if menu not in ["1", "2", "3"]: #verificamos que el usuario ingrese una opcion válida
        os.system("cls")
        print(msjBienvenida + msjMenu)
        print("🤬 DEJA DE HACERTE EL VIVO Y PRESIONA UNA OPCION CORRECTA 🤬\n")
        continue
    elif int(menu) == 1: #si el usuario ingresa 1, comienza el juego
        break
    elif int(menu) == 2: #si el usuario ingresa 2, se muestran las reglas
        os.system("cls")
        print(msjBienvenida + msjReglas + "\n")
        while True: #loop infinito para volver al menú solo si se hace lo que pide
            ojito = input("🤐 Presiona ENTER para continuar...🤐\n")
            if len(ojito) == 0:
                os.system("cls")
                print(msjBienvenida + msjMenu)
                break
            else:
                os.system("cls")
                print(msjBienvenida + msjReglas)
                print("\n🤬 DEJA DE HACERTE EL VIVO Y PRESIONA ENTER 🤬\n")
    elif int(menu) == 3: #si el usuario ingresa 3, se cierra el programa
        os.system("cls")
        print(msjBienvenida + "\n\n¡Hasta la próxima!\n")
        print(muñequito_ASCII(6))
        print(msjDespedida)
        exit()
os.system("cls") #limpia el menú

while juego: #loop infinito, para que el juego se vuelva a ejecutar siempre que el usuario quiera seguir jugando
    print("Nota: escribi ""$salir"" para salir del juego")
    while intentos < 6 and not gano: #loop para que el juego se ejecute mientras no se gane ni se excedan los intentos
        print(muñequito_ASCII(intentos)) #llamamos a la función que muestra el muñequito según los intentos
        print(mostrar_palabra(palabra_aleatoria, letras_adivinadas)) #llamamos a la función que muestra la palabra con guiones bajos y letras adivinadas
        print("Intentos anteriores: ")
        for letras in letras_ingresadas: #muestra el historial de letras ingresadas validas
            print(letras, end=" ")
        print("\nVeces que te hiciste el vivo y no pusiste una letra: ")
        for letras in letras_ingresadas_no_validas: #muestra el historial de letras ingresadas no validas
            print(letras, end=" ")

        letra = input("\n\nIngresa una letra o la palabra secreta: ").lower() #pido al usuario que ingrese una letra o la palabra secreta y la paso a minúscula
        os.system("cls")  # Limpia la consola

        if letra == "$salir": #verifico si el usuario quiere salir
            os.system("cls")
            print(muñequito_ASCII(6))
            print(msjDespedida)
            exit()

        if len(letra) == 0: #verificamos si no ingresó nada
            print("⚠️ No ingresaste nada. ⚠️")
            continue
        elif len(letra) > 1: 
            if letra == palabra_aleatoria: #verificamos que no ingrese una palabra que no sea la secreta
                gano = True #si la palabra coincide con la secreta, gana
                break
            intentos += 1 # Incrementa los intentos si ingresa una palabra que no sea la secreta
            print("⚠️ Ingresaste una palabra incorrecta. ⚠️")
            letras_ingresadas.append(letra) # agrega la palabra ingresada a la lista de letras ingresadas
            continue
        elif letra not in letras_abecedario: #verificamos que no ingrese números ni caracteres especiales
            intentos += 1 # Incrementa los intentos si ingresa números o caracteres especiales
            print("⚠️ No se permiten números, caracteres especiales ni letras especiales. ⚠️")
            letras_ingresadas_no_validas.append(letra) # agrega la letra ingresada a la lista de letras ingresadas no validas
            continue

        letras_ingresadas.append(letra) # agrega la letra ingresada a la lista de letras ingresadas

        if letra in letras_adivinadas: # Verificamos si la letra ya fue adivinada
            intentos += 1 # Incrementa los intentos si la letra ya fue adivinada
            print("⚠️ Ya adivinaste esa letra, intenta otra vez. ⚠️")
            continue

        # Verificamos si la letra está en la palabra
        if len(letra) == 1: #verificamos que la letra ingresada sea solo una. Si ingresa más de una el programa funciona de formas no predecibles ni deseadas
            if letra in palabra_aleatoria:
                print("✅ ¡Correcto! ✅")
                letras_adivinadas.append(letra) # agrega la letra ingresada a la lista de letras adivinadas
            else:
                intentos += 1  # Incrementa los intentos si la letra es incorrecta
                print("🚫 Letra incorrecta. Intenta nuevamente. 🚫")
        else:
            intentos += 1 # Incrementa los intentos si me ingrea mas de 1 letra
            print("⚠️ Ingrese unicamente 1 letra o la palabra secreta ⚠️")

        # Verificamos si se adivinaron todas las letras
        if len(letra) == 1: #verificamos que la letra ingresada sea solo una. Si ingresa mas de una el programa funciona de formas no predecibles ni deseadas
            if set(letras_adivinadas) == set(palabra_aleatoria): #acá transformamos la lista en set y verifico que las letras ingresadas coincidan con las de la palabra secreta
                gano = True #si las letras ingresadas coinciden con las de la palabra secreta, gana
                break
        elif len(letra) == len(palabra_aleatoria): #acá verificamos que la longitud de la palabra ingresada sea la misma que la palabra secreta 
            if letra == palabra_aleatoria:
                gano = True #si la palabra coincide con la secreta, gana
                break

    os.system("cls") #se limpia todo lo que esté puesto antes en la consola

    estadisticas_jugador(gano) #llamo a la función que muestra las estadísticas del jugador
    while True: #loop infinito para que el usuario ingrese una opcion válida
        jugar = input("¿Querés volver jugar? (s/n): ").lower() #pregunto si quiere jugar y lo paso a minúscula
        if jugar not in ["s", "n"]: #verificamos que el usuario ingrese una opción válida
            os.system("cls")
            estadisticas_jugador(gano)
            print("🤬 DEJA DE HACERTE EL VIVO Y PRESIONA UNA OPCION CORRECTA 🤬\n")
            continue
        elif jugar == "s": #si el usuario ingresa s, se reinician las variables y listas para entrar al bucle del juego
            palabra_aleatoria = palabras[random.randint(0, len(palabras) - 1)]
            gano = False
            intentos = 0
            letras_adivinadas = []
            letras_ingresadas = []
            letras_ingresadas_no_validas = []
            os.system("cls")
            break
        elif jugar == "n":
            juego = False #si el usuario ingresa n, sale del bucle del juego
            os.system("cls")
            break

print(muñequito_ASCII(6)) #llamo a la función que muestra el muñequito en su estado muerto
print(msjDespedida+"\n\n\n") #mensaje de despedida y créditos

#fin del programa
