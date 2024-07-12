import json

f = open('pokemon.json')

data = json.load(f)

#print(data)

for i in range(1,1302):
    if (i == 1140 or i == 1141 or i == 1141 or i ==1142 or i == 1143 or i ==1145 or i == 1146 or i == 1117 or i == 1152 or 
        i == 1153 or i == 1168 or i == 1169 or i == 1170 or i == 1173 or i == 1174
        or i == 1175 or i == 1177 or i == 1178 or i == 1182 or i ==1183 or i == 1216
        or i == 1288 or i == 1289 or i == 1290 or i == 1291 or i == 1292 or i == 1293 or i == 1294 or i == 1295
        or i == 1104 or i == 1105 or i ==1106 or i ==1107 or i ==1108 or i ==1109 or i ==1118 or i ==1119 or i ==1120
        or i ==1121 or i ==1122 or i ==1123 or i ==1172 or i ==1184 or i ==1085):
        pass
    elif (len(data[str(i)]["forms"]) > 1):
        print(data[str(i)]["name"])