#author:quikziii
#max to store the maximun answer run again the list and add the number one
#by one to the temp if temp equal to negative mean infront sublist is useless
#if temp bigger than maximun mean that the temp is the bigger sublist
#ispositive flag to check if the all the element in the list is negative

N = int(input())
numberArray = [int(element) for element in input().split()]
sublist =[]
anslist=[]
max = numberArray[0]
temp = 0
isPositive = False
for i in numberArray:
    if(i>=0):
        isPositive =True
    temp = temp + i
    sublist.append(i)
    if(temp>max):
        max = temp
        anslist =[]
        anslist.extend(sublist)
    if(temp<0):
        temp=0
        sublist = []

    
if(isPositive):
    try:
        print(max,anslist[0],anslist[len(anslist)-1])
    except:
        print(max,max,max)
else:
    print(0,numberArray[0],numberArray[len(numberArray)-1])
    
