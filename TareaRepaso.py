"""
Escribe un programa que muestre tu nombre en la pantalla.

Crea un programa que calcule y muestre el resultado de sumar 10 + 20.

Escribe un programa que pregunte al usuario su nombre y luego lo salude con un "Hola, [nombre]".

Crea un programa que muestre tu comida favorita en la pantalla.

Escribe un programa que reste 5 a 15 y muestre el resultado.

Crea un programa que pregunte al usuario cuántos años tiene y muestre el número en pantalla.

Escribe un programa que muestre en pantalla el nombre de tu mascota o, si no tienes, el de una mascota que te gustaría tener.

Crea un programa que multiplique 3 por 4 y muestre el resultado.

Escribe un programa que pregunte al usuario cuál es su color favorito y responda "¡Qué buen gusto! El [color] es genial."

Crea un programa que muestre la letra de tu canción favorita.

"""

#1. Escribe un programa que muestre tu nombre en la pantalla.

print("Franyino Ramirez")



#2. Crea un programa que calcule y muestre el resultado de sumar 10 + 20.

print(12 + 12)



#3. Escribe un programa que pregunte al usuario su nombre y luego lo salude con un "Hola, [nombre]".

nombre = input("Cual es tu nombre? ")
print("Hola, " + nombre)

#4. Crea un programa que muestre tu comida favorita en la pantalla.

print("Hamburguesa")

#5. Escribe un programa que reste 5 a 15 y muestre el resultado.

print(15 - 5)

#6. Crea un programa que pregunte al usuario cuántos años tiene y muestre el número en pantalla.

edad = input("Cual es tu edad? ")
print(edad)

#7. Escribe un programa que muestre en pantalla el nombre de tu mascota o, si no tienes, el de una mascota que te gustaría tener.

print("Tengo una mascota llamada Luna")

#8. Crea un programa que multiplique 3 por 4 y muestre el resultado.

print(3 * 4)

#9. Escribe un programa que pregunte al usuario cuál es su color favorito y responda "¡Qué buen gusto! El [color] es genial."

color = input("Cual es tu color favorito? ")
print("¡Qué buen gusto! El " + color + " es genial.")

#10. Crea un programa que muestre la letra de tu canción favorita.
 
import sys
from time import sleep

def printLyrics():
    lines = [
        ("I wanna da-", 0.06), 
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07), 
        ("I wanna rock your body", 0.08), 
        ("I wanna go", 0.08), 
        ("I wanna go for a ride", 0.068), 
        ("Hop in the music and", 0.07), 
        ("Rock your body", 0.08), 
        ("Rock that body", 0.069), 
        ("come on, come on", 0.035), 
        ("Rock that body", 0.05), 
        ("(Rock your body)", 0.03), 
        ("Rock that body", 0.049), 
        ("come on, come on", 0.035), 
        ("Rock that body", 0.08), 
    ]
    
    for line, delay in lines:

        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay)
        
        print("")
        
        sleep(0.1) 
        
printLyrics()
