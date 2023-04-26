import pickle

import keras.models
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder, MinMaxScaler


def choose_team():
    data = pd.read_csv('Final.csv')
    return list(data['TEAM'].unique())


def choose_player(team):
    data = pd.read_csv('Final.csv')
    return list(data[(data['TEAM'] == team) & (data['Season'] == '2022-23')]['PLAYER_NAME'].unique())


def preprocess(data, clean_data2=None):
    source_data = pd.read_csv('Final.csv')
    source_data.dropna(inplace=True)
    source_data.reset_index(inplace=True)
    source_data['ShotClock Range'] = source_data['ShotClock Range'].astype('string')
    source_data['Dist'] = source_data['Dist'].astype('string')
    p1_raw = source_data[source_data['PLAYER_NAME'] == data[0]]
    p2_raw = source_data[source_data['PLAYER_NAME'] == data[1]]
    p3_raw = source_data[source_data['PLAYER_NAME'] == data[2]]
    p4_raw = source_data[source_data['PLAYER_NAME'] == data[3]]
    p5_raw = source_data[source_data['PLAYER_NAME'] == data[4]]
    clock = source_data[source_data['PLAYER_NAME'] == data[5]]
    # quarter = data[6]

    p1_data = p1_raw.loc[:, ['FGM', 'FGA', 'FG%', 'ShotClock Range', 'Dist']]
    p2_data = p2_raw.loc[:, ['FGM', 'FGA', 'FG%', 'ShotClock Range', 'Dist']]
    p3_data = p3_raw.loc[:, ['FGM', 'FGA', 'FG%', 'ShotClock Range', 'Dist']]
    p4_data = p4_raw.loc[:, ['FGM', 'FGA', 'FG%', 'ShotClock Range', 'Dist']]
    p5_data = p5_raw.loc[:, ['FGM', 'FGA', 'FG%', 'ShotClock Range', 'Dist']]

    datalist = [p1_data, p2_data, p3_data, p4_data, p5_data]
    arrayy = []
    for data in datalist:
        fgm_max = data['FGM'].mean()
        fga_max = data['FGA'].mean()
        fgpct_max = data['FG%'].mean()
        shtclk_max = data['ShotClock Range'].max()
        dist_max = data['Dist'].max()
        listt = [fgm_max, fga_max, fgpct_max, shtclk_max, dist_max]
        arrayy.append(listt)

    df = pd.DataFrame(arrayy, columns=['FGM', 'FGA', 'FG%', 'ShotClock Range', 'Dist'])

    pipe = pickle.load(open('pipe.pkl', 'rb'))
    inputs = pipe.transform(df)
    return predict(inputs)


def predict(dataset):
    model = keras.models.load_model('dm')
    preds = model.predict(dataset)
    preds = [list(x) for x in zip(*preds)]
    final_preds = [max(x) for x in preds]
    print(final_preds)


# print(choose_team())
# print(choose_player('LAC'))
preprocess(['Jason Preston', 'John Wall', 'Kawhi Leonard', 'Marcus Morris Sr.', 'Mason Plumlee', '22-18 Very Early'])
