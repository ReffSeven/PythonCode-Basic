"""
Memisahkan angka Ganjil dan Genap

100    20   2020 50 
    11    5         
"""

n_data = [100, 11, 20, 5, 2020, 50]
t_genap = ""
t_ganjil = ""
for i in n_data:
	i_len = len(str(i))
	if i % 2 == 0:
		t_genap += str(i) + " "
		t_ganjil += (i_len * " ") + " "
	else:
		t_ganjil += str(i) + " "
		t_genap += (i_len * " ") + " "
print(t_genap)
print(t_ganjil)
