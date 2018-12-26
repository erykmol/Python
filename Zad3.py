
# coding: utf-8

# In[7]:

from decimal import Decimal

def GeneratorListy(poczatek, koniec, skok):
    DeciLista = []
    while(poczatek<koniec):
        poczatek+=skok
        DeciLista.append(Decimal(poczatek))
    return DeciLista   
        
print(GeneratorListy(2,5.5,0.5))       


# In[ ]:



