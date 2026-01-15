import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

def plot_one_field(data_values):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    nrow_c, ncol_c = 16, 32
    delr_c, delc_c = 4.0, 4.0
    
    refine_factor = 4
    
    cells = [] 
    count = 0
    for r in range(nrow_c):
        for c in range(ncol_c):
            if 6 <= r < 11 and 4 <= c < 19:
                continue 
            x0, x1 = c * delr_c, (c + 1) * delr_c
            y0, y1 = r * delc_c, (r + 1) * delc_c
            cells.append([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])
            count += 1

    
    x_off, y_off = 4 * 4.0, 6 * 4.0 # xoff=16, yoff=20 
    nrow_f, ncol_f = 5 * 4, 15 * 4
    delr_f, delc_f = 1.0, 1.0



    for r in range(nrow_f):
        for c in range(ncol_f):
            x0, x1 = x_off + c * delr_f, x_off + (c + 1) * delr_f
            y0, y1 = y_off + r * delc_f, y_off + (r + 1) * delc_f
            cells.append([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


    coll = PolyCollection(cells, array=data_values, cmap='RdBu_r', 
                          edgecolors='white', linewidths=0.1)
    
    ax.add_collection(coll)
    

    ax.set_xlim(0, ncol_c * delr_c)
    ax.set_ylim(0, nrow_c * delc_c)
    ax.set_aspect('equal')
    ax.invert_yaxis() 
    
    ax.axis('off')
    
    cb = fig.colorbar(coll, ax=ax, shrink=0.8)
    cb.ax.tick_params(labelsize=12)
    plt.tight_layout()
    plt.show()


def plot_time_series(sample_data_12pts):


    fig, axes = plt.subplots(4, 3, figsize=(16, 10))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.1, hspace=0.2)
    axes = axes.flatten()
    
    nrow_c, ncol_c = 16, 32
    delr_c, delc_c = 4.0, 4.0
    
    cells = [] 
    for r in range(nrow_c):
        for c in range(ncol_c):
            if 6 <= r < 11 and 4 <= c < 19:
                continue 
            x0, x1 = c * delr_c, (c + 1) * delr_c
            y0, y1 = r * delc_c, (r + 1) * delc_c
            cells.append([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])

    x_off, y_off = 4 * 4.0, 6 * 4.0 
    nrow_f, ncol_f = 20, 60
    delr_f, delc_f = 1.0, 1.0

    for r in range(nrow_f):
        for c in range(ncol_f):
            x0, x1 = x_off + c * delr_f, x_off + (c + 1) * delr_f
            y0, y1 = y_off + r * delc_f, y_off + (r + 1) * delc_f
            cells.append([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])

    vmin = np.min(sample_data_12pts)
    vmax = np.max(sample_data_12pts)

    for i in range(12):
        ax = axes[i]
        
 
        coll = PolyCollection(cells, array=sample_data_12pts[i], cmap='RdBu_r', 
                              edgecolors='white', linewidths=0.05)
        

        coll.set_clim(vmin, vmax)
        
        ax.add_collection(coll)
        

        ax.set_xlim(0, ncol_c * delr_c)
        ax.set_ylim(0, nrow_c * delc_c)
        ax.set_aspect('equal')
        ax.invert_yaxis()
        

        ax.axis('off')
        
        cbar = fig.colorbar(coll, ax=ax, shrink=0.9, aspect=15)
        cbar.ax.tick_params(labelsize=10)

    plt.show()