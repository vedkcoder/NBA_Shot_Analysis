# NBA api ka usage explained here
# Sab data is stored in endpoints class. Endpoints dhundo nba.com/advanced stats pe jake jo required ho or nba_api ke github pe you will find names of endpoints.
# Import from endpoints any data you need, and then create an object with the parameters. store as json and convert to df using .get_data_frames() method

from nba_api.stats.endpoints import leaguedashplayershotlocations as zone
from nba_api.stats.endpoints import leaguedashplayerptshot as shot


def create_zone_dataset():
    dataset = []
    seasons = ['2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18']
    for season in seasons:
        obj = zone.LeagueDashPlayerShotLocations(distance_range='By Zone', per_mode_detailed='Totals',
                                                 season_type_all_star='Regular Season', season=season)
        df = obj.get_data_frames()[0]
        df.to_csv(path_or_buf=f'ZoneData/zone_for_{season}.csv'.format(season=season), sep=',')


def create_dist_dataset():
    dataset = []
    seasons = ['2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18']
    for season in seasons:
        obj = zone.LeagueDashPlayerShotLocations(distance_range='5ft Range', per_mode_detailed='Totals',
                                                 season_type_all_star='Regular Season', season=season)
        df = obj.get_data_frames()[0]
        df.to_csv(path_or_buf=f'DistData/dist_for_{season}.csv'.format(season=season))


def create_shotclock_dataset():
    dataset = []
    seasons = ['2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18']

    for season in seasons:
        shot_clocks = ['24-22', '22-18 Very Early', '18-15 Early', '15-7 Average', '7-4 Late', '4-0 Very Late']
        for clock in shot_clocks:
            obj = shot.LeagueDashPlayerPtShot(season=season, per_mode_simple='Totals', season_type_all_star='Regular Season', shot_clock_range_nullable=clock)
            df = obj.get_data_frames()[0]
            df.to_csv(path_or_buf=f'ShotclockData/shotclock_for_{season}_{clock}.csv'.format(season=season, clock=clock))