'''
This file contains the raw data for the contents of each bin
and the instantiation of that data into Parts
'''
from Part import Part

# TODO: classify alike parts into categories to limit
# combinations to unique stat sets

RACERS = [
    Part("Mario"            ,6,2,4,2,2,6,6,6,6,4,4,4,4),
    Part("Luigi"            ,6,2,5,1,2,6,6,6,6,5,5,5,5),
    Part("Peach"            ,4,3,3,3,3,5,5,5,5,5,5,5,5),
    Part("Daisy"            ,4,3,3,3,3,5,5,5,5,5,5,5,5),
    Part("Yoshi"            ,4,3,3,3,3,5,5,5,5,5,5,5,5),
    Part("Toad"             ,3,4,3,4,3,3,3,3,3,7,7,7,7),
    Part("Toadette"         ,2,5,4,2,4,2,2,2,2,7,7,7,7),
    Part("Koopa Troopa"     ,2,4,1,5,4,2,2,2,2,8,8,8,8),
    Part("Bowser"           ,10,0,6,0,0,10,10,10,10,0,0,0,0),
    Part("Donkey Kong"      ,8,1,10,0,1,9,9,9,9,2,2,2,2),
    Part("Wario"            ,9,0,5,1,0,10,10,10,10,1,1,1,1),
    Part("Waluigi"          ,8,1,10,0,1,9,9,9,9,2,2,2,2),
    Part("Rosalina"         ,7,1,9,3,2,7,7,7,7,3,3,3,3),
    Part("Metal Mario"      ,10,1,8,1,1,8,8,8,8,3,3,3,3),
    Part("Pink Gold Peach"  ,10,1,8,1,1,8,8,8,8,3,3,3,3),
    Part("Lakitu"           ,2,4,1,5,4,2,2,2,2,8,8,8,8),
    Part("Shy Guy"          ,3,4,3,4,3,3,3,3,3,7,7,7,7),
    Part("Baby Mario"       ,1,5,2,4,4,1,1,1,1,8,8,8,8),
    Part("Baby Luigi"       ,1,5,2,4,4,1,1,1,1,8,8,8,8),
    Part("Baby Peach"       ,0,4,3,5,5,0,0,0,0,10,10,10,10),
    Part("Baby Daisy"       ,0,4,3,5,5,0,0,0,0,10,10,10,10),
    Part("Baby Rosalina"    ,0,5,4,3,5,0,0,0,0,9,9,9,9),
    Part("Larry"            ,3,4,3,4,3,3,3,3,3,7,7,7,7),
    Part("Lemmy"            ,0,5,4,3,5,0,0,0,0,9,9,9,9),
    Part("Wendy"            ,2,5,4,2,4,2,2,2,2,7,7,7,7),
    Part("Ludwig"           ,6,2,4,2,2,6,6,6,6,4,4,4,4),
    Part("Iggy"             ,6,2,5,1,2,6,6,6,6,5,5,5,5),
    Part("Roy"              ,8,1,10,0,1,9,9,9,9,2,2,2,2),
    Part("Morton"           ,10,0,6,0,0,10,10,10,10,0,0,0,0),
    Part("Mii (medium)"     ,6,2,4,2,2,6,6,6,6,4,4,4,4),
    Part("Tanooki Mario"    ,5,3,7,1,3,5,5,5,5,5,5,5,5),
    Part("Link"             ,7,1,9,3,2,7,7,7,7,3,3,3,3),
    Part("Villager (male)"  ,5,3,7,1,3,5,5,5,5,5,5,5,5),
    Part("Isabelle"         ,2,5,4,2,4,2,2,2,2,7,7,7,7),
    Part("Cat Peach"        ,3,4,2,3,3,4,4,4,4,6,6,6,6),
    Part("Dry Bowser"       ,9,0,5,1,0,10,10,10,10,1,1,1,1),
    Part("Villager (female)",3,4,2,3,3,4,4,4,4,6,6,6,6),
    Part("Gold Mario"       ,10,1,8,1,1,8,8,8,8,3,3,3,3),
    Part("Dry Bones"        ,1,5,2,4,4,1,1,1,1,8,8,8,8),
    Part("Bowser Jr."       ,2,4,1,5,4,2,2,2,2,8,8,8,8),
    Part("King Boo"         ,7,1,9,3,2,7,7,7,7,3,3,3,3),
    Part("Inkling Girl"     ,3,4,2,3,3,4,4,4,4,6,6,6,6),
    Part("Inkling Boy"      ,5,3,7,1,3,5,5,5,5,5,5,5,5)
]

