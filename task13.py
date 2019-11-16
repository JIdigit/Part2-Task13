number=int(input())
print('Our number is '+str(number))
my_nums=range(1,number,1)
i=0
while my_nums[i]*my_nums[i]<=number:
    print(str(my_nums[i]**2))
    i+=1