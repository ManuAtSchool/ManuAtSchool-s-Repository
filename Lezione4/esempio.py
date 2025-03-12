#esempio di dichiarazione e uso variabili
print("scrivi il tuo nome, Caro Utente!")

#per poter acquisire qualcosa che digita l'utente utilizzo la funzione print()
# nomeUser = "Manuel"
nomeUser = input()

print("Benvenuto", nomeUser)

#Facciamo la stessa cosa in modo più veloce passando come argomento all'input una frase
#funzione(argomento)--> tutto questo si chiama FIRMA del METODO
cognomeUser = input("Scrivi il tuo cognome")
print("il tuo cognome è" , cognomeUser)
#ATTENZIONE: Tutto ciò che recupero da un utente è considerato una string, un testo. Per poter fare un calcolo devo fare
#il type CASTING, ovvero forzare quella variabile ad essere un numero e non una stringa
num1 = int(input("scrivi il primo numero"))
num2 = int(input("scrivi il secondo numero"))
somma = num1 + num2
print("la somma vale", somma)

num3 = int("3")
num4 = int("6")
somma2 = num3 + num4
print(somma2)

