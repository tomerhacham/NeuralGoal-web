from Server.Persistent.DTOs import match
from datetime import date

def responseToMatchDTO(response):
    return match(league=response.league, date=date.fromisoformat(response.date), round=response.round,
             home_team_name=response.home_team_name, away_team_name=response.away_team_name,
             home_team_rank=response.home_team_rank, away_team_rank=response.away_team_rank,
             home_team_scored=response.home_team_scored, away_team_scored=response.away_team_scored,
             home_team_received=response.home_team_received, away_team_received=response.away_team_received,
             home_att=response.home_att, away_att=response.away_att,home_def=response.home_def, away_def=response.away_def,
             home_mid=response.home_mid, away_mid=response.away_mid,
             home_odds_n=response.home_odds_n, draw_odds_n=response.draw_odds_n, away_odds_n=response.away_odds_n,
             result=response.result,home_odds_nn=response.home_odds_nn,draw_odds_nn=response.draw_odds_nn,away_odds_nn=response.away_odds_nn)
