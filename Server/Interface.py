import logging,grpc
import protol
import Server.protocol as protocol
from datetime import date, datetime
from concurrent import futures
from dateutil.parser import parse
#from Server.protocs import match_pb2_grpc, match_pb2
from Server.Persistent.DTOs import match
from Server.Persistent import DBController
from Server.NeuralNetwork import NeuralNetworkController

match_pb2, match_pb2_grpc = protol.load('protocs/match.proto')


class MatchSender(match_pb2_grpc.MatchSenderServicer):
    def getMatchInLastSeasons(self, request, context):
        matchlist = match_pb2.MatchList()
        #for game in DBController.getAllData(league=request.league,as_dataframe=False):
        for game in DBController.getAllData(as_dataframe=False):
            game=match(**game)
            _match = matchlist.list.add()
            _match.league=game.league
            _match.date=game.date
            _match.round=game.round
            _match.home_team_name=game.home_team_name
            _match.away_team_name=game.away_team_name
            _match.home_team_rank=game.home_team_rank
            _match.away_team_rank=game.away_team_rank
            _match.home_team_scored=game.home_team_scored
            _match.away_team_scored=game.away_team_scored
            _match.home_team_received=game.home_team_received
            _match.away_team_received=game.away_team_received
            _match.home_att=game.home_att
            _match.away_att=game.away_att
            _match.home_def=game.home_def
            _match.away_def=game.away_def
            _match.home_mid=game.home_mid
            _match.away_mid=game.away_mid
            _match.home_odds_n=game.home_odds_n
            _match.draw_odds_n=game.draw_odds_n
            _match.away_odds_n=game.away_odds_n
            _match.result=game.result
            _match.home_odds_nn=game.home_odds_nn
            _match.draw_odds_nn=game.draw_odds_nn
            _match.away_odds_nn=game.away_odds_nn
            break
        return matchlist

    def getUpcomingGames(self, request, context):
        matchlist=match_pb2.MatchList()
        upcoming=DBController.getUpcomingGames(league=request.league)
        for game in upcoming :
            game = match(**game)
            _match = matchlist.list.add()
            _match.league = game.league
            _match.date = game.date
            _match.round = game.round
            _match.home_team_name = game.home_team_name
            _match.away_team_name = game.away_team_name
            _match.home_team_rank = game.home_team_rank
            _match.away_team_rank = game.away_team_rank
            _match.home_team_scored = game.home_team_scored
            _match.away_team_scored = game.away_team_scored
            _match.home_team_received = game.home_team_received
            _match.away_team_received = game.away_team_received
            _match.home_att = game.home_att
            _match.away_att = game.away_att
            _match.home_def = game.home_def
            _match.away_def = game.away_def
            _match.home_mid = game.home_mid
            _match.away_mid = game.away_mid
            _match.home_odds_n = game.home_odds_n
            _match.draw_odds_n = game.draw_odds_n
            _match.away_odds_n = game.away_odds_n
            _match.result = game.result
            _match.home_odds_nn = game.home_odds_nn
            _match.draw_odds_nn = game.draw_odds_nn
            _match.away_odds_nn = game.away_odds_nn
        return  matchlist

    def setOddsforUpcominGames(self, request, context):
        matchlist = match_pb2.MatchList()
        for game in request.list:
            DBController.updateUpcomingGameOdds(protocol.responseToMatchDTO(game))
        for game in DBController.getUpcomingGames(league='all'):
            game = match(**game)
            _match = matchlist.list.add()
            _match.league = game.league
            _match.date = date.fromisoformat(game.date)
            _match.date = parse(game.date)
            _match.round = game.round
            _match.home_team_name = game.home_team_name
            _match.away_team_name = game.away_team_name
            _match.home_team_rank = game.home_team_rank
            _match.away_team_rank = game.away_team_rank
            _match.home_team_scored = game.home_team_scored
            _match.away_team_scored = game.away_team_scored
            _match.home_team_received = game.home_team_received
            _match.away_team_received = game.away_team_received
            _match.home_att = game.home_att
            _match.away_att = game.away_att
            _match.home_def = game.home_def
            _match.away_def = game.away_def
            _match.home_mid = game.home_mid
            _match.away_mid = game.away_mid
            _match.home_odds_n = game.home_odds_n
            _match.draw_odds_n = game.draw_odds_n
            _match.away_odds_n = game.away_odds_n
            _match.result = game.result
            _match.home_odds_nn = game.home_odds_nn
            _match.draw_odds_nn = game.draw_odds_nn
            _match.away_odds_nn = game.away_odds_nn
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
           #DBController.clearDB()
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
    print("Server is Live")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()