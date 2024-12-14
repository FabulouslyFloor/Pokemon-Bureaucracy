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
    144:"Freeze Pokemon",145:"Electric Pokemon",146:"Flame Pokemon",147:"Dragon Pokemon",148:"Dragon Pokemon",149:"Dragon Pokemon",150:"Genetic Pokemon",
    151:"New Species Pokemon",152:"Leaf Pokemon",153:"Leaf Pokemon",154:"Herb Pokemon",155:"Fire Mouse Pokemon",156:"Volcano Pokemon",157:"Volcano Pokemon",
    158:"Big Jaw Pokemon",159:"Big Jaw Pokemon",160:"Big Jaw Pokemon",161:"Scout Pokemon",162:"Long Body Pokemon",163:"Owl Pokemon",164:"Owl Pokemon",
    165:"Five Star Pokemon",166:"Five Star Pokemon",167:"String Spit Pokemon",168:"Long Leg Pokemon",169:"Bat Pokemon",170:"Angler Pokemon",171:"Light Pokemon",
    172:"Tiny Mouse Pokemon",173:"Star Shape Pokemon",174:"Balloon Pokemon",175:"Spike Ball Pokemon",176:"Happiness Pokemon",177:"Tiny Bird Pokemon",178:"Mystic Pokemon",
    179:"Wool Pokemon",180:"Wool Pokemon",181:"Light Pokemon",182:"Flower Pokemon",183:"Aqua Mouse Pokemon",184:"Aqua Rabbit Pokémon",185:"Imitation Pokémon",
    186:"Frog Pokémon",187:"Cottonweed Pokémon",188:"Cottonweed Pokémon",189:"Cottonweed Pokémon",190:"Long Tail Pokémon",191:"Seed Pokémon",192:"Sun Pokémon",
    193:"Clear Wing Pokémon",194:"Water Fish Pokémon",195:"Water Fish Pokémon",196:"Sun Pokémon",197:"Moonlight Pokémon",198:"Darkness Pokémon",199:"Royal Pokémon",
    200:"Hexpert Pokémon",201:"Symbol Pokémon",202:"Patient Pokémon",203:"Long Neck Pokémon",204:"Bagworm Pokémon",205:"Bagworm Pokémon",206:"Land Snake Pokémon",
    207:"Fly Scorpion Pokémon",208:"Iron Snake Pokémon",209:"Fairy Pokémon",210:"Fairy Pokémon",211:"Balloon Pokémon",212:"Pincer Pokémon",213:"Mold Pokémon",
    214:"Single Horn Pokémon",215:"Sharp Claw Pokémon",216:"Little Bear Pokémon",217:"Hibernator Pokémon",218:"Lava Pokémon",219:"Lava Pokémon",220:"Pig Pokémon",
    221:"Swine Pokémon",222:"Coral Pokémon",223:"Jet Pokémon",224:"Jet Pokémon",225:"Delivery Pokémon",226:"Kite Pokémon",227:"Armor Bird Pokémon",228:"Dark Pokémon",
    229:"Dark Pokémon",230:"Dragon Pokémon",231:"Long Nose Pokémon",232:"Armor Pokémon",233:"Virtual Pokémon",234:"Big Horn Pokémon",235:"Painter Pokémon",
    236:"Scuffle Pokémon",237:"Handstand Pokémon",238:"Kiss Pokémon",239:"Electric Pokémon",240:"Live Coal Pokémon",241:"Milk Cow Pokémon",242:"Happiness Pokémon",
    243:"Thunder Pokémon",244:"Volcano Pokémon",245:"Aurora Pokémon",246:"Rock Skin Pokémon",247:"Hard Shell Pokémon",248:"Armor Pokémon",249:"Diving Pokémon",
    250:"Rainbow Pokémon",251:"Time Travel Pokémon",252:"Wood Gecko Pokémon",253:"Wood Gecko Pokémon",254:"Forest Pokémon",255:"Chick Pokémon",256:"Young Fowl Pokémon",
    257:"Blaze Pokémon",258:"Mud Fish Pokémon",259:"Mud Fish Pokémon",260:"Mud Fish Pokémon",261:"Bite Pokémon",262:"Bite Pokémon",263:"Tiny Raccoon Pokémon",
    264:"Rushing Pokémon",265:"Worm Pokémon",266:"Cocoon Pokémon",267:"Butterfly Pokémon",268:"Cocoon Pokémon",269:"Poison Moth Pokémon",270:"Water Weed Pokémon",
    271:"Jolly Pokémon",272:"Carefree Pokémon",273:"Acorn Pokémon",274:"Wily Pokémon",275:"Wicked Pokémon",276:"Tiny Swallow Pokémon",277:"Swallow Pokémon",
    278:"Seagull Pokémon",279:"Water Bird Pokémon",280:"Feeling Pokémon",281:"Emotion Pokémon",282:"Embrace Pokémon",283:"Pond Skater Pokémon",284:"Eyeball Pokémon",
    285:"Mushroom Pokémon",286:"Mushroom Pokémon",287:"Slacker Pokémon",288:"Wild Monkey Pokémon",289:"Lazy Pokémon",290:"Trainee Pokémon",291:"Ninja Pokémon",
    292:"Shed Pokémon",293:"Whisper Pokémon",294:"Big Voice Pokémon",295:"Loud Noise Pokémon",296:"Guts Pokémon",297:"Arm Thrust Pokémon",298:"Polka Dot Pokémon",
    299:"Compass Pokémon",300:"Kitten Pokémon",301:"Prim Pokémon",302:"Darkness Pokémon",303:"Deceiver Pokémon",304:"Iron Armor Pokémon",305:"Iron Armor Pokémon",
    306:"Iron Armor Pokémon",307:"Meditate Pokémon",308:"Meditate Pokémon",309:"Lightning Pokémon",310:"Discharge Pokémon",311:"Cheering Pokémon",312:"Cheering Pokémon",
    313:"Firefly Pokémon",314:"Firefly Pokémon",315:"Thorn Pokémon",316:"Stomach Pokémon",317:"Poison Bag Pokémon",318:"Savage Pokémon",319:"Brutal Pokémon",
    320:"Ball Whale Pokémon",321:"Float Whale Pokémon",322:"Numb Pokémon",323:"Eruption Pokémon",324:"Coal Pokémon",325:"Bounce Pokémon",326:"Manipulate Pokémon",
    327:"Spot Panda Pokémon",328:"Ant Pit Pokémon",329:"Vibration Pokémon",330:"Mystic Pokémon",331:"Cactus Pokémon",332:"Scarecrow Pokémon",333:"Cotton Bird Pokémon",
    334:"Humming Pokémon",335:"Cat Ferret Pokémon",336:"Fang Snake Pokémon",337:"Meteorite Pokémon",338:"Meteorite Pokémon",339:"Whiskers Pokémon",340:"Whiskers Pokémon",
    341:"Ruffian Pokémon",342:"Rogue Pokémon",343:"Clay Doll Pokémon",344:"Clay Doll Pokémon",345:"Sea Lily Pokémon",346:"Barnacle Pokémon",347:"Old Shrimp Pokémon",
    348:"Plate Pokémon",349:"Fish Pokémon",350:"Tender Pokémon",351:"Weather Pokémon",352:"Color Swap Pokémon",353:"Puppet Pokémon",354:"Marionette Pokémon",
    355:"Requiem Pokémon",356:"Beckon Pokémon",357:"Fruit Pokémon",358:"Wind Chime Pokémon",359:"Disaster Pokémon",360:"Bright Pokémon",361:"Snow Hat Pokémon",
    362:"Face Pokémon",363:"Clap Pokémon",364:"Ball Roll Pokémon",365:"Ice Break Pokémon",366:"Bivalve Pokémon",367:"Deep Sea Pokémon",368:"South Sea Pokémon",
    369:"Longevity Pokémon",370:"Rendezvous Pokémon",371:"Rock Head Pokémon",372:"Endurance Pokémon",373:"Dragon Pokémon",374:"Iron Ball Pokémon",375:"Iron Claw Pokémon",
    376:"Iron Leg Pokémon",377:"Rock Peak Pokémon",378:"Iceberg Pokémon",379:"Iron Pokémon",380:"Eon Pokémon",381:"Eon Pokémon",382:"Sea Basin Pokémon",
    383:"Continent Pokémon",384:"Sky High Pokémon",385:"Wish Pokémon",386:"DNA Pokémon",387:"Tiny Leaf Pokémon",388:"Grove Pokémon",389:"Continent Pokémon",
    390:"Chimp Pokémon",391:"Playful Pokémon",392:"Flame Pokémon",393:"Penguin Pokémon",394:"Penguin Pokémon",395:"Emperor Pokémon 	",396:"Starling Pokémon",
    397:"Starling Pokémon",398:"Predator Pokémon",399:"Plump Mouse Pokémon",400:"Beaver Pokémon",401:"Cricket Pokémon",402:"Cricket Pokémon",403:"Flash Pokémon",
    404:"Spark Pokémon",405:"Gleam Eyes Pokémon",406:"Bud Pokémon",407:"Bouquet Pokémon",408:"Head Butt Pokémon",409:"Head Butt Pokémon",410:"Shield Pokémon",
    411:"Shield Pokémon",412:"Bagworm Pokémon",413:"Bagworm Pokémon",414:"Moth Pokémon",415:"Tiny Bee Pokémon",416:"Beehive Pokémon",417:"EleSquirrel Pokémon",
    418:"Sea Weasel Pokémon",419:"Sea Weasel Pokémon",420:"Cherry Pokémon",421:"Blossom Pokémon",422:"Sea Slug Pokémon",423:"Sea Slug Pokémon",
    424:"Long Tail Pokémon",425:"Balloon Pokémon",426:"Blimp Pokémon",427:"Rabbit Pokémon",428:"Rabbit Pokémon",429:"Magical Pokémon",430:"Big Boss Pokémon",
    431:"Catty Pokémon",432:"Tiger Cat Pokémon",433:"Bell Pokémon",434:"Skunk Pokémon",435:"Skunk Pokémon",436:"Bronze Pokémon",437:"Bronze Bell Pokémon",
    438:"Bonsai Pokémon",439:"Mime Pokémon",440:"Playhouse Pokémon",441:"Music Note Pokémon",442:"Forbidden Pokémon",443:"Land Shark Pokémon",444:"Cave Pokémon",
    445:"Mach Pokémon",446:"Big Eater Pokémon",447:"Emanation Pokémon",448:"Aura Pokémon",449:"Hippo Pokémon",450:"Heavyweight Pokémon",451:"Scorpion Pokémon",
    452:"Ogre Scorpion Pokémon",453:"Toxic Mouth Pokémon",454:"Toxic Mouth Pokémon",455:"Bug Catcher Pokémon",456:"Wing Fish Pokémon",457:"Neon Pokémon",
    458:"Kite Pokémon",459:"Frost Tree Pokémon",460:"Frost Tree Pokémon",461:"Sharp Claw Pokémon",462:"Magnet Area Pokémon",463:"Licking Pokémon",464:"Drill Pokémon",
    465:"Vine Pokémon",466:"Thunderbolt Pokémon",467:"Blast Pokémon",468:"Jubilee Pokémon",469:"Ogre Darner Pokémon",470:"Verdant Pokémon",471:"Fresh Snow Pokémon",
    472:"Fang Scorpion Pokémon",473:"Twin Tusk Pokémon",474:"Virtual Pokémon",475:"Blade Pokémon",476:"Compass Pokémon",477:"Gripper Pokémon",478:"Snow Land Pokémon",
    479:"Plasma Pokémon",480:"Knowledge Pokémon",481:"Emotion Pokémon",482:"Willpower Pokémon",483:"Temporal Pokémon",484:"Spatial Pokémon",485:"Lava Dome Pokémon",
    486:"Colossal Pokémon",487:"Renegade Pokémon",488:"Lunar Pokémon",489:"Sea Drifter Pokémon",490:"Seafaring Pokémon",491:"Pitch-Black Pokémon",492:"Gratitude Pokémon",
    493:"Alpha Pokémon",494:"Victory Pokémon",495:"Grass Snake Pokémon",496:"Grass Snake Pokémon",497:"Regal Pokémon",498:"Fire Pig Pokémon",499:"Fire Pig Pokémon",
    500:"Mega Fire Pig Pokémon",501:"Sea Otter Pokémon",502:"Discipline Pokémon",503:"Formidable Pokémon",504:"Scout Pokémon",505:"Lookout Pokémon",506:"Puppy Pokémon",
    507:"Loyal Dog Pokémon",508:"Big-Hearted Pokémon",509:"Devious Pokémon",510:"Cruel Pokémon",511:"Grass Monkey Pokémon",512:"Thorn Monkey Pokémon",513:"High Temp Pokémon",
    514:"Ember Pokémon",515:"Spray Pokémon",516:"Geyser Pokémon",517:"Dream Eater Pokémon",518:"Drowsing Pokémon",519:"Tiny Pigeon Pokémon",520:"Wild Pigeon Pokémon",
    521:"Proud Pokémon",522:"Electrified Pokémon",523:"Thunderbolt Pokémon",524:"Mantle Pokémon",525:"Ore Pokémon",526:"Compressed Pokémon",527:"Bat Pokémon",
    528:"Courting Pokémon",529:"Mole Pokémon",530:"Subterrene Pokémon",531:"Hearing Pokémon",532:"Muscular Pokémon",533:"Muscular Pokémon",534:"Muscular Pokémon",
    535:"Tadpole Pokémon",536:"Vibration Pokémon",537:"Vibration Pokémon",538:"Judo Pokémon",539:"Karate Pokémon",540:"Sewing Pokémon",541:"Leaf-Wrapped Pokémon",
    542:"Nurturing Pokémon",543:"Centipede Pokémon",544:"Curlipede Pokémon",545:"Megapede Pokémon",546:"Cotton Puff Pokémon",547:"Windveiled Pokémon",548:"Bulb Pokémon",
    549:"Flowering Pokémon",550:"Hostile Pokémon",551:"Desert Croc Pokémon",552:"Desert Croc Pokémon",553:"Intimidation Pokémon",554:"Zen Charm Pokémon",
    555:"Blazing Pokémon",556:"Cactus Pokémon",557:"Rock Inn Pokémon",558:"Stone Home Pokémon",559:"Shedding Pokémon",560:"Hoodlum Pokémon",561:"Avianoid Pokémon",
    562:"Spirit Pokémon",563:"Coffin Pokémon",564:"Prototurtle Pokémon",565:"Prototurtle Pokémon",566:"First Bird Pokémon",567:"First Bird Pokémon",568:"Trash Bag Pokémon",
    569:"Trash Heap Pokémon",570:"Tricky Fox Pokémon",571:"Illusion Fox Pokémon",572:"Chinchilla Pokémon",573:"Scarf Pokémon",574:"Fixation Pokémon",
    575:"Manipulate Pokémon",576:"Astral Body Pokémon",577:"Cell Pokémon",578:"Mitosis Pokémon",579:"Multiplying Pokémon",580:"Water Bird Pokémon",
    581:"White Bird Pokémon",582:"Fresh Snow Pokémon",583:"Icy Snow Pokémon",584:"Snowstorm Pokémon",585:"Season Pokémon",586:"Season Pokémon",587:"Sky Squirrel Pokémon",
    588:"Clamping Pokémon",589:"Cavalry Pokémon",590:"Mushroom Pokémon",591:"Mushroom Pokémon",592:"Floating Pokémon",593:"Floating Pokémon",594:"Caring Pokémon",
    595:"Attaching Pokémon",596:"EleSpider Pokémon",597:"Thorn Seed Pokémon",598:"Thorn Pod Pokémon",599:"Gear Pokémon",600:"Gear Pokémon",601:"Gear Pokémon",
    602:"EleFish Pokémon",603:"EleFish Pokémon",604:"EleFish Pokémon",605:"Cerebral Pokémon",606:"Cerebral Pokémon",607:"Candle Pokémon",608:"Lamp Pokémon",609:"Luring Pokémon",
    610:"Tusk Pokémon",611:"Axe Jaw Pokémon",612:"Axe Jaw Pokémon",613:"Chill Pokémon",614:"Freezing Pokémon",615:"Crystallizing Pokémon",616:"Snail Pokémon",
    617:"Shell Out Pokémon",618:"Trap Pokémon",619:"Martial Arts Pokémon",620:"Martial Arts Pokémon",621:"Cave Pokémon",622:"Automaton Pokémon",623:"Automaton Pokémon",
    624:"Sharp Blade Pokémon",625:"Sword Blade Pokémon",626:"Bash Buffalo Pokémon",627:"Eaglet Pokémon",628:"Valiant Pokémon",629:"Diapered Pokémon",630:"Bone Vulture Pokémon",
    631:"Anteater Pokémon",632:"Iron Ant Pokémon",633:"Irate Pokémon",634:"Hostile Pokémon",635:"Brutal Pokémon",636:"Torch Pokémon",637:"Sun Pokémon",638:"Iron Will Pokémon",
    639:"Cavern Pokémon",640:"Grassland Pokémon",641:"Cyclone Pokémon",642:"Bolt Strike Pokémon",643:"Vast White Pokémon",644:"Deep Black Pokémon",645:"Abundance Pokémon",
    646:"Boundary Pokémon",647:"Colt Pokémon",648:"Melody Pokémon",649:"Paleozoic Pokémon",650:"Spiny Nut Pokémon",651:"Spiny Armor Pokémon",652:"Spiny Armor Pokémon",
    653:"Fox Pokémon",654:"Fox Pokémon",655:"Fox Pokémon",656:"Bubble Frog Pokémon",657:"Bubble Frog Pokémon",658:"Ninja Pokémon",659:"Digging Pokémon",660:"Digging Pokémon",
    661:"Tiny Robin Pokémon",662:"Ember Pokémon",663:"Scorching Pokémon",664:"Scatterdust Pokémon",665:"Scatterdust Pokémon",666:"Scale Pokémon",667:"Lion Cub Pokémon",
    668:"Royal Pokémon",669:"Single Bloom Pokémon",670:"Single Bloom Pokémon",671:"Garden Pokémon",672:"Mount Pokémon",673:"Mount Pokémon",674:"Playful Pokémon",
    675:"Daunting Pokémon",676:"Poodle Pokémon",677:"Restraint Pokémon",678:"Constraint Pokémon",679:"Sword Pokémon",680:"Sword Pokémon",681:"Royal Sword Pokémon",
    682:"Perfume Pokémon",683:"Fragrance Pokémon",684:"Cotton Candy Pokémon",685:"Meringue Pokémon",686:"Revolving Pokémon",687:"Overturning Pokémon",688:"Two-Handed Pokémon",
    689:"Collective Pokémon",690:"Mock Kelp Pokémon",691:"Mock Kelp Pokémon",692:"Water Gun Pokémon",693:"Howitzer Pokémon",694:"Generator Pokémon",695:"Generator Pokémon",
    696:"Royal Heir Pokémon",697:"Despot Pokémon",698:"Tundra Pokémon",699:"Tundra Pokémon",700:"Intertwining Pokémon",701:"Wrestling Pokémon",702:"Antenna Pokémon",
    703:"Jewel Pokémon",704:"Soft Tissue Pokémon",705:"Soft Tissue Pokémon",706:"Dragon Pokémon",707:"Key Ring Pokémon",708:"Stump Pokémon",709:"Elder Tree Pokémon",
    710:"Pumpkin Pokémon",711:"Pumpkin Pokémon",712:"Ice Chunk Pokémon",713:"Iceberg Pokémon",714:"Sound Wave Pokémon",715:"Sound Wave Pokémon",716:"Life Pokémon",
    717:"Destruction Pokémon",718:"Order Pokémon",719:"Jewel Pokémon",720:"Mischief Pokémon",721:"Steam Pokémon",722:"Grass Quill Pokémon",723:"Blade Quill Pokémon",
    724:"Arrow Quill Pokémon",725:"Fire Cat Pokémon",726:"Fire Cat Pokémon",727:"Heel Pokémon",728:"Sea Lion Pokémon",729:"Pop Star Pokémon",730:"Soloist Pokémon",
    731:"Woodpecker Pokémon",732:"Bugle Beak Pokémon",733:"Cannon Pokémon",734:"Loitering Pokémon",735:"Stakeout Pokémon",736:"Larva Pokémon",737:"Battery Pokémon",
    738:"Stag Beetle Pokémon",739:"Boxing Pokémon",740:"Woolly Crab Pokémon",741:"Dancing Pokémon",742:"Bee Fly Pokémon",743:"Bee Fly Pokémon",744:"Puppy Pokémon",
    745:"Wolf Pokémon",746:"Small Fry Pokémon",747:"Brutal Star Pokémon",748:"Brutal Star Pokémon",749:"Donkey Pokémon",750:"Draft Horse Pokémon",751:"Water Bubble Pokémon",
    752:"Water Bubble Pokémon",753:"Sickle Grass Pokémon",754:"Bloom Sickle Pokémon",755:"Illuminating Pokémon",756:"Illuminating Pokémon",757:"Toxic Lizard Pokémon",
    758:"Toxic Lizard Pokémon",759:"Flailing Pokémon",760:"Strong Arm Pokémon",761:"Fruit Pokémon",762:"Fruit Pokémon",763:"Fruit Pokémon",764:"Posy Picker Pokémon",
    765:"Sage Pokémon",766:"Teamwork Pokémon",767:"Turn Tail Pokémon",768:"Hard Scale Pokémon",769:"Sand Heap Pokémon",770:"Sand Castle Pokémon",771:"Sea Cucumber Pokémon",
    772:"Synthetic Pokémon",773:"Synthetic Pokémon",774:"Meteor Pokémon",775:"Drowsing Pokémon",776:"Blast Turtle Pokémon",777:"Roly-Poly Pokémon",778:"Disguise Pokémon",
    779:"Gnash Teeth Pokémon",780:"Placid Pokémon",781:"Sea Creeper Pokémon",782:"Scaly Pokémon",783:"Scaly Pokémon",784:"Scaly Pokémon",785:" 	Land Spirit Pokémon",
    786:"Land Spirit Pokémon",787:"Land Spirit Pokémon",788:"Land Spirit Pokémon",789:"Nebula Pokémon",790:"Protostar Pokémon",791:"Sunne Pokémon",792:"Moone Pokémon",
    793:"Parasite Pokémon",794:"Swollen Pokémon",795:"Lissome Pokémon",796:"Glowing Pokémon",797:"Launch Pokémon",798:"Drawn Sword Pokémon",799:"Junkivore Pokémon",
    800:"Prism Pokémon",801:"Artificial Pokémon",802:"Gloomdweller Pokémon",803:"Poison Pin Pokémon",804:"Poison Pin Pokémon",805:"Rampart Pokémon",806:"Fireworks Pokémon",
    807:"Thunderclap Pokémon",808:"Hex Nut Pokémon",809:"Hex Nut Pokémon",810:"Chimp Pokémon",811:"Beat Pokémon",812:"Drummer Pokémon",813:"Rabbit Pokémon",814:"Rabbit Pokémon",
    815:"Striker Pokémon",816:"Water Lizard Pokémon",817:"Water Lizard Pokémon",818:"Secret Agent Pokémon",819:"Cheeky Pokémon",820:"Greedy Pokémon",821:"Tiny Bird Pokémon",
    822:"Raven Pokémon",823:"Raven Pokémon",824:"Larva Pokémon",825:"Radome Pokémon",826:"Seven Spot Pokémon",827:"Fox Pokémon",828:"Fox Pokémon",829:"Flowering Pokémon",
    830:"Cotton Bloom Pokémon",831:"Sheep Pokémon",832:"Sheep Pokémon",833:"Snapping Pokémon",834:"Bite Pokémon",835:"Puppy Pokémon",836:"Dog Pokémon",837:"Coal Pokémon",
    838:"Coal Pokémon",839:"Coal Pokémon",840:"Apple Core Pokémon",841:"Apple Wing Pokémon",842:"Apple Nectar Pokémon",843:"Sand Snake Pokémon",844:"Sand Snake Pokémon",
    845:"Gulp Pokémon",846:"Rush Pokémon",847:"Skewer Pokémon",848:"Baby Pokémon",849:"Punk Pokémon",850:"Radiator Pokémon",851:"Radiator Pokémon",852:"Tantrum Pokémon",
    853:"Jujitsu Pokémon",854:"Black Tea Pokémon",855:"Black Tea Pokémon",856:"Calm Pokémon",857:"Serene Pokémon",858:"Silent Pokémon",859:"Wily Pokémon",860:"Devious Pokémon",
    861:"Bulk Up Pokémon",862:"Blocking Pokémon",863:"Viking Pokémon",864:"Coral Pokémon",865:"Wild Duck Pokémon",866:"Comedian Pokémon",867:"Grudge Pokémon",
    868:"Cream Pokémon",869:"Cream Pokémon",870:"Formation Pokémon",871:"Sea Urchin Pokémon",872:"Worm Pokémon",873:"Frost Moth Pokémon",874:"Big Rock Pokémon",
    875:"Penguin Pokémon",876:"Emotion Pokémon",877:"Two-Sided Pokémon",878:"Copperderm Pokémon",879:"Copperderm Pokémon",880:"Fossil Pokémon",881:"Fossil Pokémon",
    882:"Fossil Pokémon",883:"Fossil Pokémon",884:"Alloy Pokémon",885:"Lingering Pokémon",886:"Caretaker Pokémon",887:"Stealth Pokémon",888:"Warrior Pokémon",
    889:"Warrior Pokémon",890:"Gigantic Pokémon",891:"Wushu Pokémon",892:"Wushu Pokémon",893:"Rogue Monkey Pokémon",894:"Electron Pokémon",895:"Dragon Orb Pokémon",
    896:"Wild Horse Pokémon",897:"Swift Horse Pokémon",898:"King Pokémon",899:"Big Horn Pokémon",900:"Axe Pokémon",901:"Peat Pokémon",902:"Big Fish Pokémon",
    903:"Free Climb Pokémon",904:"Pin Cluster Pokémon",905:"Love-Hate Pokémon",906:"Grass Cat Pokémon",907:"Grass Cat Pokémon",908:"Magician Pokémon",
    909:"Fire Croc Pokémon",910:"Fire Croc Pokémon",911:"Singer Pokémon",912:"Duckling Pokémon",913:"Practicing Pokémon",914:"Dancer Pokémon",915:"Hog Pokémon",
    916:"Hog Pokémon",917:"String Ball Pokémon",918:"Trap Pokémon",919:"Grasshopper Pokémon",920:"Grasshopper Pokémon",921:"Mouse Pokémon",922:"Mouse Pokémon",
    923:"Hands-On Pokémon",924:"Couple Pokémon",925:"Family Pokémon",926:"Puppy Pokémon",927:"Dog Pokémon",928:"Olive Pokémon",929:"Olive Pokémon",930:"Olive Pokémon",
    931:"Parrot Pokémon",932:"Rock Salt Pokémon",933:"Rock Salt Pokémon",934:"Rock Salt Pokémon",935:"Fire Child Pokémon",936:"Fire Warrior Pokémon",937:"Fire Blades Pokémon",
    938:"EleTadpole Pokémon",939:"EleFrog Pokémon",940:"Storm Petrel Pokémon",941:"Frigatebird Pokémon",942:"Rascal Pokémon",943:"Boss Pokémon",944:"Toxic Mouse Pokémon",
    945:"Toxic Monkey Pokémon",946:"Tumbleweed Pokémon",947:"Tumbleweed Pokémon",948:"Woodear Pokémon",949:"Woodear Pokémon",950:"Ambush Pokémon",951:"Spicy Pepper Pokémon",
    952:"Spicy Pepper Pokémon",953:"Rolling Pokémon",954:"Rolling Pokémon",955:"Frill Pokémon",956:"Ostrich Pokémon",957:"Metalsmith Pokémon",958:"Hammer Pokémon",
    959:"Hammer Pokémon",960:"Garden Eel Pokémon",961:"Garden Eel Pokémon",962:"Item Drop Pokémon",963:"Dolphin Pokémon",964:"Dolphin Pokémon",965:"Single-Cyl Pokémon",
    966:"Multi-Cyl Pokémon",967:"Mount Pokémon",968:"Earthworm Pokémon",969:"Ore Pokémon",970:"Ore Pokémon",971:"Ghost Dog Pokémon",972:"Ghost Dog Pokémon",
    973:"Synchronize Pokémon",974:"Terra Whale Pokémon",975:"Terra Whale Pokémon",976:"Jettison Pokémon",977:"Big Catfish Pokémon",978:"Mimicry Pokémon",979:"Rage Monkey Pokémon",
    980:"Spiny Fish Pokémon",981:"Long Neck Pokémon",982:"Land Snake Pokémon",983:"Big Blade Pokémon",984:"Paradox Pokémon",985:"Paradox Pokémon",986:"Paradox Pokémon",
    987:"Paradox Pokémon",988:"Paradox Pokémon",989:"Paradox Pokémon",990:"Paradox Pokémon",991:"Paradox Pokémon",992:"Paradox Pokémon",993:"Paradox Pokémon",
    994:"Paradox Pokémon",995:"Paradox Pokémon",996:"Ice Fin Pokémon",997:"Ice Fin Pokémon",998:"Ice Dragon Pokémon",999:"Coin Chest Pokémon",1000:"Coin Entity Pokémon",
    1001:"Ruinous Pokémon",1002:"Ruinous Pokémon",1003:"Ruinous Pokémon",1004:"Ruinous Pokémon",1005:"Paradox Pokémon",1006:"Paradox Pokémon",1007:"Paradox Pokémon",
    1008:"Paradox Pokémon",1009:"Paradox Pokémon",1010:"Paradox Pokémon",1011:"Candy Apple Pokémon",1012:"Matcha Pokémon",1013:"Matcha Pokémon",1014:"Retainer Pokémon",
    1015:"Retainer Pokémon",1016:"Retainer Pokémon",1017:"Mask Pokémon",1018:"Alloy Pokémon",1019:"Apple Hydra Pokémon",1020:"Paradox Pokémon",1021:"Paradox Pokémon",
    1022:"Paradox Pokémon",1023:"Paradox Pokémon",1024:"Tera Pokémon",1025:"Subjugation Pokémon",
            }
