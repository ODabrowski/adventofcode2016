import math
from turtle import *
#Oscar Dabrowski
#Advent puzzle 1

def rotate_vect(v,angle):
    v_res=[0,0]
    rot_matrix=[[math.cos(angle), -1*math.sin(angle)],[math.sin(angle),math.cos(angle)]]
    for i in range(len(rot_matrix)):
        for j in range(len(rot_matrix[0])):
            v_res[i]+=round(rot_matrix[i][j]*v[j])
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
def proj(a,b):
    proj_a_b=scalar_product(a,b)/norm_vect(b)
    return proj_a_b

def add_vect(v1,v2):
    v_res=[0,0]
    if len(v1)!=len(v2):
        print('error : vectors have same length!')
    for i in range(len(v1)):
        v_res[i]+=v1[i]+v2[i]
    return v_res

p_dir='I'#initial, special case
c_dir=''
d_vect=[0, 1]#initial vector
#total displacement vector
d_vect_tot=[0,0]
lst=''
lst2=[]
direction=''

with open('puzzle1.txt','r') as f:
    for ln in f:
        lst=lst+ln

lst=lst.split(',')
for i in lst:
    lst2.append(i.strip())#remove spaces

for i in lst2:
    d=i[1:]
    direction=i[0]#d_vect[1]
    #turtle path display
    speed(30)
    if direction=='R':
        right(90)
        forward(int(d))
    elif direction=='L':
        left(90)
        forward(int(d))


disp_vect=[pos()[0], pos()[1]]
print(disp_vect)
#Manhattan distance is the sum of the projections on X and Y axis of the
#displacement vector
L1_norm=proj(disp_vect,[disp_vect[0],0])+proj(disp_vect,[0,disp_vect[1]])
#or just sum up the abs value of the components of the vector 
L1_norm_v2=abs(disp_vect[0])+abs(disp_vect[1])
print('Path length with Manhattan distance:',L1_norm)

print('Path length with Manhattan distance:',L1_norm_v2)


done()
