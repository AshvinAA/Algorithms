n=int(input())
trainArr=[]

class Trains():
    def __init__(self,train,time,destination):
        self.train=train 
        self.time=time
        self.asciiVal=ascii(train)
        self.destination=destination

def swap(arr,l,r):
    temp=arr[l]
    arr[l] = arr[r]
    arr[r] =temp

def ascii(str):
    sum=0
    for i in str:
        sum+= ord(i)
    return sum

def isSame(t1, t2):
    return t1.train == t2.train


def latestTime(t1,t2):
    t1hours,t1minutes= map(int ,t1.time.split(":"))
    t2hours,t2minutes= map(int ,t2.time.split(":"))

    t1totalminutes=t1hours*60 + t1minutes
    t2totalminutes=t2hours*60 + t2minutes

    result= max(t1totalminutes, t2totalminutes)

    if(result==t1totalminutes):
        return t1
    else:
        return t2

for i in range(n):
    line1 = input().split()
    train = Trains(line1[0], line1[6],line1[4])
    trainArr.append(train)

for i in range(n) :
    minIndex=i
    for j in range(i,n,+1):
       if(trainArr[j].asciiVal <= trainArr[minIndex].asciiVal):
            if(isSame(trainArr[minIndex],trainArr[j])):
                minIndex = trainArr.index(latestTime(trainArr[minIndex], trainArr[j]))
            else:
                minIndex=j
    
    swap(trainArr,i,minIndex)
        



    

for i in range(n):
    print(f"{trainArr[i].train} will departure for {trainArr[i].destination} at {trainArr[i].time}")








