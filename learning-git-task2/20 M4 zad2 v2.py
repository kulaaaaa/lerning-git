def dodawanie(x, y):
    return x + y
 
def odejmowanie(x, y):
    return x - y
 
def mnozenie(x, y):
    if x == 0 or y == 0:
        print('Nie możesz mnożyć przez zero!')
    else:
      return x * y

def dzielenie(x, y):
    if x == 0 or y == 0:
        print('Nie możesz dzielić przez zero!')
    else:
      return x / y
 
print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
 
while True:
    wybor = input("Wybierz (1,2,3,4): ")
 
    if wybor in ('1', '2', '3', '4'):
      while True:
        try:
          num1 = float(input("Podaj składnik 1.: "))
          num2 = float(input("Podaj składnik 2.: "))
        except ValueError:
          continue

        else:
          
          if wybor == '1':
            print("Dodaję", num1, "i", num2)
            print("Wynik to", dodawanie(num1, num2))
            break
                   
          elif wybor == '2':
            print("Odejmuję", num1, "i", num2)
            print("Wynik to", odejmowanie(num1, num2))
            break
 
          elif wybor == '3':
            print("Mnożę", num1, "i", num2)
            print("Wynik to", mnozenie(num1, num2))
            break

          elif wybor == '4':
            print("Dzielę", num1, "i", num2)
            print("Wynik to", dzielenie(num1, num2))
            break
    else:
        print("Niewłaściwy numer, wybierz ponownie")
        