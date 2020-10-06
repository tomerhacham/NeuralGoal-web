from datetime import datetime
from Server.DataAccess.Utils.DTOs import raw_match, calc_match
import pandas as pd
from Server.DataAccess.MongoDBConnection import MongoDBConnection
from typing import Dict

# Initialize Data
Teams = {}
SIDE=0
MATCH_DETAILS=1
TEAM_RELATED_FEATURES = ['scored',
                         'received',
                         'shots',
                         'shots_on_target',
                         'corners',
                         'fouls',
                         'yellow_cards',
                         'red_cards']
calc_dataFrame = pd.DataFrame()
N = 3


class Team:
    def __init__(self, league: str, name: str):
        self.league = league
        self.name = name
        self.matches = [] #lsit of tuple (side,match_details)
        # team_related_features
        self.avg_scored = -1
        self.avg_received = -1
        self.avg_shots = -1
        self.avg_shots_on_target = -1
        self.avg_corners = -1
        self.avg_fouls = -1
        self.avg_yellow_cards = -1
        self.avg_red_cards = -1

    def addMatch(self, side:str,match: raw_match):
        '''
        @param side:str {'home'/'away'}
        @param match:raw_match object
        @return:
        '''
        self.matches.append((side,match))
        if self.matches.__len__() < N:
            pass
        else:
            n_last_matches = self.matches[-N:]
            for feature in TEAM_RELATED_FEATURES:
                _value = 0
                for pair in n_last_matches:
                    attribute=completeStat(pair[SIDE],feature)
                    _value = _value + getattr(pair[MATCH_DETAILS], attribute)
                _value = float(_value / N)
                setattr(self,f'avg_{feature}', _value)


class Match:
    def __init__(self, home: Team, away: Team, raw_data: raw_match):
        self.home = home
        self.away = away
        self.raw_data = raw_data
        self.home.addMatch(side='home',match=raw_data)
        self.away.addMatch(side='away',match=raw_data)


    def convert(self) -> calc_match:
        values_dict={
            'league' : self.home.league,
            'date' : self.raw_data.date,
            'round' : self.raw_data.round,
            'home_team_name' : self.raw_data.home_team_name,
            'away_team_name' : self.raw_data.away_team_name,
            'home_team_rank' : self.raw_data.home_team_rank,
            'away_team_rank' : self.raw_data.away_team_rank,
            'home_avg_scored' : self.home.avg_scored,
            'home_avg_received' : self.home.avg_received,
            'away_avg_scored' : self.away.avg_scored,
            'away_avg_received' : self.away.avg_received,
            'home_att' : self.raw_data.home_att,
            'away_att' : self.raw_data.away_att,
            'home_def' : self.raw_data.home_def,
            'away_def' : self.raw_data.away_def,
            'home_mid' : self.raw_data.home_mid,
            'away_mid' : self.raw_data.away_mid,
            'home_avg_shots' : self.home.avg_shots,
            'away_avg_shots' : self.away.avg_scored,
            'home_avg_shots_on_target' : self.home.avg_shots_on_target,
            'away_avg_shots_on_target' : self.away.avg_shots_on_target,
            'home_avg_corners' : self.home.avg_corners,
            'away_avg_corners' : self.away.avg_corners,
            'home_avg_fouls' : self.home.avg_fouls,
            'away_avg_fouls' : self.away.avg_fouls,
            'home_avg_yellow_cards' : self.home.avg_yellow_cards,
            'away_avg_yellow_cards' : self.away.avg_yellow_cards,
            'home_avg_red_cards' : self.home.avg_red_cards,
            'away_avg_red_cards' : self.away.avg_red_cards,
            'home_odds_n' : self.raw_data.home_odds_n,
            'draw_odds_n' : self.raw_data.draw_odds_n,
            'away_odds_n' : self.raw_data.away_odds_n,
            'home_odds_nn' : self.raw_data.home_odds_nn,
            'draw_odds_nn' : self.raw_data.draw_odds_nn,
            'away_odds_nn' : self.raw_data.away_odds_nn,
            'result' : self.raw_data.result}
        calc = calc_match(**values_dict)
        #calc.league = self.home.league
        #calc.date = self.raw_data.date
        #calc.round = self.raw_data.round
        #calc.home_team_name = self.raw_data.home_team_name
        #calc.away_team_name = self.raw_data.away_team_name
        #calc.home_team_rank = self.raw_data.home_team_rank
        #calc.away_team_rank = self.raw_data.away_team_rank
        #calc.home_avg_scored = self.home.avg_scored
        #calc.home_avg_received = self.home.avg_received
        #calc.away_avg_scored = self.away.avg_scored
        #calc.away_avg_received = self.away.avg_received
        #calc.home_att = self.raw_data.home_att
        #calc.away_att = self.raw_data.away_att
        #calc.home_def = self.raw_data.home_def
        #calc.away_def = self.raw_data.away_def
        #calc.home_mid = self.raw_data.home_mid
        #calc.away_mid = self.raw_data.away_mid
        #calc.home_avg_shot = self.home.avg_shot
        #calc.away_avg_shot = self.away.avg_scored
        #calc.home_avg_shot_on_target = self.home.avg_shot_on_target
        #calc.away_avg_shot_on_target = self.away.avg_shot_on_target
        #calc.home_avg_corners = self.home.avg_corner
        #calc.away_avg_corners = self.away.avg_corner
        #calc.home_avg_fouls = self.home.avg_fouls
        #calc.away_avg_fouls = self.away.avg_fouls
        #calc.home_avg_yellow_cards = self.home.avg_yellow_cards
        #calc.away_avg_yellow_cards = self.away.avg_yellow_cards
        #calc.home_avg_red_cards = self.home.avg_red_cards
        #calc.away_avg_red_cards = self.away.avg_red_cards
        #calc.home_odds_n = self.raw_data.home_odds_n
        #calc.draw_odds_n = self.raw_data.draw_odds_n
        #calc.away_odds_n = self.raw_data.away_odds_n
        #calc.home_odds_nn = self.raw_data.home_odds_nn
        #calc.draw_odds_nn = self.raw_data.draw_odds_nn
        #calc.away_odds_nn = self.raw_data.away_odds_nn
        #calc.result = self.raw_data.result
        return calc


