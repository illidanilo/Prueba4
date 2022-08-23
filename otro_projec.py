import json
import requests

import conf

def obtener_token(clave, usuario):
    data = {"password":clave, "username":usuario}
    cabecera = {"content-type": "application/json"}
    respuesta = requests.post("http://127.0.0.1:58000/api/v1/ticket", json.dumps(data), headers=cabecera)
    token = (respuesta.json()["response"]["serviceTicket"])
    return token
token = obtener_token(conf.clave, conf.usuario)


header = {"content-type": "application/json", "X-Auth-Token": token}
dispositivos = requests.get("http://127.0.0.1:58000/api/v1/network-health", headers=header)


salud_de_red = (dispositivos.json()['healthyClient'])
b = "100"

if salud_de_red > b:
    print("Equipos : Fuera de linea")
else:
    print("Equipos : en linea ")
print("nivel de salud            "+dispositivos.json()['healthyClient']+"%")
print("Cantidad de routers       "+dispositivos.json()["numLicensedRouters"])
print("Cantidad de switches      "+dispositivos.json()["numLicensedSwitches"])
print("total de equipos          "+dispositivos.json()["numNetworkDevices"])

