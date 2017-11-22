


file = open('testfile.txt','r') 

text = file.read()
valeurs_string = text.split('[')[1].split(']')[0].split(',')


valeurs = []

for i in valeurs_string:
	valeurs.append(int(i))

print valeurs


import matplotlib.pyplot as plt
plt.plot(valeurs)
plt.show()