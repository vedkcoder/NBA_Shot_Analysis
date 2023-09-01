import Datascraper
import pandas as pd
import numpy as np
import preprocess
import CourtPlot
import ZonePlot
import matplotlib.pyplot as plt

# Only run if csv files empty in project folder.
# Datascraper.create_zone_dataset()
# Datascraper.create_dist_dataset()
# Datascraper.create_shotclock_dataset()


# Run only once to preprocess and generate all the processed datasets
# preprocess.process_zone()
# preprocess.process_dist()
# preprocess.process_shotclock()

CourtPlot.draw_plot('Houston Rockets','Alperen', 'Sengun', '2020-21', 'PTS')
# fig = plt.figure(figsize=(4, 3.76))
# ax = fig.add_axes([0, 0, 1, 1])
# ZonePlot.create_court_paint(ax, 'black')

