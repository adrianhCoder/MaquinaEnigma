import math, time


def generar_rotores():
    """
    Rotor mas rapido --> derecha
    rotor mas lento---> izquierda
     R0 = derecha RAPIDO
     R1= medio
     R2 = izquierdo LENT0
    """
    rotores = []
#rotores[1][0]
    R1 = []
    R1.append([16, 23, 10, 5, 4, 11, 7, 19, 9, 13, 24, 2, 0, 1, 15, 6, 18, 20, 21, 17, 25, 12, 14, 8, 22, 3])
    R1.append([19, 6, 18, 5, 8, 0, 23, 13, 3, 16, 10, 1, 12, 2, 17, 9, 25, 14, 7, 15, 21, 11, 24, 4, 20, 22])
    R2 = []
    R2.append([10, 14, 23, 8, 24, 1, 0, 13, 18, 16, 15, 22, 21, 6, 9, 17, 25, 11, 19, 2, 20, 12, 4, 3, 7, 5])
    R2.append([13, 15, 2, 1, 22, 23, 9, 8, 18, 17, 21, 11, 16, 24, 0, 10, 19, 5, 3, 12, 6, 7, 14, 25, 4, 20])
    R3 = []
    R3.append([25, 0, 17, 10, 1, 12, 16, 11, 15, 9, 24, 2, 18, 21, 19, 7, 5, 3, 8, 6, 23, 22, 13, 14, 4, 20])
    R3.append([7, 16, 1, 9, 23, 5, 8, 11, 18, 15, 21, 6, 22, 10, 12, 25, 0, 19, 2, 14, 20, 17, 13, 4, 24, 3])

    rotores.append(R1)
    rotores.append(R2)
    rotores.append(R3)

    """
    print(R1)
    print("\n")
    print("Rotoress")
    eje = "------------------------------------------------------------+----------------------------------------------------------------------------"
    print(eje)
    print(eje)
    print(eje)
    for x in rotores:
        print(x)
    print("\n")
    """
    return rotores


def introdusca_codigos_rotores():
    print("Introdusca los codigos de descifrado , son tres")
    print("A1 -A3 Comenzand de izquierda a derecha")
    print("Dos numeros como maximo")
    Final = []
    while len(Final) < 3:
        A1 = int(input("Introdusca el codigo A%i :  " % len(Final)))
        if A1 >= 24 or A1 < 1:
            print("Numero no disponible")
            print("\n")
        else:
            Final.append(A1)
    return Final


def encryptacion_militar():
    abecedario = "abcdefghijqlmnñopqrstuvwxyz"
    abecedario = abecedario.upper()
    Abc = []
    for x in abecedario:
        Abc.append(x)
    print("\n")
    print("En esta zona se agregara la encriptacion militar")
    print("Podras conectar 5 pares de letras")
    print("Ejemplo    AB ,  OK  ,  YU   ,QW  se imprimiran tus letras enlazadas")
    print("\n")

    Pares = []
    while len(Pares) < 5:
        print("Letras disponibles: %s " % Abc)
        par = str(input("Ingresa las dos letras del par %s:    " % (len(Pares) + 1)))
        print("\n")

        validar = 0
        for x in par:
            if x in Abc and par[0] != par[1]:
                validar += 1
        if validar == 2:
            for x in par:
                Abc.remove(x.upper())
            Pares.append(par)
        else:
            print("Error-------------------")

    print(Pares)
    return Pares


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def nuevo_abecedario():
    normal = 'ABCDEFGHIJQLMNÑOPQRSTUVWXYZ'
    Antigua = list(normal)
    remplazos = encryptacion_militar()
    normal = list(normal)

    for x in remplazos:
        valores = list(x)
        normal = swapPositions(normal, normal.index(valores[0]), normal.index(valores[1]))
    print(Antigua)
    print(normal)


def girar_rotor(a):
    global rotores
    primer_vuelta = rotores[a][0]
    primer_vuelta = primer_vuelta[-1:] + primer_vuelta[:-1]
