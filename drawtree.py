def drawtree(parents,names):
    currentrootidx=0
    for i in range(len(parents)):
        if (parents[i]==-1):
            currentrootidx=i;break
    tree=["+-"+names[currentrootidx]]
    treehelper(parents,names,currentrootidx,tree,(2)*" ")
    return tree

def treehelper(parents,names,currentrootidx,tree,prefix):
    if (len(tree)==len(parents)):
        return
    else:
        for i in range(len(parents)):
            if (parents[i]==currentrootidx):
                multiple=0
                for j in range(i+1,len(parents)):
                    if (parents[j]==currentrootidx):
                        multiple=1;break
                node="+-"+names[i]
                toappend=prefix+node
                tree.append(toappend)
                if (multiple==1):
                    prefixchild=prefix+"|"+(3-2)*" "
                else:
                    prefixchild=prefix+(3-1)*" "
                treehelper(parents,names,i,tree,prefixchild)

def printtree(tree):
    for i in tree:
        print(i)

names=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
parents=[-1,0,1,1,2,2,3,3,0,8,8,9,9,10,10]
tree=drawtree(parents,names)
printtree(tree)
names1=["Root","SubB","LEAF1","LEAF2","LEAF3","SubA","LEAF4","LEAF5"]
parents1=[-1,0,1,1,0,0,5,5]
tree1=drawtree(parents1,names1)
printtree(tree1)