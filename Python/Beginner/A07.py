#citacoes dentro de citacoes
print("I'm Belchior Soares")
print('Estou "bem!"')

#String multiline

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#As cordas são matrizes
name = 'belchior'
print(name[0])

#Looping através de uma string
for x in "Belchior Soares":
    print(x)
    
#Check StringTras:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Cordas de ligacao
frase = "O amanha comeca hoje"
print(frase[:7])
print(frase[-2:-2])

#Modificadores de strings
dica = " A Lenda Nunca Morre! "
print(dica.upper()) #Maiusula
print(dica.lower()) #Minuscula
print(dica.strip()) #remove espacos
print(dica.replace("A", "a")) #Substitui caracteres
print(dica.split(" ")) #Divde a string de acordo ao paranetro

#concatenacao
print("ola" + "mundo") 

#Formatacao de string
idade = 20
print(f"Eu tenho de {idade} anos idade") ##f-strings

#personagem de escape
print("Sou o \"Belchior\" Soares")

#Metodos de strings
print(name.capitalize())
