from flask import Flask, render_template, url_for
import requests, json
from mcstatus import JavaServer,BedrockServer
app = Flask(__name__)

@app.route('/')
def home():
    title = '楓鈴の都'
    return render_template("home.html", title = title)


@app.route("/itd")
def itd():
    return render_template("itd.html")

@app.route("/test")
def test():
    server = JavaServer.lookup("maplelive.ddns.net")
    status = server.status()
    is_online = status.playsers.online 
    ping = status.latency



    
    

@app.route("/mcserver")
def mc():
    #java server
    java_ip = "maplelive.ddns.net"
    url = f"https://api.mcsrvstat.us/2/{java_ip}"
    idk = requests.get(url)
    idk = idk.json()
    java_server = JavaServer.lookup(java_ip)
    java_status = java_server.status()
    ping = round(java_status.latency)
    is_online = idk['online']
    ip = idk['hostname']
    server_name = idk['motd']['clean'][0]
    server_version = idk['software'] + " " + idk['version']
    online_member = str(idk['players']['online']) + " / " + str(idk['players']['max'])
    port = idk["port"]

    #bedrock server
    ip = "play.maplelive.ml"
    port1 = "25535"
    bedrock_ip = "play.maplelive.ml:25535"
    bedrock_server = BedrockServer.lookup(bedrock_ip)
    bedrock_status = bedrock_server.status()
    players_online = bedrock_status.players_online
    players_max = bedrock_status.players_max
    bedrock_ping =  round(bedrock_status.latency )
    name = bedrock_status.motd


    return render_template("mc.html", mc1=is_online,mc2=ip,mc3=server_name,mc4=server_version,mc5=ping,mc6=online_member,mc7=port,mc11=ip,mc12=port1,mc13=players_online,mc14=name,mc15=bedrock_ping,mc16=players_max)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=50, debug=True)