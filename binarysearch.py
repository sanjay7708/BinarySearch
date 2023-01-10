def Binary(array,start,end,n):
	mid=(start+end)//2
	if array[mid]==n:
		print(mid)
	else:
		while start<end:
			if array[mid]>n:
				return Binary(array,start,mid-1,n)
			elif array[mid]<n:
				return Binary(array,mid+1,end,n)
if __name__=="__main__":
	array=[1,2,3,4,5,6,7,8,9,10]
	start=array[0]
	end=array[-1]
	print(array)
	n=int(input("Which Element Do Yo Want Search?:"))
	print(Binary(array,start,end,n))
	
