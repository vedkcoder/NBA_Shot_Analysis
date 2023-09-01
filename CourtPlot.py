import base64
import io

from nba_api.stats.endpoints import shotchartdetail
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


players = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/players.json').text)

def get_player_id(first, last):
    for player in players:
        if player['firstName'] == first and player['lastName'] == last:
            return player['playerId']
    return -1

teams = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json').text)

def get_team_id(team_name):
    for team in teams:
        if team['teamName'] == team_name:
            return team['teamId']
    return -1


def get_json_data(team_name, player_fn, player_ln, season, cms):
    shot_json = shotchartdetail.ShotChartDetail(
            team_id = get_team_id(team_name),
            player_id = get_player_id(player_fn, player_ln),
            context_measure_simple = cms,
            season_nullable = season,
            season_type_all_star = 'Regular Season')
    return json.loads(shot_json.get_json())


def json_to_df(json_data):
    relevant_data = json_data['resultSets'][0]
    headers = relevant_data['headers']
    rows = relevant_data['rowSet']

    # Create pandas DataFrame
    player_data = pd.DataFrame(rows)
    player_data.columns = headers

    return player_data, headers


def create_court(ax, color):
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
    ax.add_artist(mpl.patches.Arc((0, 35), 80, 110, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))

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

    return ax

def draw_plot(team_name, player_fn, player_ln, season = '2021-22', cms = 'FGM'):
    try:
        json_data = get_json_data(team_name, player_fn, player_ln, season, cms)
        player_data, header = json_to_df(json_data)


        mpl.rcParams['font.family'] = 'Avenir'
        mpl.rcParams['font.size'] = 18
        mpl.rcParams['axes.linewidth'] = 2

        # Create figure and axes
        fig = plt.figure(figsize=(3, 2.76))
        ax = fig.add_axes([0, 0, 1, 1])



        # Plot hexbin of shots
        ax.hexbin(player_data['LOC_X'], player_data['LOC_Y'] + 60, gridsize=(30, 30), extent=(-300, 300, 0, 940), bins='log',
                  cmap='Reds')
        ax = create_court(ax, 'black')
    except:
        fig = plt.figure(figsize=(3, 2.76))
        ax = fig.add_axes([0, 0, 1, 1])
        ax = create_court(ax, 'black')

    # Draw court

    # plt.show()
    # return
    # Annotate player name and season
    # ax.text(0, 1.05, 'Stephen Curry\n2015-16 Regular Season', transform=ax.transAxes, ha='left', va='baseline')
    buffer = io.BytesIO()
    # Save and show figure
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    return plot_data

