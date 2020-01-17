# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:13:26 2020

@author: light_pollusion_team
"""

import numpy as np
import matplotlib.pyplot as plt
#import osmnx as ox
#ox.plot_graph(ox.graph_from_place('Hong Kong'))


H = 647000

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

def lightangle(xi,yi,x,y,H):
    dx = 0.11131955/0.000001*(xi-x)
    dy = 0.11131955/0.000001*(yi-y)
    d = np.sqrt(np.square(dx) + np.square(dy))
    t = np.sqrt(np.square(dx) + np.square(dy) + H*H)
    alpha = np.arctan2(dy,dx)*180/np.pi
    theta = np.arctan2(H,d)*180/np.pi
    return alpha, theta, t # from gt to satellite

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
xy = {}
# 0903, 6 snapshots
theta,alpha,H,xc,yc = 59.805862,229.893537,H,114.055618,21.787384
x1,y1 = calsatlnglat(theta,alpha,H,xc,yc)
xy[0] = (x1,y1)
theta,alpha,H,xc,yc = 59.667007,229.417646,H,113.983470,22.095757
x1,y1 = calsatlnglat(theta,alpha,H,xc,yc)
xy[1] = (x1,y1)
theta,alpha,H,xc,yc = 59.527109,228.946545,H,113.910739,22.403419
x2,y2 = calsatlnglat(theta,alpha,H,xc,yc)
xy[2] = (x2,y2)
theta,alpha,H,xc,yc = 59.384975,228.478597,H,113.837667,22.711368
x3,y3 = calsatlnglat(theta,alpha,H,xc,yc)
xy[3] = (x3,y3)
theta,alpha,H,xc,yc = 59.242029,228.008573,H,113.762299,23.020156
x4,y4 = calsatlnglat(theta,alpha,H,xc,yc)
xy[4] = (x4,y4)
theta,alpha,H,xc,yc = 59.098805,227.554197,H,113.688673,23.325296
x5,y5 = calsatlnglat(theta,alpha,H,xc,yc)
xy[5] = (x5,y5)

# 1124, 5 snapshots
theta,alpha,H,xc,yc = 59.682734,229.378881,H,114.019364,22.105282
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[6] = (x,y)
theta,alpha,H,xc,yc = 59.537519,228.916252,H,113.950812,22.413019
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[7] = (x,y)
theta,alpha,H,xc,yc = 59.394323,228.454219,H,113.879816,22.720191
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[8] = (x,y)
theta,alpha,H,xc,yc = 59.254585,227.989189,H,113.803961,23.026051
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[9] = (x,y)
theta,alpha,H,xc,yc = 59.108449,227.535653,H,113.731478,23.331922
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[10] = (x,y)

# 0129, 6 snapshots
theta,alpha,H,xc,yc = 59.166087,230.323034,H,113.904057,21.992118
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[11] = (x,y)
theta,alpha,H,xc,yc = 59.029620,229.879404,H,113.837214,22.294281
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[12] = (x,y)
theta,alpha,H,xc,yc = 58.888193,229.437524,H,113.771295,22.598481
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[13] = (x,y)
theta,alpha,H,xc,yc = 58.746034,228.999693,H,113.704442,22.901813
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[14] = (x,y)
theta,alpha,H,xc,yc = 58.602562,228.559945,H,113.636174,23.206720
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[15] = (x,y)
theta,alpha,H,xc,yc = 58.456414,228.122974,H,113.567539,23.511954
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[16] = (x,y)

# 0311
theta,alpha,H,xc,yc = 58.948849,228.701741,H,113.677282,22.907392
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[17] = (x,y)
theta,alpha,H,xc,yc = 58.780851,228.258106,H,113.619560,23.224255
x,y = calsatlnglat(theta,alpha,H,xc,yc)
xy[18] = (x,y)

#%%
site = {}
site['HKU'] = [114.1398,22.28325]
site['iObs'] = [114.3229,22.408319]
site['HKn'] = [114.10803,22.383647]
site['TST'] = [114.17145,22.294222]
key = list(site.keys())
#for _k in key:
if True:
    _k = 'HKU'
    print(_k)
    for i in range(len(xy)):
        alpha, theta, t = lightangle(xy[i][0],xy[i][1],site[_k][0],site[_k][1],H)
        print('Satellite lng lat =',xy[i])
        out = angletodir(alpha)
        print('horizontal angle =',alpha)
        print(out)
        print('Upward vertical angle =',str(theta)[:5])
        print('Transferred distance =',str(t/1000)[:6],'km')
        print('')

#%%
ms = {}
ms['HKU'] = '^'
ms['iObs'] = 'x'
ms['HKn'] = 'v'
ms['TST'] = '>'
fig = plt.figure(figsize=(8,5),dpi=80)
for _k in key:
    plt.scatter(site[_k][0],site[_k][1],label=_k,marker=ms[_k])
plt.legend()
plt.tight_layout()
plt.show()
        
        
        
#%%
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.patches as mpatches

s = {}
s['site'] = []
s['longitude'] = []
s['latitude'] = []
for _s in site.keys():
    s['site'].append(_s)
    s['longitude'].append(site[_s][0])
    s['latitude'].append(site[_s][1])
    

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
chn = world[world['name'] == 'China']
map1 = gpd.read_file(r'D:\research\gadm36_HKG_shp\gadm36_HKG_1.shp')  
crs = {'init': 'epsg:4326'}
geometry = []
df = pd.DataFrame(site)
for _s in site.keys():
    geometry.append(Point(site[_s]))
        
gdf = gpd.GeoDataFrame(s,crs=crs,geometry=geometry)

fig,ax = plt.subplots(figsize=(8,6),dpi=100)
for _k in key:
    plt.scatter(site[_k][0],site[_k][1],label=_k,marker=ms[_k])
chn.plot(ax=ax,alpha=0.1,color='grey')
map1.plot(ax=ax, alpha=0.2, color='grey')
plt.legend(prop={'size':10})
for i in [0,1,2,3,4,5]:
    ax.scatter(xy[i][0],xy[i][1],c='r',label='18-09-03')
for i in [6,7,8,9,10]:
    ax.scatter(xy[i][0],xy[i][1],c='g',label='18-11-24')
for i in [11,12,13,14,15,16]:
    ax.scatter(xy[i][0],xy[i][1],c='b',label='19-01-29')
for i in [17,18]:
    ax.scatter(xy[i][0],xy[i][1],c='y',label='19-03-11')
plt.xlim(110,114.9)
plt.ylim(18.9,22.8)
plt.title('Satellite going north: Red-Green-Blue-Yellow as 0903-1124-0129-0311')
plt.tight_layout()
plt.savefig('a.pdf')
plt.show()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    