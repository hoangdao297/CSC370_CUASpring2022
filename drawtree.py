def drawtree(parents,names):
    currentrootidx=0
    for i in range(len(parents)):
        if (parents[i]==-1):
            currentrootidx=i;break
    tree=["+-"+names[currentrootidx]]
    treehelper(parents,names,currentrootidx,tree,(len(tree[0])-1)*" ")
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
                    prefixchild=prefix+"|"+(len(node)-2)*" "
                else:
                    prefixchild=prefix+(len(node)-1)*" "
                treehelper(parents,names,i,tree,prefixchild)


names=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
parents=[-1,0,1,1,2,2,3,3,0,8,8,9,9,10,10]
tree=drawtree(parents,names)
for i in tree:
    print(i)