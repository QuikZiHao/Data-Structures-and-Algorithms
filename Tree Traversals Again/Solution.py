#author:quikziii
#the thing whick pop out from the stack mean the father of the node
#build the tree first and use a golbal variable to store the output to avoid the
#end of the output gor spacekey

def output(tree,root):
    global ans
    if(tree[root]["left"]!=""):
        output(tree,tree[root]["left"])
    if(tree[root]["right"]!=""):
        output(tree,tree[root]["right"])
    ans = ans + str(tree[root]["digit"]) +" "

n = int(input())
tree = []
for i in range(n+1):
    tree.append({"digit":i,"left":"","right":""})#store the tree
locate = 1 #def the node we check
Pop = False
stack=[]
for i in range(1,n*2+1):
    command = input()
    if(i == 1):
        command = command.split()
        root = int(command[1])
        mother = int(command[1])
        stack.append(int(command[1]))
        continue
    if(command == "Pop"):
        mother = stack.pop()
    else:
        command = command.split()
        locate = int(command[1])
        stack.append(locate)
        if(tree[mother]["left"] == "" ):
            tree[mother]["left"] = locate
        else:
            tree[mother]["right"] = locate
        mother = locate
ans = ""
output(tree,root)
print(ans[:-1])
