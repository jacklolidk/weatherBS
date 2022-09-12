import requests
import json
CWR=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread")
SWT=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=swt")
##CWR parse
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
##swt parser
SWT_text=SWT.text
SWT_again=json.loads(SWT_text)
SWT_OUT=SWT_again["swt"][0]["desc"]
print(CWR_HK_OUT)
print(SWT_OUT)