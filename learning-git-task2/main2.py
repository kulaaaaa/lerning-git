#Zadanie 1
print("Lista zakupów")
lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączki"],
    "warzywniak": ["marchewka", "seler", "rukola"],
}

new_lista_zakupow = dict((k.title(), v) for k, v in lista_zakupow.items())

for key, value in  new_lista_zakupow.items():
    value = [val.capitalize() for val in value]
    print("Idę do",key, "i kupuję tam:", value)

count = 0
for key, value in lista_zakupow.items():
   if isinstance(value, list):
      count += len(value)
print("W sumie kupuję", count, "produktów")

print("\n======================\n")


#Zadanie 2 "Drugie"
print("Liczby od 0 do 100 podzielne przez 2 podniesione do potęgi 3:")
for x in range(101):
   if x%5 == 0 and x>0:
       print(pow(x,3))
