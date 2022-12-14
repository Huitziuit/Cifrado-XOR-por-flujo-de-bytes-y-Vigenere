import random

#codificacion ERARMA = Posicion de la letra en al arregloa abc multiplicado por 3
abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]

def positionABC(character):
  return abc.index(character)

def vCipher(m):
  print("\n----------------------- VIGERENTE CIPHER --------------------------")
  c=[]
  k=randomKeyVigerente(len(m))
  print(f"RANDOM KEY VIGERENTE:\n{k}\n")
  for i in range(len(m)):
    c.append(abc[(positionABC(m[i]) + positionABC(k[i])) % 75])
    strC=''.join(c)
  print(f"VIGERENTE CIPHER:\n{strC}\n")
  return c

def vDescipher(c):
  print("\n----------------------- VIGERENTE DECIPHER --------------------------")
  k=input("\nENTER VIGERENTE KEY:\n")
  m=[]
  print(f"VIGERENTE CIPHER:\n{c}\n")
  for i in range(len(c)):
    m.append(abc[(positionABC(c[i]) - positionABC(k[i])) % 75])
  strM=''.join(m)
  print(f"############## DESCIPHER MESSAGE ###############\n{strM}\n")
  return strM

def decBin(numbers):#recibe arreglo de int
  bin = ''
  for num in numbers:
    modulos = []
    while num != 0:
      # se almacena el módulo en el orden correcto
      modulos.insert(0, num % 2)
      num //= 2 
    while len(modulos) !=8:
      modulos.insert(0,0)
    bin += ''.join(map(str, modulos))
  return bin 
  #retorna string con los binarios

def binDec(bin): #se recive string de los binarios de todos los bytes
  dec=[]
  for i in range(0,len(bin),8):
    byte=bin[i:i+8]
    posicion = 0
    decimal = 0
    byte = byte[::-1]
    for digito in byte:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    dec.append(decimal)
  return dec
  #Retorna arreglo con los decimales

def randomKeyXor(numBytes):
  r=[]
  for i in range(numBytes):
    r.append(random.randint(0,256))
  return(decBin(r))

def randomKeyVigerente(numCharacters):
  key=[]
  for i in range(numCharacters):
    key.append(abc[random.randint(0,75)])
  strKey=''.join(key)
  return(strKey)

def xorCipher(m): #el parametro es el array de caracteres cifrado por vegerente
  print("\n----------------------- XOR CIPHER --------------------------")
  dec=[]
  for ch in m:
    dec.append(positionABC(ch)*3)
  mBin=decBin(dec)
  print(f"BINARY MESSAGE:\n{mBin}\n")
  keyXor=randomKeyXor(len(m))
  print(f"RANDOM KEY XOR:\n{keyXor}\n")
  xorCipher=[]
  for i in range(len(mBin)):
    xorCipher.append('1') if mBin[i] != keyXor[i] else xorCipher.append('0')
  strM=''.join(xorCipher)
  print(f"XOR ( BINARY MESSAGE + RANDOM KEY XOR )\n{strM}\n")

def xorDecipher():
  print("\n----------------------- XOR DECIPHER --------------------------")
  mBin= input(f"ENTER CIPHER MESSAGE:\n")
  keyXor=input(f"ENTER KEY XOR:\n")
  xordecipher=[]
  for i in range(len(mBin)):
    xordecipher.append('1') if mBin[i] != keyXor[i] else xordecipher.append('0')
  strM=''.join(xordecipher)
  print(f"XOR DECIPHER:\n{strM}\n")
  ch=[]
  dec=binDec(strM)
  for num in dec:
    ch.append(abc[num//3])
  return ''.join(ch)

def Cipher():
  m=input('MESSAGE: ')
  xorCipher(vCipher(m))

def Decipher():
  c=xorDecipher()
  vDescipher(c)


#------------------Debug-----------
Cipher()
Decipher()  