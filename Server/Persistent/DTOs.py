import datetime
from dataclasses import dataclass
# todo:implement
# implement as datatclass: require python version 3.7 or above

@dataclass
class upcoming_match:
    league:str
    date:datetime.datetime
    round=int
    home_team_name=str
    away_team_name=str
    home_team_rank=int
    away_team_rank=int
    home_team_scored=float
    away_team_scored=float
    home_team_received=float
    away_team_received=float
    home_att=int
    away_att=int
    home_def=int
    away_def=int
    home_mid=int
    away_mid=int
    home_odds_n=float
    draw_odds_n=float
    away_odds_n=float
    home_odds_nn=float
    draw_odds_nn=float
    away_odds_nn=float

@dataclass
class match(upcoming_match):
    result:str

