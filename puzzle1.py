import math
from turtle import *
#Oscar Dabrowski
#Advent puzzle 1

#translate R L combinations into R,L,U,D
conversion_dic_L={
'L' : 'D',
'D' : 'R',
'R' : 'U',
'U' : 'L',
}

conversion_dic_R={
'R' : 'D',
'D' : 'L',
'L' : 'U',
'U' : 'R',
}

def rotate_vect(v,angle):
    v_res=[0,0]
    rot_matrix=[[math.cos(angle), -1*math.sin(angle)],[math.sin(angle),math.cos(angle)]]
    for i in range(len(rot_matrix)):
        for j in range(len(rot_matrix[0])):
            v_res[i]+=int(rot_matrix[i][j]*v[j])
    return v_res
        


def scalar_product(v1,v2):
    res=0
    for i in range(len(v1)):
        res+=v1[i]*v2[i]
    return res

def norm_vect(v):
    n=0
    for i in v:
        n+=i*i
    return math.sqrt(n)

#2D orthogonal scalar projection of vector a on vector b
#(=scalar value of the length of the projected vector)
def proj_a_b(a,b):
    proj=scalar_product(a,b)/norm_vect(b)
    return proj

def disp_vect(dist,curr_dir,prev_dir):
    v_res=[0, 0]
    new_dir=''
    #from current and previous directions, find next direction
    if prev_dir=='R':
        new_dir=conversion_dic_R[curr_dir]
    elif prev_dir=='L':
        new_dir=conversion_dic_L[curr_dir]
    else:
        new_dir=curr_dir
    #compute vector from direction
    if new_dir=='R':
        v_res=[1, 0]
    elif new_dir=='L':
        v_res=[-1, 0]
    elif new_dir=='U':
        v_res=[0, 1]
    elif new_dir=='D':
        v_res=[0, -1]
    #comput final displacement vector
    for i in range(len(v_res)):
        v_res[i]=v_res[i]*dist
    return [v_res, new_dir]

#previous dist set initially to Up as dic_L(U)->L and dic_R(U)->R
#initially equivalent to first direction from beginning
p_dist=''
c_dist=''
d_vect=[0, 0]
r_vect=[0, 0]
lst=''
lst2=[]
direction=''
with open('puzzle1.txt','r') as f:
    for ln in f:
        lst=lst+ln
lst=lst.split(',')
for i in lst:
    lst2.append(i.strip())#remove spaces

#print('proj=',proj_a_b([5,9],[10,3]))
#print(norm_vect([1,1]))
for i in lst2:
    d=i[1:]
    c_dist=i[0]
    #vector for computing L1 norm
    d_vect=disp_vect(int(d),c_dist,p_dist)
    #dir for turtle
    direction=i[0]#d_vect[1]
    p_dist=c_dist#old = new - but with regards to only L or R (not U,D)
    #print('d',d,'c_dist=',c_dist,'p_dist=',p_dist)
    #print('d_vect=',d_vect[0])
    #turtle display
    #print('dir=',d_vect[1])
##    if direction=='R':
##        right(90)
##        forward(int(d))
##    elif direction=='L':
##        right(90)
##        forward(int(d))
##    elif direction=='U':
##        forward(int(d))
##    elif direction=='D':
##        backward(int(d))
        
#print(rotate_vect([1,1],-math.pi/2))
done()
