import json
import urllib.request

BASE_URL = "https://api.rasp.yandex.net/v3.0/stations_list/?apikey=5ed2d71a-8b0e-46dd-bd83-02c1b3d30a54&format=json&lang=ru_RU"

with urllib.request.urlopen(BASE_URL) as url:
    data = json.load(url)

f = open('data2.json', 'w', encoding='utf-8')
f.write('{"stations": [\n')

for i in data["countries"]:
    for j in i["regions"]:
        for k in j["settlements"]:
            for l in k["stations"]:
                if l['station_type'] == "airport":
                    # print(k['title'], '\n',  l, '\n')
                    json.dump(l, f, ensure_ascii=False, indent=4)
                    f.write(',\n')

f.write(']}')
f.close()
