import cmath as cm
import numpy as np

def root(a,b,n):
    z = complex(a,b)
    polar = cm.polar(z)
    print('polar -',polar)
    for k in range(0,n):
        root = (polar[0]**(1/n))*complex(np.cos((2*np.pi*k+polar[1])/n),
                np.sin((2*np.pi*k+polar[1])/n))
        print(f'root {k+1} - ',root)
        
root(3,4,3)
print('\n')
root(np.sqrt(1/2),np.sqrt(1/2),3)
    
    
   