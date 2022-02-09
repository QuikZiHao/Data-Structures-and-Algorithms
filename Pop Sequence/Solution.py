#author:quikziii
#use one list to store the input list and another list to be the stack
#if the stack over maximun size or after stacking the stack still remain element
#return False else return True

def solve(size,maximun):
    stack = []
    upper = 0
    check=list(map(int,input().split()))
    count = 0
    if(check==1):
        return True
    for i in range (1,size+1):
        stack.append(i)
        temp = i 
        upper = upper +1
        if(upper == maximun+1):
            return False
        while(temp == check[count]):
            out = stack.pop()
            upper = upper - 1
            count = count + 1
            if(count == size):
                return True
            if(upper> 0):
                temp = stack[upper-1]
    if(upper != 0):
        return False
            
    
maximun,size,case=map(int,input().split(" "))
for i in range(case):
    if(solve(size,maximun)):
        print("YES")
    else:
        print("NO")        
        
