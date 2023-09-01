import base64
import io

import CourtPlot
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def create_court_left_corner_3(ax, color):
    ax.text(0, 400, "Zone: Left Corner-3", fontsize=10, ha='center', color=color)
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    # Restricted Area
    ax.add_artist(mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, fill = False, facecolor='yellow', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    x_fill = [-250, -220, -220, -250]
    y_fill = [0, 0, 140, 140]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data


def create_court_right_corner_3(ax, color):
    ax.text(0, 400, "Zone: Right Corner-3", fontsize=10, ha='center', color=color)
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    # Restricted Area
    ax.add_artist(mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, fill = False, facecolor='yellow', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    x_fill = [250, 220, 220, 250]
    y_fill = [0, 0, 140, 140]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)

    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data

def create_court_above_the_break_3(ax, color):
    ax.text(0, 400, "Zone: Above the Break-3", fontsize=10, ha='center', color=color)
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))
    ax.add_artist(mpl.patches.Arc((0, 140), 470, 345, theta1=0, theta2=180, facecolor='none', edgecolor='yellow', alpha = 0.5, lw=15))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    # Restricted Area
    ax.add_artist(mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, fill = False, facecolor='yellow', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    # x_fill = [250, 220, 220, 250]
    # y_fill = [0, 0, 140, 140]
    #
    # # Fill the region with a specific color
    # ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)

    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data


def create_court_midrange(ax, color):
    ax.text(0, 400, "Zone: Mid-Range", fontsize=10, ha='center', color=color)
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))
    ax.add_artist(mpl.patches.Arc((0, 140), 370, 245, theta1=0, theta2=180, facecolor='none', edgecolor='yellow', alpha=0.5, lw=45))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    # Restricted Area
    ax.add_artist(mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, fill = False, facecolor='yellow', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    x_fill = [220, 80, 80, 220]
    y_fill = [0, 0, 140, 140]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    x_fill = [-220, -80, -80, -220]
    y_fill = [0, 0, 140, 140]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    x_fill = [-150, -80, -80, -150]
    y_fill = [140, 140, 210, 210]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    x_fill = [150, 80, 80, 150]
    y_fill = [140, 140, 210, 210]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    x_fill = [-80, 80, 80, -80]
    y_fill = [190, 190, 216, 216]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    theta = np.linspace(0, 2 * np.pi, 100)  # 100 points for a full semicircle
    r = 60  # radius of the semicircle

    # Compute x and y coordinates of the semicircle
    x = r * np.cos(theta)
    y = r * np.sin(theta) + 190
    ax.fill_between(x, y, 190, where=(y >= 190), color='yellow', alpha=0.5)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)

    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data


def create_court_backcourt(ax, color):
    ax.text(0, 400, "Zone: Backcourt", fontsize=10, ha='center', color=color)
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))
    ax.add_artist(mpl.patches.Arc((0, 140), 650, 525, theta1=0, theta2=180, facecolor='none', edgecolor='yellow', alpha = 0.5, lw=50))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    # Restricted Area
    ax.add_artist(mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, fill = False, facecolor='yellow', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    # x_fill = [250, 220, 220, 250]
    # y_fill = [0, 0, 140, 140]
    #
    # # Fill the region with a specific color
    # ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)

    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data

def create_court_restricted(ax, color):
    ax.text(0, 400, "Zone: Restricted", fontsize=10, ha='center', color=color)
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))



    # Restricted Area
    ax.add_artist(mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, fill = False, facecolor='yellow', edgecolor=color, lw=2))
    ax.add_artist(mpl.patches.Arc((0, 35), 40, 70, theta1=0, theta2=180, facecolor='none', edgecolor='yellow', alpha=0.5, lw=30))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)


    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)

    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data

def create_court_paint(ax, color):
    # Short corner 3PT lines
    ax.text(0, 400, "Zone: Paint", fontsize=10, ha='center', color=color)
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    x_fill = [-80, 80, 80, -80]
    y_fill = [0, 0, 190, 190]

    # Fill the region with a specific color
    ax.fill_between(x_fill, y_fill, color='yellow', alpha=0.5)

    # Restricted Area

    ax.add_artist(mpl.patches.Arc((0, 35), 40, 70, theta1=0, theta2=180, facecolor='none', edgecolor='white', alpha=1, lw=30))
    ax.add_artist(
        mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, fill=False, facecolor='yellow', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)


    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)

    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data