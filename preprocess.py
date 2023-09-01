# This file handles all preprocessing of data
# Function preprocess_zone data is used for breaking down data by individual zones and vertically stacking them to make zone a column in the dataset.

import os
import pandas as pd


def process_zone():
    # mapping:- 0: Restricted, 1: Paint NonRA, 2: MidRange, 3: Left3, 4: Right3, 5: Break, 6: Backcourt, 7: Corner3

    ### Files variable is list of csv files
    files = [f for f in os.listdir('ZoneData') if os.path.isfile(os.path.join('ZoneData', f))]

    ### iterate over each csv for every season of nba
    for file in files:
        ### new columns for the final df we create
        new_cols = ['index', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM', 'Age', 'Season','FGM', 'FGA', 'FG%', 'Zone']

        ### importing csv
        df = pd.read_csv('ZoneData/' + file)

        ### df for biodata
        biodata_df = df.iloc[:, :6]

        ### split file string to get season
        x, y, z = file.split(sep='_')
        z1, z2 = z.split(sep='.')

        ### add to biodata column
        biodata_df['Season'] = z1

        ### split dataframes to get df for each zone and preprocess it
        restricted_dat = df.iloc[:, 7:10]
        restricted_dat['Zone'] = [0 for _ in range(len(restricted_dat))]
        restricted_dat = pd.concat([biodata_df, restricted_dat], axis=1)
        restricted_dat.columns = new_cols
        restricted_dat = restricted_dat.drop(restricted_dat.columns[0], axis=1)
        restricted_dat = restricted_dat.iloc[1:, :]
        restricted_dat.reset_index()

        paint_dat = df.iloc[:, 10:13]
        paint_dat['Zone'] = [1 for _ in range(len(paint_dat))]
        paint_dat = pd.concat([biodata_df, paint_dat], axis=1)
        paint_dat.columns = new_cols
        paint_dat = paint_dat.drop(paint_dat.columns[0], axis=1)
        paint_dat = paint_dat.iloc[1:, :]
        paint_dat.reset_index()

        midrange_dat = df.iloc[:, 13:16]
        midrange_dat['Zone'] = [2 for _ in range(len(midrange_dat))]
        midrange_dat = pd.concat([biodata_df, midrange_dat], axis=1)
        midrange_dat.columns = new_cols
        midrange_dat = midrange_dat.drop(midrange_dat.columns[0], axis=1)
        midrange_dat = midrange_dat.iloc[1:, :]
        midrange_dat.reset_index()

        left3_dat = df.iloc[:, 16:19]
        left3_dat['Zone'] = [3 for _ in range(len(left3_dat))]
        left3_dat = pd.concat([biodata_df, left3_dat], axis=1)
        left3_dat.columns = new_cols
        left3_dat = left3_dat.drop(left3_dat.columns[0], axis=1)
        left3_dat = left3_dat.iloc[1:, :]
        left3_dat.reset_index()

        right3_dat = df.iloc[:, 19:22]
        right3_dat['Zone'] = [4 for _ in range(len(right3_dat))]
        right3_dat = pd.concat([biodata_df, right3_dat], axis=1)
        right3_dat.columns = new_cols
        right3_dat = right3_dat.drop(right3_dat.columns[0], axis=1)
        right3_dat = right3_dat.iloc[1:, :]
        right3_dat.reset_index()

        break3_dat = df.iloc[:, 22:25]
        break3_dat['Zone'] = [5 for _ in range(len(break3_dat))]
        break3_dat = pd.concat([biodata_df, break3_dat], axis=1)
        break3_dat.columns = new_cols
        break3_dat = break3_dat.drop(break3_dat.columns[0], axis=1)
        break3_dat = break3_dat.iloc[1:, :]
        break3_dat.reset_index()

        back_dat = df.iloc[:, 25:28]
        back_dat['Zone'] = [6 for _ in range(len(back_dat))]
        back_dat = pd.concat([biodata_df, back_dat], axis=1)
        back_dat.columns = new_cols
        back_dat = back_dat.drop(back_dat.columns[0], axis=1)
        back_dat = back_dat.iloc[1:, :]
        back_dat.reset_index()

        corner3_dat = df.iloc[:, 28:31]
        corner3_dat['Zone'] = [7 for _ in range(len(corner3_dat))]
        corner3_dat = pd.concat([biodata_df, corner3_dat], axis=1)
        corner3_dat.columns = new_cols
        corner3_dat = corner3_dat.drop(corner3_dat.columns[0], axis=1)
        corner3_dat = corner3_dat.iloc[1:, :]
        corner3_dat.reset_index()

        ### combine stacking all df horizontally and saving csv
        zone_df = pd.concat(
            [restricted_dat, paint_dat, midrange_dat, left3_dat, right3_dat, break3_dat, back_dat, corner3_dat], axis=0,
            ignore_index=True)
        zone_df.reset_index()
        print(zone_df)
        zone_df.to_csv(path_or_buf='ZoneTotal.csv')


### similarly for distance
def process_dist():
    # mapping :- 0: Less than 5ft, 1: 5-9ft, 2: 10-14ft, 3: 15-19ft, 4: 20-24ft, 5: 25-29ft, 6: 30-34ft, 7: 35-39ft, 8: 40+ft
    files = [f for f in os.listdir('DistData') if os.path.isfile(os.path.join('DistData', f))]
    for file in files:
        new_cols = ['index', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'Team', 'Age', 'Season','FGM', 'FGA', 'FG%', 'Distance']
        df = pd.read_csv('DistData/' + file)
        biodata_df = df.iloc[:, :6]

        x, y, z = file.split(sep='_')
        z1, z2 = z.split(sep='.')
        biodata_df['Season'] = z1

        lessthan5_df = df.iloc[:, 7:10]
        lessthan5_df['Distance'] = [0 for _ in range(len(lessthan5_df))]
        lessthan5_df = pd.concat([biodata_df, lessthan5_df], axis=1)
        lessthan5_df.columns = new_cols
        lessthan5_df = lessthan5_df.drop(lessthan5_df.columns[0], axis=1)
        lessthan5_df = lessthan5_df.iloc[1:, :]
        lessthan5_df.reset_index()

        fiveft_df = df.iloc[:, 10:13]
        fiveft_df['Distance'] = [1 for _ in range(len(fiveft_df))]
        fiveft_df = pd.concat([biodata_df, fiveft_df], axis=1)
        fiveft_df.columns = new_cols
        fiveft_df = fiveft_df.drop(fiveft_df.columns[0], axis=1)
        fiveft_df = fiveft_df.iloc[1:, :]
        fiveft_df.reset_index()

        tenft_df = df.iloc[:, 13:16]
        tenft_df['Distance'] = [2 for _ in range(len(tenft_df))]
        tenft_df = pd.concat([biodata_df, tenft_df], axis=1)
        tenft_df.columns = new_cols
        tenft_df = tenft_df.drop(tenft_df.columns[0], axis=1)
        tenft_df = tenft_df.iloc[1:, :]
        tenft_df.reset_index()

        fifteenft_df = df.iloc[:, 16:19]
        fifteenft_df['Distance'] = [3 for _ in range(len(fifteenft_df))]
        fifteenft_df = pd.concat([biodata_df, fifteenft_df], axis=1)
        fifteenft_df.columns = new_cols
        fifteenft_df = fifteenft_df.drop(fifteenft_df.columns[0], axis=1)
        fifteenft_df = fifteenft_df.iloc[1:, :]
        fifteenft_df.reset_index()

        twentyft_df = df.iloc[:, 19:22]
        twentyft_df['Distance'] = [4 for _ in range(len(twentyft_df))]
        twentyft_df = pd.concat([biodata_df, twentyft_df], axis=1)
        twentyft_df.columns = new_cols
        twentyft_df = twentyft_df.drop(twentyft_df.columns[0], axis=1)
        twentyft_df = twentyft_df.iloc[1:, :]
        twentyft_df.reset_index()

        twentyfiveft_df = df.iloc[:, 22:25]
        twentyfiveft_df['Distance'] = [5 for _ in range(len(twentyfiveft_df))]
        twentyfiveft_df = pd.concat([biodata_df, twentyfiveft_df], axis=1)
        twentyfiveft_df.columns = new_cols
        twentyfiveft_df = twentyfiveft_df.drop(twentyfiveft_df.columns[0], axis=1)
        twentyfiveft_df = twentyfiveft_df.iloc[1:, :]
        twentyfiveft_df.reset_index()

        thirtyft_df = df.iloc[:, 25:28]
        thirtyft_df['Distance'] = [6 for _ in range(len(thirtyft_df))]
        thirtyft_df = pd.concat([biodata_df, thirtyft_df], axis=1)
        thirtyft_df.columns = new_cols
        thirtyft_df = thirtyft_df.drop(thirtyft_df.columns[0], axis=1)
        thirtyft_df = thirtyft_df.iloc[1:, :]
        thirtyft_df.reset_index()

        thirtyfiveft_df = df.iloc[:, 28:31]
        thirtyfiveft_df['Distance'] = [7 for _ in range(len(thirtyfiveft_df))]
        thirtyfiveft_df = pd.concat([biodata_df, thirtyfiveft_df], axis=1)
        thirtyfiveft_df.columns = new_cols
        thirtyfiveft_df = thirtyfiveft_df.drop(thirtyfiveft_df.columns[0], axis=1)
        thirtyfiveft_df = thirtyfiveft_df.iloc[1:, :]
        thirtyfiveft_df.reset_index()

        over40ft_df = df.iloc[:, 31:34]
        over40ft_df['Distance'] = [8 for _ in range(len(over40ft_df))]
        over40ft_df = pd.concat([biodata_df, over40ft_df], axis=1)
        over40ft_df.columns = new_cols
        over40ft_df = over40ft_df.drop(over40ft_df.columns[0], axis=1)
        over40ft_df = over40ft_df.iloc[1:, :]
        over40ft_df.reset_index()

        dist_df = pd.concat(
            [lessthan5_df, fiveft_df, tenft_df, fifteenft_df, twentyft_df, twentyfiveft_df, thirtyft_df,
             thirtyfiveft_df, over40ft_df], axis=0,
            ignore_index=True)
        dist_df.reset_index()
        print(dist_df)
        dist_df.to_csv(path_or_buf='DistTotal.csv')


def process_shotclock():
    files = [f for f in os.listdir('ShotclockData') if os.path.isfile(os.path.join('ShotclockData', f))]
    shotclock_df = pd.DataFrame()
    for file in files:
        ### code to split filename into components we want
        x,y,season,clock = file.split(sep='_')
        try:
            time, stage_raw = clock.split(sep=' ')
            stage, csv = stage_raw.split(sep='.')
        except:
            time, csv = clock.split(sep='.')
            stage = 'Beginning'

        df = pd.read_csv('ShotclockData/'+file)
        df['Season'] = [season for _ in range(len(df))]
        df['Shot Clock Time'] = [time for _ in range(len(df))]
        df['Shot Clock Range'] = [stage for _ in range(len(df))]

        shotclock_df = pd.concat([shotclock_df,df], axis=0, ignore_index=True)

    shotclock_df.to_csv(path_or_buf='ShotclockTotal.csv')