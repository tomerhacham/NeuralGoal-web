//import { makeLeagueRequest,makeEmpty,makeStrMsg } from "./MessageTypes"

const path = require('path')
const {makeStrMsg,makeLeagueRequest,makeEmpty}= require('./MessageTypes')
const PROTO_PATH = path.join(__dirname, 'match.proto')
var grpc = require('grpc')
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

const leagueRequest = {
  league: 'all'
}

/*client.getMatchInLastSeasons(leagueRequest, function(error, response) {
  if (error) console.log(error)

  console.log('The Result Is: ' + JSON.stringify(response))
})

client.dbfunctions(dbUpdate, function(error, response) {
  if (error) console.log(error)

  console.log('The Result Is: ' + JSON.stringify(response))
})*/

client.clearDB(makeEmpty(),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})
client.updateDB(makeEmpty(),function(error,response){
  if (error) console.log(error)
  console.log(JSON.stringify(response))
})