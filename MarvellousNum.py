from math import sqrt;
def ChkPrime(number):
	flag=0;
	for i in range(2,int(sqrt(number))+1):
		if(number%i==0):
			flag=1;

	if(flag==0):
		return number;
