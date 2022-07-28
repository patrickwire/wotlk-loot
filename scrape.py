import requests
import re
import json

dungensHtml=requests.get("https://wotlk.evowow.com/?zones=2.2").text
dungeonList=(re.findall("new Listview[(](.*)[)]",dungensHtml))[0].replace("LANG.tab_zones","1")

data=[]
dungeons=json.loads(dungeonList)
print(dungeons["data"])
for dungeon in dungeons["data"]: 
    print("##"+dungeon["name"])
    NPCHtml=requests.get("https://wotlk.evowow.com/?zone="+str(dungeon["id"])).text
    NPCList=re.findall("new Listview[(](.*)[)]",NPCHtml)[0].split('}],"name"')[0]+"}]}"
    npcs=json.loads(NPCList)
    bosses=[]
   
    for npc in npcs["data"]:
        #print(npc)
        if npc["boss"]!=0:
            lootOfBoss=[]
            lootOfBossHC=[]
            print("#"+npc["name"]+" "+str(npc["boss"]))
           
            LootHtml=requests.get("https://wotlk.evowow.com/?npc="+str(npc["id"])).text
            LootList=re.findall("new Listview[(](.*)[)]",LootHtml)[0].split('}],"name"')[0]+"}]}"
            loots=json.loads(LootList)
            
            for loot in loots["data"]:
                print(loot)
                if("level" in dict.keys(loot) and loot["level"]>140):
                    lootOfBoss.append({"id":loot["id"],"name":loot["name"],"level":loot["level"]})
            try:
                LootListHC=re.findall("new Listview[(](.*)[)]",LootHtml)[1].split('}],"name"')[0]+"}]}"
                lootsHC=json.loads(LootListHC)
                for loot in lootsHC["data"]:
                    #print(loot)
                    if("level" in dict.keys(loot) and loot["level"]>140):
                        lootOfBossHC.append({"id":loot["id"],"name":loot["name"]})
            except:
                print("no hc data")
            bosses.append({"name":npc["name"],"lootNHC":lootOfBoss,"lootHC":lootOfBossHC})
    data.append({"name":dungeon["name"],"id":dungeon["id"],"bosses":bosses})            
print(data)
# Serializing json
json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("data.json", "w") as outfile:
    outfile.write("export const data="+json_object)