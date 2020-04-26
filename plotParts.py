import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import os

def Plot(title, position, pitch, mark, vmin1, vmax1, yTicks, path):

    fig,ax = plt.subplots(subplot_kw=dict())
    fig.subplots_adjust(top=0.8)
    ax.figure.set_size_inches(20, 6)
    ax.set_xlabel('', fontsize = 32)
    ax.set_ylabel('', fontsize = 24)
    ax.grid(axis="both", alpha = 0.8)
    ax.set_yticks(range(0))
    ax.set_xticklabels([1*label for label in range(64)], fontsize = 0)
    ax.set_xlim(left = -1, right=17)
    
    ax.grid(which = 'major', color='k', linestyle='-', linewidth=1, alpha = 0.8)
    ax.grid(which = 'minor', color='k', linestyle='-',linewidth=1, alpha = 0.4)
    ax.xaxis.set_major_locator(MultipleLocator(4))
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    
    ax.scatter(position,pitch, s = 1200, marker = mark, cmap='PuBu_r', c = pitch, vmin=vmin1, vmax=vmax1)
    fig.savefig(path + title+".png", transparent=True)
    
def Sequence(part, vmin, vmax):
    position, pitch = [],[]
    for csv in os.listdir(part):
        if ".DS_Store" not in csv and ".png" not in csv:
            notes = pd.read_csv(part + "/" + csv)
            position = notes["Position"].tolist()
            pitch = notes["Pitch"].tolist()
            position.append(18)
            pitch.append(pitch[0])
            
            Plot(str(csv).split(".")[0], position, pitch, ">", vmin, vmax, 64, part + "/")
    

dr = os.getcwd()

Drums, Melody, Harmony = dr + "/Drums", dr + "/Melody", dr + "/Harmony"
Sequence(Drums, 10, 90)
Sequence(Melody, 60, 120)
Sequence(Harmony, 60, 120)

