"""
1 2 3 4 5 6 7 
2 3 4 5 6 7 6 
3 4 5 6 7 6 5 
4 5 6 7 6 5 4 
5 6 7 6 5 4 3 
6 7 6 5 4 3 2 
7 6 5 4 3 2 1 
"""
N = 7; Nd = 1; Nr = 0;
for y in range(1, N*N+1):
	Np = (Nd + Nr)
	Na = Np if(Np<=N) else(N-((N-Np)*-1))
	print(Na, end=" ")
	if(y%N==0): Nd = 1; Nr += 1; print("")
	else: Nd += 1
