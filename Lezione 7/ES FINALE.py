# Scrivi un programma che stampa
# tutti i numeri da 1 a 100.
# Per i multipli di 3 stampa "BOOM"
# Per i multipli di 5 stampa "ZOOM"
# Per i multipli di 3 e 5 stampa
#  "BAZINGA"

#Esempio
# 1
# 2
# 3 - BOOM
# 4
# 5 - ZOOM
# .
# .
# .
# 15 - BAZINGA
for numero in range(1,100):
    if numero % 3 ==0 and numero % 5 ==0:
        print(numero,"BAZINGA")
    elif numero % 3 ==0:
        print(numero,"BOOM")
    elif numero % 5 ==0:
        print(numero,"ZOOM")
    else:
        print(numero)