KARTS = [
    Part("Standard Kart"    ,2,4,3,3,4,3,3,3,3,3,2,3,3),
    Part("Pipe Frame"       ,1,6,3,4,6,1,3,1,1,5,4,4,2),
    Part("Mach 8"           ,3,3,2,4,4,3,3,5,4,2,2,4,2),
    Part("Steel Driver"     ,4,1,1,3,2,4,5,2,0,1,5,1,1),
    Part("Cat Cruiser"      ,2,5,4,3,5,2,2,3,4,4,2,3,4),
    Part("Circuit Special"  ,3,1,3,1,1,5,1,4,2,1,1,2,0),
    Part("Tri-Speeder"      ,4,1,1,3,2,4,5,2,0,1,5,1,1),
    Part("Badwagon"         ,4,0,2,5,0,5,2,3,1,0,1,1,0),
    Part("Prancer"          ,1,2,1,2,3,4,3,3,3,3,3,2,3),
    Part("Biddybuggy"       ,0,7,1,4,7,0,1,2,1,5,4,5,4),
    Part("Landship"         ,0,6,0,6,6,1,5,0,2,4,5,2,3),
    Part("Sneeker"          ,2,2,1,0,3,4,2,3,3,3,2,3,2),
    Part("Sports Coupe"     ,3,3,2,4,4,3,3,5,4,2,2,4,2),
    Part("Gold Standard"    ,2,2,1,0,3,4,2,3,3,3,2,3,2),
    Part("Standard Bike"    ,1,5,3,5,5,2,2,4,3,4,3,4,3),
    Part("Comet"            ,2,5,4,3,5,2,2,3,4,4,2,3,4),
    Part("Sport Bike"       ,1,2,1,2,3,4,3,3,3,3,3,2,3),
    Part("The Duke"         ,2,4,3,3,4,3,3,3,3,3,2,3,3),
    Part("Flame Rider"      ,1,5,3,5,5,2,2,4,3,4,3,4,3),
    Part("Varmint"          ,1,6,3,4,6,1,3,1,1,5,4,4,2),
    Part("Mr Scooty"        ,0,7,1,4,7,0,1,2,1,5,4,5,4),
    Part("Jet Bike"         ,1,2,1,2,3,4,3,3,3,3,3,2,3),
    Part("Yoshi Bike"       ,2,5,4,3,5,2,2,3,4,4,2,3,4),
    Part("Standard ATV"     ,4,0,2,5,0,5,2,3,1,0,1,1,0),
    Part("Wild Wiggler"     ,1,5,3,5,5,2,2,4,3,4,3,4,3),
    Part("Teddy Buggy"      ,2,5,4,3,5,2,2,3,4,4,2,3,4),
    Part("GLA"              ,4,0,2,5,0,5,2,3,1,0,1,1,0),
    Part("W 25 Silver Arrow",1,5,3,5,5,2,2,4,3,4,3,4,3),
    Part("300 SL Roadster"  ,2,4,3,3,4,3,3,3,3,3,2,3,3),
    Part("Blue Falcon"      ,0,3,1,3,3,4,2,4,3,2,3,5,1),
    Part("Tanooki Kart"     ,3,2,4,7,3,2,4,3,3,4,4,3,3),
    Part("B Dasher"         ,3,1,3,1,1,5,1,4,2,1,1,2,0),
    Part("Master Cycle"     ,2,2,1,0,3,4,2,3,3,3,2,3,2),
    Part("Streetle"         ,0,6,0,6,6,1,5,0,2,4,5,2,3),
    Part("P-Wing"           ,3,1,3,1,1,5,1,4,2,1,1,2,0),
    Part("City Tripper"     ,1,6,3,4,6,1,3,1,1,5,4,4,2),
    Part("Bone Rattler"     ,4,1,1,3,2,4,5,2,0,1,5,1,1),
    Part("Koopa Clown"      ,3,2,4,7,3,2,4,3,3,4,4,3,3),
    Part("Splat Buggy"      ,0,3,1,3,3,4,2,4,3,2,3,5,1),
    Part("Inkstriker"       ,3,3,2,4,4,3,3,5,4,2,2,4,2)
]

