/**
 * @fileoverview gRPC-Web generated client stub for match
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.match = require('./match_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.match.MatchSenderClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.match.MatchSenderPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.League,
 *   !proto.match.MatchList>}
 */
const methodDescriptor_MatchSender_getMatchInLastSeasons = new grpc.web.MethodDescriptor(
  '/match.MatchSender/getMatchInLastSeasons',
  grpc.web.MethodType.UNARY,
  proto.match.League,
  proto.match.MatchList,
  /**
   * @param {!proto.match.League} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.MatchList.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.League,
 *   !proto.match.MatchList>}
 */
const methodInfo_MatchSender_getMatchInLastSeasons = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.MatchList,
  /**
   * @param {!proto.match.League} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.MatchList.deserializeBinary
);


/**
 * @param {!proto.match.League} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.MatchList)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.MatchList>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.getMatchInLastSeasons =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/getMatchInLastSeasons',
      request,
      metadata || {},
      methodDescriptor_MatchSender_getMatchInLastSeasons,
      callback);
};


/**
 * @param {!proto.match.League} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.MatchList>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.getMatchInLastSeasons =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/getMatchInLastSeasons',
      request,
      metadata || {},
      methodDescriptor_MatchSender_getMatchInLastSeasons);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.League,
 *   !proto.match.MatchList>}
 */
const methodDescriptor_MatchSender_getUpcomingGames = new grpc.web.MethodDescriptor(
  '/match.MatchSender/getUpcomingGames',
  grpc.web.MethodType.UNARY,
  proto.match.League,
  proto.match.MatchList,
  /**
   * @param {!proto.match.League} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.MatchList.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.League,
 *   !proto.match.MatchList>}
 */
const methodInfo_MatchSender_getUpcomingGames = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.MatchList,
  /**
   * @param {!proto.match.League} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.MatchList.deserializeBinary
);


/**
 * @param {!proto.match.League} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.MatchList)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.MatchList>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.getUpcomingGames =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/getUpcomingGames',
      request,
      metadata || {},
      methodDescriptor_MatchSender_getUpcomingGames,
      callback);
};


/**
 * @param {!proto.match.League} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.MatchList>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.getUpcomingGames =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/getUpcomingGames',
      request,
      metadata || {},
      methodDescriptor_MatchSender_getUpcomingGames);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.Empty,
 *   !proto.match.PredictionList>}
 */
const methodDescriptor_MatchSender_predict = new grpc.web.MethodDescriptor(
  '/match.MatchSender/predict',
  grpc.web.MethodType.UNARY,
  proto.match.Empty,
  proto.match.PredictionList,
  /**
   * @param {!proto.match.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.PredictionList.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.Empty,
 *   !proto.match.PredictionList>}
 */
const methodInfo_MatchSender_predict = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.PredictionList,
  /**
   * @param {!proto.match.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.PredictionList.deserializeBinary
);


/**
 * @param {!proto.match.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.PredictionList)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.PredictionList>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.predict =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/predict',
      request,
      metadata || {},
      methodDescriptor_MatchSender_predict,
      callback);
};


/**
 * @param {!proto.match.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.PredictionList>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.predict =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/predict',
      request,
      metadata || {},
      methodDescriptor_MatchSender_predict);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.Empty,
 *   !proto.match.strMsg>}
 */
const methodDescriptor_MatchSender_clearDB = new grpc.web.MethodDescriptor(
  '/match.MatchSender/clearDB',
  grpc.web.MethodType.UNARY,
  proto.match.Empty,
  proto.match.strMsg,
  /**
   * @param {!proto.match.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.Empty,
 *   !proto.match.strMsg>}
 */
const methodInfo_MatchSender_clearDB = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.strMsg,
  /**
   * @param {!proto.match.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @param {!proto.match.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.strMsg)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.strMsg>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.clearDB =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/clearDB',
      request,
      metadata || {},
      methodDescriptor_MatchSender_clearDB,
      callback);
};


/**
 * @param {!proto.match.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.strMsg>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.clearDB =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/clearDB',
      request,
      metadata || {},
      methodDescriptor_MatchSender_clearDB);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.Empty,
 *   !proto.match.strMsg>}
 */
const methodDescriptor_MatchSender_updateDB = new grpc.web.MethodDescriptor(
  '/match.MatchSender/updateDB',
  grpc.web.MethodType.UNARY,
  proto.match.Empty,
  proto.match.strMsg,
  /**
   * @param {!proto.match.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.Empty,
 *   !proto.match.strMsg>}
 */
const methodInfo_MatchSender_updateDB = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.strMsg,
  /**
   * @param {!proto.match.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @param {!proto.match.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.strMsg)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.strMsg>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.updateDB =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/updateDB',
      request,
      metadata || {},
      methodDescriptor_MatchSender_updateDB,
      callback);
};


/**
 * @param {!proto.match.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.strMsg>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.updateDB =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/updateDB',
      request,
      metadata || {},
      methodDescriptor_MatchSender_updateDB);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.Match,
 *   !proto.match.Match>}
 */
const methodDescriptor_MatchSender_addMatch = new grpc.web.MethodDescriptor(
  '/match.MatchSender/addMatch',
  grpc.web.MethodType.UNARY,
  proto.match.Match,
  proto.match.Match,
  /**
   * @param {!proto.match.Match} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.Match.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.Match,
 *   !proto.match.Match>}
 */
const methodInfo_MatchSender_addMatch = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.Match,
  /**
   * @param {!proto.match.Match} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.Match.deserializeBinary
);


/**
 * @param {!proto.match.Match} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.Match)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.Match>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.addMatch =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/addMatch',
      request,
      metadata || {},
      methodDescriptor_MatchSender_addMatch,
      callback);
};


/**
 * @param {!proto.match.Match} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.Match>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.addMatch =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/addMatch',
      request,
      metadata || {},
      methodDescriptor_MatchSender_addMatch);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.SingleBet,
 *   !proto.match.strMsg>}
 */
const methodDescriptor_MatchSender_setSingleBet = new grpc.web.MethodDescriptor(
  '/match.MatchSender/setSingleBet',
  grpc.web.MethodType.UNARY,
  proto.match.SingleBet,
  proto.match.strMsg,
  /**
   * @param {!proto.match.SingleBet} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.SingleBet,
 *   !proto.match.strMsg>}
 */
const methodInfo_MatchSender_setSingleBet = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.strMsg,
  /**
   * @param {!proto.match.SingleBet} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @param {!proto.match.SingleBet} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.strMsg)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.strMsg>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.setSingleBet =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/setSingleBet',
      request,
      metadata || {},
      methodDescriptor_MatchSender_setSingleBet,
      callback);
};


/**
 * @param {!proto.match.SingleBet} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.strMsg>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.setSingleBet =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/setSingleBet',
      request,
      metadata || {},
      methodDescriptor_MatchSender_setSingleBet);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.DoubleBet,
 *   !proto.match.strMsg>}
 */
const methodDescriptor_MatchSender_setDoubleBet = new grpc.web.MethodDescriptor(
  '/match.MatchSender/setDoubleBet',
  grpc.web.MethodType.UNARY,
  proto.match.DoubleBet,
  proto.match.strMsg,
  /**
   * @param {!proto.match.DoubleBet} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.DoubleBet,
 *   !proto.match.strMsg>}
 */
const methodInfo_MatchSender_setDoubleBet = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.strMsg,
  /**
   * @param {!proto.match.DoubleBet} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @param {!proto.match.DoubleBet} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.strMsg)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.strMsg>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.setDoubleBet =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/setDoubleBet',
      request,
      metadata || {},
      methodDescriptor_MatchSender_setDoubleBet,
      callback);
};


/**
 * @param {!proto.match.DoubleBet} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.strMsg>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.setDoubleBet =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/setDoubleBet',
      request,
      metadata || {},
      methodDescriptor_MatchSender_setDoubleBet);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.Deposit,
 *   !proto.match.strMsg>}
 */
const methodDescriptor_MatchSender_depositFunds = new grpc.web.MethodDescriptor(
  '/match.MatchSender/depositFunds',
  grpc.web.MethodType.UNARY,
  proto.match.Deposit,
  proto.match.strMsg,
  /**
   * @param {!proto.match.Deposit} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.Deposit,
 *   !proto.match.strMsg>}
 */
const methodInfo_MatchSender_depositFunds = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.strMsg,
  /**
   * @param {!proto.match.Deposit} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @param {!proto.match.Deposit} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.strMsg)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.strMsg>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.depositFunds =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/depositFunds',
      request,
      metadata || {},
      methodDescriptor_MatchSender_depositFunds,
      callback);
};


/**
 * @param {!proto.match.Deposit} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.strMsg>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.depositFunds =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/depositFunds',
      request,
      metadata || {},
      methodDescriptor_MatchSender_depositFunds);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.match.amount,
 *   !proto.match.strMsg>}
 */
const methodDescriptor_MatchSender_withdraw = new grpc.web.MethodDescriptor(
  '/match.MatchSender/withdraw',
  grpc.web.MethodType.UNARY,
  proto.match.amount,
  proto.match.strMsg,
  /**
   * @param {!proto.match.amount} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.match.amount,
 *   !proto.match.strMsg>}
 */
const methodInfo_MatchSender_withdraw = new grpc.web.AbstractClientBase.MethodInfo(
  proto.match.strMsg,
  /**
   * @param {!proto.match.amount} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.match.strMsg.deserializeBinary
);


/**
 * @param {!proto.match.amount} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.match.strMsg)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.match.strMsg>|undefined}
 *     The XHR Node Readable Stream
 */
proto.match.MatchSenderClient.prototype.withdraw =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/match.MatchSender/withdraw',
      request,
      metadata || {},
      methodDescriptor_MatchSender_withdraw,
      callback);
};


/**
 * @param {!proto.match.amount} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.match.strMsg>}
 *     Promise that resolves to the response
 */
proto.match.MatchSenderPromiseClient.prototype.withdraw =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/match.MatchSender/withdraw',
      request,
      metadata || {},
      methodDescriptor_MatchSender_withdraw);
};


module.exports = proto.match;

