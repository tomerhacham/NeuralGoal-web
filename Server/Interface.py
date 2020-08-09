import logging,grpc
import Server.protocol as protocol
from datetime import date
from concurrent import futures
from Server.protocs import match_pb2_grpc, match_pb2
from Server.Persistent import DBController
from Server.NeuralNetwork import NeuralNetworkController

class MatchSender(match_pb2_grpc.MatchSenderServicer):
    def getMatchInLastSeasons(self, request, context):
        matchlist = match_pb2.MatchList()
        for game in repo.main_table.select_by_league_name_last_seasons(league=request.league,as_dataframe=False):
            match = matchlist.list.add()
            match.league=game.league
            match.date=game.date.toisoformat()
            match.round=game.round
            match.home_team_name=game.home_team_name
            match.away_team_name=game.away_team_name
            match.home_team_rank=game.home_team_rank
            match.away_team_rank=game.away_team_rank
            match.home_team_scored=game.home_team_scored
            match.away_team_scored=game.away_team_scored
            match.home_team_received=game.home_team_received
            match.away_team_received=game.away_team_received
            match.home_att=game.home_att
            match.away_att=game.away_att
            match.home_def=game.home_def
            match.away_def=game.away_def
            match.home_mid=game.home_mid
            match.away_mid=game.away_mid
            match.home_odds_n=game.home_odds_n
            match.draw_odds_n=game.draw_odds_n
            match.away_odds_n=game.away_odds_n
            match.result=game.result
            match.home_odds_nn=game.home_odds_nn
            match.draw_odds_nn=game.draw_odds_nn
            match.away_odds_nn=game.away_odds_nn
        return matchlist

    def getUpcomingGames(self, request, context):
        matchlist=match_pb2.MatchList()
        upcoming=DBController.getUpcomingGames(league=request.league)
        for game in upcoming :
            match = matchlist.list.add()
            match.league = game.league
            match.date = game.date
            match.round = game.round
            match.home_team_name = game.home_team_name
            match.away_team_name = game.away_team_name
            match.home_team_rank = game.home_team_rank
            match.away_team_rank = game.away_team_rank
            match.home_team_scored = game.home_team_scored
            match.away_team_scored = game.away_team_scored
            match.home_team_received = game.home_team_received
            match.away_team_received = game.away_team_received
            match.home_att = game.home_att
            match.away_att = game.away_att
            match.home_def = game.home_def
            match.away_def = game.away_def
            match.home_mid = game.home_mid
            match.away_mid = game.away_mid
            match.home_odds_n = game.home_odds_n
            match.draw_odds_n = game.draw_odds_n
            match.away_odds_n = game.away_odds_n
            match.result = game.result
            match.home_odds_nn = game.home_odds_nn
            match.draw_odds_nn = game.draw_odds_nn
            match.away_odds_nn = game.away_odds_nn
        return  matchlist

    def setOddsforUpcominGames(self, request, context):
        matchlist = match_pb2.MatchList()
        for game in request.list:
            DBController.updateUpcomingGameOdds(protocol.responseToMatchDTO(game))
        for game in DBController.getUpcomingGames(league='all'):
            match = matchlist.list.add()
            match.league = game.league
            match.date = date.fromisoformat(game.date)
            match.round = game.round
            match.home_team_name = game.home_team_name
            match.away_team_name = game.away_team_name
            match.home_team_rank = game.home_team_rank
            match.away_team_rank = game.away_team_rank
            match.home_team_scored = game.home_team_scored
            match.away_team_scored = game.away_team_scored
            match.home_team_received = game.home_team_received
            match.away_team_received = game.away_team_received
            match.home_att = game.home_att
            match.away_att = game.away_att
            match.home_def = game.home_def
            match.away_def = game.away_def
            match.home_mid = game.home_mid
            match.away_mid = game.away_mid
            match.home_odds_n = game.home_odds_n
            match.draw_odds_n = game.draw_odds_n
            match.away_odds_n = game.away_odds_n
            match.result = game.result
            match.home_odds_nn = game.home_odds_nn
            match.draw_odds_nn = game.draw_odds_nn
            match.away_odds_nn = game.away_odds_nn
        return matchlist

    def predict(self, request, context):
        print("Prediction in process")
        predictions=match_pb2.PredictionList()
        for dto in NeuralNetworkController.predict(league='all'):
            _prediction=predictions.list.add()
            _prediction.leauge=dto.league
            _prediction.date=dto.date.isoformat()
            _prediction.home_team_name=dto.home_team_name
            _prediction.away_team_name=dto.away_team_name
            _prediction.home_odds_nn=dto.home_odds_nn
            _prediction.draw_odds_nn=dto.draw_odds_nn
            _prediction.away_odds_nn=dto.away_odds_nn
            _prediction.pred_1=dto.pred_1
            _prediction.pred_2=dto.pred_2
            _prediction.pred_x=dto.pred_x
            _prediction.expected=dto.expected
            _prediction.reslt=dto.result
        return predictions

    def dbfunctions(self, request, context):
        if request.command==match_pb2.dbCommand.Command.CLEAR:
           print('clear Database')
           DBController.clearDB()
           msg=match_pb2.strMsg(msg='Database has been cleared')
        elif request.command==match_pb2.dbCommand.Command.UPDATE:
            print('update Database')
            DBController.updateDB()
            msg=match_pb2.strMsg(msg='Database has benn updated')
        return msg

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    match_pb2_grpc.add_MatchSenderServicer_to_server(MatchSender(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()