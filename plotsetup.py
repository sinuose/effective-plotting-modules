'''
Author: Martin Jasinski
Purpose: Plotting Tools for quick setup
'''
  
# ---------------------------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------------------------
import matplolib.pyplot as plt
# if graphics initialized: 
#     matplotlib.use("TkAgg")
#     import matplotlib

  
# ---------------------------------------------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------------------------------------------

def PlotSetup(ax):
	ax.set_title('Plot of Radius and Intensity', fontsize=20, labelpad=15, fontdict=font1)
  ax.set_xlabel('Log of Radius', fontsize=14, labelpad=15, fontdict=font1)
	ax.set_ylabel('Log of Intensity', fontsize=14, labelpad=15, fontdict=font1)
	#ax.set_yscale("log")
	#ax.set_xscale("log")
  

# ---------------------------------------------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------------------------------------------
# Styling Choices
plt.style.use("Solarize_Light2")
font1 = {'family':'monospace','color':'black'}

# initialize plots
fig, (ax1, ax2) = plt.subplots(ncols=1, nrows=2, figsize=(20, 12), constrained_layout=True)

# plot setup
PlotSetup(ax1)
PlotSetup(ax2)

# Set up Legend
handles, labels = ax2.get_legend_handles_labels()

legend2 = ax2.legend(title="Legend", loc='upper left', borderaxespad=0., handles=handles)
frame2 = legend2.get_frame()
frame2.set_alpha(0.8)

# show plots
plt.show()
