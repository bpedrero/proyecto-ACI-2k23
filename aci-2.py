import requests
import json
import conf

def pedir_token():

    requests.packages.urllib3.disable_warnings()
    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
    dato = {
        "aaaUser" : {
            "attributes" : {
                "name" : conf.usuario,
                "pwd" : conf.clave
            }
        }
    }
    cabecera = {"Content-Type": "application/json"}

    respuesta = requests.post(url, data=json.dumps(dato), headers=cabecera,verify=False)
    respuesta_json = respuesta.json()
    #print(respuesta_json)
    Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    #print("\nAPI-token: "+Token)
    return Token

API_Token = pedir_token()
print("\nAPI_Token: "+API_Token)
print("&"*70)

# GET https://10.10.20.14/api/class/topSystem.json

url =  "https://sandboxapicdc.cisco.com/api/class/topSystem.json"
cabecera = {"Content-Type": "application/json"}
cookie = {"APIC-cookie":API_Token}

try:
    respuesta = requests.get(url,headers=cabecera,cookies=cookie,verify=False)
except Exception as err:
    print("Falló la petición")
    exit(1)

respuesta_json = respuesta.json()
print (respuesta_json)
#address = respuesta_json["imdata"][0]["topSystem"]["attributes"]["address"]

for i in range(0,3):
    address = respuesta_json["imdata"][i]["topSystem"]["attributes"]["address"]
    fabricMAC = respuesta_json["imdata"][i]["topSystem"]["attributes"]["fabricMAC"]
    state = respuesta_json["imdata"][i]["topSystem"]["attributes"]["state"]

    print("address: "+address+"     "+"fabricMAC: "+fabricMAC+"     ", "state: "+state)

#En la petición
print(respuesta.request.url)
print("peticion: ",respuesta.request.headers)
#En la respuesta
print("respuesta: ",respuesta.url)