#coding=utf-8
import numpy as np
import random
import time
import numba


class lifegame:
    def __init__(self,size_x,size_y):
        """Constructor"""
        self.size_x=size_x
        self.size_y=size_y
        self.terrace = np.zeros((size_x,size_y), dtype = [('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('u', 'i4')])  
        for x in range(1,size_x-1):
            for y in range(1,size_y-1):
                e=random.randint(0, size_x*size_y)
                #if e<=(size_x*size_y*0.1):
                if y==int(size_y/2):
                    self.terrace[x][y]=(x,y,1,34)      
        
        #u=self.terrace .reshape(1,size_x*size_y)
        #u=np.sort(u,order='u')   

    def iteration(self):
        
        #mesa=np.zeros((self.size_x,self.size_y), dtype = [('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('u', 'i4')]) 
        mesa=np.zeros((self.size_x,self.size_y), dtype = [('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('u', 'i4')]) 
        dd=[0,0,0,0,0]
        for x in range(1,self.size_x-1):
            for y in range(1,self.size_y-1):
                t1=time.time()
                life=self.terrace[x][y][2]
                robust=self.terrace[x][y][3]
                if life==70:
                    mesa[x][y]=(x,y,0,0)
                else:
                    t2=time.time()
                    lifes=9
                    coun_list=[]
                    coun_list.append(self.terrace[x-1][y-1])
                    coun_list.append(self.terrace[x][y-1])
                    coun_list.append(self.terrace[x+1][y-1])
                    coun_list.append(self.terrace[x-1][y])
                    coun_list.append(self.terrace[x+1][y])
                    coun_list.append(self.terrace[x-1][y+1])
                    coun_list.append(self.terrace[x][y+1])
                    coun_list.append(self.terrace[x+1][y+1])
                    coun=0
                    #a=np.array([self.terrace[x-1][y-1],self.terrace[x][y-1],self.terrace[x+1][y-1],self.terrace[x-1][y],self.terrace[x+1][y],self.terrace[x-1][y+1],self.terrace[x][y+1],self.terrace[x+1][y+1]],dtype = [('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('u', 'i4')])
                    t3=time.time()
                    
                    for con in coun_list:
                        if con[2]>0:
                            coun+=1
                        if con[3]>robust:
                            lifes-=1
                    t4=time.time()

                    if coun ==3:
                        if life>0:
                            mesa[x][y]=(x,y,life+1,abs(34-life))
                        else:
                            mesa[x][y]=(x,y,1,1)
                    elif coun==2:
                        if life>0:
                            mesa[x][y]=(x,y,life+1,abs(34-life)) 
                    elif coun<2:
                        mesa[x][y]=(x,y,0,0)
                    else: 
                        if lifes<4:
                            mesa[x][y]=(x,y,life+1,abs(34-life)) 
                        else:
                            mesa[x][y]=(x,y,0,0)  
                    t5=time.time()
                dd[0]=dd[0]+(t2-t1)
                dd[1]=dd[1]+(t3-t2)
                dd[2]=dd[2]+(t4-t3)
                dd[3]=dd[3]+(t5-t4)
                dd[4]=dd[4]+(t5-t1)
        
        self.terrace=mesa
        return np.where(self.terrace['z']>0)
