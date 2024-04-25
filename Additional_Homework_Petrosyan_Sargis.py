import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import stats
import time

# Set up the figure and axes
fig, axs = plt.subplots(2, 3, figsize=(13, 6))

# Initialize variables
num_trials = 500
dice_r = 7
dice_f = 6
means = []
p_values = []

# Generate original distribution
orig_dist = np.random.randint(1, dice_f + 1, size=num_trials * dice_r)
orig_dist_means = np.mean(orig_dist.reshape(-1, dice_r), axis=1)

# The Histogram of the means
hist_ax = axs[0, 0]
hist_ax.set_title('The Histogram of the means')
hist_ax.set_xlabel('Mean')
hist_ax.set_ylabel('Frequency')

# QQ plot
qq_ax = axs[0, 1]
qq_ax.set_title('QQ Plot')
qq_ax.set_xlabel('Theoretical Quantiles')
qq_ax.set_ylabel('Ordered Values')

# The Original distribution
orig_dist_ax = plt.subplot2grid((2, 3), (0, 2), rowspan=2)
orig_dist_ax.set_title('The Original Distribution')
orig_dist_ax.set_xlabel('Value')
orig_dist_ax.set_ylabel('Frequency')
orig_dist_ax.yaxis.set_ticklabels([])

# Shapiro-Wilk Test p-values
dice_dist_ax =  axs[1, 0]
dice_dist_ax.set_title('Shapiro-Wilk Test p-values')

# Historical P-values from Shapiro-Wilk Test
p_values_ax = axs[1, 1]
p_values_ax.set_title('Shapiro-Wilk Test p-values')
p_values_ax.set_xlabel('Trial')
p_values_ax.set_ylabel('p-value')

# Hide unused subplot
shapiro_ax = axs[1, 2]
shapiro_ax.axis('off')

# Function to update plots
def update(frame):
    dice_t = np.random.randint(1, dice_f + 1, size=dice_r)
    means.append(np.mean(dice_t))
    
    # Update histogram of means
    hist_ax.clear()
    hist_ax.hist(means, bins=6, range=(0, 7), rwidth=0.9)
    hist_ax.set_title('The Histogram of The Means')
    hist_ax.set_xlabel('Mean')
    hist_ax.set_ylabel('Frequency')
    hist_ax.set_xlim(0, 6)
    hist_ax.set_ylim(0, 20)
 
    # Update QQ plot
    qq_ax.clear()
    stats.probplot(means, dist="norm", plot=qq_ax)
    qq_ax.set_title('QQ Plot')
    qq_ax.set_xlabel('Theoretical Quantiles')
    qq_ax.set_ylabel('Sample Quantiles')

    # Update of the original distribution plot
    orig_dist_ax.clear()
    orig_dist_ax.hist(orig_dist_means[:frame], bins=6, range=(0, 7), rwidth=0.9)
    orig_dist_ax.set_title('The Original Distribution')
    orig_dist_ax.set_xlabel('Value')
    orig_dist_ax.set_ylabel('Frequency')
    orig_dist_ax.set_xlim(0, 6)
    orig_dist_ax.set_ylim(0, 10)
    # orig_dist_ax.yaxis.set_ticklabels([])
    
    # Update of the Shapiro-Wilk test results
    shapiro_statistic, p_value = stats.shapiro(dice_t)
    p_values.append(p_value)
      
    dice_dist_ax.clear()
    dice_dist_ax.set_title('Shapiro-Wilk test results')
    dice_dist_ax.text(0.5, 0.5, f'P-values: {p_value:.3f}',fontsize=15, ha='center', va='center', transform=dice_dist_ax.transAxes)
    dice_dist_ax.axis('off')
    
    # Update p-values plot
    p_values_ax.clear()
    p_values_ax.plot(range(len(p_values)), p_values, marker='o', linestyle='-')
    p_values_ax.set_title('Shapiro-Wilk Test p-values')
    p_values_ax.set_xlabel('Trial')
    p_values_ax.set_ylabel('p-value')
    p_values_ax.set_ylim(0, 1)
    
    
    # Adding a sleep time
    time.sleep(0.05)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_trials, interval=500)

plt.tight_layout()
plt.show()

