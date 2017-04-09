# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 20:56:29 2017

@author: Sachin
"""



from Queue import PriorityQueue
from heapq import *

case = 0
o = open('C-small-2-attempt1-out.txt','w')
with open('C-small-2-attempt0.in' , 'r') as f:
    first_line = f.readline()
    s_list = []
    for line in f:
        case+=1
        del s_list
        s_list = []
        cells, people = [int(x) for x in line.split(' ' )]
        heappush(s_list, (-cells, cells)) 
        ls = 0
        rs = 0
        for i in xrange(people):
            large = heappop(s_list)[1]
            if large == 1:
                ls = 0
                rs = 0
                
            elif large%2 == 0:
                rs = large/2
                ls = rs-1
                
            else:
                rs = large/2
                ls = rs
            heappush(s_list, (-ls, ls)) 
            heappush(s_list, (-rs, rs)) 

    
        o.write('Case #'+str(case)+': '+str(rs)+ ' '+ str(ls)+'\n')
    
o.close()
        
