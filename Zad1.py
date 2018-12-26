
# coding: utf-8

# In[12]:

def generatorKodówPocztowych(poczatek, koniec):
    listaKodow = []
    splittedPoczatek = poczatek.split("-")
    splittedKoniec = koniec.split("-")
    mergedPoczatek=int(splittedPoczatek[0]+splittedPoczatek[1])
    mergedKoniec=int(splittedKoniec[0]+splittedKoniec[1])
    for i in range(mergedPoczatek+1,mergedKoniec):
        listaKodow.append(str(i)[:2]+"-"+str(i)[2:])
    return listaKodow
print(generatorKodówPocztowych("79-900","80-155"))


# In[ ]:



