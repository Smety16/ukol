#úkol A
jidloJedna=input("První jídlo: ")
jidloDva=input("Druhé jídlo: ")
jidloTri=input("Třetí jídlo: ")
kalorieJedna= int(input(""))
kalorieDva= int(input(""))
kalorieTri= int(input(""))
celkove_kalorie=kalorieJedna + kalorieDva + kalorieTri
print(celkove_kalorie)
#úkol B
aktivitaJedna= input("Zadejte první aktivitu: ")
aktivitaDva= input("Zadejte druhou aktivitu: ")
DelkaAktivityJedna= int(input("Kolik minut si vykonával první aktivitu? "))
DelkaAktivityDva= int(input("Kolik minut si vykonával druhou aktivitu? "))
delka = DelkaAktivityJedna + DelkaAktivityDva
celkovy_vydej= delka*5
print(celkovy_vydej)
#Lukáš Smetana #Adam Lucák
#společný úkol
print("Snědl jsi "and celkove_kalorie and " kcal")
print("Spálil jsi "and celkove_kalorie and " kcal")
spaleni= celkove_kalorie - celkovy_vydej
if (spaleni>0):
    print("Přebytek: "and spaleni)
else:
    print("Nedostatek: "and spaleni)