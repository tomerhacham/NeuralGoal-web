import argparse
import sys
from datetime import datetime
from .DTOs import raw_match
import pandas as pd
from ..MongoDBConnection import MongoDBConnection
from typing import Dict

# Constant
SIDE=0
MATCH_DETAILS=1
TEAM_RELATED_FEATURES = ['scored',
                         'received',
                         'shots',
                         'shots_on_target',
                         'corners',
                         'fouls',
                         'yellow_cards',
                         'red_cards',
                         'score_shots_ratio']
DATE_FORMAT='%d/%m/%Y'


class Team:
    def __init__(self,N:int, league: str, name: str):
        self.N=N
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
        self.avg_score_shots_ratio=-1

    def addMatch(self, side:str,match: raw_match):
        '''
        @param side:str {'home'/'away'}
        @param match:raw_match object
        @return:
        '''
        self.matches.append((side,match))
        if self.matches.__len__() < self.N:
            pass
        else:
            n_last_matches = self.matches[-self.N:]
            for feature in TEAM_RELATED_FEATURES:
                _value = 0
                for pair in n_last_matches:
                    attribute=completeStat(pair[SIDE],feature)
                    _value = _value + getattr(pair[MATCH_DETAILS], attribute)
                _value = float(_value / self.N)
                setattr(self,f'avg_{feature}', _value)

class Match:
    def __init__(self, home: Team, away: Team, raw_data: raw_match):
        self.home = home
        self.away = away
        self.raw_data = raw_data
        self.home.addMatch(side='home',match=raw_data)
        self.away.addMatch(side='away',match=raw_data)

    def convert(self) -> Dict:
        return {
            'league' : self.home.league,
            'date' : self.raw_data.date,
            'home_team_name' : self.raw_data.home_team_name,
            'away_team_name' : self.raw_data.away_team_name,
            'home_team_rank' : self.raw_data.home_team_rank,
            'away_team_rank' : self.raw_data.away_team_rank,
            'home_avg_scored' : self.home.avg_scored,
            'home_avg_received' : self.home.avg_received,
            'away_avg_scored' : self.away.avg_scored,
            'away_avg_received' : self.away.avg_received,
            'home_avg_score_shots_ratio':self.home.avg_score_shots_ratio,
            'away_avg_score_shots_ratio':self.away.avg_score_shots_ratio,
            #'round' : self.raw_data.round,
            #'home_att' : self.raw_data.home_att,
            #'away_att' : self.raw_data.away_att,
            #'home_def' : self.raw_data.home_def,
            #'away_def' : self.raw_data.away_def,
            #'home_mid' : self.raw_data.home_mid,
            #'away_mid' : self.raw_data.away_mid,
            #'home_avg_shots' : self.home.avg_shots,
            #'away_avg_shots' : self.away.avg_shots,
            #'home_avg_shots_on_target' : self.home.avg_shots_on_target,
            #'away_avg_shots_on_target' : self.away.avg_shots_on_target,
            #'home_avg_corners' : self.home.avg_corners,
            #'away_avg_corners' : self.away.avg_corners,
            #'home_avg_fouls' : self.home.avg_fouls,
            #'away_avg_fouls' : self.away.avg_fouls,
            #'home_avg_yellow_cards' : self.home.avg_yellow_cards,
            #'away_avg_yellow_cards' : self.away.avg_yellow_cards,
            #'home_avg_red_cards' : self.home.avg_red_cards,
            #'away_avg_red_cards' : self.away.avg_red_cards,
            #'home_odds_n' : self.raw_data.home_odds_n,
            #'draw_odds_n' : self.raw_data.draw_odds_n,
            #'away_odds_n' : self.raw_data.away_odds_n,
            #'home_odds_nn' : self.raw_data.home_odds_nn,
            #'draw_odds_nn' : self.raw_data.draw_odds_nn,
            #'away_odds_nn' : self.raw_data.away_odds_nn,
            'result' : self.raw_data.result}

def convertStrtoDate(dict: Dict) -> Dict:
    dict['date'] = datetime.strptime(dict['date'], DATE_FORMAT).date()
    return dict


def convertDateToStr(dict: Dict) -> Dict:
    dict['date'] = dict['date'].strftime(DATE_FORMAT)
    return dict

def completeStat(side:str, feature:str)->str:
    if side=='home' and feature=='received':
        return 'away_scored'
    elif side=='away' and feature=='received':
        return 'home_scored'
    else: return f'{side}_{feature}'

def execute():
    #Parsing arguments
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('-i',type=str,action="store",required=True,help='Input from mongoDB or local CSV [mongo/path]')
    parser.add_argument('-n',type=int,action="store",required=True,help='number of game to average')
    parser.add_argument('-o',type=str,action="store",required=True,default='calc-avg',help='name of the output file')
    args = parser.parse_args()
    if args.n==None:
        raise Exception('missing require argument')
        exit(1)

    # Initialize Data
    N=args.n
    print(f'Start calculation for avg of {N}')
    Teams = {}
    calc_dataFrame = pd.DataFrame()
    dataframe=None

    if args.i=='mongo':
        connection = MongoDBConnection(mode='explore')
        connection.MainTable.delete_many({})
        #connection.RawData.remove({})
        raw_data = connection.RawData.find({}, projection={'_id': False})
        dataframe = pd.DataFrame.from_records(raw_data)
    else:
        dataframe=pd.read_csv(args.i)
    all_teams = dataframe['home_team_name'].unique()

    # construction Team's dictionary:
    print('Building Teams dictionary')
    for team in all_teams.tolist():
        if team not in Teams:
            filter = dataframe['home_team_name'] == team
            selected_frame = dataframe.where(filter, inplace=False).copy()
            selected_frame=selected_frame.dropna(how='all')
            selected_frame=selected_frame['league']
            league=selected_frame.iloc[0]
            Teams[team] = Team(N=int(N),league=league, name=team)
            print(f'{team} at {league} has been added')
    # sanity check
    if not (all_teams.__len__() == Teams.keys().__len__()) :
        print('WARNING: There is missing team',file=sys.stderr)

    # creating the calculated dataframe
    print('Start processing')
    total_rows=dataframe.shape[0]
    for index,row in dataframe.iterrows():
        a:Dict=row.to_dict()
        b=convertStrtoDate(a)
        _raw :raw_match=  raw_match(**b).adv_calc()
        obj_match:Match = Match(home=Teams[_raw.home_team_name], away=Teams[_raw.away_team_name], raw_data=_raw)
        to_insert:Dict = convertDateToStr(obj_match.convert())
        calc_dataFrame=calc_dataFrame.append(to_insert,ignore_index=True)
        #write to DB
        #connection.MainTable.insert_one(to_insert)
        print(f'{index+1}/{total_rows}',end='\r',flush=True)
    calc_dataFrame.to_csv(f'{args.o}.csv')
    print('DONE')

if __name__ == "__main__":
    execute()