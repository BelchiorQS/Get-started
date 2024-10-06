varible_nome = "Belchior"
VarableIdade = 20

print("Nome: "+varible_nome)
print("Idade: "+str(VarableIdade)) #casting

print(type(varible_nome)) #Obter o  tipo de dados

#Muitos valores para várias variáveis
nome, apelido, Sobre_Nome = "Belhior", "Quirinda", "Soares"

print(nome)
print(apelido)
print(Sobre_Nome)

#Um valor para várias variáveis
x = y = z = "QS"
print(x, y, z)

#descompactamento
frutas = ["banana","manga","limao"]
b, m, l = frutas
print(b, m, l)

#variavel global

j = "aqui"

def call():
    print(j)
call()

def myfunc():
  global x  #Podemos transformar uma variavel em global
  x = "fantastic"

myfunc()
print("Python is " + x) 
