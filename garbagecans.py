import random
import time
import thread


class GarbageCanAggregator:
     def __init__(self):
         self.cans = []
     def register_can(self,garbagecan):
         self.cans.append(garbagecan)
     def remove_can(self,garbagecan):
         self.cans.remove(garbagecan)
     def get_info(self):
         for can in self.cans:
             print can.getlevel()

class GarbageCan:
     def __init__(self,canid,areaid,currentLevel,maxCapacity,xcord,ycord):
         self._canid = canid
         self._areaid = areaid
         self._currentLevel = currentLevel
         self._maxCapacity = maxCapacity
         self._location = [xcord,ycord]

     def getlevel(self):
         return self._currentLevel

     def changelevel(self,newval):
         self._currentLevel = newval

def print_agg_info(threadname,AGGREGATOR):
     timeout = time.time() + 100
     while True:
         if time.time() > timeout:
             print threadname + ' runtime over\n'
             break
         inner_timeout =time.time()+7
         while True:
             if time.time() > inner_timeout:
                 print '\n----'+threadname+' AGGREGATOR INFO---------\n'
                 AGGREGATOR.get_info()
                 break

def change_cans_level(threadname,cans):
    timeout = time.time() + 80
    while True:
        if time.time() > timeout:
            print threadname + ' runtime over\n'
            break
        inner_timeout = time.time()+5
        while True:
            if time.time() > inner_timeout:
                print '\n-----------'+threadname+' UPDATE IN CANS----------------\n'
                new_currentlevels = []
                [new_currentlevels.append(random.randint(0,30)) for x in xrange(len(cans))]
                print new_currentlevels

                for x,can in enumerate(cans):
                    can.changelevel(new_currentlevels[x])
                break

if __name__ == '__main__':

    canid = [1,2,3,4,5]
    areaid = 100
    currentlevel = [10,15,5,25,12]
    maxcapacity = 30
    xcord = [41.13,45.55,56.67,42.32,47.770]
    ycord = [67.89,65.44,64.32,67.78,69.90]


    cans = []
    global AGGREGATOR
    AGGREGATOR =  GarbageCanAggregator()


    for x in xrange(5):
         g = GarbageCan(canid[x],areaid,currentlevel[x],maxcapacity,xcord[x],ycord[x])
         cans.append(g)

    for can in cans:
        AGGREGATOR.register_can(can)

    print '\n----INITIAL AGGREGATOR INFO---------\n'
    AGGREGATOR.get_info()


    #try:
    thread.start_new_thread(change_cans_level,("THREAD 1",cans))
    thread.start_new_thread(print_agg_info,("THREAD 2",AGGREGATOR))

    while True:
        pass




