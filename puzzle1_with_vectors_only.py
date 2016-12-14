import math
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
def disp_vect(v,cursor_dir):
    #normalize vector
    if v[0]!=0:
        v[0]=v[0]/abs(v[0])
    if v[1]!=0:
        v[1]=v[1]/abs(v[1])
    ###################
    if cursor_dir =='L':
        #-90 degree rotation
        v_res=rotate_vect(v,-math.pi/2)
    elif cursor_dir=='R':
        #90 degree rotation
        v_res=rotate_vect(v,math.pi/2)
    return v_res

p_dir='I'#initial, special case
c_dir=''
i_vect=[0, 1]#initial vector
#total displacement vector
d_vect_tot=[0,0]#initialized to 0 0 !
lst=''
lst2=[]
direction=''
temp_v=[0,0]
cnt=0
with open('puzzle1.txt','r') as f:
    for ln in f:
        lst=lst+ln

lst=lst.split(',')
for i in lst:
    lst2.append(i.strip())#remove spaces

for i in lst2:
    if cnt==0:
        if i[0]=='R':
            i_vect=[1,0]
        elif i[0]=='L':
            i_vect=[-1,0]
        cnt=cnt+1
    else:
        i_vect=disp_vect(i_vect,i[0])
    #print('i_vect=',i_vect)
    temp_v=i_vect
    temp_v[0]=temp_v[0]*float(i[1:])
    temp_v[1]=temp_v[1]*float(i[1:])
    #print('temp v=', temp_v)
    d_vect_tot=add_vect(d_vect_tot,temp_v)
    
    

print(d_vect_tot)
#Manhattan distance = sum of the projections (projx + proj y) or vallue of the sum of the abs val of the x y components
total_distance=abs(d_vect_tot[0])+abs(d_vect_tot[1])
print('Manhattan distance =' , total_distance)
#print('test rot:',rotate_vect([0, 1],math.pi/2))
