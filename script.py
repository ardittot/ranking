import numpy as np
import matplotlib.pyplot as plt
#from collections import Counter

## GENERATE USER ID FOR EACH TRANSACTION
TOTAL = 10000
MAX = 4000
filename = "transaction - uid.txt"
fout = open(filename,'w')
for i in range(1,TOTAL):
	uid = str(np.random.random_integers(MAX) - 1) + "\n"
	fout.write(uid)

fout.close()

## EXTRACT LIST OF NAMES TO VARIABLE
filename = "list - name.txt"
#fin.readline()
with open(filename,'r') as fin:
	list_name = [line.rstrip('\n') for line in fin]

## ANNOTATE NAME FOR EACH TRANSACTION
finname = "transaction - uid.txt"
foutname = "transaction - name.txt"
fin = open(finname,'r')
fout = open(foutname,'w')
for line in fin:
	idx = int(line)
	fout.write(list_name[idx] + "\n")

fin.close()
fout.close()

## EXTRACT LIST OF DOMICILE TO VARIABLE
filename = "list - domicile.txt"
#fin.readline()
with open(filename,'r') as fin:
	list_dom = [line.rstrip('\n') for line in fin]

## ANNOTATE Journey-from FOR EACH TRANSACTION
finname = "transaction - uid.txt"
foutname = "transaction - from.txt"
fin = open(finname,'r')
fout = open(foutname,'w')
for line in fin:
	idx = int(line)
	fout.write(list_dom[idx] + "\n")

fin.close()
fout.close()

## EXTRACT LIST OF Area TO VARIABLE
filename = "list - area.txt"
#fin.readline()
with open(filename,'r') as fin:
	list_area = [line.rstrip('\n') for line in fin]

list_local = list_area[0:6]
list_country = ["Singapore", "Malaysia", "Thailand", "Hongkong", "Vietnam", "Filipina", "Australia", "Kamboja"]

## ANNOTATE Journey-to FOR EACH TRANSACTION
finname = "transaction - from.txt"
foutname = "transaction - to.txt"
fin = open(finname,'r')
fout = open(foutname,'w')
for line in fin:
	pl = line.rstrip('\n')
	list_to = list(list_area)
	list_to.remove(pl)
	if pl != "Jakarta":
		for area in list_country:
			list_to.remove(area)
		
	
	N = len(list_to)
	idx = np.random.random_integers(N) - 1
	fout.write(list_to[idx] + "\n")

fin.close()
fout.close()

## SET THE FLIGHT PRICE
list_price_overseas = np.array([350, 670, 670, 1500, 2000, 1700, 3000, 1500])
list_price_domestic = np.zeros(shape=(6,6), dtype=np.int)
filename = "list - price_dom.txt"
fin = open(filename,'r')
for irow in range(6):
	line = fin.readline()
	lprice = line.rstrip('\n')
	lprice = lprice.strip().split('\t')
	for icol in range(6):
		list_price_domestic[irow,icol] = lprice[icol]
	


## SET THE TRANSACTION Price
finname = "transaction - from.txt"
finname2 = "transaction - to.txt"
foutname = "transaction - price.txt"
fin = open(finname,'r')
fin2 = open(finname2,'r')
fout = open(foutname,'w')
for line in fin:
	jfrom = line.rstrip('\n')
	jto = fin2.readline()
	jto = jto.rstrip('\n')
	if jfrom != "Jakarta":
		icol = list_local.index(jfrom)
		irow = list_local.index(jto)
		price = list_price_domestic[irow,icol]
	else:
		if jto in list_country:
			icol = list_country.index(jto)
			price = list_price_overseas[icol]
		else:
			icol = list_local.index(jfrom)
			irow = list_local.index(jto)
			price = list_price_domestic[irow,icol]
		
	
	price1 = (np.random.rand() * (1.2 - 0.75) + 0.75) * price
	price2 = (np.random.rand() * (1.2 - 0.75) + 0.75) * price
	price = int(price1 + price2)
	fout.write(str(price) + '\n')
	

fin.close()
fout.close()

## EVALUATE TOTAL PURCHASE OF EACH USER
foutname = "list - purchase.txt"
fout = open(foutname,'w')

## EXTRACT LIST OF NAMES TO VARIABLE
filename = "list - name.txt"
with open(filename,'r') as fin:
	list_name = [line.rstrip('\n') for line in fin]

#list_name = ["Leah Bower"]
for name in list_name:
	totalprice = 0
	finname1 = "transaction - name.txt"
	finname2 = "transaction - price.txt"
	finname3 = "transaction - from.txt"
	finname4 = "transaction - to.txt"
	fin1 = open(finname1,'r')
	fin2 = open(finname2,'r')
	fin3 = open(finname3,'r')
	fin4 = open(finname4,'r')
	for line1 in fin1:
		line2 = fin2.readline()
		line3 = fin3.readline()
		line4 = fin4.readline()
		line1 = line1.rstrip('\n')
		line2 = int(line2.rstrip('\n'))
		line3 = line3.rstrip('\n')
		line4 = line4.rstrip('\n')
		#print(name + " " + line1 + " " + str(line2))
		if name == line1:
			totalprice = line2 + totalprice
	fout.write(str(totalprice) + "\n")
	fin1.close()
	fin2.close()
	fin3.close()
	fin4.close()

fout.close()
	
## EXTRACT LIST OF NAMES TO VARIABLE
filename = "list - purchase.txt"
with open(filename,'r') as fin:
	list_purchase = [int(line.rstrip('\n')) for line in fin]

list_uid = range(4000)

sort_purchase = sorted(list_purchase)
sort_uid = sorted(range(len(list_purchase)), key=lambda k: list_purchase[k])

## EXTRACT LIST OF TOP100: RANK#1 Total Purchase
foutname = "rank1 - totalpurchase.txt"
fout = open(foutname,'w')
for i in range(100):
	idx = sort_uid[- (i+1)]
	fout.write(str(list_purchase[idx]) + "\n")

fout.close()

foutname = "rank1 - name.txt"
fout = open(foutname,'w')
for i in range(100):
	idx = sort_uid[- (i+1)]
	fout.write(str(list_name[idx]) + "\n")

fout.close()

## EXTRACT LIST OF TOP100: RANK#2 Freq Purchase
filename = "transaction - uid.txt"
fin = open(filename,'r')
list_ntran = np.zeros(shape=(4000), dtype=np.int)
for line in fin:
	tuid = int(line.rstrip('\n'))
	tnum = list_ntran[tuid]
	tnum = tnum + 1
	list_ntran[tuid] = tnum

fin.close()

sort_ntran = sorted(list_ntran)
sort_uid_tran = sorted(range(len(list_ntran)), key=lambda k: list_ntran[k])

foutname = "rank2 - name.txt"
fout = open(foutname,'w')
for i in range(100):
	idx = sort_uid_tran[- (i+1)]
	fout.write(str(list_name[idx]) + "\n")

fout.close()

foutname = "rank2 - ntransaction.txt"
fout = open(foutname,'w')
for i in range(100):
	idx = sort_uid_tran[- (i+1)]
	fout.write(str(list_ntran[idx]) + "\n")

fout.close()

