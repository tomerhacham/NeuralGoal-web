import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class raw_match:
    '''
    match-related data
    '''
    league:str
    date:datetime.date
    round:int
    home_team_name:str
    away_team_name:str
    home_team_rank:int
    away_team_rank:int
    home_scored:int
    away_scored:int
    home_att:int
    away_att:int
    home_def:int
    away_def:int
    home_mid:int
    away_mid:int
    home_shot:int
    away_shot:int
    home_shot_on_target:int
    away_shot_on_target:int
    home_corners:int
    away_corners:int
    home_fouls:int
    away_fouls:int
    home_yellow_card:int
    away_yellow_card:int
    home_red_card:int
    away_red_card:int
    home_odds_n:float
    draw_odds_n:float
    away_odds_n:float
    home_odds_nn:float
    draw_odds_nn:float
    away_odds_nn:float
    result:str

@dataclass_json
@dataclass
class calc_match:
    '''
    inferred match data to be learn with
    '''
    league: str
    date: datetime.date
    round: int
    home_team_name: str
    away_team_name: str
    home_team_rank: int
    away_team_rank: int
    home_avg_scored: int
    home_avg_received: int
    away_avg_scored: int
    away_avg_received: int
    home_att: int
    away_att: int
    home_def: int
    away_def: int
    home_mid: int
    away_mid: int
    home_avg_shot: int
    away_avg_shot: int
    home_avg_shot_on_target: int
    away_avg_shot_on_target: int
    home_avg_corners: int
    away_avg_corners: int
    home_avg_fouls: int
    away_avg_fouls: int
    home_avg_yellow_cards: int
    away_avg_yellow_cards: int
    home_avg_red_cards: int
    away_avg_red_cards: int
    home_odds_n: float
    draw_odds_n: float
    away_odds_n: float
    home_odds_nn: float
    draw_odds_nn: float
    away_odds_nn: float
    result:str


