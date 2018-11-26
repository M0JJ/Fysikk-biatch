import pandas as pd
from pylab import *
import re

#lister
f = []
i = []
atomnr =[]
massenr =[]
massev = []

#Første fil som vi leser av
fil = open("atomer.txt","r")
linjer = fil.readlines()
fil.close()

#Fil som vi skriver, men tar bort de irrelevante linjene
fil = open("atomer2.txt","w")
for linje in linjer:
    if "Isotopic" in linje:
        linje = linje.replace('.','')
    elif "Notes" in linje:
        linje = linje.replace('.','')
    elif "Symbol" in linje:
        linje = linje.replace('.','')
    elif "Standard" in linje:
        linje = linje.replace('.','')
    else:
        fil.write(linje)    
fil.close()

#Åpner filen igjen sånn at vi kan lese av den
fil2 = open("atomer2.txt","r")

#Filen går inn i en string
nukleider = fil2.read()

#Finner alle integerne, heltallene, i stringen og lager en liste med de 
for s in nukleider.split():
    if s.isdigit():
        i.append(s)

#Finner de ulike atomnummerene og setter de i en liste
for n in range(0,len(i),2):
    atomnr.append(i[n])

#Finner de ulike massenummerene og putter de i en liste
for x in range(1,len(i),2):
    massenr.append(i[x])

#Finner flyt tallene i stringen
flyt = re.findall("\d+\.\d+", nukleider)

#Legger flyt tallene inn i en liste
for t in flyt:
    massev.append(t)

#Lager Dataframe
df = pd.DataFrame()
sa = pd.Series(atomnr)
sb = pd.Series(massenr)
sc = pd.Series(massev)
df['Atom Nr'] = sa.values
df['Masse Nr']= sb.values
df = df.drop(df.index[3179])
df = df.drop(df.index[3175])
df['Masse Vekt']= sc.values

print(df.describe())
