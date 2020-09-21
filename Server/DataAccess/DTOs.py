import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List,Tuple

# todo:implement
# implement as datatclass: require python version 3.7 or above

@dataclass_json
@dataclass
class upcoming_match:
    league:str
    date:datetime.date
    round:int
    home_team_name:str
    away_team_name:str
    home_team_rank:int
    away_team_rank:int
    home_team_scored:float
    away_team_scored:float
    home_team_received:float
    away_team_received:float
    home_att:int
    away_att:int
    home_def:int
    away_def:int
    home_mid:int
    away_mid:int
    home_odds_n:float
    draw_odds_n:float
    away_odds_n:float
    home_odds_nn:float
    draw_odds_nn:float
    away_odds_nn:float

@dataclass_json
@dataclass
class match(upcoming_match):
    result:str

@dataclass_json
@dataclass
class prediction:
    league:str
    date:datetime.date
    home_team_name:str
    away_team_name:str
    home_odds_nn:float
    draw_odds_nn:float
    away_odds_nn:float
    pred_1:float
    pred_2:float
    pred_x:float
    expected:float
    result:str

@dataclass_json
@dataclass
class betMatch:
    matchID:str
    date: str
    league:str
    home_team_name:str
    away_team_name:str
    result:str
    associateBets:List[str]

@dataclass_json
@dataclass
class betForm:
    receiptID:str
    date: datetime.date
    bet_value:float
    bet_odd:float
    isWin:bool
    profitExpectation:float
    bets:List[Tuple[str,str]]