# Categories for alternate forms who don't have their own national dex number
Otherforms = { "Hisuan Growlithe":"Scout Pokemon", "Galarian Ponyta":"Unique Horn Pokemon","Galarian Rapidash":"Unique Horn Pokemon","Hisuian Voltorb":"Sphere Pokemon",
    "Hisuian ELectrode":"Sphere Pokemon","Galarian Articuno":"Cruel Pokemon","Hisuian Typhlosion":"Ghost Flame Pokemon","Paldean Wooper":"Poison Fish Pokemon",
    "Galarian Slowking":"Hexpert Pokémon","Hisuian Liligant":"Spinning Pokémon","White-Striped Basculin":"Mellow Pokémon","Galarian Darmanitan":"Zen Charm Pokémon",
    "Galarian Zen Form Darmanitan":"Blazing Pokémon","Hisuian Zorua":"Spiteful Fox Pokémon","Hisuian Zoroark":"Baneful Fox Pokémon","Hisuian Braviary":"Battle Cry Pokémon",
    "Hisuian Sliggoo":"Snail Pokémon","Hisuian Goodra":"Shell Bunker Pokémon","Hoopa Unbound":"Djinn Pokémon","Calyrex Ice Rider":"High King Pokémon","Calyrex Shadow Rider":"High King Pokémon",
    "Hero Form Palafin":"Hero Pokémon","Roaming Gimmighoul":"Coin Hunter Pokémon",
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
    # Checks if we have reached call 1025. Changes the number to reflect the address change in the rest of them
    if control == 1025:
        control = 10001

    # These entries are for pokemon forms we don't need in game, like all the unique pikachu-in-hat's
    if (counter == 1140 or counter == 1141 or counter == 1141 or counter ==1142 or counter == 1143 or counter ==1145 
        or counter == 1146 or counter == 1117 or counter == 1152 or counter == 1153 or counter == 1168 or counter == 1169 
        or counter == 1170 or counter == 1173 or counter == 1174 or counter == 1175 or counter == 1177 or counter == 1178 
        or counter == 1182 or counter ==1183 or counter == 1216 or counter == 1288 or counter == 1289 or counter == 1290 
        or counter == 1291 or counter == 1292 or counter == 1293 or counter == 1294 or counter == 1295 or counter == 1104 
        or counter == 1105 or counter ==1106 or counter ==1107 or counter ==1108 or counter ==1109 or counter ==1118 
        or counter ==1119 or counter ==1120 or counter ==1121 or counter ==1122 or counter ==1123 or counter ==1172 
        or counter ==1184 or counter ==1085):
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
            pokemon[counter]["abilities"].append(contents["abilities"][i]["ability"]["name"])

        # If statement only for while we don't have all the categories recorded
        if counter < 1026:
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
