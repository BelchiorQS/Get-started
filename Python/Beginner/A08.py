#Os valores booleanos
print(2 > 1)
print(2 < 1)
print(10 == 10)

a = 10
b = 5


if a > b:
    print("maior")
else:
    print("menor")

#Avaliar os valores e variáveis
print(bool(10))
print(bool("Belchior"))

#As class podem retorar valores booleanos
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#As funcoes podem retorar valores booleanos
def myFunction() :
  return True

print(myFunction())