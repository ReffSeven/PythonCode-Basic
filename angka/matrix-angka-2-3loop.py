"""
1 2 3 4 5 6 7 
2 3 4 5 6 7 6 
3 4 5 6 7 6 5 
4 5 6 7 6 5 4 
5 6 7 6 5 4 3 
6 7 6 5 4 3 2 
7 6 5 4 3 2 1 
"""
N = 7;
for y in range(1, N):
	for x1 in range(y,N+1):
		print(x1, end=" ")
	for x2 in range(y-1):
		print((N-x2-2), end=" ")
	print("")
