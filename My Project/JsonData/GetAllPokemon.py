import json
import requests

categories = {1:"Seed Pokemon",2:"Seed Pokemon",3:"Seed Pokemon",4:"Lizard Pokemon",5:"Flame Pokemon",6:"Flame Pokemon",7:"Tiny Turtle Pokemon",
    8:"Turtle Pokemon",9:"Shellfish Pokemon",10:"Worm Pokemon",11:"Cocoon Pokemon",12:"Butterfly Pokemon",13:"Hairy Bug Pokemon",14:"Cocoon Pokemon",
    15:"Poison Bee Pokemon",16:"Tiny Bird Pokemon",17:"Bird Pokemon",18:"Bird Pokemon",19:"Mouse Pokemon",20:"Mouse Pokemon",21:"Tiny Bird Pokemon",
    22:"Beak Pokemon",23:"Snake Pokemon",24:"Cobra Pokemon",25:"Mouse Pokemon",26:"Mouse Pokemon",27:"Mouse Pokemon",28:"Mouse Pokemon",
    29:"Poison Pin Pokemon",30:"Poison Pin Pokemon",31:"Drill Pokemon",32:"Poison Pin Pokemon",33:"Poison Pin Pokemon",34:"Drill Pokemon",
    35:"Fairy Pokemon",36:"Fairy Pokemon",37:"Fox Pokemon",38:"Fox Pokemon",39:"Balloon Pokemon",40:"Balloon Pokemon",41:"Bat Pokemon",
    42:"Bat Pokemon",43:"Weed Pokemon",44:"Weed Pokemon",45:"Flower Pokemon",46:"Mushroom Pokemon",47:"Mushroom Pokemon",48:"Insect Pokemon",
    49:"Poison Moth Pokemon",50:"Mole Pokemon",51:"Mole Pokemon",52:"Scratch Cat Pokemon",53:"Classy Cat Pokemon",54:"Duck Pokemon",55:"Duck Pokemon",
    56:"Pig Monkey Pokemon",57:"Pig Monkey Pokemon",58:"Puppy Pokemon",59:"Legendary Pokemon",60:"Tadpole Pokemon",61:"Tadpole Pokemon",62:"Tadpole Pokemon",
    63:"Psi Pokemon",64:"Psi Pokemon",65:"Psi Pokemon",66:"Superpower Pokemon",67:"Superpower Pokemon",68:"Superpower Pokemon",69:"Flower Pokemon",
    70:"Flycatcher Pokemon",71:"Flycatcher Pokemon",72:"Jellyfish Pokemon",73:"Jellyfish Pokemon",74:"Rock Pokemon",75:"Rock Pokemon",76:"Megaton Pokemon",
    77:"Fire Horse Pokemon",78:"Fire Horse Pokemon",79:"Dopey Pokemon",80:"Hermit Crab Pokemon",81:"Magnet Pokemon",82:"Magnet Pokemon",83:"Wild Duck Pokemon",
    84:"Twin Bird Pokemon",85:"Triple Bird Pokemon",86:"Sea Lion Pokemon",87:"Sea Lion Pokemon",88:"Sludge Pokemon",89:"Sludge Pokemon",90:"Bivalve Pokemon",
    91:"Bivalve Pokemon",92:"Gas Pokemon",93:"Gas Pokemon",94:"Shadow Pokemon",95:"Rock Snake Pokemon",96:"Hypnosis",97:"Hypnosis Pokemon",98:"River Crab Pokemon",
    99:"Pincer Pokemon",100:"Ball Pokemon",101:"Ball Pokemon",102:"Egg Pokemon",103:"Coconut Pokemon",104:"Lonely Pokemon",105:"Bone Keeper Pokemon",
    106:"Kicking Pokemon",107:"Punching Pokemon",108:"Licking Pokemon",109:"Poison Gas Pokemon",110:"Poison Gas Pokemon",111:"Spikes Pokemon",
    112:"Drill Pokemon",113:"Egg Pokemon",114:"Vine Pokemon",115:"Parent Pokemon",116:"Dragon Pokemon",117:"Dragon Pokemon",118:"Goldfish Pokemon",
    119:"Goldfish Pokemon",120:"Star Shape Pokemon",121:"Mysterious Pokemon",122:"Barrier Pokemon",123:"Mantis Pokemon",124:"Human Shape Pokemon",
    125:"Electric Pokemon",126:"Spitfire Pokemon",127:"Stag Beetle Pokemon",128:"Wild Bull Pokemon",129:"Fish Pokemon",130:"Atrocious Pokemon",
    131:"Transport Pokemon",132:"Transform Pokemon",133:"Evolution Pokemon",134:"Bubble Jet Pokemon",135:"Lightning Pokemon",136:"Flame Pokemon",
    137:"Virtual Pokemon",138:"Spiral Pokemon",139:"Spiral Pokemon",140:"Shellfish Pokemon",141:"Shellfish Pokemon",142:"Fossil Pokemon",143:"Sleeping Pokemon",
    144:"Freeze Pokemon",145:"Electric Pokemon",146:"Flame Pokemon",147:"Dragon Pokemon",148:"Dragon Pokemon",149:"Dragon Pokemon",150:"Genetic Pokemon",151:"New Species Pokemon",
    152:"Leaf Pokemon",153:"Leaf Pokemon",154:"Herb Pokemon",155:"Fire Mouse Pokemon",156:"Volcano Pokemon",157:"Volcano Pokemon",158:"Big Jaw Pokemon",
    159:"Big Jaw Pokemon",160:"Big Jaw Pokemon",161:"Scout Pokemon",162:"Long Body Pokemon",163:"Owl Pokemon",164:"Owl Pokemon",165:"Five Star Pokemon",166:"Five Star Pokemon",167:"String Spit Pokemon",
    168:"Long Leg Pokemon",169:"Bat Pokemon",170:"Angler Pokemon",171:"Light Pokemon",172:"Tiny Mouse Pokemon"
            }
