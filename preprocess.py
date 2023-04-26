# This file handles all preprocessing of data
# Function preprocess_zone data is used for breaking down data by individual zones and vertically stacking them to make zone a column in the dataset.
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
import os
import pandas as pd
import random
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense
import pickle


def process_zone():
    # mapping:- 0: Restricted, 1: Paint NonRA, 2: MidRange, 3: Left3, 4: Right3, 5: Break, 6: Backcourt, 7: Corner3

    ### Files variable is list of csv files
    files = [f for f in os.listdir('ZoneData') if os.path.isfile(os.path.join('ZoneData', f))]
    zone_df_t = pd.DataFrame()
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
        biodata_df['Season'] = [z1 for _ in range(len(biodata_df))]

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
        zone_df_t = pd.concat([zone_df_t, zone_df], axis=0)

    zone_df_t.to_csv(path_or_buf='ZoneTotal.csv')


### similarly for distance
def process_dist():
    # mapping :- 0: Less than 5ft, 1: 5-9ft, 2: 10-14ft, 3: 15-19ft, 4: 20-24ft, 5: 25-29ft, 6: 30-34ft, 7: 35-39ft, 8: 40+ft
    files = [f for f in os.listdir('DistData') if os.path.isfile(os.path.join('DistData', f))]
    dist_df_t = pd.DataFrame()
    for file in files:
        new_cols = ['index', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'Team', 'Age', 'Season','FGM', 'FGA', 'FG%', 'Distance']
        df = pd.read_csv('DistData/' + file)
        biodata_df = df.iloc[:, :6]

        x, y, z = file.split(sep='_')
        z1, z2 = z.split(sep='.')
        biodata_df['Season'] = [z1 for _ in range(len(biodata_df))]

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
        dist_df_t= pd.concat([dist_df_t,dist_df], axis=0)

    dist_df_t.to_csv(path_or_buf='DistTotal.csv')



def process_shotclock():
    files = [f for f in os.listdir('ShotclockData') if os.path.isfile(os.path.join('ShotclockData', f))]
    shotclock_df = pd.DataFrame()
    for file in files:
        ### code to split filename into components we want
        x,y,season,clock = file.split(sep='_')
        time, csv = clock.split('.')

        df = pd.read_csv('ShotclockData/'+file)
        df['Season'] = [season for _ in range(len(df))]
        df['Shot Clock Time'] = [time for _ in range(len(df))]

        shotclock_df = pd.concat([shotclock_df,df], axis=0, ignore_index=True)

    shotclock_df.to_csv(path_or_buf='ShotclockTotal.csv')


