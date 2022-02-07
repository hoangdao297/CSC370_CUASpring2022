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

def dirsort(dirarr):
    for i in range(len(dirarr)-1):
        minidx=i
        for j in range(i+1,len(dirarr)):
            if (comparetwodirisS1smallerthanS2(dirarr[j],dirarr[minidx])==1):
                minidx=j
        dirarr[i],dirarr[minidx]=dirarr[minidx],dirarr[i]
dirarr=["/a/b/","/ab/cd/","/c/d/","/a/b/c/","/ab/c/d/","/a/bc/d/","/a/b/cd/"]
dirsort(dirarr)
print(dirarr)
