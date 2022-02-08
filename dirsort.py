def dirstringprocess(s,stringlist):
    tempstring=""
    for i in range(1,len(s)):
        if (s[i]=="/"):
            stringlist.append(tempstring);tempstring=""
        else:
            tempstring+=s[i]

def comparetwodirisS1smallerthanS2(s1,s2):
    s1list=[];s2list=[]
    dirstringprocess(s1,s1list)
    dirstringprocess(s2,s2list)
    if (len(s1list)<len(s2list)):
        return 1
    elif(len(s1list)>len(s2list)):
        return 0
    else:
        for i in range(len(s1list)):
            if (s1list[i]==s2list[i]):
                continue
            elif (s1list[i]>s2list[i]):
                return 0
            else:
                break
    return 1

def dirsortSelectionSort(dirarr):
    #Time complexity: (n^3)
    for i in range(len(dirarr)-1):
        minidx=i
        for j in range(i+1,len(dirarr)):
            if (comparetwodirisS1smallerthanS2(dirarr[j],dirarr[minidx])==1):
                minidx=j
        dirarr[i],dirarr[minidx]=dirarr[minidx],dirarr[i]

def dirsortQuickSort(dirarr):
    #Time complexity: (n^2)logn
    pass

dirarr=["/a/b/","/ab/cd/","/c/d/","/a/b/c/","/ab/c/d/","/a/bc/d/","/a/b/cd/","/"]
dirarr1=["/","/usr/","/usr/local/","/usr/local/bin/","/games/","/games/snake/","/homework/","/temp/downloads/"]
dirarr2=["/usr/","/usr/local/","/bin/","/usr/local/bin/","/usr/bin/","/bin/local/","/bin/local/"]
dirarr3=["/","/a/","/b/","/c/","/d/","/e/","/f/","/g/"]
dirarr4=["/","/a/","/b/","/c/","/d/","/e/","/f/","/g/","/a/a/","/b/g/c/","/g/f/"]
dirarr5=["/a/b/c/d/e/f/g/h/i/j/k/l/m/n/","/o/p/q/r/s/t/u/v/w/x/y/z/"]
#dirarr.sort()
#print(dirarr)
dirsortSelectionSort(dirarr)
dirsortSelectionSort(dirarr1)
dirsortSelectionSort(dirarr2)
dirsortSelectionSort(dirarr3)
dirsortSelectionSort(dirarr4)
dirsortSelectionSort(dirarr5)
print(dirarr);print(dirarr1);print(dirarr2);print(dirarr3);print(dirarr4);print(dirarr5)
