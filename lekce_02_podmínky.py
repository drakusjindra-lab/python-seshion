vek = 27
print ("Muj vek je: "+str(vek))

if vek >= 18 and vek < 70: #dvojtečka mega důležitá
    print("Jsem dospělý") #pokud podmínka if platí vše co je za ní odsazené se stane
    print("Tak pojďme chlastat") #mezera je 1 tab
elif vek <= 15:
    print("jsem mladivství")
    print("a chlastat můžu jen když vypadám na 18")
elif vek > 70:
    print("jsem fosílie")
else:
    print("Jsem dítě") #nesplní se IF udělá se else
    print("....Ale stejně jdem chlastat")


muj_vek= vek

if muj_vek >=70:
    print ("Jsem, dospělý a dostávám od státu prachy")

    if muj_vek >= 80:
        print ("ti mladivství jsou dneska arogantní to za mích mladých let......")

    if muj_vek < 25:
        print ("mučí mě ve škole")

else:
    print("chodím do práce a místo romantického života mám kočku")

print ("Tečka.") 