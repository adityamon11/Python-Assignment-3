def main():
	arr = list();
	x = int(input("Enter the number of elements "));
	for i in range(0,x):
		arr.append(int(input("Enter the number ")));
	arr.sort()
	print(arr[0])
if __name__ == '__main__':
	main();
