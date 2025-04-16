#Crea un programma che legge un numero inserito da un utente e stabilisce se questo numero è pari o dispari. Il programma si inerrompe se l'utente inserisce il numero 0
print("Pari/Dispari")
numero = None

while numero != 0:
    numero = int(input("Inserisci un numero (0 per uscire): "))
    if numero == 0:
        print("Programma terminato.")
    else:
        print("Il numero è pari." if numero % 2 == 0 else "Il numero è dispari.")


#Crea un programma per indovinare un numero segreto, fino a quando l'utente non inserisce il numero corretto composto da 3 cifre il programma continuera a dirgli che non è possibile
#entrare, ci sono un massimo di 4 tentativi, numero segreto 123
print("Indovina il numero segreto!")
numero_segreto = 123
tentativi = 4

while tentativi > 0:
    numero = int(input("Inserisci un numero a 3 cifre: "))
    if numero == numero_segreto:
        print("Accesso consentito!")
    else:
        tentativi -= 1
        print("Accesso negato. Riprova.")
        if tentativi > 0:
            print(f"Tentativi rimasti: {tentativi}")
        else:
            print("Hai esaurito i tentativi. Accesso bloccato.")