def process_combined():
    files = [f for f in os.listdir('CombinedData') if os.path.isfile(os.path.join('CombinedData', f))]
    new_cols = ['index', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM', 'Age', 'Season', 'FGM', 'FGA', 'FG%', 'Zone','ShotClock Range']
    combined_df_t = pd.DataFrame()
    for file in files:
        df = pd.read_csv('CombinedData/' + file)

        ### df for biodata
        biodata_df = df.iloc[:, :6]

        ### split file string to get season
        x, y, z = file.split(sep='_')
        z1, z2 = z.split(sep='.')

        ### add to biodata column
        biodata_df['Season'] = [y for _ in range(len(biodata_df))]

        ### split dataframes to get df for each zone and preprocess it
        restricted_dat = df.iloc[:, 7:10]
        restricted_dat['Zone'] = [0 for _ in range(len(restricted_dat))]
        restricted_dat['ShotClock Range'] = [z1 for _ in range(len(restricted_dat))]
        restricted_dat = pd.concat([biodata_df, restricted_dat], axis=1)
        restricted_dat.columns = new_cols
        restricted_dat = restricted_dat.drop(restricted_dat.columns[0], axis=1)
        restricted_dat = restricted_dat.iloc[1:, :]
        restricted_dat.reset_index()

        paint_dat = df.iloc[:, 10:13]
        paint_dat['Zone'] = [1 for _ in range(len(paint_dat))]
        paint_dat['ShotClock Range'] = [z1 for _ in range(len(paint_dat))]
        paint_dat = pd.concat([biodata_df, paint_dat], axis=1)
        paint_dat.columns = new_cols
        paint_dat = paint_dat.drop(paint_dat.columns[0], axis=1)
        paint_dat = paint_dat.iloc[1:, :]
        paint_dat.reset_index()

        midrange_dat = df.iloc[:, 13:16]
        midrange_dat['Zone'] = [2 for _ in range(len(midrange_dat))]
        midrange_dat['ShotClock Range'] = [z1 for _ in range(len(midrange_dat))]
        midrange_dat = pd.concat([biodata_df, midrange_dat], axis=1)
        midrange_dat.columns = new_cols
        midrange_dat = midrange_dat.drop(midrange_dat.columns[0], axis=1)
        midrange_dat = midrange_dat.iloc[1:, :]
        midrange_dat.reset_index()

        left3_dat = df.iloc[:, 16:19]
        left3_dat['Zone'] = [3 for _ in range(len(left3_dat))]
        left3_dat['ShotClock Range'] = [z1 for _ in range(len(left3_dat))]
        left3_dat = pd.concat([biodata_df, left3_dat], axis=1)
        left3_dat.columns = new_cols
        left3_dat = left3_dat.drop(left3_dat.columns[0], axis=1)
        left3_dat = left3_dat.iloc[1:, :]
        left3_dat.reset_index()

        right3_dat = df.iloc[:, 19:22]
        right3_dat['Zone'] = [4 for _ in range(len(right3_dat))]
        right3_dat['ShotClock Range'] = [z1 for _ in range(len(right3_dat))]
        right3_dat = pd.concat([biodata_df, right3_dat], axis=1)
        right3_dat.columns = new_cols
        right3_dat = right3_dat.drop(right3_dat.columns[0], axis=1)
        right3_dat = right3_dat.iloc[1:, :]
        right3_dat.reset_index()

        break3_dat = df.iloc[:, 22:25]
        break3_dat['Zone'] = [5 for _ in range(len(break3_dat))]
        break3_dat['ShotClock Range'] = [z1 for _ in range(len(break3_dat))]
        break3_dat = pd.concat([biodata_df, break3_dat], axis=1)
        break3_dat.columns = new_cols
        break3_dat = break3_dat.drop(break3_dat.columns[0], axis=1)
        break3_dat = break3_dat.iloc[1:, :]
        break3_dat.reset_index()

        back_dat = df.iloc[:, 25:28]
        back_dat['Zone'] = [6 for _ in range(len(back_dat))]
        back_dat['ShotClock Range'] = [z1 for _ in range(len(back_dat))]
        back_dat = pd.concat([biodata_df, back_dat], axis=1)
        back_dat.columns = new_cols
        back_dat = back_dat.drop(back_dat.columns[0], axis=1)
        back_dat = back_dat.iloc[1:, :]
        back_dat.reset_index()

        corner3_dat = df.iloc[:, 28:31]
        corner3_dat['Zone'] = [7 for _ in range(len(corner3_dat))]
        corner3_dat['ShotClock Range'] = [z1 for _ in range(len(corner3_dat))]
        corner3_dat = pd.concat([biodata_df, corner3_dat], axis=1)
        corner3_dat.columns = new_cols
        corner3_dat = corner3_dat.drop(corner3_dat.columns[0], axis=1)
        corner3_dat = corner3_dat.iloc[1:, :]
        corner3_dat.reset_index()

        ### combine stacking all df horizontally and saving csv
        combined_df = pd.concat(
            [restricted_dat, paint_dat, midrange_dat, left3_dat, right3_dat, break3_dat, back_dat, corner3_dat], axis=0,
            ignore_index=True)
        combined_df.reset_index()
        combined_df_t = pd.concat([combined_df_t, combined_df], axis=0)

    combined_df_t.to_csv(path_or_buf='CombinedTotal.csv')

### code to preprocess and merge all 3 features
def merge(df):
    new_df = pd.DataFrame()
    for i in range(len(df)):
        print(i)
        datapoint = pd.DataFrame(df.loc[i,:])
        datapoint = datapoint.transpose()
        datapoint['Dist'] = None
        new_df = pd.concat([new_df, datapoint], axis=0)
        if datapoint.loc[i,'Zone'].item() == 0:
            new_df.loc[i, 'Dist'] = '<5'

        if datapoint.loc[i, 'Zone'].item() == 1:
            num = random.randint(0, 1)
            if num == 0:
                new_df.loc[i, 'Dist'] = '5-9'
            else:
                new_df.loc[i, 'Dist'] = '10-14'

        if datapoint.loc[i, 'Zone'].item() == 2:
            num = random.randint(0,2)
            if num == 0:
                new_df.loc[i, 'Dist'] = '15-19'
            elif num == 1:
                new_df.loc[i, 'Dist'] = '20-24'
            else:
                new_df.loc[i, 'Dist'] = '25-30'

        if datapoint.loc[i, 'Zone'].item() == 3:
            num = random.randint(0, 1)
            if num == 0:
                new_df.loc[i, 'Dist'] = '25-29'
            else:
                new_df.loc[i, 'Dist'] = '30-34'

        if datapoint.loc[i, 'Zone'].item() == 4:
            num = random.randint(0, 1)
            if num == 0:
                new_df.loc[i, 'Dist'] = '25-29'
            else:
                new_df.loc[i, 'Dist'] = '30-34'

        if datapoint.loc[i, 'Zone'].item() == 5:
            new_df.loc[i, 'Dist'] = '30-34'

        if datapoint.loc[i, 'Zone'].item() == 6:
            num = random.randint(0, 1)
            if num == 0:
                new_df.loc[i, 'Dist'] = '35-39'
            else:
                new_df.loc[i, 'Dist'] = '40>'

    return new_df

def train():
    data = pd.read_csv('Final.csv')
    data1 = data.dropna()
    clean_data = data1.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'PLAYER_NAME', 'PLAYER_ID', 'TEAM_ID', 'TEAM', 'Age', 'Season'])
    clean_data = clean_data.reset_index()
    clean_data1 = clean_data.drop('index', axis=1)
    y = clean_data[['Zone']]
    clean_data2 = clean_data1.drop(['Zone'], axis=1)

    sc = StandardScaler()
    cat_cols = ['ShotClock Range', 'Dist']
    OE = OneHotEncoder()
    oe = OneHotEncoder()
    oe.fit(clean_data2)
    # print(OE)
    # return
    numeric_cols = ['FGM', 'FGA', 'FG%']
    num_pipeline = Pipeline(steps=[('Imputer', SimpleImputer(strategy='median')), ('Standard Scaler', StandardScaler())])
    ct = ColumnTransformer(transformers=[('cats', OE, cat_cols), ('num', num_pipeline, numeric_cols)])
    pipe = Pipeline(steps=[('pipe', ct)])
    pipe.fit(clean_data2)
    inputs = pipe.transform(clean_data2)
    inputs = inputs.toarray()
    x_train, x_test, y_train, y_test = train_test_split(inputs, y, test_size=0.2, random_state=0)

    model = Sequential()
    model.add(Dense(units=256, activation='leaky_relu', input_dim=19, name='Input'))
    model.add(Dense(units=256, activation='leaky_relu', name='Hidden_1'))
    model.add(keras.layers.Dropout(rate=0.2, name='Dropout_1'))
    model.add(Dense(units=256, activation='leaky_relu', name='Hidden_2'))
    model.add(keras.layers.Dropout(rate=0.2, name='DropOut_2'))
    model.add(Dense(units=7, activation='softmax', name='Output'))

    model.compile(optimizer=keras.optimizers.Adam(lr=0.0001), loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    model.summary()

    model.fit(x_train, y_train, epochs=5, validation_split=0.1, batch_size=32)
    keras.models.save_model(model, filepath='dm/')
    pickle.dump(pipe, open('pipe.pkl', 'wb'))