WHEELS = [
    Part("Standard"      ,2,4,2,5,3,2,3,2,3,3,3,3,3),
    Part("Monster"       ,4,2,3,7,2,2,2,2,1,0,1,0,1),
    Part("Roller"        ,0,6,0,4,6,0,3,0,3,4,4,4,4),
    Part("Slim"          ,2,2,4,1,2,3,2,4,2,4,4,3,4),
    Part("Slick"         ,3,1,4,0,0,4,0,4,0,2,0,2,1),
    Part("Metal"         ,4,0,1,2,0,4,3,1,2,2,2,1,0),
    Part("Button"        ,0,5,1,3,5,1,2,2,2,3,3,4,2),
    Part("Off-Road"      ,3,3,3,6,1,3,4,2,1,1,1,2,2),
    Part("Sponge"        ,1,4,2,6,4,1,1,1,4,2,1,2,3),
    Part("Wood"          ,2,2,4,1,2,3,2,4,2,4,4,3,4),
    Part("Cushion"       ,1,4,2,6,4,1,1,1,4,2,1,2,3),
    Part("Blue Standard" ,2,4,2,5,3,2,3,2,3,3,3,3,3),
    Part("Hot Monster"   ,4,2,3,7,2,2,2,2,1,0,1,0,1),
    Part("Azure Roller"  ,0,6,0,4,6,0,3,0,3,4,4,4,4),
    Part("Crimson Slim"  ,2,2,4,1,2,3,2,4,2,4,4,3,4),
    Part("Cyber Slick"   ,3,1,4,0,0,4,0,4,0,2,0,2,1),
    Part("Retro Off-Road",3,3,3,6,1,3,4,2,1,1,1,2,2),
    Part("Gold Tires"    ,4,0,1,2,0,4,3,1,2,2,2,1,0),
    Part("GLA Tires"     ,2,4,2,5,3,2,3,2,3,3,3,3,3),
    Part("Triforce Tires",3,3,3,6,1,3,4,2,1,1,1,2,2),
    Part("Leaf Tires"    ,0,5,1,3,5,1,2,2,2,3,3,4,2)
]

GLIDERS = [
    Part("Super Glider" ,1,1,1,1,1,1,1,0,2,1,0,1,1),
    Part("Cloud Glider" ,0,2,1,1,2,0,1,1,1,1,0,1,2),
    Part("Wario Wing"   ,2,1,2,0,1,1,0,1,2,1,1,0,1),
    Part("Waddle Wing"  ,1,1,1,1,1,1,1,0,2,1,0,1,1),
    Part("Peach Parasol",1,2,2,0,2,0,0,1,1,1,1,0,2),
    Part("Parachute"    ,0,2,1,1,2,0,1,1,1,1,0,1,2),
    Part("Parafoil"     ,1,2,2,0,2,0,0,1,1,1,1,0,2),
    Part("Flower Glider",0,2,1,1,2,0,1,1,1,1,0,1,2),
    Part("Bowser Kite"  ,1,2,2,0,2,0,0,1,1,1,1,0,2),
    Part("Plane Glider" ,2,1,2,0,1,1,0,1,2,1,1,0,1),
    Part("MKTV Parafoil",1,2,2,0,2,0,0,1,1,1,1,0,2),
    Part("Gold Glider"  ,2,1,2,0,1,1,0,1,2,1,1,0,1),
    Part("Hylian Kite"  ,1,1,1,1,1,1,1,0,2,1,0,1,1),
    Part("Paper Glider" ,0,2,1,1,2,0,1,1,1,1,0,1,2)
]
