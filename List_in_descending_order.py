lst=[]
n=int(input("No.of elements : "))
for i in range(0,n):
    ele=input()
    lst.append(ele)
lst.sort(reverse = True)
print(lst)
