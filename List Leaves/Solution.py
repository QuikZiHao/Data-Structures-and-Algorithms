#author:quikziii
#use queqe to solve the problem so the tree can search with BFV,mean layer by layer

def findLeaf(Root,Tree):
    leaf = []
    queqe = [Tree[Root]]
    while(len(queqe)!= 0):
        node = queqe.pop()
        leftLeaf = node["leftLeaf"]
        if (leftLeaf != ""):
            leftLeaf = int(leftLeaf)
            queqe.insert(0,Tree[leftLeaf])
        rightLeaf = node["rightLeaf"]
        if (rightLeaf != ""):
            rightLeaf = int(rightLeaf)
            queqe.insert(0,Tree[rightLeaf])
        if(rightLeaf == "" and leftLeaf == ""):
            leaf.append(node["Value"])
    return leaf


n = int(input())
checkRoot = []
tree = []
leaf=[]
for i in range(0,n):
    checkRoot.append(i)
for i in range(0,n):
    information = input().split()
    node = {"Value":i,"leftLeaf":"","rightLeaf":""}
    if(information[0] != "-"):
        node["leftLeaf"] = int(information[0])
        try:
            checkRoot.remove(int(information[0]))
        except:
            checkRoot =checkRoot
    if(information[1] != "-"):
        node["rightLeaf"] = int(information[1])
        try:
            checkRoot.remove(int(information[1]))
        except:
            checkRoot =checkRoot
    if(information[0] != "-" and information[1] != "-"):
        leaf.append(i)
    tree.append(node)
root = checkRoot[0]
leaf = findLeaf(root,tree)
ans =""
for i in leaf:
    ans = ans + str(i) + " "
if(len(leaf)>0):
    ans = ans[:-1]
    
print(ans)

