import random

#vytvoření pole
arraya = [1, 69, 52, 49, 3, 85, 41, 22, 23,]

#změnění pateho čisla na 34
arraya[5] = 34

#vypsaní prvního prostředního a posledního čísla
print (arraya[0])
print (arraya[4])
print (arraya[8])

#vypsání sedmého čísla
print(arraya[7])

#vypsání délky pole
print(len(arraya))

#vypsání min a max jednotky pole
print(min(arraya))
print(max(arraya))

#vytvoření druheho pole
arrayb = [5, 89, 56, 96, 42, 4, 8, 32, 72]

#sečitaní polí
print(sum(arraya + arrayb))

#sečítaní pateho a prvního čisla z pole 2
print(sum([arrayb[5] + arrayb[1]]))

#tady se randomizuje  druhe pole
random.shuffle(arrayb)
print(arrayb)
