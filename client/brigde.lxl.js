//LiteXLoader Dev Helper
/// <reference path="c:\Users\xx093\.vscode\extensions\moxicat.lxldevhelper-0.1.8/Library/JS/Api.js" /> 

if (!File.exists("plugins\\Mcc")) {File.mkdir("plugins\\Mcc")}
if (!File.exists("plugins\\Mcc\\Bridge")) {File.mkdir("plugins\\Mcc\\Bridge")}
var CONFIG = data.openConfig("plugins\\Mcc\\Bridge\\config.json","json",JSON.stringify({
    AdminInLive:[]
}))

// function reloadConfig() {
//     CONFIG = data.openConfig("plugins\\Mcc\\Bridge\\config.json","json",JSON.stringify({}))
// }

mc.broadcast(`>> §e嘗試連接OM直播聊天同步工具`)
wsc = new WSClient()
let check = wsc.connect("ws://127.0.0.1:13254")
if (check) {mc.broadcast(`>> §a連接成功`)}
else {mc.broadcast(`>> §c連接失敗`)}

wsc.listen("onTextReceived",function(msg) {
    msgView = JSON.parse(msg);
    if (msgView["sender"] == "dada878_bot") {return}
    if (msgView["type"] == "comment") {
        if (msgView["message"].startsWith("/") && CONFIG.get("AdminInLive").includes(msgView["sender"])) {
            let cmd = mc.runcmdEx(msgView["message"].substring(1,msgView["message"].length)).output
            if (cmd) {
                mc.broadcast(`§6[OM直播(指令)]§b${msgView["sender"]} §f>> §a${cmd}`)
            }
            else {
                mc.broadcast(`§6[OM直播(指令)]§b${msgView["sender"]} §f>> §f執行了一條指令`)
            }
            
            return
        }
        if (msgView["subscriber"]) {
            mc.broadcast(`§6[直播]§c[訂閱者]§b${msgView["sender"]} §e>> §f${msgView["message"]}`)
        }
        else {
            mc.broadcast(`§6[直播]§b${msgView["sender"]} §e>> §f${msgView["message"]}`)
        }
        
    }
    else if (msgView["type"] == "buff") {
        mc.broadcast(`§e----------§c系統廣播§e----------\n§b感謝乾爹 §a${msgView["sender"]}\n§b贊助了我們§a${msgView["ombCount"]}omb\n§e-----------------------------`)
        mc.runcmdEx(`title @a title §b${msgView["sender"]}`)
        mc.runcmdEx(`title @a subtitle §a${msgView["message"]}`)
        mc.runcmdEx(`playsound mob.enderdragon.growl @a`)
    }
    else if (msgView["type"] == "subscribe") {
        mc.broadcast(`§e----------§c系統廣播§e----------\n§d感謝乾爹 §b${msgView["sender"]}\n§d訂閱並成為贊助者！\n§e-----------------------------`)
        mc.runcmdEx(`title @a title §6${msgView["sender"]}`)
        mc.runcmdEx(`title @a subtitle §c成為了訂閱者！`)
        mc.runcmdEx(`playsound mob.wither.death @a`)
    }
})

wsc.listen("onLostConnection",function(code) {
    mc.broadcast(`>> §cOM直播聊天同步工具已斷線`)
    mc.broadcast(`>> §e自動嘗試重連中`)
    let check = wsc.connect("ws://127.0.0.1:13254")
    if (check) {mc.broadcast(`>> §a連接成功`)}
    else {mc.broadcast(`>> §c連接失敗`)}
})

mc.regPlayerCmd("connect","連接om直播訊息同步工具",function(player,args) {
    mc.broadcast(`>> §e嘗試連接OM直播聊天同步工具`)
    let check = wsc.connect("ws://127.0.0.1:13254")
    if (check) {mc.broadcast(`>> §a連接成功`)}
    else {mc.broadcast(`>> §c連接失敗`)}
},1)