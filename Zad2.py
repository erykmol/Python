
# coding: utf-8

# In[2]:

def ZnajdzBrakujace(lista,n):
    listaBraujacyh = []
    for i in range(1,n+1):
        if i not in lista:
            listaBraujacyh.append(i)
    return listaBraujacyh
print(ZnajdzBrakujace([2,3,7,4,9],10))


# In[ ]:



