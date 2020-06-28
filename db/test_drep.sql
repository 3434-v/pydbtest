/*
 Navicat MongoDB Data Transfer

 Source Server         : test_drep
 Source Server Type    : MongoDB
 Source Server Version : 40011
 Source Host           : localhost:27017
 Source Schema         : test_drep

 Target Server Type    : MongoDB
 Target Server Version : 40011
 File Encoding         : 65001

 Date: 27/06/2020 22:28:26
*/


// ----------------------------
// Collection structure for Address_Msg
// ----------------------------
db.getCollection("Address_Msg").drop();
db.createCollection("Address_Msg");

// ----------------------------
// Documents of Address_Msg
// ----------------------------
db.getCollection("Address_Msg").insert([ {
    _id: ObjectId("5ee8929f707b8c0a270a1213"),
    Address: "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c",
    Money: "9654989189964405644125294223"
} ]);
db.getCollection("Address_Msg").insert([ {
    _id: ObjectId("5ee893422258f6455a378802"),
    Address: "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c",
    Money: "9654989189964405644125294223"
} ]);
db.getCollection("Address_Msg").insert([ {
    _id: ObjectId("5ee893540258788059c5190a"),
    Address: "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c",
    Money: "9654989189964405644125294223"
} ]);
db.getCollection("Address_Msg").insert([ {
    _id: ObjectId("5ee8935e5c2aee0b13fe8ce5"),
    Address: "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c",
    Money: "9654989189964377552125294123"
} ]);

// ----------------------------
// Collection structure for Create_Account
// ----------------------------
db.getCollection("Create_Account").drop();
db.createCollection("Create_Account");

// ----------------------------
// Documents of Create_Account
// ----------------------------
db.getCollection("Create_Account").insert([ {
    _id: ObjectId("5ee8ade9360a410bc6429028"),
    Account: "0x404d0ad3478c720c91f633e4fb5417b66805271f",
    "Create_Time": "2020-06-16 19:32:57"
} ]);
db.getCollection("Create_Account").insert([ {
    _id: ObjectId("5ee8aeba56082584cbe8f8f1"),
    Account: "0x263a4164575772088860ac9d3192067eaae489f9",
    "Create_Time": "2020-06-16 19:36:26"
} ]);

// ----------------------------
// Collection structure for DoMainName
// ----------------------------
db.getCollection("DoMainName").drop();
db.createCollection("DoMainName");

// ----------------------------
// Documents of DoMainName
// ----------------------------
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee88758b588a8d5217e571d"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee88806cfc5b8bbf5d0580c"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee8886d4f497c29d0fc9a8f"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee8888e91cc8afd37a9c33e"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee888b28d35551b48b9e3ef"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee8890d13c574c296e7d479"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee88934e48f4bd45d4b199f"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee889644de7ff7080386ab6"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee88991bf621b7479c6a068"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee889e85f01a120bfa65c3b"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee88dab4e540efdb40f2de1"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);
db.getCollection("DoMainName").insert([ {
    _id: ObjectId("5ee89092a1969d2716b8501b"),
    name: "测试环境",
    url: "http://39.98.39.224:35645"
} ]);

// ----------------------------
// Collection structure for MoneyCount
// ----------------------------
db.getCollection("MoneyCount").drop();
db.createCollection("MoneyCount");

// ----------------------------
// Documents of MoneyCount
// ----------------------------
db.getCollection("MoneyCount").insert([ {
    _id: ObjectId("5ef5eca45cf548112b8849fe"),
    address: "0x01E8D0e1916afBF6d501b3aADa10C53eA19F8A39",
    money: "0"
} ]);
db.getCollection("MoneyCount").insert([ {
    _id: ObjectId("5ef5eca45cf548112b8849ff"),
    address: "0x01f24C6415BbcE8C426185DabE0E3995583d1372",
    money: "1000000802931848000000000"
} ]);

// ----------------------------
// Collection structure for TestCase
// ----------------------------
db.getCollection("TestCase").drop();
db.createCollection("TestCase");

// ----------------------------
// Documents of TestCase
// ----------------------------
db.getCollection("TestCase").insert([ {
    _id: ObjectId("5ee8a2dc4440e5fc45fbd0fb"),
    TestID: NumberInt("1"),
    Launch: "0x96168C5A6C50D6d3fb240175F4aeaA6E52373281",
    Receive: "0x7C6015407AE0421e196593E238B135E159987F8e",
    money: NumberInt("1000"),
    gaslimt: NumberInt("18000000"),
    gasprice: NumberInt("40000000")
} ]);

// ----------------------------
// Collection structure for method
// ----------------------------
db.getCollection("method").drop();
db.createCollection("method");

// ----------------------------
// Documents of method
// ----------------------------
db.getCollection("method").insert([ {
    _id: ObjectId("5eeadfeb25d74d1746d37ffc"),
    name: "sendRawTransaction",
    method: "blockmgr_sendRawTransaction",
    describe: "发送已签名的交易"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae0a2117ce06beb20d984"),
    name: "gasPrice",
    method: "blockmgr_gasPrice",
    describe: "获取系统的给出的gasprice建议值"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae0b5006c9bae3600ebb9"),
    name: "GetPoolTransactions",
    method: "blockmgr_getPoolTransactions",
    describe: "取交易池中的交易信息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae0c4955242d20895b1be"),
    name: "GetTransactionCount",
    method: "blockmgr_getTransactionCount",
    describe: "获取地址发出的交易总数"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae0d48adbd552bb6a690f"),
    name: "GetTxInPool",
    method: "blockmgr_getTxInPool",
    describe: "查询交易是否在交易池，如果在，返回交易"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae673cf61000023006071"),
    name: "getblock",
    method: "chain_getBlock",
    describe: "区块明细信息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae699cf61000023006072"),
    name: "getMaxHeight",
    method: "chain_getMaxHeight",
    describe: "用于获取当前最高区块"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae6b3cf61000023006073"),
    name: "getBlockGasInfo",
    method: "getBlockGasInfo",
    describe: "获取gas相关信息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae6c7cf61000023006074"),
    describe: "查询地址余额",
    name: "getBalance",
    method: "chain_getBalance"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae6dbcf61000023006075"),
    name: "getNonce",
    describe: "查询地址在链上的nonce",
    method: "chain_getNonce"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae6ffcf61000023006076"),
    method: "chain_getReputation",
    name: "getNonce_s",
    describe: "查询地址的名誉值"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae714cf61000023006077"),
    name: "getTransactionByBlockHeightAndIndex",
    method: "chain_getTransactionByBlockHeightAndIndex",
    describe: "获取区块中特定序列的交易"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae714cf61000023006078"),
    name: "getTransactionByBlockHeightAndIndex",
    method: "chain_getTransactionByBlockHeightAndIndex",
    describe: "获取区块中特定序列的交易"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae728cf61000023006079"),
    name: "getAliasByAddress",
    method: "chain_getAliasByAddress",
    describe: "根据地址获取地址对应的别名"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae738cf6100002300607a"),
    name: "getAddressByAlias",
    method: "chain_getAddressByAlias",
    describe: "根据别名获取别名对应的地址"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae746cf6100002300607b"),
    name: "getReceipt",
    method: "chain_getReceipt",
    describe: "根据txhash获取receipt信息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae756cf6100002300607c"),
    name: "getLogs",
    describe: "根据txhash获取交易log信息",
    method: "chain_getLogs"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae766cf6100002300607d"),
    name: "getCancelCreditDetail",
    method: "chain_getCancelCreditDetail",
    describe: "根据txhash获取退质押或者退投票信息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae783cf6100002300607e"),
    name: "getByteCode",
    method: "chain_getByteCode",
    describe: "根据地址获取bytecode"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae792cf6100002300607f"),
    name: "getVoteCreditDetails",
    method: "chain_getCreditDetails",
    describe: "根据地址获取stake 所有细节信息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae7a5cf61000023006080"),
    name: "GetCancelCreditDetails",
    method: "chain_getCancelCreditDetails",
    describe: "获取所有退票请求的细节"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae7b6cf61000023006081"),
    name: "GetCandidateAddrs",
    method: "chain_getCandidateAddrs",
    describe: "获取所有候选节点地址和对应的信任值"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae7b6cf61000023006082"),
    name: "GetCandidateAddrs",
    method: "chain_getCandidateAddrs",
    describe: "获取所有候选节点地址和对应的信任值"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae7d6cf61000023006083"),
    name: "getInterestRate",
    method: "chain_getInterestRate",
    describe: "年华后三个月利息, 年华后六个月利息, 一年期利息, 一年以上期利息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae7e6cf61000023006084"),
    name: "getChangeCycle",
    method: "chain_getChangeCycle",
    describe: "获取出块节点换届周期"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae7f7cf61000023006085"),
    name: "getPeers",
    method: "p2p_getPeers",
    describe: "获取当前连接的节点"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae80bcf61000023006086"),
    name: "addPeer",
    method: "p2p_addPeer",
    describe: "添加节点"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae81acf61000023006087"),
    name: "removePeer",
    method: "p2p_removePeer",
    describe: "移除节点"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae837cf61000023006088"),
    name: "setLevel",
    method: "log_setLevel",
    describe: "设置日志级别"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae846cf61000023006089"),
    name: "setVmodule",
    method: "log_setVmodule",
    describe: "分模块设置级别"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae856cf6100002300608a"),
    name: "getRawTransaction",
    method: "trace_getRawTransaction",
    describe: "根据交易hash查询交易字节"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae86bcf6100002300608b"),
    name: "getTransaction",
    method: "trace_getTransaction",
    describe: "根据交易hash查询交易详细信息"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae87ccf6100002300608c"),
    name: "decodeTrasnaction",
    method: "trace_decodeTrasnaction",
    describe: "把交易字节信息反解析成交易详情"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae88dcf6100002300608d"),
    name: "getSendTransactionByAddr",
    method: "trace_getSendTransactionByAddr",
    describe: "根据地址查询该地址发出的交易，支持分页"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeae8b3cf6100002300608e"),
    name: "getReceiveTransactionByAd",
    method: "trace_getReceiveTransactionByAddr",
    describe: "根据地址查询该地址接受的交易，支持分页"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf00acf6100002300608f"),
    name: "rebuild",
    method: "trace_rebuild",
    describe: "重建trace中的区块记录"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf028cf61000023006090"),
    name: "listAddress",
    method: "account_listAddress",
    describe: "列出所有本地地址"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf037cf61000023006091"),
    name: "createAccount",
    method: "account_createAccount",
    describe: "创建本地账号"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf063cf61000023006092"),
    name: "createWallet",
    describe: "创建本地钱包",
    method: "account_createWallet"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf079cf61000023006093"),
    name: "lockAccount",
    describe: "锁定账号",
    method: "account_lockAccount"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf088cf61000023006094"),
    name: "account_unlockAccount",
    method: "account_unlockAccount",
    describe: "解锁账号"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf099cf61000023006095"),
    name: "openWallet",
    method: "account_openWallet",
    describe: "打开钱包"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf0a9cf61000023006096"),
    name: "closeWallet",
    method: "account_closeWallet",
    describe: "关闭钱包"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf0b6cf61000023006097"),
    name: "transfer",
    method: "account_transfer",
    describe: "转账"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf0cfcf61000023006098"),
    name: "transferWithNonce",
    method: "account_transferWithNonce",
    describe: "转账"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf0dfcf61000023006099"),
    name: "setAlias",
    method: "account_setAlias",
    describe: "设置别名"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf0eccf6100002300609a"),
    name: "VoteCredit",
    method: "account_voteCredit",
    describe: "投票"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf0ffcf6100002300609b"),
    name: "CancelVoteCredit",
    method: "account_cancelVoteCredit",
    describe: "取消投票"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf10dcf6100002300609c"),
    name: "CandidateCredit",
    method: "account_candidateCredit",
    describe: "候选节点质押"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf11bcf6100002300609d"),
    name: "CancelCandidateCredit",
    method: "account_cancelCandidateCredit",
    describe: "取消候选"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf12bcf6100002300609e"),
    name: "readContract",
    method: "account_readContract",
    describe: "读取智能合约（无数据被修改）"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf138cf6100002300609f"),
    name: "estimateGas",
    method: "account_estimateGas",
    describe: "估算交易需要多少gas"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf148cf610000230060a0"),
    name: "executeContract",
    method: "account_executeContract",
    describe: "执行智能合约（导致数据被修改）"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf156cf610000230060a1"),
    name: "createCode",
    method: "account_createCode",
    describe: "部署合约"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf169cf610000230060a2"),
    name: "dumpPrivkey",
    method: "account_dumpPrivkey",
    describe: "导出地址对应的私钥"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf176cf610000230060a3"),
    name: "DumpPubkey",
    method: "account_dumpPubkey",
    describe: "导出地址对应的公钥"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf1c0cf610000230060a4"),
    name: "sign",
    method: "account_sign",
    describe: "关闭钱包"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf1d5cf610000230060a5"),
    name: "generateAddresses",
    method: "account_generateAddresses",
    describe: "生成其他链的地址"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf1f1cf610000230060a6"),
    name: "importKeyStore",
    method: "account_importKeyStore",
    describe: "导入keystore"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf1fbcf610000230060a7"),
    name: "importPrivkey",
    method: "account_importPrivkey",
    describe: "导入私钥"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf205cf610000230060a8"),
    name: "changeWaitTime",
    describe: "修改leader等待时间 (ms)",
    method: "consensus_changeWaitTime"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeaf21ccf610000230060a9"),
    name: "getMiners",
    method: "consensus_getMiners",
    describe: "获取当前出块节点"
} ]);
db.getCollection("method").insert([ {
    _id: ObjectId("5eeb210dcf610000230060aa"),
    method: "p2p_localNode",
    name: "localNode",
    describe: "需要获取本地的enode，用于P2p链接"
} ]);

// ----------------------------
// Collection structure for result_msg
// ----------------------------
db.getCollection("result_msg").drop();
db.createCollection("result_msg");

// ----------------------------
// Documents of result_msg
// ----------------------------
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eec9c6e23c554a287e8e3ef"),
    method: "account_listAddress",
    result: [
        "0x01E8D0e1916afBF6d501b3aADa10C53eA19F8A39",
        "0x01f24C6415BbcE8C426185DabE0E3995583d1372",
        "0x023A9E863c228aED391532808599BF005a2a62e5",
        "0x02cdA3979630A73A4e0100CE2B67669b50cd6293",
        "0x02e07c38aB87de40DefF4D4123aD027cefB2F840",
        "0x06B4Ae76f3443Db9161A273B196282CF4B5346d4",
        "0x07332150A19Bc85E0416b19F2F6ee255BA34126B",
        "0x087FF7EaD4ba5c7Ba488AfF8717Ea89DCb36D55c",
        "0x0893B1390d740eAEeB3120CEF1D4672221D4D3eA",
        "0x102383B782Ad1efc1FD0FD1d640155AB4c7C2a04",
        "0x1049779b630eEa9526dD392707FCa953B2Db4420",
        "0x1242b0Db7420a3ED8452C383aB7A31A25ac83042",
        "0x14aF424238BD4eA60C356c967D5709AB3f8224ed",
        "0x15A4D9ED30f8978aFFbF430C0E243ab48AeCE2C9",
        "0x15fd240a553ac596d6C65F4d128D12A28D04D7Be",
        "0x16838CC5B6d97b43874421DcC123Ba31f13e9725",
        "0x17c73cef41e22AC8aDDa071F4f66F0FCD976c129",
        "0x18d953d11f670179eeE9f0309E77977518bb1E9F",
        "0x1A0E45Ac31EdF54C3Ea212461d5301247CDfFa29",
        "0x1A61B43d6e53954735dd300D5090599A17F8E4db",
        "0x1B9827399687A3D89674Ee9f1e10837C0f914FfA",
        "0x1Edaa4b87589DB29B80Fc7b3CA85a24c9050a968",
        "0x1F38aA88949e858E0fd611ea272EA596555363c1",
        "0x1a660A30e7f578F28f28D6f1D6Ade0843757895F",
        "0x1acb44FFf91aC20A40A701d2ED9092F2Dc6eF10c",
        "0x1bC97cA5E63e25843b9ED636C10f0B38EE16fF1F",
        "0x20170A0d5209Cb757293f85c08Bb77d20AaF5BAF",
        "0x22Ced64f390877BeC54a82f957a66F62dE4b80Bd",
        "0x25D0BB9e32B94dDE17Ba121af24b44640BC025Ee",
        "0x263A4164575772088860AC9d3192067eAae489F9",
        "0x26cA62B95095F01AecBfE3A79e62d6795A0a9894",
        "0x281Df2b3Fb8F14140d8861577AB61CE2B46ea3C2",
        "0x2905C198de4ac07E10749Beb33464747Ea5E1270",
        "0x2B5bB7206E449056C5eFB6ad8473e0aCD57B0A2F",
        "0x2EeDcffad0854129883CA8c0b9a58B96f6e669e5",
        "0x2a25c6DD0aa2924e447459b6dD1B2c848681170e",
        "0x2e59B11dd0221EC8776662a35AA9F5c3B79B946C",
        "0x3127bCbDE2b0cc1c963E44A9c29A2883A33a301E",
        "0x3155D2CA715772EE687dCcb87345F75B86b7b3c7",
        "0x3191037dE5D604cdE2588f281090313B204AF841",
        "0x3202172fA3B58d78e2963F28fdd2367d4F3AbF83",
        "0x3275AD121a4bA9d38c963783e9A3FB11aC1ee6D1",
        "0x32b7382424187c8727e040cce0D87b51d0Ddb342",
        "0x35A49641E78500C79ae60FE02a153e49cF899971",
        "0x35D36D63bc7E7209e5869b1a8a8bf960e6C11848",
        "0x36AF1B1eAFc62f2495906D51B97c8abc58932CA2",
        "0x3726430e6E3448753F29E1d3ca24120850433Ff9",
        "0x375135B2aC2968c08c04f4eBe9EAA5E105bdDF49",
        "0x37623744D58645fa763c08e10c9cd9aa9aA92e32",
        "0x37F436D39093c312A6145f17cCE7fa04A9570620",
        "0x3851E1cEcbEb1Dc593B98ba1812EbB34918b3576",
        "0x3C55C788dB9999Cb8C57D00774D8E37014C5c5D9",
        "0x3Fe98a15ec576F8aA7F8E18352B9Fa05dba3A77a",
        "0x3ab375b4aD8d4A770b8662072cAe26c92Ccdb82C",
        "0x3c03D972b70ed891335B63CeF8CEeEf399e128A5",
        "0x3cd4fcdC85d9BFC4Cba1553328e1D7EF811F854e",
        "0x3f1a9B2F29399F88176DB37f2b959f4B9118055f",
        "0x404d0ad3478C720c91f633e4Fb5417B66805271f",
        "0x4248bea40F4FB0a9105B04E7fC1bf89FE24B4B16",
        "0x42971A0568095A4A38D9c4272d371959cEB2bdBE",
        "0x43c5b1F454DdE5Da4b564570F6740fB6349678f7",
        "0x446AaC9e444613b172A4968cc431A984b69f320F",
        "0x44DDf1Bf5f325e4Db0199B22D39A3286c29b4082",
        "0x474Da9675DE3f918bDBdb6f0d7D285064eF34A0c",
        "0x48c7f77bE6c65010A049826C110cDE5F7F3d3354",
        "0x49CC483b1123FF3063b2E90F5C2554bB7C77d5c4",
        "0x49de216D11E162F9bF1EaDb8f5E14c3d1923Bf27",
        "0x4BE1fdF8c04cDbDAd383334Ce4c3442da1A75b80",
        "0x4CB9D49f4E92B8452d47F5fF51439ed617fA8137",
        "0x4D147033F46cc58e2b44666Ce3317c084987391f",
        "0x4d8A55ac670D8d3FbFE9FC1D4EF6Afc0B68105c6",
        "0x4ecEecf468d2F4d985537d530FaD938b9583810A",
        "0x4f52EA3f7C761Cb6b13f1993fda45BF6b075D186",
        "0x4f831f2BAb486E73f7D3Cc70db7D1541767094cf",
        "0x517F99b57EDa71fD52Cf43133C040972D20F7f2D",
        "0x53e55A002BD6303d795aa6B26c96F51A564d94D9",
        "0x563D06F970Ad1B3A461f6Bdb87e5284b9528Bd9c",
        "0x563FA7b3048501b98848B3Ce2947EB0E549581C2",
        "0x57023162350C8823C5036852AFb4879281C748d5",
        "0x5730316f38AEf532c2917af1d9E4E18853899F66",
        "0x573F9D85D6feB1C87910D733d9C372d4640e5E7b",
        "0x577aFf8B6773a6CaFd6AAdBB0b0b3E9665fC42f6",
        "0x5840d06119F85FE6F6685bEF185021cc12549938",
        "0x595bACe179e4174B26d533dAb223DFc1FD27850D",
        "0x596E880E7962c177d18F7dB62c70882b041a85b4",
        "0x5B732b5b8199aF48c8b78B98d5B2A0BE483f3E14",
        "0x5Bc1782F0f59de815B70a534fE2aE5792B4da186",
        "0x5CfA74d261514774C647B671fb36F7aB3C4f4F1C",
        "0x5Da6Ab9EF7dd5a5B3472d855885aF0C4A7656a89",
        "0x5dE780B8412fC2977e158Ac60cC6d9bfce7A1e9F",
        "0x5e85aAeb9a4974EB24b4660b94451AB491361f1A",
        "0x6387A71Be221d40BF897A5556cC369Eff653fa53",
        "0x63eB85Aea74eB9bda284F6f157c5F795B6922eDc",
        "0x6511F783077F1C2fC1BbB0a83aA75D248258e528",
        "0x6666F5cc2A938fd197F93254B41C5d5EE864C196",
        "0x679F91a3c73943B69Af5ceC1a4F93eC7D348B025",
        "0x67AB89DcFB051bDcF15d8b665f568cb118EeAB2D",
        "0x695686cfC39D9F06794dA2BC68e6abEEd9E955e6",
        "0x6B69859bF4A9e0be97446687Ba650D5120e75De1",
        "0x6C09Dc42420B79b1222BD62d964E9E2DcCC558EA",
        "0x6DDf4bD80C274711d8022E9251323377BA09a2D9",
        "0x6b2eB86AdE050D58899705582d5234BCCDD28A37",
        "0x6b9b62f5B0e0f24b9f9dff6aa33F6B17855A7e53",
        "0x712F7df84303D953870540B43c21bcFfd2dae12c",
        "0x72fbaD34459b1d0F9984DD295261887C661Ee841",
        "0x7409BE9D7cCE96B2660a0C6fA5c0dfba027A9EA6",
        "0x742D10bFB8fF0181c50815ef6035A0D6F8b50eE9",
        "0x76add6DAd1e3C86EbE45AF36582CD73582838d07",
        "0x77eeB46c48Af4f97D65fFf93A0e31323C4d3C0b4",
        "0x7Bb9378acEDe5Db60AC4C20e124A4E9FBf7e92EF",
        "0x7C6015407AE0421e196593E238B135E159987F8e",
        "0x7D6Df208FaA51f942Fa32070290C62A4C1097dde",
        "0x7a9EEc03141A2937BaA0d385f7e68867A5E3E499",
        "0x7b69E7b3c9a955ddB869a81B2075bD0aB1C77c1E",
        "0x7d1d99B761457d8905c16e2Bd6022282D53135fD",
        "0x7e2E012477a5b55f9f7dE318794d2ee6FAF1A0Fb",
        "0x7ffe19669365991EF5275794618090d29664A359",
        "0x80F90500D6E080B37A4C500b64Eb412bD0E1AbFa",
        "0x80b9CAb400732A98545420cd26c2C4F44B086420",
        "0x815F9E8b3241937c5eD2476C7BCea030152E6383",
        "0x8235573D8Aa121e4BAE297f2D375a23E705553Ba",
        "0x82D178cEBa3cA47c590e48e1C80DCffCd85309Fc",
        "0x85D7F211CB0A18FF2558908bcDBF41098bfc8A99",
        "0x86C526c46e751A02Ec3653c8AA07A64E901972fa",
        "0x86aE857bf0193630C40853B15cEF08d26ACE97ba",
        "0x86c3e25DDbc831f7d781fA932e617fA9EA618E69",
        "0x87b68353fC1335e61aE4b7dca911A7aD558a1f11",
        "0x8D64991e4DCa06f7D10FA88E6F14b39B06C5CFDf",
        "0x8F5C10ee9C6a543bEb7e6b5464cA5F196d678C33",
        "0x8ccdB4165E125ec4617535Eef52E710742A47af9",
        "0x8e427731Bf6467aD4631678dEEc7776843F81d05",
        "0x8eB04B06Ff6f9E24423e28Edf6691Fa266430BF3",
        "0x8eCA2B45002D56c8D10229c96652A5dea90302ec",
        "0x90033092c0797Db9528b6963Ab0A9d9f28679181",
        "0x9023d52C4EA6993d0EEf4b3C856C5c051A871E11",
        "0x91523927dE1471d317cDF94fD614A414d0AC0867",
        "0x91749bE41D456D3e29bB6B60415Fc7291cF5b8a1",
        "0x925FA80CFA4ddf5A06C9d13D7De290401F0517CC",
        "0x9337732F160a947D148C64bd5e922270EA552954",
        "0x94Ac62739CD764fdcC4E7d13cbEda37FbF8C103d",
        "0x9513bA41693ECdF030b64058480FA66f2485A99c",
        "0x96168C5A6C50D6d3fb240175F4aeaA6E52373281",
        "0x972E8cD2940b16262c735193952Ce4A6A7f2B25b",
        "0x98DBd76D2731B9B27172B08C864473BC10E2966D",
        "0x990ABaDb5D43e6d13bE7fb7f5E6798B6D9D74297",
        "0x9A29680E23e9AAfc615F0eff066617856C152938",
        "0x9DaE6e2F69B045ED9c0d922e2E110EB4955203F1",
        "0x9E51D0696A5BA9B871754110aa64E881B11cd69A",
        "0x9F39c34f6b2035868186b80d7818C7cD597D25D3",
        "0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4",
        "0x9bbaa7359eE892858F114Fe0e18E7Bf8A92286eB",
        "0x9d2769b6315D7E6f4b8Ae11E5f83640Cf15Bb41d",
        "0x9eA3754d1f9b968EFdC20528F0192EF25e59611C",
        "0x9eC73a447B6Dc1fc72736887cBd180E255eF09F3",
        "0xA1042a4f689c865B9EDC79d7775DaEC7dA12150e",
        "0xA279C2887a2BfAb6327cb8389d858c9333bd4b46",
        "0xA4B9Dc7D6a2188Dc9B6DA224a86a99cE5Ea6989A",
        "0xA5DCf9E8BBB5d3b3463FE860a4Ed1Cb3Feb7687D",
        "0xA882b9650BB89b82279cf36bB4553e3F93631553",
        "0xAef8b9D0093F15647Dc8b43a3CFa19334476D74b",
        "0xAf88Bd3f3a7316f532ac3cdE64e8B27Ea5e7fE19",
        "0xB01B2Dca9F9b40f4E2D31e1F00560b16223E4287",
        "0xB22A413Cc762222275D06db3FC56ac49C88D0eD7",
        "0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b",
        "0xB5b8E571024Ce2F1C8605eF72657E41d535b5948",
        "0xB7c5F20eED9d0834b97348142A616CE449510009",
        "0xC03386ECc08f5e5309434E9cAAf5D5FcFE31EBDd",
        "0xC26AE82545933a990d9744edA50de8ccd91De942",
        "0xC3fe1e33907f9B12d467FcBa6E4FC6877588065E",
        "0xC78a80B2f5bE10D78F9f4d888845953D2F9FF400",
        "0xC851CA92f6f75b0d6a30B767b12959fb3A4a3bfa",
        "0xC9312d7E2edd8680c9e99E15B37be21d913dAd25",
        "0xCA345D024BC00EEE65Bdfb802262f71b37Ca6415",
        "0xCb4A105793758477E6301C29e1ea3ead7f226CBA",
        "0xD1233d1d61F919D0d44661349728BcE594fcc3A1",
        "0xD3df1AFBF61433Af8902Ab91bDCe9D29Ec18c27d",
        "0xD6491c67b8A601B4E1a6aD0A1C42F1Db7f2f477f",
        "0xD7B3aF702A3eE290cE94F7Bae8E4E9b2E47aA7f2",
        "0xD8B15fe38EAf7d289885f46Ba3FE5a4039f10A23",
        "0xDA85131e40EA08C05628F7708E20E0068315f018",
        "0xDa11853BE3Ba58A5d64ACa9B6B17d8a9d16327B9",
        "0xE1e956A75c3f6F57Fe687f0b83e51EDF02A005Ba",
        "0xE5915990ae66A2aBE07DF7EA09C25A9C7405Ba83",
        "0xE65a46e7F5583a5436EFE0d3037380B60DF5b2BB",
        "0xE70aE3477f31689F54436bc739961a62Ed0A0AbB",
        "0xE73Fd0a5161EeC0585cEaDaa2C18040C4677a972",
        "0xEA7fE43EdBA518Bbb642909576DBE14E2C931e2C",
        "0xEB6ed766ca0Bf5459f082913202EF4eE0dd82319",
        "0xEBa7E6584a92CF1273D1D3A5fA6faf188173D08C",
        "0xEEF07631054C3cb61C86503b88EDf6474687374B",
        "0xEa65704Be03BC740ED295930942ab7f3d02Bc1Ad",
        "0xEbcE82BCCFcC2EdDE722D0F3A0fb2e82ACbddD1C",
        "0xEecA8879721045B27B05c592B5F82601f5aE87f0",
        "0xF235853C26fCb7C59f048C3d1C98016d0F49C50e",
        "0xF64174cea8FFacadc9371C5Bd838B50f91d85D03",
        "0xF66B24217798De4600A079C8b7BCFa8AcfdD5C80",
        "0xFD90B2086076BCa5219364d2601c1e8FAfAB92d2",
        "0xFF4FEf6F0Aad400e75f1E9c29800378A783BEAEB",
        "0xa0BacDd7d7AeaD49AF9A9b4307eE7DAd183d8D31",
        "0xa411260AeF74FB1D36f8a07310d42B356F9D5357",
        "0xa7f22Ee6DD46df92470313eb7794A4Ab3eFf5C98",
        "0xaA71b2d63113cA9038B68FA6be8C785AFD2525c3",
        "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c",
        "0xae4543C02412A208A53F2FDf56eE3E5d943022A0",
        "0xb0A784FbF41BB6bDdd308FBcEeA8c58c94D34526",
        "0xb5f699E9FEFb4aa4871a1e378b209BBD44866Ee5",
        "0xb68e455bdA3e37Ed5a87167b107E125b0b18808e",
        "0xbcD1e6bFbf25aAB3eBDd84083855A17Ca01E4B25",
        "0xc00b7fD2a605c9bCed1D73a66f5E7F1e88c177E6",
        "0xc241CEDed13E5D4ff7217253047a40f57EE0b985",
        "0xc33E7bE3F12ecBE11D566DE9Aa7552C0B6AAE9d5",
        "0xc391CDEB69490ed54f0a017afcbBDe26a48B7A0D",
        "0xc71698c947B19bA97Dd04D5f23aaabB7cA09CA46",
        "0xcC0fD14Cb9E50357FEA53Fa45B7cC0351DAdA728",
        "0xcCDA8911aCD7f68A7CE24570D5e8e6A324C4980c",
        "0xd1a2670949d77a1846F8c829c375395a66F695b4",
        "0xd2034451D6624dCA53dAd80c9bAe9c53aDC8f338",
        "0xd36e9299Aca1a32776b8CdEdaCEeCc0Bee8F693d",
        "0xd3EE25DB3F3eb7b266c347f97504f442ADb91846",
        "0xd4B4e8a57b49319b8706937bA60c6350d8811Ba8",
        "0xd6e1b15eDDd2e93FE48e62583FD32C22044e7B6f",
        "0xd8ce7301ccefFb4C71b7800659bd9F6aa6c153F5",
        "0xd93ce24d296e8a737ac783A3E264E628D094787F",
        "0xde7aB227F230a6d1bC46D1b5299075010cd10d44",
        "0xdf740B9eEc3866fFa777d5fD534cFdf885864a9A",
        "0xe24bd83418624e641BcD6E22e027F33477d22E34",
        "0xe36142D3D10354d15ca01C2dd3132cFaFD21Dae4",
        "0xe4B02b36f2Af93d038b3e456Ec5e5cDC15ca5B9D",
        "0xe8434d26b2DaA9534250475ff263E08247a0eAb2",
        "0xeBE551a3460eAE110a275A57A0Cb0E260978A46a",
        "0xee91efe703BE64b08F6c5fd91Fee9aE3813ccfE5",
        "0xef2Bb3FC203b8CB6a245eF31AD8d169ffd78b801",
        "0xf04957c69e18Eb4867901eB732ffc9C5bb15e4b6",
        "0xf4F4851C96eaBDD8e410F8691D0f695558AbB6A3",
        "0xf783741A1F125c2E0c0e9dAFd2017f03c03E403b",
        "0xfB121DAFBBfA52F35225B39837CA4C85f2327de8",
        "0xfF8d52bB3337B42C4f717cD742F5b38A193Cac07",
        "0xfFf3eF8CCED8B35837dd48798C826241324362b5",
        "keystore.zip"
    ],
    time: "2020-06-23 14:55:07"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eec9d75c80ccfb0a65de848"),
    method: "chain_getBalance",
    result: "1000000802931848000000000",
    time: "2020-06-26 20:40:04"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecbeaef6d8a5a46d081f7c"),
    method: "account_voteCredit",
    result: "0x2fae901bcc6c31eb8f36bb03fdaecec09b17dfab551b60ec9d4b49fc9de301c2",
    time: "2020-06-24 19:07:09"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecc11cbb4998d896424846"),
    method: "chain_getCancelCreditDetail",
    result: null,
    time: "2020-06-24 16:46:56"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecc1fb72504b3b3af471df"),
    method: "account_cancelVoteCredit",
    result: "0xde66433fef4da1b825fe26e601a3703be2be377b13ed60935802ab57218f59ca",
    time: "2020-06-19 22:37:18"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecc2c881c7214b26ef22c2"),
    method: "chain_getCreditDetails",
    result: "",
    time: "2020-06-19 22:37:18"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecc414eb523d86ae000330"),
    method: "chain_getCandidateAddrs",
    result: "[{\"Addr\":\"0x3726430e6e3448753f29e1d3ca24120850433ff9\",\"Credit\":\"0x1bc16d674ec93312\"},{\"Addr\":\"0x6c09dc42420b79b1222bd62d964e9e2dccc558ea\",\"Credit\":\"0x7da\"},{\"Addr\":\"0x16838cc5b6d97b43874421dcc123ba31f13e9725\",\"Credit\":\"0xa\"},{\"Addr\":\"0xb490ffa71d9d1d9f4472fbc46ee6e4ffd2bb486b\",\"Credit\":\"0x1a784379d99db420000c8\"}]",
    time: "2020-06-24 18:26:51"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecc6ddeee1dd8bb3aa47d1"),
    method: "blockmgr_getPoolTransactions",
    result: [
        [ ],
        [ ]
    ],
    time: "2020-06-24 19:01:11"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecc78132dc24203b683da9"),
    method: "blockmgr_getTxInPool",
    result: {
        Data: {
            Version: NumberInt("1"),
            Nonce: NumberInt("6972"),
            Type: NumberInt("6"),
            To: "0x0000000000000000000000000000000000000000",
            ChainId: NumberInt("0"),
            Amount: "0x84595161401484a000000",
            GasPrice: "0x2625a00",
            GasLimit: "0x112a880",
            Timestamp: NumberInt("1592995479"),
            Data: "eyJQdWJrZXkiOiIweDAyN2YyMjE1OGY4Njg5ZmFhZDFkZWZkMzNiMTUwNjZhMjMyNmJhZTYwNTc5ODAwOTE4YjMxMWRiODY3YWZhZmI0NyIsIk5vZGUiOiJlbm9kZTovLzMyOGJjZDQxYzM3YTdjYjkzODIwNDhmMWVjNmI5YjU0NmY3YjI2MWMxMTc3ZGNmOTkyODU5YTY2NWNjNjY0Y2FAMTkyLjE2OC4zLjIyOjQ0NDQ0In0="
        },
        Sig: "HwSHeYk/mTNlQuBM5umVJ+4+tZ703FNbbFNWtDV0rLFaLymo69b/cQZdm1hyBbdd2PHYiIeeh9qnbDXcuPfSdB8="
    },
    time: "2020-06-24 18:47:06"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eecc96119f199306f2d7d1a"),
    method: "chain_getByteCode",
    result: "",
    time: "2020-06-19 22:37:18"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eeccda868856619f2f36fca"),
    method: "account_dumpPubkey",
    result: "0x037178385e428cd7e45c592770c900a81383601682d59d04786120149d6da9fffe",
    time: "2020-06-24 19:01:01"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eeccda968856619f2f36fcb"),
    method: "p2p_localNode",
    result: "enode://328bcd41c37a7cb9382048f1ec6b9b546f7b261c1177dcf992859a665cc664ca@127.0.0.1:44444",
    time: "2020-06-24 19:01:01"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5eeccf93b523403cf02f461c"),
    method: "account_cancelCandidateCredit",
    result: "0x0c2653dbdea9e57f9fc797c98e7eb29bdbfdc468a28a68a3e8ab1fcc7b150ead",
    time: "2020-06-21 17:48:52"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5ef19f7dfae06ce9d7446df8"),
    method: "account_transfer",
    result: "0x2f3307a6915ee80a2f65e82581b6d9d3462d26da4fb586a38823638a954bba43",
    time: "2020-06-24 17:42:53"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5ef19fd3b4238d477be7eb14"),
    method: "account_transferWithNonce",
    result: "0xdad47c51d794878f104c5f12207291fc4071550fac533aa3adcdc40786a42e0e",
    time: "2020-06-23 14:23:15"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5ef1e421539be0a65e9784dc"),
    method: "account_unlockAccount",
    result: null,
    time: "2020-06-24 18:26:52"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5ef1f4487fe137acfd0c8b7f"),
    method: "account_dumpPrivkey",
    result: "0xea2fe1fbc82095dec11a2632cdf34120711b59e6d059bfaf11aeba729471bb9b",
    time: "2020-06-24 18:26:52"
} ]);
db.getCollection("result_msg").insert([ {
    _id: ObjectId("5ef312db85a6147a0804f300"),
    method: "chain_getLogs",
    result: null,
    time: "2020-06-24 16:46:27"
} ]);
