# -*- coding: utf-8 -*-

n=int(raw_input("Inserisci un numero naturale n maggiore di 1: "))
primo=True # ipotizziamo che N sia primo
for i in range(2,n): # test di divisibilità
    if n%i==0:
        primo=False
if primo: # se N è primo
    print n," è un numero primo"
else:
    print n," non è un numero primo"