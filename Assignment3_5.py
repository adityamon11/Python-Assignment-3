from MarvellousNum import *;

def main():
	arr = list();
	x = int(input("Enter the number of elements "));
	for i in range(0,x):
		arr.append(int(input("Enter the number ")));
	y = list(filter(ChkPrime,arr));
	#print(y)
	print(sum(y));
if __name__ == '__main__':
	main();