def convertStrtoDate(dict: Dict) -> Dict:
    dict['date'] = datetime.strptime(dict['date'], '%d/%m/%Y').date()
    return dict


def convertDateToStr(dict: Dict) -> Dict:
    dict['date'] = dict['date'].strftime("%d/%m/%Y")
    return dict

def completeStat(side:str, feature:str)->str:
    if side=='home' and feature=='received':
        return 'away_scored'
    elif side=='away' and feature=='received':
        return 'home_scored'
    else: return f'{side}_{feature}'



connection = MongoDBConnection(mode='explore')
connection.MainTable.remove({})
#connection.RawData.remove({})
raw_data = connection.RawData.find({}, projection={'_id': False})
dataframe = pd.DataFrame.from_records(raw_data)
all_teams = dataframe['home_team_name'].unique()

# construction Team's dictionary:
for team in all_teams.tolist():
    if team not in Teams:
        filter = dataframe['home_team_name'] == team
        league = dataframe.where(filter, inplace=False).loc[0,'league']
        Teams[team] = Team(league=league, name=team)
# sanity check
print(f'is same length?: {all_teams.__len__() == Teams.keys().__len__()}')

# creating the calculated dataframe
for row in dataframe.iterrows():
    a=row[1].to_dict()
    _raw =  raw_match(**(convertStrtoDate(a)))
    obj_match = Match(home=Teams[_raw.home_team_name], away=Teams[_raw.away_team_name], raw_data=_raw)
    to_insert = convertDateToStr(obj_match.convert().to_dict())
    calc_dataFrame=calc_dataFrame.append(to_insert,ignore_index=True)
    #write to DB
    connection.MainTable.insert_one(to_insert)

print('Calculation ended')
