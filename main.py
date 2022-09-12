import requests
import json
CWR=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread")
FND=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd")
SWT=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=swt")
CWR_text=CWR.text
CWR_again=json.loads(CWR_text)
for CWR_again_1 in CWR_again["temperature"]["data"]:
    if CWR_again_1["place"] == "Hong Kong Park":
        CWR_HK_json=CWR_again_1
CWR_HK_OUT_1=CWR_HK_json["place"]
CWR_HK_OUT_2_int=CWR_HK_json["value"]
CWR_HK_OUT_2=str(CWR_HK_OUT_2_int)
CWR_HK_OUT_3=CWR_HK_json["unit"]
ListsAreFun1=[CWR_HK_OUT_2, CWR_HK_OUT_3]
ListsAreFunAir1=""
CWR_HK_OUT_23=ListsAreFunAir1.join(ListsAreFun1)
ListsAreFun2=[CWR_HK_OUT_1, CWR_HK_OUT_23]
ListsAreFunAir2="@"
CWR_HK_OUT=ListsAreFunAir2.join(ListsAreFun2)
print(CWR_HK_OUT)
