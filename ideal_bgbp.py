#import required python modules
import numpy as np
import numpy.ma as ma
import matplotlib.pylab as plt
import matplotlib.ticker as mtick
from scipy import stats
from matplotlib import cm
import matplotlib.patches as mpatches

# set the font size globally to get the ticklabels big too:
plt.rcParams["font.size"] = 22


#BPH
dtbp_deftrop      = np.array([0.4,-0.01,-0.04,-0.04,0.18,0.,1.2,0.2,-0.07,-0.2,-0.2,0.044,-0.01,-0.13,-0.05,0.2,0.4,0.6])
dtbp_deftemp	= np.array([-0.68,-0.5,-1.1,-0.077,-0.04,0.28])
dtbp_defbor	= np.array([-0.35,-0.23,-0.9,-0.54,-2.8,-0.377,-0.28,-1.,-0.8,-1.53])

#BGC
dtbg_deftrop      = np.array([0.3,1.06,0.72,0.26,0.19])
dtbg_deftemp	= np.array([0.1,0.39,0.23])
dtbg_defbor	= np.array([0.11,0.06,0.12,0.32,0.02,0.02,0.09])

#dt_defglob	= np.array([-0.38,-1.2,-1.6,-1.5,-0.2,-1.1,-2.33,-1.])

dt_aftrop 	= np.array([-0.03,0.71])
dt_aftemp	= np.array([0.3,1.14,0.27,0.3])
dt_afbor	= np.array([0.31])
dt_afglob	= np.array([1.3,0.,1.2])

dt_af		= [dt_aftrop, dt_aftemp, dt_afbor]

#tropics BGC & BPH
dt_deftrop	= [dt_aftrop, dtbg_deftrop, dtbp_deftrop]

y1 		= np.arange(len(dt_aftrop))
y1[:]		= 1

y2 		= np.arange(len(dtbg_deftrop))
y2[:]		= 2
y3 		= np.arange(len(dtbp_deftrop))
y3[:]		= 3

tropy		= [y1,y2,y3]

#temperate BGC & BPH
dt_deftemp	= [dt_aftemp, dtbg_deftemp,dtbp_deftemp]

y1 		= np.arange(len(dt_aftemp))
y1[:]		= 1
y2 		= np.arange(len(dtbg_deftemp))
y2[:]		= 2
y3 		= np.arange(len(dtbp_deftemp))
y3[:]		= 3


tempy		= [y1,y2,y3]


#boreal BGC & BPH
dt_defbor	= [dt_afbor,dtbg_defbor,dtbp_defbor]

y1 		= np.arange(len(dt_afbor))
y1[:]		= 1
y2 		= np.arange(len(dtbg_defbor))
y2[:]		= 2
y3 		= np.arange(len(dtbp_defbor))
y3[:]		= 3
bory		= [y1,y2,y3]




#******************CREATE FIGURE HERE**************************
fig = plt.figure(figsize=[14,14])

#Historical data panel 1
a = fig.add_subplot(4,1,1)
#a.set_title('Historical',loc='right')
colors = ['#f03b20','#2c7fb8','#2c7fb8'] #colors = [red,red, blue, blue] # Taken from here http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3  #colorblind safe is chosen
markers= ['X','o','o']
lb = ['Deforestation','Afforestation',''] 

ii=0
for x, val in zip(dt_defbor, bory):
    a.scatter(x, val, marker=markers[ii],color=colors[ii],alpha=0.7,s=80,label=lb[ii])
    ii=ii+1

#a.xaxis.set_visible(False) # Hide only x axis
a.set_xlim(-4,4)
a.set_ylim(0,4)
#a.axhline(y=0.,c="k",linewidth=0.5,linestyle='--')
a.axvline(x=0.,c="k",linewidth=1)
#a.axvline(x=0.2,c="k",linewidth=0.4,linestyle='--')
#a.axvline(x=0.4,c="k",linewidth=0.4,linestyle='--')
#a.axvline(x=-0.2,c="k",linewidth=0.4,linestyle='--')
#a.axvline(x=-0.4,c="k",linewidth=0.4,linestyle='--')
#a.set_yticklabels([], rotation=0)
#a.yaxis.set_ticks_position('none') 
a.text(0.147,1.2, "Biophysical effects", size=22, ha="center",  transform=a.transAxes, color=colors[2])
a.text(0.177,1.03, "Biogeochemical effects", size=22, ha="center",  transform=a.transAxes, color=colors[0])
a.set_ylabel('BOREAL')
#a.spines['bottom'].set_visible(False)

