"""
1 2 3 4 5 6 7 
2 3 4 5 6 7 6 
3 4 5 6 7 6 5 
4 5 6 7 6 5 4 
5 6 7 6 5 4 3 
6 7 6 5 4 3 2 
7 6 5 4 3 2 1 
"""

N = 9;
for y in range(N):
	for x in range(1,N+1):
		Axy = (x+y)
		An = Axy if(Axy<=N) else(N-((N-Axy)*-1))
		print(An, end=" ")
	print("")
