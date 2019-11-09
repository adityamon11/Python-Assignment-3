def main():
	
	x = int(input("Enter the number of elements "));
	for i in range(0,x):
		arr.append(int(input("Enter the number ")));

def search(num1):
	count=0;
	for i in range(len(arr)):
		if(arr[i]==num1):
			count = count+1;
	print(count);

if __name__ == '__main__':
	arr = list();
	main();
	y = int(input("Enter element to search"))
	search(y);