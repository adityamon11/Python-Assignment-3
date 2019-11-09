
def main():
	arr = list();
	x = int(input("Enter the number of elements "));
	sum=0;
	for i in range(0,x):
		arr.append(int(input("Enter the number ")));
		sum = sum + arr[i];
	print(sum);

if __name__ == '__main__':
	main();
