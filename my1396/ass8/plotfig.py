'''
Created on Nov 10, 2015

@author: ds-ga-1007
'''
import matplotlib.pyplot as plt

def plotfig(position,daily_ret):
    plt.hist(daily_ret,100,range=[-1,1])
    plt.xlim(-1,1)
    plt.title("histogram of "+ str(position)+" position")
    plt.xlabel("daily return")
    plt.ylabel("frequency")
    file_name= "histogram_"+ str(position).zfill(4)+"_pos.pdf"
    plt.savefig(file_name)
    plt.clf()
    
    