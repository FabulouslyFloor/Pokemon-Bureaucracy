import json
import requests

categories = {1:"Seed Pokemon",2:"Seed Pokemon",3:"Seed Pokemon",
            4:"Lizard Pokemon",5:"Flame Pokemon",6:"Flame Pokemon",
            7:"Tiny Turtle Pokemon",8:"Turtle Pokemon",9:"Shellfish Pokemon",
            10:"Worm Pokemon",11:"Cocoon Pokemon",12:"Butterfly Pokemon",
            13:"Hairy Bug Pokemon",14:"Cocoon Pokemon",15:"Poison Bee Pokemon",
            16:"Tiny Bird Pokemon",17:"Bird Pokemon",18:"Bird Pokemon",
            19:"Mouse Pokemon",20:"Mouse Pokemon",21:"Tiny Bird Pokemon",
            22:"Beak Pokemon",23:"Snake Pokemon",24:"Cobra Pokemon",
            25:"Mouse Pokemon",26:"Mouse Pokemon",27:"Mouse Pokemon",
            28:"Mouse Pokemon",29:"Poison Pin Pokemon",30:"Poison Pin Pokemon",
            31:"Drill Pokemon",32:"Poison Pin Pokemon",33:"Poison Pin Pokemon",
            34:"Drill Pokemon",35:"Fairy Pokemon",36:"Fairy Pokemon",
            37:"Fox Pokemon",38:"Fox Pokemon",39:"Balloon Pokemon",
            40:"Balloon Pokemon",41:"Bat Pokemon",42:"Bat Pokemon",
            43:"Weed Pokemon",44:"Weed Pokemon",45:"Flower Pokemon",
            46:"Mushroom Pokemon",47:"Mushroom Pokemon",48:"Insect Pokemon",
            49:"Poison Moth Pokemon",50:"Mole Pokemon",51:"Mole Pokemon",
            52:"Scratch Cat Pokemon",53:"Classy Cat Pokemon",54:"Duck Pokemon",
            55:"Duck Pokemon",56:"Pig Monkey Pokemon",57:"Pig Monkey Pokemon",
            58:"Puppy Pokemon",59:"Legendary Pokemon",60:"Tadpole Pokemon",
            61:"Tadpole Pokemon",62:"Tadpole Pokemon",63:"Psi Pokemon",
            64:"Psi Pokemon",65:"Psi Pokemon",66:"Superpower Pokemon",
            67:"Superpower Pokemon",68:"Superpower Pokemon",69:"Flower Pokemon",
            70:"Flycatcher Pokemon",71:"Flycatcher Pokemon",72:"Jellyfish Pokemon",
            73:"Jellyfish Pokemon",74:"Rock Pokemon",75:"Rock Pokemon",
            76:"Megaton Pokemon",77:"Fire Horse Pokemon",78:"Fire Horse Pokemon"
            }
Otherforms = { "Hisuan Growlithe":"Scout Pokemon", "Galarian Ponyta":"Unique Horn Pokemon","Galarian Rapidash":"Unique Horn Pokemon",
              

            }
result = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1302")
contents = result.json()
counter = 1
poke ="https://pokeapi.co/api/v2/pokemon/"
pokemon = {}
for i in range(1025):
    fullUrl = poke+str(counter)
    api = requests.get(fullUrl)
    contents = api.json()

    name = contents["name"]
    #Set Dictionary Entry For That Pokemon
    pokemon[name] = {}

    pokemon[name]["types"] = list()
    
    for i in range(0,len(contents["types"])):
        pokemon[name]["types"].append(contents["types"][i]["type"]["name"])

    pokemon[name]["height"] = contents["height"]

    pokemon[name]["weight"] = contents["weight"]

    pokemon[name]["forms"] = list()

    for i in range(0,len(contents["forms"])):
        pokemon[name]["forms"].append(contents["forms"][i]["name"])

    pokemon[name]["moves"] = list()

    for i in range(0,len(contents["moves"])):
        pokemon[name]["moves"].append(contents["moves"][i]["move"]["name"])

    if counter < 52:
        pokemon[name]["category"] = categories[counter]

    pokemon[name]["gender"] = list()

    pokemon[name]["shiny"] = [False,True]

    print(counter)
    counter = counter + 1

with open("pokemon.json","w") as fp:
    json.dump(pokemon,fp,indent = 4)
print("Check your folder for the file!")

'''
result = requests.get("https://pokeapi.co/api/v2/gender?limit=3")
contents = result.json()
counter = 1
poke ="https://pokeapi.co/api/v2/gender/"
for i in range(3):
    fullUrl = poke+str(counter)
    api = requests.get(fullUrl)
    contents = api.json()
    for i in range(0,len(contents["pokemon_species_details"])):
        if i == 221:
            pokemon["basculin-red-striped"]["gender"].append(contents["name"])
        elif i == 289:
            pokemon["pumpkaboo-average"]["gender"].append(contents["name"])
        elif i == 299:
            pokemon["oricorio-baile"]["gender"].append(contents["name"])
        elif i == 302:
            pokemon["wishiwashi-solo"]["gender"].append(contents["name"])    
        elif i == 320:
            pokemon["mimikyu-disguised"]["gender"].append(contents["name"]) 
        elif i == 349:
            pokemon["eiscue-ice"]["gender"].append(contents["name"]) 
        elif i == 350:
            pokemon["indeedee-male"]["gender"].append(contents["name"]) 
        elif i == 351:
            pokemon["morpeko-full-belly"]["gender"].append(contents["name"]) 
        elif i == 356:
            pokemon["enamorus-incarnate"]["gender"].append(contents["name"])   
        elif i == 586:
            pokemon["wormadam-plant"]["gender"].append(contents["name"]) 
            pokemon["wormadam-sandy"]["gender"].append(contents["name"])
            pokemon["wormadam-trash"]["gender"].append(contents["name"])  
        elif i == 654:
            pokemon["darmanitan-standard"]["gender"].append(contents["name"])
        elif i == 707:
            pokemon["meowstic-male"]["gender"].append(contents["name"])
        elif i == 723:
            pokemon["gourgeist-average"]["gender"].append(contents["name"])
        elif i == 739:
            pokemon["lycanroc-midday"]["gender"].append(contents["name"])
        elif i == 775:
            pokemon["toxtricity-amped"]["gender"].append(contents["name"])
        elif i == 791:
            pokemon["urshifu-single-strike"]["gender"].append(contents["name"])
        elif i == 795:
            pokemon["basculegion-male"]["gender"].append(contents["name"])
        else:
            pokemon[contents["pokemon_species_details"][i]["pokemon_species"]["name"]]["gender"].append(contents["name"])

    counter = counter + 1




with open("pokemon.json","w") as fp:
    json.dump(pokemon,fp,indent = 4)
print("Check your folder for the file!")
'''