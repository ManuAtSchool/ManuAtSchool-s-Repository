nomeUtente = "Manuel Farinato"
#in questo caso, utilizzo il simbolo + per concatenare le stringhe
presentazione = "Ciao " + nomeUtente + " questa è la calcolatrice più semplice"
print(presentazione)
numero1 = 42.3
numero2 = 6.4
#calcolare le 4 operazione matematiche di base
somma = numero1 + numero2
print("la somma vale:", somma)
prod = numero1 * numero2
print("il prodotto vale:", prod)
sottr = numero1 - numero2
print("la sottrazione vale:", sottr)
div = numero1 / numero2
print("il quoziente vale:", div)
#ora faremo le potenze, eleviamo alla potenza 2 entrambi i numeri
potenza1 = numero1 **2
potenza2 = numero2 **2
print("la potenza del primo numero vale:", potenza1)
print("la potenza del secondo numero vale:", potenza2)
#ora calcoleremo la radice quadrata, utilizzando le potenze
radice1 = numero1 ** (1/2)
radice2 = numero2 ** (1/2)
print("la radice del primo numero vale:", radice1)
print("la radice del secondo numero vale:", radice2)
numeroProva= 2
elevazioneNeg = numeroProva ** (-2)
print(elevazioneNeg)
numeroProva2 = -2
elevazionePos = numeroProva2 ** 2
print(elevazionePos)
#metodo 2
numero3 = 4
#elevo sto numero alla potenza 2
potenza3 = pow(numero3, 2)
print("la potenza di", numero3, "alla seconda vale", potenza3)
#calcolo la radice di 4 utilizzando la funzione sqrt
#devo importare la libreria math, librerie da utilizzare gia dentro il programma, se invece non ci fossero, importare da in alto nella pagina
import math
radice3 = math.sqrt(numero3)
print("la radice di", numero3, "vale", radice3)



