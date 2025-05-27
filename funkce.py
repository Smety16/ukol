
menu=["1. Pozdrav","2. Dnešní den","3. Čísla 1 až 5","4. Obdélník z hvězdiček","5. Nálada dne","6. Konec"]
for i in menu:
    print(i)
volba=input("Zadejte číslo: ")
if volba == "1":
    pozdrav()
elif volba == "2":
    den()
elif volba == "3":
    cisla()
elif volba == "4":
    obdelnik()
elif volba == "5":
    nalada_dne()
elif volba == "6":
    print("Ukončuji program.")
else:
    print("Neplatná volba, zkus to znovu.")

def pozdrav():
    print("Ahoj! Jak se máš?")
pozdrav()
 
def den():
    print("Zadejte dnešní den: ")
    den = input()
    print(den)
den()
   
 
def cisla():
    cisla = (1,2,3,4,5)
    print(cisla)
cisla()
 
def obdelnik():
    hvezdy="*****"
    for i in range(3):
        print(hvezdy)
obdelnik()
 
def nalada_dne():
    nalady = ["veselá", "smutná", "unavená", "líná", "autistická"]
    vybrana_nalada = random(nalady)
    print("Dnešní nálada je:", vybrana_nalada)

