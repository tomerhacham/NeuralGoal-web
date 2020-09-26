const path = require('path')
const {makeStrMsg,makeLeague,makeEmpty,makeDeposit,makeAmount,makeMatch,makeSingleBet,makeDoubleBet} = require('./MessageTypes')
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

client.getMatchInLastSeasons(makeLeague('all'), function(error, response) {
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.getUpcomingGames(makeLeague('all'), function(error, response) {
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})

client.clearDB(makeEmpty(),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.updateDB(makeEmpty(),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.addMatch(makeMatch('Without result and matchID','22/12/2020','Home_name','Away_name'),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.addMatch(makeMatch('With result and matchID','22/12/2020','Home_name','Away_name','ID',3),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.setSingleBet(makeSingleBet('receiptID',12.33,1.43,'matchID',1),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.setDoubleBet(makeDoubleBet('receiptID',12.33,1.43,'match1_ID',1,'match2_ID',2),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.depositFunds(makeDeposit('Tomer',123.43),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.withdraw(makeAmount(100),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})