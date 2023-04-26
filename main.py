import Datascraper
import pandas as pd
import numpy as np
import preprocess

# Only run if csv files empty in project folder.
# Datascraper.create_zone_dataset()
# Datascraper.create_dist_dataset()
# Datascraper.create_shotclock_dataset()
# Datascraper.combined_dataset()
# Datascraper.morecombined_dataset()

# Run only once to preprocess and generate all the processed datasets
# preprocess.process_zone()
# preprocess.process_dist()
# preprocess.process_shotclock()
# preprocess.process_combined()

# df = pd.read_csv('CombinedTotal.csv')
# new_df = preprocess.merge(df)
# new_df.to_csv('Final.csv')

preprocess.train()