Otherforms = { "Hisuan Growlithe":"Scout Pokemon", "Galarian Ponyta":"Unique Horn Pokemon","Galarian Rapidash":"Unique Horn Pokemon",
              "Hisuian Voltorb":"Sphere Pokemon","Hisuian ELectrode":"Sphere Pokemon","Galarian Articuno":"Cruel Pokemon","Hisuian Typhlosion":"Ghost Flame Pokemon",
            }
result = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1302")
contents = result.json()
control = 1
counter = 1
poke ="https://pokeapi.co/api/v2/pokemon/"
pokemon = {}
for i in range(1301):
    if control == 1025:
        control = 10001

    if (counter == 1140 or counter == 1141 or counter == 1141 or counter ==1142 or counter == 1143 or counter ==1145 or counter == 1146 or counter == 1117 or counter == 1152 or 
        counter == 1153 or counter == 1168 or counter == 1169 or counter == 1170 or counter == 1173 or counter == 1174
        or counter == 1175 or counter == 1177 or counter == 1178 or counter == 1182 or counter ==1183 or counter == 1216
        or counter == 1288 or counter == 1289 or counter == 1290 or counter == 1291 or counter == 1292 or counter == 1293 or counter == 1294 or counter == 1295
        or counter == 1104 or counter == 1105 or counter ==1106 or counter ==1107 or counter ==1108 or counter ==1109 or counter ==1118 or counter ==1119 or counter ==1120
        or counter ==1121 or counter ==1122 or counter ==1123 or counter ==1172 or counter ==1184 or counter ==1085):
        pass
    else:
        fullUrl = poke+str(control)
        api = requests.get(fullUrl)
        contents = api.json()

        #Set Dictionary Entry For That Pokemon
        pokemon[counter] = {}

        pokemon[counter]["name"] = contents["name"]

        pokemon[counter]["types"] = list()
    
        for i in range(0,len(contents["types"])):
            pokemon[counter]["types"].append(contents["types"][i]["type"]["name"])

        pokemon[counter]["height"] = contents["height"]

        pokemon[counter]["weight"] = contents["weight"]

        pokemon[counter]["forms"] = list()

        for i in range(0,len(contents["forms"])):
            pokemon[counter]["forms"].append(contents["forms"][i]["name"])

        pokemon[counter]["moves"] = list()

        for i in range(0,len(contents["moves"])):
            pokemon[counter]["moves"].append(contents["moves"][i]["move"]["name"])

        pokemon[counter]["abilities"] = list()

        for i in range(0,len(contents["abilities"])):
            pokemon[counter]["abilities"] = contents["abilities"][i]["ability"]["name"]

        if counter < 173:
            pokemon[counter]["category"] = categories[counter]

        pokemon[counter]["gender"] = list()

        pokemon[counter]["shiny"] = [False,True]

    print(counter)
    control = control + 1
    counter = counter + 1

result = requests.get("https://pokeapi.co/api/v2/gender?limit=3")
contents = result.json()
counter = 1
poke ="https://pokeapi.co/api/v2/gender/"
for x in range(3):
    fullUrl = poke+str(counter)
    api = requests.get(fullUrl)
    contents = api.json()
    for i in range(0,len(contents["pokemon_species_details"])):
        getDexNum = requests.get(contents["pokemon_species_details"][i]["pokemon_species"]["url"])
        dex = getDexNum.json()
        number = dex["pokedex_numbers"][0]["entry_number"]
        pokemon[number]["gender"].append(contents["name"])
        print(str(x) + ": " + str(i))
    control = control + 1




with open("pokemon.json","w") as fp:
    json.dump(pokemon,fp,indent = 4)
print("Check your folder for the file!")
