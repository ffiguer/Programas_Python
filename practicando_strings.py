print('hola'+' '+'mi'+' '+'nombre'+' '+'es'+' '+'Fabio')#cadena de caracteres
string_1 ='la casa'#declaración de string_1
string_2= ' '#declaración de string_2
string_3= 'es verde'#declaración de string_3
string_total = string_1 + string_2 + string_3 #suma de cadenas
print(string_total)#impresion del string resultante
print("martes"[0])#captura de la letra de la posición 0
print("martes"[1])#captura de la letra de la posición 1
print("martes"[2])#captura de la letra de la posición 2
print("martes"[3])#captura de la letra de la posición 3
print("martes"[4])#captura de la letra de la posición 4
print("martes"[5])#captura de la letra de la posición 5
print("martes"[0:3])#captura de la letra de la posición 0
a=str.upper(string_1) #la primera cadena está en minuscula y la convierte a mayuscula
print(a) #imprime el contenido de la variable a
b="LA CAsA mUY FEA" #declaración de la variable b
b=str.lower(b) #se transforma a minuscula
print(b)#imprime el último contenido de b
b=b.strip("a") #la función strip busca en los extremos de la frase en donde hay letra a
print(b)#imprime el ultimo resultado
s = "Acaso hubo buhos aca"
t = s[2:9]+s[0:1]
print(t)
s="hola que tal"
print(len(s))
x="notar"
b=x.replace("v","n")
print(b)
