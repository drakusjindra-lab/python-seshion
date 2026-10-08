cislo = 10
pocet_kusu_dobytka = 3

print (pocet_kusu_dobytka)
print (type(pocet_kusu_dobytka))

#co napíšu za hešteg není v kódu jen poznámka
nevim = cislo % pocet_kusu_dobytka  #zbytek po celočíselném dělení
print (nevim)
print (type(nevim))

nevim = cislo // pocet_kusu_dobytka #celočíśelné dělení, nezaokrouhlí ale zahodí desetiny aneb 7,654=7
print (nevim)
print (type(nevim))

nevim = cislo / pocet_kusu_dobytka #dělení
print (nevim)
print (type(nevim))

nevim = cislo * pocet_kusu_dobytka #krát
print (nevim)
print (type(nevim))

nevim = cislo ** pocet_kusu_dobytka #mocnina
print (nevim)
print (type(nevim))
print (2**(1/2)) #takže odmocnina ze 2. zlomek do odmocniny je mocnina 