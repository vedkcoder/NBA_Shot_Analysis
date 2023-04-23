import Datascraper
import pandas as pd
import numpy as np
import preprocess

# Only run if csv files empty in project folder.
# Datascraper.create_zone_dataset()
# Datascraper.create_dist_dataset()
# Datascraper.create_shotclock_dataset()


# Run only once to preprocess and generate all the processed datasets
# preprocess.process_zone()
# preprocess.process_dist()
preprocess.process_shotclock()







