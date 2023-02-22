from cmath import pi
import math
from turtle import clear

def calculate(n_scans, resolution, length = 1, width = 0.6, lidar_pos = (0.3, 0.9)):
    n = n_scans # the number of raw laser scans
    res = resolution # resolution for descritezed scans
    l = length # region len
    w = width # region width
    x, y = lidar_pos
    inc = 2*pi/n # increment
    ''' Center is the lidar position, phase number are shown below:
                     \ 5|4 /
                    6 \ | / 3
                       \|/
              ----------O --------
                       /|\  
                    7 / | \ 2
                     / 8|1 \
    
    '''

    index= []
    safe_ranges=[]
    
    # *******************   Phase I   *****************************
    # 含中线，不含角线
    for i in range(int(w/2/res)):
        index.append(round(math.atan((i)* res/y)/inc))
        safe_ranges.append(math.sqrt(math.pow((i)*res, 2) +  math.pow(y ,2) ))
    
    # *******************   Phase II   *****************************   
    # 不含横线，含角线
    for i in range(int(y/res)):
        j = int(y/res)- i
        angle = math.pi/2 - math.atan(j*res/(w/2))
        index.append(  round(angle/inc))
        safe_ranges.append(math.sqrt( math.pow(w/2,2) + math.pow(j*res,2) ))
    
    # *******************   Phase III   ***************************** 
    # 含横线，不含角线    
    for i in range(int(( round((l-y),1) /res))):
        angle = math.pi/2 + math.atan(i*res/(w/2))
        index.append(round(angle/inc))
        safe_ranges.append(math.sqrt(math.pow(w/2,2) + math.pow(i*res, 2))) 
    
    # *******************   Phase IV   ***************************** 
    # 不含中线，含角线 
    for i in range(int(w/2/res)):
        j = int(w/2/res)-i
        angle = math.pi - math.atan(j*res/(l-y))
        index.append(round(angle/inc))
        safe_ranges.append(math.sqrt(math.pow(l-y,2) + math.pow(j*res,2)))    
    
    # *******************   Phase V   ***************************** 
    # 含中线，不含角线 
    for i in range(int(w/2/res)):
        angle = math.pi + math.atan(i*res/(l-y))
        index.append(round(angle/inc))
        safe_ranges.append(math.sqrt(math.pow(l-y,2) + math.pow(i*res,2)))  

    # *******************   Phase VI   ***************************** 
    # 不含横线，含角线 
    for i in range(int(( round((l-y),1) /res))):
        j = int(( round((l-y),1) /res)) - i
        angle = 3*math.pi/2 - math.atan(j*res/(w/2))
        index.append(round(angle/inc))
        safe_ranges.append(math.sqrt(math.pow(w/2,2) + math.pow(j*res,2)))  

    # *******************   Phase VII   ***************************** 
    # 含横线，不含角线 
    for i in range(int(y/res)):
        angle = 3*math.pi/2 + math.atan(i*res/(w/2))
        index.append(round(angle/inc))
        safe_ranges.append(math.sqrt(math.pow(w/2,2) + math.pow(i*res,2)))  

    # *******************   Phase VIII   ***************************** 
    # 不含中线，含角线 
    for i in range(int((w/2)/res)):
        j = int((w/2)/res)-i
        angle = 2*math.pi - math.atan(j*res/(y))
        index.append(round(angle/inc))
        safe_ranges.append(math.sqrt(math.pow(y,2) + math.pow(j*res,2)))  

    return index, safe_ranges
# main
index, safe_ranges = calculate(360, 0.095)
if len(index)!= len(safe_ranges):
    print ('Length not equal!!!!!')
print('The number of descretized scans is: '+ str(len(index)))
for i in range(len(index)):
    print('#' + str(i+1)+ "  Index: " + str(index[i]) + "   Distance: "+str(safe_ranges[i]))
ranges = []
for j in range(len(index)):
    ranges.append(round(safe_ranges[j], 3))

print(index)
print(ranges)
zeros = []
for i in range(40):
    zeros.append(0)
print(zeros)


# [1.962, 1.896, 1.678, 1.526, 1.508, 1.478, 1.454, 1.428, 1.332, 1.164, 1.014, 0.91, 0.908, 0.994, 1.078, 1.42, 1.09, 1.472, 1.164, 1.088, 1.036, 1.086, 1.234, 7.288, 6.536, 6.08, 2.996, 2.808, 2.66, 2.52, 2.276, 2.088]


