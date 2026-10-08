import abc


logicka_promenna = True
logicka_2 = False

print (logicka_promenna)
print (type(logicka_promenna))

print (logicka_promenna and logicka_2)
print (type(logicka_promenna and logicka_promenna))

print (logicka_promenna or logicka_2)
print (type(logicka_promenna or logicka_promenna))

print (not logicka_2)

print ("__________________________________________")

print (5 > 3)
print (5<3)

print (5>=3)
print (5<=3)
print (5>=5)

print (5==3)
print (5==5) #porovnání hodnot. 5 se rovná 5

print (5 !=6) #toto lepší, nerovná se
print (not 5==6) #toto funguje ale je hnusný

print (5>7 and 4==4)

print (5>7 and 4==4 or 5>4)

print ((5>7 and 4==4) or 5>4)

retezec_znaku = "ahoj kámo O´sheterhande"
print (retezec_znaku)
print (type (retezec_znaku))

text = "logicka_2"
netext = logicka_2

skladani_textu ="abc" + "def"
q="abc"
r="def"
s=q+r
print (skladani_textu)

print ("_"*60)

rozdil_mezi = "10" + "10" #dostanu jen text
a =10 + 10
print (rozdil_mezi)
print (a)
j=5 + "a" #nebude fungovat, hodí erorr
o=5
x=5 + int(o)
print (j)