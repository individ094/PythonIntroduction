# Booleans speichern den Wert 'true' oder 'false' der Variable.
# 'true' wurd zurück gegeben.

Zustand = True
print(Zustand)

# Vergleichsparameter

# '==' bedeutet 'ist gleich'
# '!=' bedeutet 'ist ungleich'
# '<' kleiner, oder '<=' kleiner geleich
# '>' größer, oder '>=' größer gelich

# !! ein einzelnes '=' wird benutzt um Variablen einen Wert zu zuweisen!!

num = 6

print(num >= 10)
print(num <= 6)
print(num!= 12)

# Ausgabe sollte False, True und True sein.


# If-Bedingungen

#if(condition):
#   doSometing()

condition = True

if condition:
    print('It is True 1')
else:
    print('It was False')

#condition != True

if condition:
    print('It is True 2')
else:
    print('It was False')
pass

# Komplexe Boolean Konditionen mit 'and' und 'or'

number = 1
str = 'boolean'

if str == 'boolean' and number == 1:
    print('Beide Bedingungn sind erfüllt')

# der 'in' Operator Untersucht ob ein Objekt in einem Container von Obgjekten vorkommt

x = 4
f = "found"
nums = [1, 2, 3, 4, 5, 6, 7, 4 ]
num4 = nums.count(4)

if x in nums:
    print("found", nums.count(4))

    print(nums.count(4), nums.count(2))

# der 'is' Operator bezieht sich nicht auf den Wert der Variable sondern auf die Art der Variable (z.B. ob eine Variable ein String ist)
str = 'python'
ist = str

if ist is str:
    print("'ist' ist ein String")

# der 'not' Operator negiert alle nachfolgenden Aussagen

if not (x < 2) :
    print("'X' ist nicht kleiner als 2")

