'''
Created on Nov 10, 2015

@author: ds-ga-1007
'''
from getposition import *
from output import *

initial_capital=1000

def main():
    position_list=getposition()
    num_trials=get_num_trials()
    dothetrial(position_list,initial_capital,num_trials)
    
if __name__=="__main__":
    try:
        main()
    except(KeyboardInterrupt):
        print"Keyboard Interrupt"
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            









                