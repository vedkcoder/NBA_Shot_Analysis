import pickle

import pandas as pd
from flask import Flask, request, render_template, g
import Backend
import CourtPlot, ZonePlot
import numpy as np
import matplotlib.pyplot  as plt


app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
# model = pickle.load(open('model.pkl', 'rb'))
#
# df_1 = pd.read_csv("Dataset/first_telc.csv")
q = ''


@app.route('/')
def loadPage():
    global teamList
    teamList = Backend.choose_team()
    final_team_list = []
    for i in teamList:
        dict1 = {}
        dict1['teams'] = i
        final_team_list.append(dict1)
    return render_template('index.html', data=final_team_list)




@app.route('/',methods=['GET', 'POST'])
def playerList():
    if request.method == 'POST':
        teamList1 = Backend.choose_team()
        final_team_list = []
        for i in teamList1:
            dict1 = {}
            dict1['teams'] = i
            final_team_list.append(dict1)
        global selected_team
        selected_team = request.form.get('temp')
        print(selected_team)
        # Pass the selected_team value to another function
        players = Backend.choose_player(selected_team)
        final_player_list = []
        for i in players:
            dict2 = {}
            dict2['players'] = i
            final_player_list.append(dict2)
        return render_template('index1.html',
                               data=final_team_list,
                               data1 = final_player_list,
                               data2 = [{'q': 'Quarter'}, {'q': '1'}, {'q': '2'}, {'q': '3'}, {'q': '4'}])


@app.route('/index1',methods=['POST'])
def predict():
    print(selected_team)
    if request.method == 'POST':
        player1 = request.form['temp1']
        player2 = request.form['temp2']
        player3 = request.form['temp3']
        player4 = request.form['temp4']
        player5 = request.form['temp5']
        shotClock = int(request.form['ShotClock'])
        quarter = request.form['temp6']

        if shotClock < 5:
            shotClock = '4-0 Very Late'
        elif 5 <= shotClock < 7:
            shotClock = '7-4 Late'
        elif 8 <= shotClock < 15:
            shotClock = '15-7 Average'
        elif 16 <= shotClock < 18:
            shotClock = '18-15 Early'
        elif 18 <= shotClock < 22:
            shotClock = '22-18 Very Early'
        else:
            shotClock = '24-22'

        data = [player1, player2, player3, player4, player5, shotClock, quarter]


        p_list =  [player1, player2, player3, player4, player5]
        prob_list = Backend.preprocess(data)

        str_team = str(selected_team)

        index1 = teamList.index(str_team)

        nba_teams = ['Denver Nuggets', 'Indiana Pacers', 'Boston Celtics', 'Phoenix Suns', 'Chicago Bulls',
                     'Oklahoma City Thunder', 'New York Knicks', 'Golden State Warriors', 'Los Angeles Lakers',
                     'Washington Wizards', 'Brooklyn Nets', 'Los Angeles Clippers', 'Cleveland Cavaliers', 'Miami Heat',
                     'Portland Trail Blazers', 'Minnesota Timberwolves', 'Houston Rockets', 'Philadelphia 76ers',
                     'Toronto Raptors', 'Milwaukee Bucks', 'Charlotte Hornets', 'Dallas Mavericks', 'Atlanta Hawks',
                     'Utah Jazz', 'Memphis Grizzlies', 'New Orleans Pelicans', 'Sacramento Kings', 'Orlando Magic',
                     'Detroit Pistons', 'San Antonio Spurs']

        plot_list = []
        for i in p_list:
            try:
                fname, lname = i.split(' ')
            except:
                fname, lname, ext = i.split(' ')
                lname = lname+ ' ' +ext


            plot_data = CourtPlot.draw_plot(nba_teams[index1], fname, lname)
            plot_list.append(plot_data)

        max_prob = np.argmax(prob_list)
        min_prob = np.argmin(prob_list)

        max_plot = which_zone(max_prob)
        min_plot = which_zone(min_prob)


        return render_template('index2.html',
                               plot_list= plot_list,
                               p_list = p_list,
                               max_plot = max_plot,
                               min_plot = min_plot)


def which_zone(x):
    fig = plt.figure(figsize=(3, 2.76))
    ax = fig.add_axes([0, 0, 1, 1])
    if x == 0:
        return ZonePlot.create_court_restricted(ax, 'black')
    elif x == 1:
        return ZonePlot.create_court_paint(ax, 'black')
    elif x == 2:
        return ZonePlot.create_court_midrange(ax, 'black')
    elif x == 3:
        return ZonePlot.create_court_left_corner_3(ax, 'black')
    elif x == 4:
        return ZonePlot.create_court_right_corner_3(ax, 'black')
    elif x == 5:
        return ZonePlot.create_court_above_the_break_3(ax, 'black')
    else:
        return ZonePlot.create_court_backcourt(ax, 'black')

if __name__ == "__main__":
    app.run(debug=True)
