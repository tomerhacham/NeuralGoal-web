const makeEmpty = function () {return {}}
const makeLeague = function (league) {return {league:league}}
const makeStrMsg = function (msg) {return {msg:msg} }
const makeDeposit = function (name, amount) {return {name:name,amount:amount}}
const makeAmount = function (amount) {return {amount:amount}}
const makeMatch = function (league,date,home_team,away_team,matchID="",result=0){
    return {
        league:league,
        date:date,
        home_team:home_team,
        away_team:away_team,
        result:result,
        matchID:matchID
    }
}
const makeSingleBet = function (receiptID,bet_value,bet_odd,matchID,result){
    return {
        receiptID:receiptID,
        bet_value:bet_value,
        bet_odd:bet_odd,
        matchID:matchID,
        result:result
    }
}
const makeDoubleBet = function (receiptID,bet_value,bet_odd,match1_ID,result_1,match2_ID,result_2){
    return {
        receiptID:receiptID,
        bet_value:bet_value,
        bet_odd:bet_odd,
        match1_ID:match1_ID,
        result_1:result_1,
        match2_ID:match2_ID,
        result_2:result_2
    }
}


module.exports = {makeStrMsg,makeLeague,makeEmpty,makeDeposit,makeAmount,makeMatch,makeSingleBet,makeDoubleBet}