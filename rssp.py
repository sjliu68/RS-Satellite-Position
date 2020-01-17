# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:13:26 2020

@author: SJ Liu
sjliu.me@gmail.com

"""
import numpy as np
import matplotlib.pyplot as plt

H = 647000 # satellite height in meter

'''
@arguments
theta: evaluation angle
alpha: azimuth angle
H: satellite height
xc: image center x/longitude
yc: image center y/latitude

@return: satellite longitude and latitude on the projected horizontal plane
'''
def calsatlnglat(theta, alpha, H, xc, yc):
    if alpha>180:
        sign = -1
    else:
        sign = 1
    theta = theta*np.pi/180
    alpha = alpha*np.pi/180
    a = np.tan(alpha)
    delta = H/(np.tan(theta)*np.sqrt(1+a*a)) # meter
    delta = 0.000001/0.11131955*delta # longtitude
    x = sign*delta + xc # lng
    y = sign*a*delta + yc # lat
    return x,y


'''
@arguments
xi: satellite longitude
yi: satellite latitude 
x: target longitude
y: target latitude
H: satellite height

@return
alpha: target azimuth to satellite
theta: target evaluation to satellite
t: target distance to satellite
'''
def lightangle(xi,yi,x,y,H):
    dx = 0.11131955/0.000001*(xi-x)
    dy = 0.11131955/0.000001*(yi-y)
    d = np.sqrt(np.square(dx) + np.square(dy))
    t = np.sqrt(np.square(dx) + np.square(dy) + H*H)
    alpha = np.arctan2(dy,dx)*180/np.pi
    theta = np.arctan2(H,d)*180/np.pi
    return alpha, theta, t # from gt to satellite


'''
@input
alpha: evaluation from function lightangle

@return
out: evaluation angle description (string)
'''
def angletodir(alpha):
    if alpha<0:
        if alpha<-90:
            out = 'Southwest, S->W ' +str(np.abs(alpha)-90)[:5] 
        else:
            out = 'Northwest, N->W ' +str(-alpha)[:5]
    if alpha>=0:
        if alpha>90:
            out = 'Southeast, S->E ' +str(180-alpha)[:5] 
        else:
            out = 'Northeast, N->E'+str(alpha)[:5]
    return out

#%%
theta,alpha,H,xc,yc = 59.805862,229.893537,H,114.055618,21.787384
x1,y1 = calsatlnglat(theta,alpha,H,xc,yc) # satellite position on the projected horizontal plane
alpha, theta, t = lightangle(x1,y1,site[_k][0],site[_k][1],H)
print('Satellite lng lat =',x1,y1)
out = angletodir(alpha)
print('horizontal angle =',alpha)
print(out)
print('Upward vertical angle =',str(theta)[:5])
print('Transferred distance =',str(t/1000)[:6],'km')
print('')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