# 123123123
    segunda_vuelta = rotores[a][1]
    segunda_vuelta = segunda_vuelta[-1:] + segunda_vuelta[:-1]

    rotores[a][0] = primer_vuelta
    rotores[a][1] = segunda_vuelta
    return True


def encriptar_texto(texto):
    rotores = generar_rotores()
    index = 12


    TextoFinal = ""
    for x in texto:
        rotores[0] = girar_rotor(rotores[0][0])

        rapido = int(rotores[0][0][index])
        medio = int(rotores[1][0][index])
        lento = int(rotores[2][0][index])

        if rapido == 1:
            # Girar medio rotor
            rotores[1] = girar_rotor(rotores[1][0])
        if medio == 1:
            # Girar lento rotor
            rotores[2] = girar_rotor(rotores[2][0])

        """
        rapido=int(rotores[0][0][index])
        medio=int(rotores[1][0][index])
        lento=int(rotores[2][0][index])

        print(rapido)
        print(medio)
        print(lento)
        """


def generar_diccionario_basico():
    numeros = ''
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {}
    for x in range(1, len(letras) + 1):
        dic[x - 1] = letras[x - 1]
    return dic


def entreada_rotores(numero):
    global rotores

    # Primer Rotor
    a = numero
    A1 = rotores[0][0].index(a)
    A2 = rotores[0][1].index(A1)
    # print(A2)

    # Segundo Rotor
    A3 = rotores[1][0].index(A2)
    A4 = rotores[1][1].index(A3)
    # Tercer rotor
    A5 = rotores[2][0].index(A4)
    A6 = rotores[2][1].index(A5)
    # Final

    final = A6
    return final



def salida_rotores(numero):
    global rotores

    guia = rotores[2][1][numero]
    G2 = rotores[2][0][guia]
    # Tercer rotor ---->
    G3 = rotores[1][1][G2]
    G4 = rotores[1][0][G3]
    # Segundo rotor --->
    G5 = rotores[0][1][G4]
    G6 = rotores[0][0][G5]
    # Final
    return G6


def espejo_reflector(letra):
    cleartxt = letra
    abc = "abcdefghijklmnopqrstuvwxyz"
    secret = "".join([abc[(abc.find(c) + 13) % 26] for c in cleartxt])
    return secret


def ingresar_letra(n):
    global rotores
    global reflector
    global num_to_letra
    global letra_to_num

    n = n.upper()
    letra_en_numero = letra_to_num[n]

    girar_rotor(0)

    if rotores[0][0].index(1) == 12:
        girar_rotor(2)
    if rotores[1][1].index(1) == 12:
        girar_rotor(3)

        # Ya casi acabamos :)))
    Entrada = entreada_rotores(letra_en_numero)
    Espejo = letra_to_num[espejo_reflector(num_to_letra[Entrada].lower()).upper()]
    Salida = salida_rotores(Espejo)
    return Salida


def configurar_rotores():
    conf = []
    while len(conf) < 3:
        txt = ("Ingrese un numero del 0-25 para el rotor %s" % len(conf))
        print(txt)
        z = int(input())
        if z >= 0 and z <= 25:
            conf.append(z)
    for i in range(0, len(conf)):
        while rotores[i][0][0] != conf[i]:
            girar_rotor(i)

    print("Configurados")
    print("\n")


def iniciar_maquina():
    global rotores
    global reflector
    global num_to_letra
    global letra_to_num
    rotores = generar_rotores()
    num_to_letra = generar_diccionario_basico()
    letra_to_num = {v: k for k, v in num_to_letra.items()}

    if input(str("Ingrese 1 para configurar rotores:   ")) == '1':
        configurar_rotores()

    a_encriptar = input(str("Ingrese el texto:"))
    # w = num_to_letra[ingresar_letra(a_encriptar)]
    a_encriptar = a_encriptar.replace(" ", "")
    texto = ''

    for x in a_encriptar:
        w = num_to_letra[ingresar_letra(x)]
        texto += w
    print(texto)


iniciar_maquina()

print("Finalizado")