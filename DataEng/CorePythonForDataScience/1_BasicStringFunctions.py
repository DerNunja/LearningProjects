string = "    Hello, world! \t\t\n"
string = string.strip() #entfernt whitespace, tabulatoren \t und neue zeilen \n; lstrip() und rstrip() entfernen jeweils links und rechts vom string
print(string)

stringX = "xxHello, world!xx"
stringX = stringX.strip("x") #entfernt bestimmte Zeichen
print(stringX)


string = string.split() #wenn nicht spezifizert wird bei jedem whitespace gesplitet und alle aufeinader folgenden whitespaces werden zusammengefasst
print (string)

string = "www.google.com"
string = string.split(".")
print(string)


glue = ", "
string = glue.join(string) #join() , joins eine  liste von strings zu Einem mit dem object string "glue" als kleber 
print(string)

string = "1.617.305.1985"
string = "-".join(string.split(".")) # split wandelt in eine liste von strings um und join verwandelt diese wieder zu Einem, so können z.B "-" mit "." getauscht werden
print(string)

string = "This string\n\r has    many\t\tspaces"
string = " ".join(string.split())
print(string)


string = "www.google.com"
needle = ".com"
found = string.find(needle) #gibt den index des gefunden teil zurück, wenn dieser nicht gefunden wird -1
print(found)


string = "www.google.com"
tocount = "."
counted = string.count(tocount) #gibt zurück wie oft das zu zählende Element gefunden wurde
print(counted)