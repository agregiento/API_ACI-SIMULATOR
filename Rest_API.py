import json
import requests


url1 = "http://127.0.0.1:58000/api/v1/ticket"
data = {
    "password":"admin123!",
    "username":"admin"
}
cabecera1 = {"content-type":"application/json"}
respuesta1 = requests.post(url1,json.dumps(data), headers=cabecera1)

#print(respuesta.text)
repuesta_json = respuesta1.json()
print(repuesta_json)

API_Token = repuesta_json["response"]["serviceTicket"]
url2 = "http://127.0.0.1:58000/api/v1/network-device"
cabecera2 = {"content-type":"application/json","X-Auth-Token":API_Token}

respuesta_inventario = requests.get(url2, headers=cabecera2)
repuesta_inventario_json = respuesta_inventario.json()
print(repuesta_inventario_json)