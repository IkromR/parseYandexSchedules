import json
import urllib.request

# Parse Yandex schedules - list of stations

BASE_URL = "https://api.rasp.yandex.net/v3.0/stations_list/?apikey=5ed2d71a-8b0e-46dd-bd83-02c1b3d30a54&format=json&lang=ru_RU"

with urllib.request.urlopen(BASE_URL) as url:
    data = json.load(url)

f = open('data.json', 'w', encoding='utf-8')
f.write('{"stations": [\n')
atr = ["direction", "codes", "station_type", "title", "transport_type"]
temp = ''

for i in data["countries"]:
    for j in i["regions"]:
        for k in j["settlements"]:
            for l in k["stations"]:
                if l['station_type'] == "airport":
                    # print(k['title'], '\n',  l, '\n')
                    temp = '{\n\t' + f'"city": "{k["title"]}",\n\t'
                    for m in l:
                        if m in atr:
                            attribute = l[m]
                            if m == "codes":
                                # print('{"yandex_code: "' + f'"{attribute["yandex_code"]}"' + '}')
                                # for n in attribute:
                                temp += f'"{m}": ' + '{"yandex_code": ' + f'"{attribute["yandex_code"]}"' + '}'
                            else:
                                temp += f'"{m}": ' + f'"{l[m]}"'
                            if m != "transport_type":
                                temp += ','
                            temp += '\n\t'
                    temp += "}"
                    # print(temp)
                    # json.dump(temp, f, ensure_ascii=False, indent=4)
                    f.write(temp)
                    f.write(',\n')

f.write(']}')
f.close()
