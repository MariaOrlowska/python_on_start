warzywa=["marchewka", "salata", "ogorek", "kapusta", "kalafior"]


for idx in range(len(warzywa)):
    print("idx: "+str(idx)+" : "+warzywa[idx])

lista="a,b,c,d,e"
print(",".join(warzywa))
print(lista.split(","))
del warzywa[1]
print(warzywa)
warzywa[2]="pietruszka"
print(warzywa)
warzywa.append("pomidor")
print(warzywa)