#TEMPERATE panel 2
a0 = fig.add_subplot(4,1,2)

a0.axvline(x=0.,c="k",linewidth=1,)
#a0.axvline(x=0.2,c="k",linewidth=0.4,linestyle='--')
#a0.axvline(x=0.4,c="k",linewidth=0.4,linestyle='--')
#a0.axvline(x=-0.2,c="k",linewidth=0.4,linestyle='--')
#a0.axvline(x=-0.4,c="k",linewidth=0.4,linestyle='--')
#a0.axhline(y=3.4,c="k",linewidth=0.4,linestyle='--')

ii=0
for x, val in zip(dt_deftemp, tempy):
    a0.scatter(x, val, marker=markers[ii],color=colors[ii],alpha=0.7,s=100)
    ii=ii+1

a0.set_xlim(-4,4)
a0.set_ylim(0,4)
#a0.xaxis.set_visible(False) # Hide only x axis
#a0.set_yticklabels([], rotation=0)
#a0.yaxis.set_ticks_position('none') 
a0.set_ylabel('TEMPERATE')
#a0.spines['bottom'].set_visible(False)
#a0.spines['top'].set_visible(False)

#TROPICAL panel 3
a1 = fig.add_subplot(4,1,3)
#a0.set_title('RCP4.5',loc='right')

a1.axvline(x=0.,c="k",linewidth=1)
#a1.axvline(x=0.2,c="k",linewidth=0.4,linestyle='--')
#a1.axvline(x=0.4,c="k",linewidth=0.4,linestyle='--')
#a1.axvline(x=-0.2,c="k",linewidth=0.4,linestyle='--')
#a1.axvline(x=-0.4,c="k",linewidth=0.4,linestyle='--')
#a1.axhline(y=3.3,c="k",linewidth=0.4,linestyle='--')

ii=0
for x, val in zip(dt_deftrop, tropy):
    a1.scatter(x, val, marker=markers[ii],color=colors[ii],alpha=0.7,s=80)
    ii=ii+1

a1.set_xlim(-4,4)
a1.set_ylim(0,4)
#a1.xaxis.set_visible(False) # Hide only x axis
#a1.set_yticklabels([], rotation=0)
#a1.yaxis.set_ticks_position('none') 
a1.set_ylabel('TROPICAL')
#a1.spines['bottom'].set_visible(False)
#a1.spines['top'].set_visible(False)


#lb1 = ['','TROPICAL','','TEMPERATE','','BOREAL'] 
#a2.set_yticklabels(lb1, rotation=90,fontsize=14)
#a2.yaxis.set_ticks_position('none') 
#a2.set_ylabel('Future RCP2.6')
#a2.spines['top'].set_visible(False)

a1.set_xlabel(r'Mean global annual change in surface air temperature ($^o$C)')
fig.subplots_adjust(hspace=0.5, wspace=0.4)
#fig.subplots_adjust(hspace=0)
a.legend(bbox_to_anchor=(0.65, 1.4), loc=2, borderaxespad=0.,fontsize=16)
leg = a.get_legend()
leg.legendHandles[0].set_color('k')
leg.legendHandles[1].set_color('k')
#leg.legendHandles[2].set_color('k')
#red_patch = mpatches.Patch(color='k')
#a2.legend(bbox_to_anchor=(0.0, 0.94), loc=2, borderaxespad=0.,fontsize=16)
#leg1 = a2.get_legend()
#leg1.legendHandles[1].set_color('#f03b20')

plt.savefig('ideal_bgbp.png', dpi=200)
#plt.show()








#colors = ['#f03b20','#f03b20','#2c7fb8']  # Taken from here http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3  #colorblind safe is chosen
#https://betterfigures.org/2015/06/23/picking-a-colour-scale-for-scientific-graphics/























