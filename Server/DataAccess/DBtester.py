import unittest
from datetime import date

from Server.BetsFinancial.Match import Match, Result
from Server.DataAccess.DTOs import match,betForm,betMatch,upcoming_match
from Server.DataAccess import DBController as db

today = date.today()

class MyTestCase(unittest.TestCase):
    def test_insertMatchToMainTable(self):
        db.DBConnection.MainTable.remove({})
        _match=match(away_att=77,away_def=67,away_mid=69,away_odds_n=0.27669516494195245,
                    away_odds_nn=3.2583333333333333,away_team_name="Sampdoria",away_team_rank=11,
                    away_team_received=2,away_team_scored=1,date=today,draw_odds_n=0.31504895018143103,
                    draw_odds_nn=2.8616666666666664,home_att=80,home_def=71,home_mid=74,home_odds_n=0.4082558848766165,
                    home_odds_nn=2.208333333333333,home_team_name="Fiorentina",home_team_rank=18,
                    home_team_received=1,home_team_scored=2,league="Serie",result="1",round=1)
        db.insertMatchToMainTable(_match)
        record=db.DBConnection.MainTable.find_one({},projection={'_id': False})
        record = db.convertStrtoDate(record)
        found = match.from_dict(record)
        self.assertEqual(_match, found)
    def test_insertMatchToUpcomingGames(self):
        db.DBConnection.UpcomingGames.remove({})
        _match=upcoming_match(away_att=77,away_def=67,away_mid=69,away_odds_n=0.27669516494195245,
                    away_odds_nn=3.2583333333333333,away_team_name="Sampdoria",away_team_rank=11,
                    away_team_received=2,away_team_scored=1,date=today,draw_odds_n=0.31504895018143103,
                    draw_odds_nn=2.8616666666666664,home_att=80,home_def=71,home_mid=74,home_odds_n=0.4082558848766165,
                    home_odds_nn=2.208333333333333,home_team_name="Fiorentina",home_team_rank=18,
                    home_team_received=1,home_team_scored=2,league="Serie",round=1)
        db.insertMatchToUpcomingGames(_match)
        record=db.DBConnection.UpcomingGames.find_one({},projection={'_id': False})
        record = db.convertStrtoDate(record)
        found = upcoming_match.from_dict(record)
        self.assertEqual(_match, found)
    def test_deleteMatchFromUpcomingGames(self):
        self.test_insertMatchToUpcomingGames()
        db.deleteMatchFromUpcomingGames(date=today.strftime('%d-%m-%Y'),home_team_name="Fiorentina",away_team_name="Sampdoria")
        number_of_record=db.DBConnection.UpcomingGames.find({}).count()
        self.assertEqual(number_of_record,0)
    def test_getUpcomingGames(self):
        db.DBConnection.UpcomingGames.remove({})
        _match = upcoming_match(away_att=77, away_def=67, away_mid=69, away_odds_n=0.27669516494195245,
                       away_odds_nn=3.2583333333333333, away_team_name="Sampdoria", away_team_rank=11,
                       away_team_received=2, away_team_scored=1, date=today, draw_odds_n=0.31504895018143103,
                       draw_odds_nn=2.8616666666666664, home_att=80, home_def=71, home_mid=74,
                       home_odds_n=0.4082558848766165,
                       home_odds_nn=2.208333333333333, home_team_name="Fiorentina", home_team_rank=18,
                       home_team_received=1, home_team_scored=2, league="Serie", round=1)
        db.insertMatchToUpcomingGames(_match)
        dtos=db.getUpcomingGames(league='all')
        self.assertEqual(_match, dtos[0])
    def test_saveMatch(self):
        db.DBConnection.Matches.remove({})
        newMatch = Match(matchID='{}_TeamA_TeamB'.format(today),date=today,league='league',
                         home_team='TeamA', away_team='TeamB', result=Result.Home)
        db.saveMatch(newMatch.toDTO())
        found=db.findMatch(matchID='{}_TeamA_TeamB'.format(today))
        self.assertEqual(newMatch,found)
    def test_saveBetForm(self):
        db.DBConnection.BetForms.remove({})
        form=betForm(receiptID='ID',date=today,bet_value=10.3131,
                     bet_odd=11.33,isWin=False,profitExpectation=10.3131*11.33,
                     bets=[('{}_TeamA_TeamB'.format(today),'1')])
        db.saveBetForm(form)
        found=betForm.from_dict(db.convertStrtoDate(db.DBConnection.BetForms.find_one({"receiptID":'ID'},projection={'_id': False})) )
        self.assertEqual(form,found)
    def test_findBetForm(self):
        from Server.BetsFinancial.BetForm import BetForm
        db.DBConnection.BetForms.remove({})
        db.DBConnection.Matches.remove({})
        match = Match(matchID='{}_TeamA_TeamB'.format(today), date=today, league='league',
                      home_team='TeamA', away_team='TeamB', result=Result.Home)
        form = BetForm(receiptID='ID',date=today,bet_value=10.3131, bet_odd=11.33,
                       bets_list=[(match, Result.Home)])
        db.saveMatch(match.toDTO())
        db.saveBetForm(form.toDTO())
        found=db.findBetForm(receiptID='ID')
        self.assertEqual(form,found)
    def test_updateFundStatus(self):
        db.updateFundStatus(18)
        #list=db.DBConnection.FundStatus.find().sort([('time',-1)]).limit(1)
        record=db.getLastFundStatus()
        self.assertEqual(record,18)

if __name__ == '__main__':
    unittest.main()
