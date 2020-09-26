//#region  Communication-Related
import * as grpcWeb from 'grpc-web'
import {MatchSenderClient} from './match_grpc_web_pb'
import {Empty,League,MatchList,MatchData,} from './match_pb'
//const path = require('path')
/*const {makeStrMsg,makeLeague,makeEmpty,makeDeposit,makeAmount,makeMatch,makeSingleBet,makeDoubleBet} = require('./MessageTypes')
const PROTO_PATH = path.join(__dirname, 'match.proto')
var grpc = require('@grpc/grpc-js')
var protoLoader = require('@grpc/proto-loader')

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
})
// Load in our service definition
const matchProto = grpc.loadPackageDefinition(packageDefinition).match
const client = new matchProto.MatchSender('localhost:50051', grpc.credentials.createInsecure())
//#endregion
*/
const service = new MatchSenderClient('http://localhost:8080', null, null);

export const testfunc = function(){
  const league=new League()
  league.setLeague('all')
  service.getMatchInLastSeasons(league, function(error, response) {
    if (error) console.log(error)
    console.log(JSON.stringify(response))
  })
}



//#region Remote Procedure Call

export const getMatchInLastSeasons = function(league){
  service.getMatchInLastSeasons(league, function(error, response) {
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
/*
const getUpcomingGames = function(league){
  service.getUpcomingGames(makeLeague(league), function(error, response) {
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
const clearDB = function (){
  service.clearDB(makeEmpty(),function(error,response){
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
const updateDB = function (){
  service.updateDB(makeEmpty(),function(error,response){
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
const addMatch = function (league,date,home_team,away_team,matchID="",result=0){
  service.addMatch(makeMatch(league,date,home_team,away_team,matchID,result),function(error,response){
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
const setSingleBet = function (receiptID,bet_value,bet_odd,matchID,result){
  service.setSingleBet(makeSingleBet(receiptID,bet_value,bet_odd,matchID,result),function(error,response){
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
const setDoubleBet = function (receiptID,bet_value,bet_odd,match1_ID,result_1,match2_ID,result_2){
  service.setDoubleBet(makeDoubleBet(receiptID,bet_value,bet_odd,match1_ID,result_1,match2_ID,result_2),function(error,response){
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
const depositFunds = function (name, amount){
  service.depositFunds(makeDeposit(name, amount),function(error,response){
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
const withdraw = function (amount){
  service.withdraw(makeAmount(amount),function(error,response){
        if (error) console.log(error)
        console.log(JSON.stringify(response))
      })
}
*/
//#endregion
//module.exports = {getMatchInLastSeasons,getUpcomingGames,clearDB,updateDB,addMatch,setSingleBet,setDoubleBet,depositFunds,withdraw}