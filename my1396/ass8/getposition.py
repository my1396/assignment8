'''
Created on Nov 10, 2015

@author: ds-ga-1007
'''
import sys
def getposition():
    position_list=list()
    
    try:
        tmp=raw_input("please input a list of positions to buy: e.g. 1,10,100,1000\n ")
    except(KeyboardInterrupt):
        sys.exit()
        
    if tmp=='quit':
        sys.exit()
    
    try:
        tmp_split=tmp.split(",")
        for item in tmp_split:
            position_list.append(int(item))
    except:
        print "Invalid Input"
        return getposition()
    
    return position_list

def get_num_trials():
    try:
        tmp=raw_input("please enter an interger as the repeat time for the trial:\n ")
    except(KeyboardInterrupt):
        sys.exit()
        
    if tmp=="quit":
        sys.exit()
        
    try:
        number_trials=int(tmp)
    except:
        print "Invalid Input"
        return get_num_trials()
    
    return number_trials

        
        
        
        
        
        
        
        
        
    