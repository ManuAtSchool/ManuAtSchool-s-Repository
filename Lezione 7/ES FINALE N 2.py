#ESERCIZIO 2
#Data la seguente lista di numeri:
# 1. Trova i Numeri Pari
# 2. Calcola la Somma dei Numeri Dispari
# 3. Trova il Numero Massimo

numeri = [12, 3, 7, 24, 5, 18, 9, 10, 15, 2]
for numero in numeri:
    if numero % 2 ==0:
        print(numero,"pari")
somma_dispari = 0
for numero in numeri:
    if numero % 2 != 0:
        somma_dispari+=numero
print("Somma dei numeri dispari:", somma_dispari)
massimo=max(numeri)
print("numero massimo", massimo)
