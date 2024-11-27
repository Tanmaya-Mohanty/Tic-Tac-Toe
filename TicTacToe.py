print("Tic-Tac-Toe!")

def subset_sum(l):
	for i in l:
		for j in l:
			for k in l:
				if i!=j!=k!=i and i+j+k==15:
					return True
	else:
		return False
					
def check():
	for i in a:
		if i.isdigit():
			break
	else:
		print("It's a draw!")
		exit()
	    	
l1=[]
l2=[]

a='''\n4 9 2
3 5 7
8 1 6\n'''

print(a)

while True:
	n1=input("Player 1, choose your number: ")
	l1.append(int(n1))
	a=a.replace(n1,'×')
	print(a)
	if len(l1)>2:
		if subset_sum(l1):
			print("Player 1 won!")
			exit()
		else:
			check()
	n2=input("Player 2, choose your number: ")
	l2.append(int(n2))
	a=a.replace(n2,'○')
	print(a)
	if len(l2)>2:
		if subset_sum(l2):
			print("Player 2 won!")
			exit()
		else:
			check()