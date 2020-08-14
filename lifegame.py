import numba
import numpy as np
import random



@numba.njit
def initial(size_x,size_y):
    terrace = np.zeros((size_x,size_y), dtype = numba.int32)  
    for x in range(1,size_x-1):
        for y in range(1,size_y-1):
            if y==int(size_y/2) and x>size_x*0.1 and x< size_x*0.9:
                terrace[x][y]=(1)  
    return terrace


@numba.njit  
def iteration(terrace):
    size=terrace.shape
    size_x=size[0]
    size_y=size[1]
    mess=np.zeros((size_x,size_y), dtype = numba.int32) 
    for x in range(1,size_x-1):
        for y in range(1,size_y-1):
            if terrace[x][y]==70:
                mess[x][y]=0
            else:
                mo=[]
                mo.append(terrace[x-1][y-1])
                mo.append(terrace[x][y-1])
                mo.append(terrace[x+1][y-1])
                mo.append(terrace[x-1][y])
                mo.append(terrace[x+1][y])
                mo.append(terrace[x-1][y+1])
                mo.append(terrace[x][y+1])
                mo.append(terrace[x+1][y+1])
                lifes=9
                coun=0
                for xu in mo:
                    if xu>0:
                        coun+=1
                    if abs(35-xu)>abs(35-terrace[x][y]) and abs(35-terrace[x][y])<15:
                        lifes-=1
                        
                if coun ==3:
                    if terrace[x][y]>0:
                        mess[x][y]=terrace[x][y]+1
                    else:
                        mess[x][y]=1
                elif coun==2:
                    if terrace[x][y]>0:
                        mess[x][y]=terrace[x][y]+1
                elif coun<2:
                    mess[x][y]=0
                else:
                    if lifes<4:
                        mess[x][y]=terrace[x][y]+1
                    else:
                        mess[x][y]=0     
    return mess
                    
            
            


