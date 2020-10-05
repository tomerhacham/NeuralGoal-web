from datetime import datetime
from .DTOs import raw_match, calc_match
import pandas as pd
from Server.DataAccess.MongoDBConnection import MongoDBConnection
from typing import Dict

# Initialize Data
Teams = {}
TEAM_RELATED_FEATURES = ['avg_scored',
                         'avg_received',
                         'avg_shot',
                         'avg_shot_on_target',
                         'avg_corner',
                         'avg_fouls',
                         'avg_yellow_cards',
                         'avg_red_cards']
calc_dataFrame = pd.DataFrame()
n = 3


class Team:
    def __init__(self, league: str, name: str):
        self.league = league
        self.name = name
        self.matches = []
        # team_related_features
        self.avg_scored = -1
        self.avg_received = -1
        self.avg_shot = -1
        self.avg_shot_on_target = -1
        self.avg_corner = -1
        self.avg_fouls = -1
        self.avg_yellow_cards = -1
        self.avg_red_cards = -1

    def addMatch(self, match: raw_match):
        self.matches.append(match)
        if self.matches.__len__() < n:
            pass
        else:
            n_last_matches = self.matches[:-self.n]
            for feature in TEAM_RELATED_FEATURES:
                _value = 0
                for match in n_last_matches:
                    _value = _value + getattr(match, feature)
                _value = float(_value / self.n)
                setattr(self, feature, _value)


class Match:
    def __init__(self, home: Team, away: Team, raw_data: raw_match):
        self.home = home
        self.away = away
        self.raw_data = raw_data

    def convert(self) -> calc_match:
        calc = calc_match()
        calc.league = self.home.league
        calc.date = self.raw_data.date
        calc.round = self.raw_data.round
        calc.home_team_name = self.raw_data.home_team_name
        calc.away_team_name = self.raw_data.away_team_name
        calc.home_team_rank = self.raw_data.home_team_rank
        calc.away_team_rank = self.raw_data.away_team_rank
        calc.home_avg_scored = self.home.avg_scored
        calc.home_avg_received = self.home.avg_received
        calc.away_avg_scored = self.away.avg_scored
        calc.away_avg_received = self.away.avg_received
        calc.home_att = self.raw_data.home_att
        calc.away_att = self.raw_data.away_att
        calc.home_def = self.raw_data.home_def
        calc.away_def = self.raw_data.away_def
        calc.home_mid = self.raw_data.home_mid
        calc.away_mid = self.raw_data.away_mid
        calc.home_avg_shot = self.home.avg_shot
        calc.away_avg_shot = self.away.avg_scored
        calc.home_avg_shot_on_target = self.home.avg_shot_on_target
        calc.away_avg_shot_on_target = self.away.avg_shot_on_target
        calc.home_avg_corners = self.home.avg_corner
        calc.away_avg_corners = self.away.avg_corner
        calc.home_avg_fouls = self.home.avg_fouls
        calc.away_avg_fouls = self.away.avg_fouls
        calc.home_avg_yellow_cards = self.home.avg_yellow_cards
        calc.away_avg_yellow_cards = self.away.avg_yellow_cards
        calc.home_avg_red_cards = self.home.avg_red_cards
        calc.away_avg_red_cards = self.away.avg_red_cards
        calc.home_odds_n = self.raw_data.home_odds_n
        calc.draw_odds_n = self.raw_data.draw_odds_n
        calc.away_odds_n = self.raw_data.away_odds_n
        calc.home_odds_nn = self.raw_data.home_odds_nn
        calc.draw_odds_nn = self.raw_data.draw_odds_nn
        calc.away_odds_nn = self.raw_data.away_odds_nn
        calc.result = self.raw_data.result
        return calc


def convertStrtoDate(dict: Dict) -> Dict:
    dict['date'] = datetime.datetime.strptime(dict['date'], '%d-%m-%Y').date()
    return dict


def convertDateToStr(dict: Dict) -> Dict:
    dict['date'] = dict['date'].strftime("%d-%m-%Y")
    return dict


connection = MongoDBConnection(mode='explore')
connection.MainTable.remove({})
raw_data = connection.RawData.find({}, projection={'_id': False})
dataframe = pd.DataFrame.from_records(raw_data)
all_teams = dataframe['home_team_name'].unique()

# construction Team's dictionary:
for team in all_teams.tolist():
    if Teams[team] == None:
        filter = dataframe['home_team_name'] == team
        league = dataframe.where(filter, inplace=False)['league']
        Teams[team] = Team(league=league, name=team)
# sanity check
print(f'is same length?: {all_teams.__len__() == Teams.keys().__len__()}')

# creating the calculated dataframe
for row in raw_data:
    _raw_match = raw_match(**convertStrtoDate(row))
    obj_match = Match(home=Teams[_raw_match.home_team_name], away=Teams[_raw_match.away_team_name], raw_data=_raw_match)
    to_insert = convertDateToStr(obj_match.convert().to_dict())
    calc_dataFrame.append(to_insert)
    #write to DB
    connection.MainTable.insert_one(to_insert.to_dict())

print('Calculation ended')
