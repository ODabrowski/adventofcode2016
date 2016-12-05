import math
from turtle import *
#Oscar Dabrowski
#Advent puzzle 1

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

def add_vect(v1,v2):
    v_res=[0,0]
    if len(v1)!=len(v2):
        print('error : vectors have same length!')
    for i in range(len(v1)):
        v_res[i]+=v1[i]+v2[i]
    return v_res
        

#Compute displacement vector.
#if same direction between 2 calls of the function e.g. R->R or L->L in the puzzle,
#then do a 90 degrees rot else if different e.g. R->L or L->R do a -90 degrees rot
def disp_vect(v,curr_dir,prev_dir):
    v_res=[]
    if prev_dir=='I':
        #convention for initial
        if curr_dir=='R':
            v_res=[1,0]
        elif curr_dif=='L':
            v_res=[-1,0]
    else:
        if prev_dir != curr_dir:
            #-90 degree rotation
            v_res=rotate_vect(v,-math.pi/2)
        else:
            #-90 degree rotation
            v_res=rotate_vect(v,math.pi/2)
    return v_res

p_dir='I'#initial, special case
c_dir=''
d_vect=[0, 0]
v=[0,1]#initial vector
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
    c_dir=i[0]
    #total displacement vector for computing L1 norm
    d_vect=add_vect(d_vect,disp_vect(v,c_dir,p_dir))
    print('d_v=',d_vect)
    #dir for turtle
    direction=i[0]#d_vect[1]
    p_dir=c_dir#old = new
    #print('d',d,'c_dist=',c_dist,'p_dist=',p_dist)
    #print('d_vect=',d_vect[0])
    #turtle path display
    speed(20)
    if direction=='R':
        right(90)
        forward(int(d))
    elif direction=='L':
        left(90)
        forward(int(d))

goto(0,0)
color("red")
goto(d_vect[0],d_vect[1])
#print(d_vect)
#print(rotate_vect([1,1],-math.pi/2))
#print('test=',add_vect([1,2],[-5,1]))
done()
