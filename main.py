P = str(input('-> '))
ltt = input('-> ')
lettre = []
for i in ltt :
  lettre.append(i)
#print(lettre)
nombre = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
i = True
t = 0
while i:
    nb = nombre[0]
    nombre[0] = nb + 1
    for i in nombre:
        if len(lettre) in nombre:
            tour = 0
            for n in nombre:
                if int(n) == int(len(lettre)):
                    changement = tour
                tour = tour + 1
            nombre[changement] = 0
            target = changement + 1
            nb = nombre[target]
            nombre[target] = int(nb) + 1

    position = 0
    total = len(nombre) - 1
    final = []
    while position < total:
        if int(nombre[position]) != -1:
            po = int(nombre[position])
            lf = lettre[po]
            final.append(str(lf))
        position = position + 1
    mot = ''.join(final)
    if mot == P :
        print(t)
        i = False
    t += 1
