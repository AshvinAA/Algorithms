import sys

class Train:
    def __init__(self, name , destination , time ):
        self.name=name 
        self.destination = destination
        self.time = time 
        
    
trains = []

no_of_inputs= int(sys.stdin.readline())

for i in range( no_of_inputs ):
    train_now = sys.stdin.readline().split()   
    train= Train(train_now[0] , train_now[4] , train_now[6] )
    trains.append(train)
    
trains.sort( key = lambda t: t.time , reverse=True)
trains.sort(key = lambda t:t.name.swapcase())

def printer(trains):
    for train in trains:
        print (f"{train.name} will depart for {train.destination} at {train.time}")
        
printer(trains)