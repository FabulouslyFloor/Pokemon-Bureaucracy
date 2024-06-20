import json
import requests
import re

# Manual dictionary of all the pokemon categories
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
# Categories for alternate forms who don't have their own national dex number
Otherforms = { "Hisuan Growlithe":"Scout Pokemon", "Galarian Ponyta":"Unique Horn Pokemon","Galarian Rapidash":"Unique Horn Pokemon",
              "Hisuian Voltorb":"Sphere Pokemon","Hisuian ELectrode":"Sphere Pokemon","Galarian Articuno":"Cruel Pokemon","Hisuian Typhlosion":"Ghost Flame Pokemon",
            }

# Used to put at the end of the api calls
control = 1
# Used to number the entries
counter = 1
# Save the beginning of the call
poke ="https://pokeapi.co/api/v2/pokemon/"
# Set up the dictionary
pokemon = {}
# Loop through every entry in the API
for i in range(1301):
    # Checks if we have reached call 1205. Changes the number to reflect the address change in the rest of them
    if control == 1025:
        control = 10001

    # These entries are for pokemon forms we don't need in game, like all the unique pikachu-in-hat's
    if (counter == 1140 or counter == 1141 or counter == 1141 or counter ==1142 or counter == 1143 or counter ==1145 or counter == 1146 or counter == 1117 or counter == 1152 or 
        counter == 1153 or counter == 1168 or counter == 1169 or counter == 1170 or counter == 1173 or counter == 1174
        or counter == 1175 or counter == 1177 or counter == 1178 or counter == 1182 or counter ==1183 or counter == 1216
        or counter == 1288 or counter == 1289 or counter == 1290 or counter == 1291 or counter == 1292 or counter == 1293 or counter == 1294 or counter == 1295
        or counter == 1104 or counter == 1105 or counter ==1106 or counter ==1107 or counter ==1108 or counter ==1109 or counter ==1118 or counter ==1119 or counter ==1120
        or counter ==1121 or counter ==1122 or counter ==1123 or counter ==1172 or counter ==1184 or counter ==1085):
        # Moves to the next entry
        pass
    # If it is a form we want
    else:
        # Concatenates the full url
        fullUrl = poke+str(control)
        # Gets the api call
        api = requests.get(fullUrl)
        # converts it to a dictionary
        contents = api.json()

        # Set Dictionary Entry For That Pokemon
        # Identified by national dex number (or another number if it is a different form)
        pokemon[counter] = {}

        hyphenPresent = contents["name"].find("-")
        if(hyphenPresent != -1):
            box = re.compile(r"\w+\-(hisui|alola|galar|paldea|mega|gmax)\.*")
            justDelete = box.search(contents["name"])
            if justDelete != None:
                splitString = contents["name"].split("-")
                newName = splitString[0]
                pokemon[counter]["name"] = newName
            # nidoran♀
            elif counter == 29:
                splitString = contents["name"].split("-")
                newName = splitString[0] + "♀"
                pokemon[counter]["name"] = newName
            # nidoran♂
            elif counter == 32:
                splitString = contents["name"].split("-")
                newName = splitString[0] + "♂"
                pokemon[counter]["name"] = newName
            # mr. mime
            elif counter == 122:
                splitString = contents["name"].split("-")
                newName = splitString[0] + ". " + splitString[1]
                pokemon[counter]["name"] = newName
            # mime jr.
            elif counter == 439:
                splitString = contents["name"].split("-")
                newName = splitString[0] + " " + splitString[1] +"."
                pokemon[counter]["name"] = newName
            # type: null
            elif counter == 772:
                splitString = contents["name"].split("-")
                newName = splitString[0] + ": " + splitString[1]
                pokemon[counter]["name"] = newName
            # mr. rime
            elif counter == 866:
                splitString = contents["name"].split("-")
                newName = splitString[0] + ". " + splitString[1]
                pokemon[counter]["name"] = newName
            # Tapu's, Paradox Pokemon
            elif (counter == 785 or counter == 786 or counter == 787 or counter == 788 or counter == 984 or counter == 985 or 
                counter == 986 or counter == 987 or counter == 988 or counter == 989 or counter == 990 or counter == 991 or counter == 992 or
                counter == 993 or counter == 994 or counter == 995 or counter == 1005 or counter == 1006 or counter == 1009 or counter == 1010 
                or counter == 1020 or counter == 1021 or counter == 1022 or counter == 1023):
                splitString = contents["name"].split("-")
                newName = splitString[0] + " " + splitString[1]
                pokemon[counter]["name"] = newName
            else:
                pokemon[counter]["name"] = contents["name"]
        else:
            # Adds the name
            pokemon[counter]["name"] = contents["name"]

        # Sets up the list for the types
        pokemon[counter]["types"] = list()
    
        # Iterates through the types
        for i in range(0,len(contents["types"])):
            # Adds each type present
            pokemon[counter]["types"].append(contents["types"][i]["type"]["name"])

        # Adds height
        pokemon[counter]["height"] = contents["height"]

        # Adds weight
        pokemon[counter]["weight"] = contents["weight"]

        # Sets up form list
        pokemon[counter]["forms"] = list()

        # Iterates through the forms and adds all of them
        for i in range(0,len(contents["forms"])):
            pokemon[counter]["forms"].append(contents["forms"][i]["name"])

        # Sets up the move list
        pokemon[counter]["moves"] = list()

        # Iterates through the moves and adds all of them
        for i in range(0,len(contents["moves"])):
            pokemon[counter]["moves"].append(contents["moves"][i]["move"]["name"])

        # Sets up the abilities list
        pokemon[counter]["abilities"] = list()

        # Iterates through the abilities and adds them
        for i in range(0,len(contents["abilities"])):
            pokemon[counter]["abilities"] = contents["abilities"][i]["ability"]["name"]

        # If statement only for while we don't have all the categories recorded
        if counter < 173:
            # Adds the category
            pokemon[counter]["category"] = categories[counter]

        # Sets up the gender list for use later
        pokemon[counter]["gender"] = list()

        # Adds a shiny category for using in game later
        pokemon[counter]["shiny"] = [False,True]

    # Prints counter for human to see the program is running
    print(counter)
    # Increments 
    control = control + 1
    counter = counter + 1

# Save the beginning of the call
poke ="https://pokeapi.co/api/v2/gender/"
# Iterates through all the entries in the api
for x in range(1,4):
    # Concotenates the full url
    fullUrl = poke+str(x)
    # Calls API
    api = requests.get(fullUrl)
    # Translate into a dictionary
    contents = api.json()
    # Iterate through all the species listed in the dictionary for that gender
    for i in range(0,len(contents["pokemon_species_details"])):
        # Make an api call to the url listed under that species
        getDexNum = requests.get(contents["pokemon_species_details"][i]["pokemon_species"]["url"])
        # Translate to dictionary
        dex = getDexNum.json()
        # Pull the national dex number from it
        number = dex["pokedex_numbers"][0]["entry_number"]
        # Use that to fill in the gender of the appropriate pokemon
        pokemon[number]["gender"].append(contents["name"])
        # Prints the gender and the entry currently being worked on for the human
        print(str(x) + ": " + str(i))



# Opens or creates the pokemon.json file
with open("pokemon.json","w") as fp:
    # Dumps the dictionary created into the file
    json.dump(pokemon,fp,indent = 4)
# Lets user know the file has been updated
print("Check your folder for the file!")
