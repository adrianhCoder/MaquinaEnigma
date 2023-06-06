rotores = []
reflector = None
num_to_letra = {}
letra_to_num = {}


def iniciar_maquina():
    """
  Esta función inicia la máquina Enigma para encriptar el texto proporcionado.
  Recibe como parámetro el texto a encriptar.

  Y configuracion de rotores si se quiere personalizar, pues no es obligatorio
  Ejemplo 14,12,10 esto para tener una encriptacion personalizada.

  Inputs:
      texto_a_encriptar (str): El texto que se va a encriptar.
      configuracion_de_rotores: La configuracion de rotores que se desea usar [10,11,12], en caso
      de que se quiera confugurar , si no , se puede usar configuracion default

  Returns:
      Texto procesado (str)
  """
    global rotores, reflector, num_to_letra, letra_to_num

    rotores = generar_rotores()

    num_to_letra = generar_diccionario_letra_a_numero()

    """
    Este código crea un diccionario llamado letra_to_num que asigna a cada letra
    su correspondiente valor numérico. Utiliza el diccionario num_to_letra, el 
    cual contiene las letras como claves y los números como valores, para intercambiar 
    las claves y valores.
    """
    letra_to_num = {v: k for k, v in num_to_letra.items()}

    print(" Ingrese '1' para configurar rotores")
    if input(str("Enter para usar la configuracion predeterminada: ")) == '1':
        configurar_rotores()

    texto_a_encriptar = input(str("Ingrese el texto:"))

    # Eliminamos espacios
    texto_a_encriptar = texto_a_encriptar.replace(" ", "")
    texto = ''

    for letra in texto_a_encriptar:
        w = num_to_letra[ingresar_letra(letra)]
        texto += w

    return texto


def generar_rotores():
    """
    Rotor mas rapido --> derecha
    rotor mas lento---> izquierda
     r1 = derecha RAPIDO
     r2= medio
     r3= izquierdo LENT0
    """
    r1 = [[16, 23, 10, 5, 4, 11, 7, 19, 9, 13, 24, 2, 0, 1, 15, 6, 18, 20, 21, 17, 25, 12, 14, 8, 22, 3],
          [19, 6, 18, 5, 8, 0, 23, 13, 3, 16, 10, 1, 12, 2, 17, 9, 25, 14, 7, 15, 21, 11, 24, 4, 20, 22]]
    r2 = [[10, 14, 23, 8, 24, 1, 0, 13, 18, 16, 15, 22, 21, 6, 9, 17, 25, 11, 19, 2, 20, 12, 4, 3, 7, 5],
          [13, 15, 2, 1, 22, 23, 9, 8, 18, 17, 21, 11, 16, 24, 0, 10, 19, 5, 3, 12, 6, 7, 14, 25, 4, 20]]
    r3 = [[25, 0, 17, 10, 1, 12, 16, 11, 15, 9, 24, 2, 18, 21, 19, 7, 5, 3, 8, 6, 23, 22, 13, 14, 4, 20],
          [7, 16, 1, 9, 23, 5, 8, 11, 18, 15, 21, 6, 22, 10, 12, 25, 0, 19, 2, 14, 20, 17, 13, 4, 24, 3]]

    rotores_ = [r1, r2, r3]

    return rotores_


def girar_rotor(indice_rotor_a_girar):
    global rotores
    primer_vuelta = rotores[indice_rotor_a_girar][0]
    primer_vuelta = primer_vuelta[-1:] + primer_vuelta[:-1]
    # 123123123
    segunda_vuelta = rotores[indice_rotor_a_girar][1]
    segunda_vuelta = segunda_vuelta[-1:] + segunda_vuelta[:-1]

    rotores[indice_rotor_a_girar][0] = primer_vuelta
    rotores[indice_rotor_a_girar][1] = segunda_vuelta
    return True


def generar_diccionario_letra_a_numero():
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    diccionario = {}
    for x in range(1, len(letras) + 1):
        diccionario[x - 1] = letras[x - 1]
    return diccionario


"""
Aqui la letra pasara por todos los rotores
"""


def entrada_rotores(letra_en_numero):
    global rotores

    # Primer Rotor
    a1 = rotores[0][0].index(letra_en_numero)
    a2 = rotores[0][1].index(a1)
    # Segundo Rotor
    a3 = rotores[1][0].index(a2)
    a4 = rotores[1][1].index(a3)
    # Tercer rotor
    a5 = rotores[2][0].index(a4)
    a6 = rotores[2][1].index(a5)
    # Final

    final = a6
    return final


# Aqui la letra rebota en el sepejo reflector
def espejo_reflector(letra):
    cleartxt = letra
    abc = "abcdefghijklmnopqrstuvwxyz"
    secret = "".join([abc[(abc.find(c) + 13) % 26] for c in cleartxt])
    return secret


# aqui la letra regresa hasta dar el resultado final
def salida_rotores(numero):
    global rotores

    guia = rotores[2][1][numero]
    g2 = rotores[2][0][guia]
    # Tercer rotor ---->
    g3 = rotores[1][1][g2]
    g4 = rotores[1][0][g3]
    # Segundo rotor --->
    g5 = rotores[0][1][g4]
    g6 = rotores[0][0][g5]
    # Final
    return g6


def ingresar_letra(letra):
    global rotores
    global reflector
    global num_to_letra
    global letra_to_num

    letra = letra.upper()
    letra_en_numero = letra_to_num[letra]

    girar_rotor(0)

    if rotores[0][0].index(1) == 12:
        girar_rotor(2)
    if rotores[1][1].index(1) == 12:
        girar_rotor(3)

        # Ya casi acabamos :)))
    entrada = entrada_rotores(letra_en_numero)
    espejo = letra_to_num[espejo_reflector(num_to_letra[entrada].lower()).upper()]
    salida = salida_rotores(espejo)
    return salida


def configurar_rotores():
    configuracion = []
    while len(configuracion) < 3:
        txt = ("Ingrese un numero del 0-25 para el rotor %s" % len(configuracion))
        print(txt)
        numero_ingresado = int(input())
        if 0 <= numero_ingresado <= 25:
            configuracion.append(numero_ingresado)
    for i in range(0, len(configuracion)):
        while rotores[i][0][0] != configuracion[i]:
            girar_rotor(i)

    print("Configurados")
    print("\n")


print(iniciar_maquina())  # retorna la palabra procesada
