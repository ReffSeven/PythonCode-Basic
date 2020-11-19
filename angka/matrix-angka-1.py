"""
1 2 3 4 5 6 7 
2 3 4 5 6 7 6 
3 4 5 6 7 6 5 
4 5 6 7 6 5 4 
5 6 7 6 5 4 3 
6 7 6 5 4 3 2 
7 6 5 4 3 2 1 
"""
N = 7
for y in range(N):
	for x in range(1,N+1):
		Ax = (x + y)
		An = Ax if(Ax<=N) else(N-((N-Ax)*-1))
		print(An, end=" ")
	print("")
