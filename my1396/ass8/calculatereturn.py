'''
Created on Nov 10, 2015

@author: ds-ga-1007
'''
import numpy as np


class CalculateSingleDayReturn():
    def __init__(self,positions,initial_capital,num_trials):
        self.positions=positions
        self.position_value=initial_capital/self.positions
        self.num_trials=num_trials
        
    def return_of_oneday(self):
        cumu_ret=0
        rand_list=np.random.rand(self.positions)
        for i in range(self.positions):
            if rand_list[i] <=0.51:
                cumu_ret+=self.position_value*2
        return cumu_ret
    
    def repeat_ntimes_oneday(self):
        self.cumu_ret=np.ones(self.num_trials)
        self.daily_ret=np.ones(self.num_trials)
        for trial in range(self.num_trials):
            self.cumu_ret[trial]=self.return_of_oneday()
            self.daily_ret[trial]=(self.cumu_ret[trial]/1000)-1
'''            
instance=CalculateSingleDayReturn(10,1000,10)
instance.repeat_ntimes_oneday()
print instance.cumu_ret
print instance.daily_ret
'''
            