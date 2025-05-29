import random
#Esta función valida si el valor es J Q K y retorna 10 en caso dado
def Valor(valor):
    if type(valor)==int:
        return valor
    elif(valor=="J" or valor=="Q" or valor=="K"):
        return 10
    elif valor == "A":
        return 11  # El As es inicialmente 11
    else:
        return 0
#esta función suma la lista haciendo uso de recursión
def sumbaraja(baraja):
    if baraja==[]:
        return 0
    return Valor(baraja[0][0])+sumbaraja(baraja[1:])

 #verifica el estado del az, realmente esta es función que se llama para sumar           
def az(baraja):
    if baraja == []:  
        return 0
    if baraja[0][0] == "A":  # Si la carta actual es un A
        if sumbaraja(baraja[1:]) <= 10:  #suma restante menor o igual a 10
            return 11 + az(baraja[1:])  # cuenta el A como 11
        else:
            return 1 + az(baraja[1:])  # cuenta el A como 1
    else:
        return Valor(baraja[0][0]) + az(baraja[1:])



#Aun no se validan repetidos
def pedirCarta(baraja,mano):
    print("TURNO DEL JUGADOR")
    while(True):
     if(input("1: Pedir Carta\n0: Plantar\n")=="1"):
          mano.append(baraja[random.randint(0,51)])
          print("\n")
          print(f"Mano: {mano}")
          print(f"Valor: {az(mano)}")
          if(az(mano)>21):
              print("Perdiste")
              break

     else:
          break
    return mano

#Da las primeras 2 cartas
def manoInicial(baraja,mano):
    print("\n")
    for i in range(2):
        mano.append(baraja[random.randint(0,51)]) 
    print(f"Su mano inicial es: {mano}\nEl valor es: {az(mano)}")
    return mano

#Crea la baraja en orden
def crearBaraja():
	return [(u,p) for u in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] for p in ["D","C","T","P"]]

#Retorna la bajara en desorden
def mezclar():
	return random.sample(crearBaraja(),len(crearBaraja()))
#aqui juega la casa
def juegoCasa(baraja,mano):
    #El while true lo rompo solo cuando supera los 21 o solo cuando se planta
    while(True):
        if(az(mano)<=16):
            print("\n")
            mano.append(baraja[random.randint(0,51)])
            print("LA CASA PIDIO CARTA")
            print(f"Mano: {mano}")
            print(f"Valor: {az(mano)}")
        elif(az(mano)>21):
            print("LA CASA PERDIO")
            break
        else:
            print("LA CASA PLANTA")
            break
    return mano

#Mano 1 va a ser el jugdor y mano 2 va a ser el dealer
#Tocó crear la función ganador por que sino no sabia como poner mas de una condición y que no se hicieran 2 juegos distintos
def ganador(mano1,mano2):
    if (az(mano2)<az(mano1)<22) or az(mano2)>21:
        print("----------GANO EL JUGADOR----------")
    else:
        print("--------GANO LA CASA----------")
ganador(pedirCarta(mezclar(),manoInicial(mezclar(),[])),juegoCasa(mezclar(),manoInicial(mezclar(),[])))