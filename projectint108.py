print("Enter the details of starting year---")
day=input("Enter the Day of starting date in 00 format: ")
m=input("Enter the Month of starting date in 00 format:")
year=input("Enter the Year of starting date in 0000 format:")
print("Enter the details of ending year")
day2=input("Enter the Day of ending date in 00 format: ")
m2=input("Enter the Month of ending date in 00 format:")
year2=input("Enter the Year of ending date in 0000 format:")
print("The starting date is:",day+"/"+m+"/"+year)
print("The ending date is:",day2+"/"+m2+"/"+year2)
start=int(year)
end=int(year2)
l1=[]
l2=[]
if start<end:
    for i in range(start,end+1):
        if i%4== 0 and i%100!=0:
            l1.append((i))
        elif i%100==0 and i%400==0:
            l1.append(i)
        else:
            l2.append(i)
        i=i+1
print("The leap years between the range of given dates are: ",l1)
print("The non-leap years between the range of given dates are: ",l2)

