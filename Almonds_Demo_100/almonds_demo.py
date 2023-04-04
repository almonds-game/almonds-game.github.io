from config import *

###########################################
## File dependencies for this version:   ##
##    config.py                          ##
##    chars.json                         ##
##    extra_data.json                    ##
##    nodel.json                         ##
##    settings.json                      ##
###########################################

###############################                Copyright © 2021-2022 some fucking guy i dunno literally who cares <dontcontactmeaboutthis@fuck.you>
###############################                (i don't actually know how to copyright something nor will i risk jumping through hoops to do so)
##  To do:                   ##                
##      Attacking        √   ##                Hello! Welcome to the Almonds Prototype!
##      Volume Settings  √   ##                I know it's referred to as a demo in the files
##      Stats            √   ##                but that's because I figured calling it a demo implies
##      Spells&Mana      √   ##                that the full product is a text adventure.
##      Party System     √   ##                I just never really bothered to change the actual file name.
##      Game Over        √   ##                
##      Leveling up      √   ##                But yeah! Since this is written in python,
##      Main Menu        √   ##                thi1s thing is open source wether I like it or not.
##      Progress Saver   √   ##                Honestly, I'm not gonna go through the trouble of rewritting this
##      Progress Checker √   ##                entire program in C++, or god forbid, C.
##      Inventory Disp.  √   ##
##      Item Add         √   ##
##      Item limit       √   ##
##      Item Sub         √   ##
##      Item Inspect     √   ##
##      Item Use         √   ##
##      Specials         √   ##
##      Combo Specials       ## combo specials are called conditional specials in the actual code
##                           ## HOLD IT!! The previous comment is wrong, they originally were stored in
############################### their own "conditional_specials" dictionary, but now all specials AND
############################### spells have been put in their own dedicated dictionaries, aptly named "spells" and "specials"

def set_settings():
    global settings
    settings = {
        "sound": True,
        "musicVolume": 1.0,
        "sfxVolume": 1.0,
        "debug": False,
        "hard_mode": False
    }

def set_extra_data():
    global extra_data
    extra_data = {
        "progress": {
            "seg_1_beg": False,
            "seg_1_mid": False,
            "seg_1_end": False,

            "seg_2_beg": False,
            "seg_2_mid": False,
            "seg_2_end": False
        },

        "secret": {
            "counter": 0,
            "interest": randint(0, 128)
        }
    }

def set_nodel():
    global nodel
    nodel = { #nodel = "no delete"
        "times_completed": 0,
        "first_boot": True,
        "current_name": "",
        "prev_name": "Venus"
    }

def set_dialogue():
    global dialogue
    dialogue = {
        "monkey":{
            "intro": censor("HOLY SHIT A MONKEY!"),
            "dialogue": ("The monkey reeks of bananas.", "Smells like monkies, even though there's just one.", censor("The monkey shat in its hand..."), censor("The monkey is throwing its feces... talk about going apeshit."))
        },

        "dry almond":{
            "intro": "Something approaches.",
            "dialogue": ("What could it want?", "The Dry Almond groans.", "The Dry Almond looks at you, expressionless.")
        },

        "aladron":{
            "intro": "SHE attacks!",
            "dialogue": ("Smells like corndogs.", "She glares at you.", "She looks at you, expecting a stupid joke to come out of your mouth.")
        },

        myLord("josie"):{
            "intro": myLord("Josie lunges at you, full force!... She dealt 0 damage."),
            "dialogue": (myLord("Josie gives you a death glare."), "Smells like shampoo.", "Josie eats a porkbun... No HP recovered.",
                        myLord("Josie took some fresh spaghetti out of a container, she burned her tongue trying to eat it,\nno HP lost."),
                        myLord("Josie plays with her lighter and almost burns her hair."), f"She broke up with boyfriend number {randint(16, 128)} today.")
        },

        "joe hawley":{
            "intro": "Joe Hawley attacks!",
            "dialogue": ("In the time you were reading this, he went hurdlin.", "Clearly, he's ovulating.", "Joe Hawley.", f"{'Joe Hawley ' * randint(2, 8)}",
                         "shuck'S SO fussING BONKERS AT THE FARMER'S MARKET.")
        },

        "driver d.":{
            "intro": "Driver D. stands in the way!",
            "dialogue": ("The metal smells nasty.", "Smoke is filling the room.", "A gasolined powered robot? In THIS day in age?",
                         "One of the plates on Driver D.'s torso lifts, revealing a sawblade attached to an arm")
        }
    }

def set_levels():
    global levels
    levels = {
        "1": {
            "hp": 69 if not settings['hard_mode'] else 59,
            "atk": 20 if not settings['hard_mode'] else 15,
            "defn": 10 if not settings['hard_mode'] else 5,
            "threshold": 0
        },
        
        "2": {
            "hp": 80 if not settings['hard_mode'] else 70,
            "atk": 25 if not settings['hard_mode'] else 15,
            "defn": 15 if not settings['hard_mode'] else 10,
            "threshold": 16
        },

        "3": {
            "hp": 128 if not settings['hard_mode'] else 90,
            "atk": 32 if not settings['hard_mode'] else 20,
            "defn": 24 if not settings['hard_mode'] else 15,
            "threshold": 32
        },

        "4": {
            "hp": 150 if not settings['hard_mode'] else 120,
            "atk": 40 if not settings['hard_mode'] else 30,
            "defn": 32 if not settings['hard_mode'] else 20,
            "threshold": 64
        },

        "5": {
            "hp": 200 if not settings['hard_mode'] else 140,
            "atk": 60 if not settings['hard_mode'] else 40,
            "defn": 45 if not settings['hard_mode'] else 32,
            "threshold": 128
        },

        "6": {
            "hp": 256 if not settings['hard_mode'] else 180,
            "atk": 128 if not settings['hard_mode'] else 80,
            "defn": 64 if not settings['hard_mode'] else 40,
            "threshold": 256
        },

        "7": {
            "hp": 300 if not settings['hard_mode'] else 230,
            "atk": 150  if not settings['hard_mode'] else 110,
            "defn": 80 if not settings['hard_mode'] else 55,
            "threshold": 512
        },

        "8": {
            "hp": 512 if not settings['hard_mode'] else 350,
            "atk": 256 if not settings['hard_mode'] else 130,
            "defn": 128 if not settings['hard_mode'] else 70,
            "threshold": 1024
        },
    }

def set_items():
    global items
    items = {
        "pizza": {
            "name": "Pizza",
            "hp": 16,
            "atk": 0,
            "defn": 0,
            "desc": "Pizza!",
            "statDesc": [f"Heals \033[1;32;40m{printRoman(16)} \033[1;31;40mHP\033[0;37;40m,", "| not the healthiest option,", "\nbut it's PIZZA for god's sake!"],
            "price": 6
        },

        "apple": {
            "name": "Apple",
            "hp": 10,
            "atk": 0,
            "defn": 0,
            "desc": "What was the saying again? \"An apple a week keeps the children meek!\"",
            "statDesc": [f"Heals \033[1;32;40m{printRoman(10)} \033[1;31;40mHP\033[0;37;40m,", "| I THINK this isn't rotten..."],
            "price": 3
        },

        "feces": {
            "name": "Feces",
            "hp": -3,
            "atk": 0,
            "defn": 10,
            "desc": "JESUS CHRIST WHERE DID YOU GET THIS?!?!",
            "statDesc": [f"Heals \033[1;31;40m{'-3' if not settings['hard_mode'] else '-III'} \033[1;31;40mHP \033[0;37;40mand \033[0;37;40mraises \033[1;34;40mDEF \033[0;37;40mby \033[1;34;40m{printRoman(10)}\033[0;37;40m,", "\n\033[0;37;40msince no one wants to get near you,", "| nasty."],
            "price": -10
        },

        "mcintosh": {
            "name": "McIntosh",
            "hp": 20,
            "atk": 0,
            "defn": 20,
            "desc": "It's a McIntosh apple, sadly it doesn't taste like a computer...",
            "statDesc": [f"Heals \033[1;32;40m{printRoman(20)} HP \033[0;37;40mand raises \033[1;34;40mDEF \033[0;37;40mby \033[1;34;40m{printRoman(20)}.", "\n\033[0;37;40mUse this apple wisely, it's expensive!"],
            "price": 200
        },

        "window": {
            "name": "Window",
            "hp": -10,
            "atk": 10,
            "defn": 0,
            "desc": "A window shard with the number 10 etched onto it.",
            "statDesc": ["You know, if you eat it, your hands'll get stabbed", f"\nand you'll lose \033[1;31;40m{printRoman(20)} HP\033[0;37;40m, but GAIN \033[0;31;40m{printRoman(10)} ATK", "| \033[0;37;40mbecause of the", "\nglass shards in your hands."],
            "price": 50
        },

        "popsicle": {
            "name": "Popsicle",
            "hp": 8,
            "atk": 0,
            "defn": 0,
            "desc": "It's a popsicle, it's very... uh... WHAT DO YOU WANT FROM ME? IT'S A POPSICLE!",
            "statDesc": [f"Heals \033[1;32;40m{printRoman(8)} HP\033[0;37;40m."], ### DO THE STUFF FOR HARD MODE NOW NOW NOW NOW NOW NOW NOW 
            "price": 3
        },

        censor("dildo"): {
            "name": censor("Dildo"),
            "hp": 0,
            "atk": 0,
            "defn": 15,
            "desc": censor("It's Josie's dildo... It has the name \"Kyler\" written on it in marker.\n    Sounds like a \033[1;31;40mno life \033[0;37;40mfrom New York."),
            "statDesc": [f"Raises \033[1;34;40mDEF \033[0;37;40mby \033[1;34;40m{printRoman(15)}, \033[0;37;40mnot sure how, but it does!"],
            "price": 45
        },

        "almond milk": {
            "name": "Almond Milk",
            "hp": 20,
            "atk": 0,
            "defn": 5,
            "desc": "A small glass bottle of almond milk made from the almond.",
            "statDesc": [f"Heals \033[1;32;40m{printRoman(20)} HP and raises \033[1;34;40mDEFN by {printRoman(5)}"],
            "price": 30
        },

        "deodorant": {
            "name": "Deodorant",
            "hp": 10,
            "atk": 5,
            "defn": 0,
            "desc": "It's... deodorant???",
            "statDesc": [f"Heals \033[1;31;40m10 HP\033[0;37;40m and \033[0;31;40mraises ATK by 5."]
        },

        "flesh": {
            "name": "Flesh",
            "hp": 35,
            "atk": -10,
            "defn": -5
        }
    }

def set_spells():
    global spells
    spells = {
        ### Edward spells ### 
        "aid_enemy": { # DEFAULT
            "name": "AID Enemy",
            "hp": 0,
            "atk": [3, 10],
            "atk_raise": 0,
            "defn": 0,
            
            "offensive": True,
            "partyWide": False,
            "lingers": True,
            "turns": -1,
            "base_turns": -1,
            
            "randomized": False,
            "mana_cost": 20,
            "desc": ("Gives the target AIDs, it lingers permanently.", " Like the real AIDS! (Because it IS the real AIDS.)")
        },

        "death": { # DEFAULT
            "name": "death.",
            "hp": 0,
            "atk": [696969, 696969],
            "atk_raise": 0,
            "defn": 0,
            
            "offensive": True,
            "partyWide": False,
            "lingers": False,

            "randomized": True,
            "chance": [1, 128],
            "threshold": 74,
            "mana_cost": 100,
            "desc": ("There's a random chance that this spell instantly kills the enemy.", "However, the chance is very slight.")
        },

        "smoke_screen": { # if Edward & Louis in party 
            "name": "Smoke Screen",
            "hp": 0,
            "atk": [0, 0],
            "atk_raise": 0,
            "defn": 0,

            "offensive": False,
            "partyWide": False,
            "lingers": True,
            "turns": 3,
            "base_turns": 3,

            "randomized": False,
            "mana_cost" : 32,
            "desc": ("Edward forces Louis to make him \033[0;32;40mfart\033[0;37;40m.", "This \033[1;33;40mstuns the opponent for 3 turns\033[0;37;40m and \033[1;34;40mlowers their DEFN by 25%\033[0;37;40m.")
        },

        ### Aidan Spells ### 
        "heal_prayer": { # DEFAULT
            "name": "Heal Prayer",
            "hp": 25,
            "atk": [0, 0],
            "atk_raise": 0,
            "defn": 0,

            "offensive": False,
            "partyWide": False,
            "lingers": False,

            "randomized": False,
            "mana_cost": 25,
            "desc": ()
        },

        "safe_guard": { # DEFAULT
            "name": "Safe Guard",
            "hp": 0,
            "atk": [0, 0],
            "atk_raise": 0,
            "defn": 10,

            "offensive": False,
            "partyWide": True,
            "lingers": True,
            "turns": 6,
            "base_turns": 6,
            
            "randomized": False,
            "mana_cost": 32,
            "desc": ()
        }
    }

def set_specials():
    global specials
    specials = {
        # Remember to add a smokescreen attack where louis makes edward fart

        # Specials to add later:
        # ALL CLEAR!


        "fuck_you": { # DEFAULT FOR JOSE
            "name": "Fuck You", # Fuck You was originally Fuck You: part II, which was originally named Guard Breaker
            "atk": [0, 0],
            "lingers": True,
            "turns": 6,
            "base_turns": 6,

            "randomized": False,
            "mana_cost": 80,
            "desc": ("Jose punches the enemy HARD. Somehow does no damage,", " but slices the enemy's DEFN in half for 6 turns")
        },

        "fuck_you_ii": { # DEFAULT FOR JOSE
            "name": "Fuck You: part II",
            "atk": [32, 32],
            "lingers": False,

            "randomized": False,
            "mana_cost": 50,
            "desc": ("Just a placeholder!")
        },

        "fuck_thee_iii": { # if Jose & Other in party, for Jose
            "name": "Fuck Thee: part III",
            "atk": [64, 64],
            "lingers": False,

            "randomized": False,
            "mana_cost": 60,
            "desc": ("Jose grabs Diego, spins him around town and throws him to the enemy.", "Wouldn't wanna have THAT done to me.") # The real life diego (me) has had that done to him.
  
        },


        ### Louis Specials ###

        "slam_dunk": { # DEFAULT
            "name": "Slam Dunk",
            "atk": [5, 10],
            "lingers": True,
            "turns": 6,
            "base_turns": 6,

            "randomized": False,
            "mana_cost": 50,
            "desc": ("Louis slams dunks the enemy into a big metal sink and \033[1;31;40mdeals some damage on impact\033[0;37;40m.", "This \033[1;33;40mskips the enemy's turns 6 times\033[0;34;40m.", "However, the sink \033[1;34;40mraises their DEFN by 25%\033[0;34;70m.")
        },

        "do_nothing": {
            "name": "literally do nothing",
            "atk": [0, 0],
            "lingers": False,

            "randomized": False,
            "mana_cost": 0,
            "desc": ("Louis literally does nothing for the low low price of free!")
        },

        "chimp_gun": { # if Louis & Aidan in party
            "name": "Chimp Gun",
            "atk": [32, 42],
            "lingers": True,
            "turns": 3,
            "base_turns": 3,

            "randomized": False,
            "mana_cost": 90,
            "desc": ("Louis grabs Aidan and uses him as a gun against the enemy!", "\033[1;31;40mHe shoots at the enemy\033[0;37;40m for \033[1;33;40m3 of his turns.")

        }  
    }

def set_chars():
    global chars
    chars  = {
        "player": {
            "name": "Melanie",
            "nameColor": "\033[1;34;6m",
            "lv": 1,

            "money": 0,
            "exp": 0,
            "mana": 100,

            "item_amount": 0,
            "inventory": ["Empty"]*12,

            "party": ["edward", "jose"],
            "has_magic": False,
            "effects": [],
            "specials": None
        },

        "edward": {
            "name": "Edward",
            "nameColor": "\033[38;5;92m",
            "lv": 1,

            "base_hp": 80,
            "hp": 80,
            "base_atk": [20, 30],
            "atk": 20,
            "base_defn": 20,
            "defn": 20,
            "has_magic": True,
            
            "spells": {
                "aid_enemy": spells["aid_enemy"],
                "death": spells["death"]
            }
        },

        "jose": {
            "name": "Jose",
            "nameColor": "\033[1;34;40m",
            "lv": 1,

            "base_hp": 90,
            "hp": 90,
            "base_atk": [35, 40],
            "atk": 35,
            "base_defn": 25,
            "defn": 25,
            
            "has_magic": False,
            "specials": {
                "fuck_you": specials["fuck_you"],
                "fuck_you_ii": specials["fuck_you_ii"]
            }
        },

        "aidan": {
            "name": "Aidan",
            "nameColor": "\033[1;32;40m",
            "lv": 1,

            "base_hp": 60,
            "hp": 60,
            "base_atk": [10, 15],
            "atk": 10,
            "base_defn": 15,
            "defn": 15,

            "has_magic": True,
            
            "spells": {
                "heal_prayer": spells["heal_prayer"],
                "safe_guard": spells["safe_guard"]
            }
        },

        "louis": {
            "name": "Louis",
            "nameColor": "\033[1;37;40m",
            "lv": 1,

            "base_hp": 80,
            "hp": 80,
            "base_atk": [15, 25],
            "atk": 15,
            "base_defn": 25,
            "defn": 25,

            "has_magic": False,

            "specials": {
                "slam_dunk": specials["slam_dunk"],
                "do_nothing": specials["do_nothing"]
            }
        },

        "monkey": {
            "name": "Monkey",
            "nameColor": "\033[1;31;40m",
            "base_hp": 80,
            "hp": 80,
            "base_atk": [12, 18],
            "atk": 12,
            "base_defn": 15,
            "defn": 15,

            # "exp": [8*4, 18*4],
            "exp": (64, 64),
            "money": (4, 8),
            "effects": [],
        },

        "dry almond": {
            "name": "Dry Almond",
            "nameColor": "\033[0;31;40m",
            "base_hp": 90,
            "hp": 90,
            "base_atk": [15, 20],
            "atk": 10,
            "base_defn": 10,
            "defn": 10,

            "exp": (16, 25),
            "money": (8, 16),
            "effects": [],
        },

        "aladron":{
            "name": "Aladron",
            "nameColor": "\033[0;31;40m",
            "base_hp": 256,
            "hp": 256,
            "base_atk": [32, 40],
            "atk": 32,
            "base_defn": 0,
            "defn": 0,

            "exp": (20, 40),
            "money": (32, 128),
            "effects": [],
        },
        
        myLord("josie"): {
            "name": myLord("Josie"),
            "nameColor": "\033[1;33;40m",
            "base_hp": 128,
            "hp": 128,
            "base_atk": [10, 15],
            "atk": 10,
            "base_defn": 25,
            "defn": 25,

            "exp": (15, 32),
            "money": (128, 250),
            "effects": [],
        },
        
        "joe hawley": {
            "name": "Joe Hawley",
            "nameColor": "\033[1;31;40m",
            "base_hp": 140,
            "hp": 140,
            "base_atk": [35, 45],
            "atk": 35,
            "base_defn": 30,
            "defn": 30,

            "exp": (16, 24),
            "money": (57, 57),
            "effects": [],
        },

        "driver d.": {
            "name": "Driver D.",
            "nameColor": "\033[0;45;40m",
            "base_hp": 128,
            "hp": 128,
            "base_atk": [64, 75],
            "atk": 64,
            "base_defn": 32,
            "defn": 32,

            "exp": (128, 256),
            "money": (32, 64),
            "effects": [],
        }
    }

def setAll():
    set_settings()
    set_extra_data()
    set_nodel()
    set_levels()
    set_items()
    set_spells()
    set_specials()
    set_chars()
    set_dialogue()

setAll()

def playSound(file):
    if settings["sound"]:
        match os.getcwd():
            case directory if "sound" in directory:
                pass
            case _:
                os.chdir("sound")
        soundEffect = mixer.Sound(file + ".ogg")
        soundEffect.set_volume(settings["sfxVolume"] if not settings["sfxVolume"] > 1.0 else 1.0)
        soundEffect.play()
        match os.getcwd():
            case directory if "sound" in directory:
                os.chdir("../")
            case _:
                pass

def playMusic(file, loops=0, volume=settings["musicVolume"], ogg=True):
    if settings["sound"]:
        match os.getcwd():
            case directory if "sound" in directory:
                pass
            case _:
                os.chdir("sound")
        volume = 1.0 if volume > 1.0 else settings["musicVolume"]
        mixer.music.load(f"{file + '.ogg' if ogg else file + '.wav'}")
        mixer.music.play(loops)
        mixer.music.set_volume(volume)
        match os.getcwd():
            case directory if "sound" in directory:
                os.chdir("../")
            case _:
                pass
        
    # try:
    #     mixer.music.load(f"sound/{file + '.ogg'}")
    #     mixer.music.play(loops)
    #     mixer.music.set_volume(volume)
    # except:
    #     os.chdir("../")
    #     mixer.music.load(f"sound/{file + '.ogg'}")
    #     mixer.music.play(loops)
    #     mixer.music.set_volume(volume)
    # print(settings["musicVolume"])


                    #case char if char in silentChars or char == "\n" or snd_switch:
                    #    snd_switch = False
                    #    pass
def musicInOut(ms=0, slep=0):
    if settings["sound"]:
        mixer.music.fadeout()
        time.sleep(slep)
        mixer.music.unload()

def printRoman(number):
    #number = int(number)
    #print(settings["hard_mode"])
    if settings["hard_mode"]:
        num = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
        sym = ("I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M")

        full = "" if number > 0 else "-"
        if not number > 0:
            number -= (number * 2)
        i = 12

        while number:
            div = number // num[i]
            number %= num[i]
            while div:
                full = full + sym[i]
                div -= 1
            i -= 1
        return full
    else:
        return number
set_settings()

def say(phrase, interval=0.03, voice=None):
    silentChars = " ,.!?()\"\'"
    for char in phrase:
        print(char, end="", flush=True)
        match voice:
            case None:
                pass
            case _:
                match char:
                    case char if char in silentChars or char == "\n":
                        pass
                    case _:
                        playSound(voice)
        time.sleep(interval)

################################################
### For applying player stats to their level ###
################################################

def base_stat_set():
    if not chars["player"]["lv"] > 8:
        chars["player"]["base_hp"] = levels[f"{chars['player']['lv']}"]["hp"]
        chars["player"]["base_atk"] = [levels[f"{chars['player']['lv']}"]["atk"], levels[f"{chars['player']['lv']}"]["atk"] + 5]
        chars["player"]["base_defn"] = levels[f"{chars['player']['lv']}"]["defn"]
    else:
        chars["player"]["base_hp"] = 999
        chars["player"]["base_atk"] = [999, 999]
        chars["player"]["base_defn"] = 999

def full_recover():
    chars["player"]["hp"] = chars["player"]["base_hp"]
    chars["player"]["atk"] = chars["player"]["base_atk"][0]
    chars["player"]["defn"] = chars["player"]["base_defn"]
    chars["player"]["effects"] = []

    for member in chars["player"]["party"]:
        chars[member]["hp"] = chars[member]["base_hp"]
        chars[member]["atk"] = chars[member]["base_atk"][0]
        chars[member]["defn"] = chars[member]["base_defn"]

def spell_turn_reset():
    for member in chars["player"]["party"]:
        moveType = "spells" if chars[member]["has_magic"] else "specials"
        for move in chars[member][moveType]:
            if chars[member][moveType][move]["lingers"]:
                chars[member][moveType][move]["turns"] = chars[member][moveType][move]["base_turns"]

def fuckingDied(inspected, enemy, death_sound):
    # chars["player"]["party"][0]
    # chars["player"]["party"][1]
    match inspected["hp"]:
        case hp if hp <= 0 and inspected["name"] == chars["player"]["name"]:
            clear()
            musicInOut(1300, 1.4)
            time.sleep(2.5)
            playMusic("game_over")

            waited = False
            while True:
                clear()
                print("\033[0;37;40mGame Over.")
                base_stat_set()
                inspected["defn"] = inspected["base_defn"]
                enemy["hp"] = enemy["base_hp"]
                enemy["atk"] = enemy["base_atk"][0]
                enemy["defn"] = enemy["base_defn"]
                enemy["effects"] = []
                if waited == False:
                    time.sleep(2)

                contin = input("Start from last save point?(\033[1;32;40my\033[0;47;40m/\033[1;31;40mn\033[0;37;40m): ").strip().casefold()
                if contin == "y":
                    musicInOut(1300, 1.4)
                    contin = None
                    return (True, True)
                
                elif contin == "n":
                    contin = input("Are you sure? This will quit the game.(\033[1;32;40my\033[0;47;40m/\033[1;31;40mn\033[0;37;40m): ").strip().casefold()
                    if contin == "y":
                        musicInOut(1300, 1.4)
                        contin = None
                        return (True, False) # Player Died, Will not start from checkpoint
                    elif contin == "n":
                        musicInOut(1300, 1.4)
                        contin = None
                        return (True, True) # Player Died, Will start from checkpoint
                    else:
                        invalidInput(783)
                        time.sleep(1.3)
                        continue
                else:
                    invalidInput(787)
                    time.sleep(1.3)
                    continue
            
        case hp if hp <= 0 and inspected["name"] == enemy["name"]: # The attack vector or whatever 
            base_stat_set()
            inspected["defn"] = inspected["base_defn"]
            inspected["hp"] = inspected["base_hp"]
            inspected["atk"] = inspected["base_atk"][0]
            playSound(death_sound)
            time.sleep(0.13)
            musicInOut(1300, 1.35)

            time.sleep(0.5)
            clear()
            print("\033[0;37;40mBattle won!")
            player = chars["player"]
            moneyGained = randint(enemy["money"][0], enemy["money"][1]) + chars["player"]["mana"] // 2
            expGained = randint(enemy["exp"][0], enemy["exp"][1])
            player["money"] += moneyGained
            player["exp"] += expGained
            print(f"\033[1;32;40mGot ${printRoman(moneyGained)}")
            time.sleep(1)
            print(f"\033[1;31;40mEarned {printRoman(expGained)} EXP.")
            time.sleep(2)
            if leveler(chars["player"]) == False:
                input("\n\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")

            clear()
            return [True, True] # Useless, Enemy Died
        
        case _:
            match inspected["hp"]:
                case hp if hp <= 0 and inspected["name"].casefold() == chars["player"]["party"][0]:
                    print(f"{inspected['nameColor'] + inspected['name']} \033[1;31;40mgot d(owned)!\033[0;37;40m")
                    time.sleep(1)
                    return [False, False]
                case hp if hp <= 0 and inspected["name"].casefold() == chars["player"]["party"][1]:
                    print(f"{inspected['nameColor'] + inspected['name']} \033[1;31;40mgot d(owned)!\033[0;37;40m")
                    time.sleep(1)
                    return [False, False]
                case _:
                    return [False, False]

def invent_display(secs=0):
    clear()
    sorting = {}
    for index, thing in enumerate(chars["player"]["inventory"]):
        sorting[index] = f"{printRoman(index + 1)}. {chars['player']['inventory'][index]}"

        if "11" in sorting[index]:
            sorting[index] = f"{printRoman(index + 1)}. {chars['player']['inventory'][index]}"
        else:
            if index <= 9:
                sorting[index] = f" {printRoman(index + 1)}. {chars['player']['inventory'][index]}"

    index = 0 if not settings["hard_mode"] else 11
    takeaway = 1 if not settings["hard_mode"] else -1
    switch = True

    for thing in sorting:
        if switch:
            print("%-15s" % sorting[index], end="")
            time.sleep(secs)
            index += takeaway
            switch = False
            continue
        
        else:
            print("%15s" % sorting[index])
            time.sleep(secs)
            index += takeaway
            switch = True
            continue



def thing_inspect(itemName):
    newline = "\n"
    print("\n" + itemName + ": ")
    try:
        print(f"    {items[f'{itemName.casefold()}']['desc']}")
        time.sleep(1)
        for line in items[f"{itemName.casefold()}"]["statDesc"]:
            print(f"{newline if line[0] == newline else ''}{'' if line[0] == '|' else '    '}{line[1:] if line[0] == '|' else line if line[0] != newline else line[1:]}", end="", flush=True)
            time.sleep(0.4)

    except KeyError:
        print()
        print(itemName)
    
    itemName = None

    '''
    itemName = itemName.casefold().replace(" ", "_")
    print("\n" + playerInv[index]["name"] + ": ")
    for line in playerInv[index]["desc"]:
        print(f"    {line}", end="", flush=True)
        time.sleep(0.4)  # Guessing this is for something idfk
    '''



def invent_sub(index):
    chars["player"]["inventory"][index] = "Empty"
    chars["player"]["item_amount"] -= 1
    index = None

def invent_limit():
    if chars["player"]["item_amount"] == 12:
        clear()
        print("\033[1;31;40mYou're carrying too many items.\033[0;37;40m")
        return True
    else:
        return False

def invent_add(item):
    index = 0
    for thing in chars["player"]["inventory"]:
        if invent_limit():
            time.sleep(1)
            action = input("Throw an item away(\033[1;31;40my\033[0;37;40m/\033[1;32;40mn\033[0;37;40m)?: ").strip()
            if action.casefold() == "n":    
                abandon = input(f"So you'll leave the {item['name']} behind(\033[1;31;40my\033[0;37;40m/\033[1;32;40mn\033[0;37;40m)?: ").strip() 
                if abandon.casefold() == "y":
                    print(f"Abandoned the {item['name']}.")
                    time.sleep(1)
                    break
                
                if abandon.casefold() == "n":
                    invent_display(0.01)
                    remChoose = input("\nWhat item would you like to throw away? (\033[1;34;40mNumber \033[0;37;40mor \033[1;31;40m\"c\" \033[0;37;40mto go back): ")
                    if remChoose.strip().casefold() == "c":
                        continue
                    else:
                        if remChoose.isnumeric():
                            remChoose = int(remChoose)
                            remChoose -= 1
                            if 0 <= remChoose <= 11:
                                threw_away = chars["player"]["inventory"][remChoose]
                                invent_sub(remChoose)
                                print(f"\nThrew away the {threw_away}.")

                                time.sleep(0.5)
                                chars["player"]["inventory"][remChoose] = item["name"]
                                chars["player"]["item_amount"] += 1
                                print(f"Added the {chars['player']['inventory'][remChoose]} to your inventory.")
                                time.sleep(0.5)
                                input("\nPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                                clear()
                                break

                            else:
                                print("\033[1;31;40mPick a number between 1 and 12.")
                                time.sleep(1)
                                continue

                        else:
                            print("\033[1;31;40mPlease pick a number.\033[0;37;40m")
                            time.sleep(1)
                            continue

            if action.casefold() == "y":
                invent_display(0.01)
                remChoose = input("\nWhat item would you like to throw away? (\033[1;34;40mNumber \033[0;37;40mor \033[1;31;40m\"c\" \033[0;37;40mto go back): ")
                if remChoose.strip().casefold() == "c":
                    continue
                else:
                    if remChoose.isnumeric():
                        remChoose = int(remChoose)
                        remChoose -= 1
                        if 0 <= remChoose <= 11:
                            threw_away = chars["player"]["inventory"][remChoose]
                                
                            invent_sub(remChoose)
                            print(f"\nThrew away the {threw_away}.")
                                
                            time.sleep(0.5)
                                
                            chars["player"]["inventory"][remChoose] = item["name"]
                            chars["player"]["item_amount"] += 1
                            print(f"Added the {chars['player']['inventory'][remChoose]} to your inventory.")
                            time.sleep(0.5)
                            input("\nPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                            clear()
                            break

                        else:
                            print("\033[1;31;40mPick a number between 1 and 12.")
                            time.sleep(1)
                            continue

                    else:
                        print("\033[1;31;40mPlease pick a number.\033[0;37;40m")
                        time.sleep(1)
                        continue
            else:
                invalidInput(995)
                time.sleep(1)
                continue
        else:
            if chars["player"]["inventory"][index] == "Empty":
                chars["player"]["inventory"][index] = item["name"]
                chars["player"]["item_amount"] += 1
                action = None
                return
            
            else:
                index += 1
                continue

def invent_reset(rem_items):
    for thing in rem_items:
        if thing in chars["player"]["inventory"]:
            invent_sub(chars["player"]["inventory"].index(thing))

def invent_menu():
    pass



###################
### SPELL STUFF ###
###################

def cast_spell(caster, spell, receiver, enemy, death_sound):
    try:
        receiver = chars[receiver]
    except TypeError:
        pass
    
    print(f"{caster['nameColor'] + caster['name']} \033[0;37;40mcast {caster['spells'][spell]['name']}!")

    if caster["spells"][spell]["randomized"]: 
        if not randint(caster["spells"][spell]["chance"][0], caster["spells"][spell]["chance"][1]) == caster["spells"][spell]["threshold"]: 
            time.sleep(1)
            print("But it didn't work...")
            time.sleep(1)
            chars["player"]["mana"] -= caster["spells"][spell]["mana_cost"]
            return

    dmg = randint(caster["spells"][spell]["atk"][0], caster["spells"][spell]["atk"][1])

    receiver["hp"] += caster["spells"][spell]["hp"]
    receiver["atk"] += caster["spells"][spell]["atk_raise"]
    receiver["defn"] += caster["spells"][spell]["defn"]
    receiver["hp"] -= dmg

    time.sleep(0.5)

    if dmg > 0:
        print(f"{caster['nameColor'] + caster['name']} \033[0;37;40mdealt \033[1;31;40m{printRoman(dmg)} \033[0;37;40mdamage to {receiver['nameColor'] + receiver['name']}\033[0;37;40m!")
        time.sleep(0.3)

    if caster["spells"][spell]["hp"] > 0:
        print(f"{receiver['nameColor'] + receiver['name']} \033[1;32;40mgained {printRoman(caster['spells'][spell]['hp'])} HP!")
        time.sleep(0.3)
        if receiver["hp"] > (receiver["base_hp"] + (receiver["base_hp"] // 4)):
            receiver["hp"] = (receiver["base_hp"] + (receiver["base_hp"] // 4))

    if caster["spells"][spell]["atk_raise"] > 0:
        print(f"{receiver['nameColor'] + receiver['name']} \033[1;31;40mgained {printRoman(caster['spells'][spell]['atk_raise'])} ATK!")
        time.sleep(0.3)

    if caster["spells"][spell]["defn"] > 0:
        print(f"{receiver['nameColor'] + receiver['name']} \033[1;34;40mgained {printRoman(caster['spells'][spell]['defn'])} DEFN!")
        time.sleep(0.3)

    try:
        chars["player"]["mana"] -= caster["spells"][spell]["mana_cost"]
    except TypeError:
        print(caster["spells"][spell]["mana_cost"])
            
    if fuckingDied(receiver, enemy, death_sound)[0]:
        return True

    input("\nPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
    return

def use_special(user, special, receiver, enemy, death_sound):
    print(f"{user['nameColor'] + user['name']} \033[0;37;40mused {user['specials'][special]['name']}!")
    if user["specials"][special]["randomized"]:
        if not randint(user["specials"][special]["chance"][0], user["specials"][special]["chance"][0]) == user["specials"]["threshold"]:
            time.sleep(1)
            print("But it didn't work...")
            time.sleep(1)
            chars["player"]["mana"] -= user["specials"][special]["mana_cost"]
            return

    dmg = randint(user["specials"][special]["atk"][0], user["specials"][special]["atk"][1])
    receiver["hp"] -= dmg

    time.sleep(0.5)

    print(f"{user['nameColor'] + user['name']} \033[0;37;40mdealt \033[1;31;40m{printRoman(dmg)} \033[0;37;40mdamage to {receiver['nameColor'] + receiver['name']}\033[0;37;40m!")
    time.sleep(0.3)

    if fuckingDied(receiver, enemy, death_sound)[0]:
        return True
    else:
        chars["player"]["mana"] -= user["specials"][special]["mana_cost"]
        return


def attack(attacker, defender):
    if settings["hard_mode"]:
        critPick = randint(1, 32 if attacker["name"] == chars["player"]["name"] or attacker["name"].casefold() in chars["player"]["party"] else 20)
    else:
        critPick = randint(1, 32) # 32
    # critPick = 12
    match critPick:
        case 12: 
            colors = ("\033[1;36;40m", "\033[1;32;40m", "\033[1;33;40m")
            playSound("crit")
            clear()
            for i in range(2):
                for color in colors:
                    print(f"\r{color}Cr1TiKaL hit!\033[0;37;40m", end="", flush=True)
                    time.sleep(0.1)
            print("\r\033[1;31;40mCr1TiKaL hit!\033[0;37;40m")
            dmg = attacker["base_atk"][1] + 15
            dmg = 3 if dmg - defender["defn"] < 3 else dmg - defender["defn"]
            chars["player"]["mana"] += randint(10, 15)

        case _:
            dmg = randint(attacker["base_atk"][0], attacker["base_atk"][1])
            #print(f"Gross damage: {dmg}")
            dmg -= defender["defn"]
            chars["player"]["mana"] += randint(3, 5)
            if dmg <= 3 and attacker["name"] == chars["player"]["name"]:
                dmg = 3
                chars["player"]["mana"] += randint(5, 10)
            elif dmg <= 3 and attacker["name"] != chars["player"]["name"]:
                dmg = 3
                chars["player"]["mana"] += randint(5, 15)

    defender["hp"] -= dmg
    print(f"{attacker['nameColor'] + attacker['name']} \033[0;37;40mdealt \033[1;31;40m{printRoman(dmg)} \033[0;37;40mdamage to {defender['nameColor'] + defender['name']}")
    colors = None
    return



def leveler(player):
    leveled_up = False
    for i in range(7):
        clear()
        nextLevel = player["lv"] + 1
        if nextLevel > 8:
            print("\033[0;32;40mLevel stayed the same.")
            print("\n\033[1;31;40mThere is no more strength\nto feed your insatiable greed for power.")
            time.sleep(3)
            return False
        else:
            if player["exp"] >= levels[f"{nextLevel}"]["threshold"]:
                leveled_up = True
                player["lv"] += 1
                
                current = player["lv"]
                prevLevel = current - 1
                nextLevel = current + 1
                
                base_stat_set()
                print("\033[0;31;40mLeveled up!")
                time.sleep(0.05)
                print(f"\033[0;37;40mFrom level \033[1;32;40m{printRoman(player['lv'] - 1)} \033[0;37;40mto \033[1;31;40m{printRoman(player['lv'])}\033[0;37;40m.")
                time.sleep(1)
            
                print(f"\n\033[1;31;40mHP: \033[1;32;40m{printRoman(levels[f'{prevLevel}']['hp'])} \033[0;37;40m-> \033[1;31;40m{printRoman(levels[f'{current}']['hp'])}")
                time.sleep(0.2)
            
                print(f"\033[0;31;40mATK: \033[1;32;40m{printRoman(levels[f'{prevLevel}']['atk'])} \033[0;37;40m-> \033[1;31;40m{printRoman(levels[f'{current}']['atk'])}")
                time.sleep(0.2)
                
                print(f"\033[1;34;40mDEF: \033[1;32;40m{printRoman(levels[f'{prevLevel}']['defn'])} \033[0;37;40m-> \033[1;31;40m{printRoman(levels[f'{current}']['defn'])}")
                player["hp"] += player["base_hp"] // 4
                
                if player["hp"] > player["base_hp"] + (player["base_hp"] // 4):
                    player["hp"] = player["base_hp"] + (player["base_hp"] // 4)

                time.sleep(0.2)
                if player["exp"] >= levels[f"{nextLevel}"]["threshold"]:
                    continue
                else:
                    input("\n\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                    return True
            else:
                if leveled_up == False:
                    print("\033[1;32;40mLevel tayed the same.")
                    time.sleep(0.05)
                    print(f"\n\033[0;37;40mCurrent level: \033[1;32;40m{printRoman(player['lv'])}")
                    print(f"Level \033[1;31;40m{printRoman(nextLevel)} \033[0;37;40mEXP threshold: \033[1;32;40m{levels[f'{nextLevel}']['threshold']}\033[0;37;40m")
                    print(f"EXP left for next level: \033[0;31;40m{printRoman(levels[f'{nextLevel}']['threshold'] - player['exp'])}")
                    return False
                else:
                    print("\033[0;31;40mLeveled up!")
                    print(f"\033[0;37;40mFrom level \033[1;32;40m{printRoman(player['lv'] - 1)} \033[0;37;40mto \033[1;31;40m{printRoman(player['lv'])}\033[0;37;40m.")
                    #current = player['lv']
                    print(f"\n\033[1;31;40mHP: \033[1;32;40m{printRoman(levels[f'{prevLevel}']['hp'])} \033[0;37;40m-> \033[1;31;40m{printRoman(levels[f'{current}']['hp'])}")
                    
                    print(f"\033[0;31;40mATK: \033[1;32;40m{printRoman(levels[f'{prevLevel}']['atk'])} \033[0;37;40m-> \033[1;31;40m{printRoman(levels[f'{current}']['atk'])}")
                    
                    print(f"\033[1;34;40mDEF: \033[1;32;40m{printRoman(levels[f'{prevLevel}']['defn'])} \033[0;37;40m-> \033[1;31;40m{printRoman(levels[f'{current}']['defn'])}")
                    input("\n\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                    return



# Gypsy intro: 8450
def battle(player, enemy, partyBattle=False, music=["battle", 0, None]):
    match settings["sound"]:
        case True:
            match music:
                case musica if musica[0] != "battle" and musica[1] != 0:
                    clear()
                    playMusic(music[0] + "_intro")
                    print("An enemy approaches...")
                    time.sleep(music[1])
                case _:
                    pass
            death_sound = music[2]
            playMusic(music[0], -1)
        case _:
            death_sound = None
    skip_enemy_turn = False
    introDialogue, playerTurn, went_back = True, 1, False
    secrets = ("So uh, come here often?", "Watchu doin here, cutie?", "You disgust me.", "How YOU doin?", "W-What are you doing out of bounds, step-player?~")
    while True:
        print(f"\n{choice(secrets)}\n")
        # print(traceback.extract_stack())
        # print(len(traceback.extract_stack()))
        clear()
        if partyBattle:
            match playerTurn:
                case 1:
                    player = chars["player"]
                
                case 2:
                    player = chars[f"{chars['player']['party'][0]}"]
                    if player["hp"] <= 0:
                        print(f"{player['nameColor'] + player['name']} \033[1;31;40mis down...")
                        time.sleep(1)
                        went_back = False
                        playerTurn += 1
                        continue
                
                case 3:
                    player = chars[f"{chars['player']['party'][1]}"]
                    if player["hp"] <= 0:
                        print(f"{player['nameColor'] + player['name']} \033[1;31;40mis down...")
                        time.sleep(1)
                        went_back = False
                        playerTurn += 1
                        continue

                case 4:
                    playerTurn -= 3
                    player = chars["player"]
                case _:
                    print("this shouldn't be possible i think...")

        if went_back == False:
            if len(enemy["effects"]) > 0:
                if "aid_enemy" in enemy["effects"]:
                    dmg = randint(chars["edward"]["spells"]["aid_enemy"]["atk"][0], chars["edward"]["spells"]["aid_enemy"]["atk"][1])
                    enemy["hp"] -= dmg
                    print(f"{enemy['nameColor'] + enemy['name']} \033[0;37;40mlost \033[1;31;40m{printRoman(dmg)} HP \033[0;37;40mfrom AIDS!")
                    time.sleep(1.3)
                    clear()
                    if fuckingDied(enemy, enemy, death_sound)[1]:
                            return False

                if "fuck_you" in enemy["effects"]:
                    if chars["jose"]["specials"]["fuck_you"]["turns"] > 0:
                        enemy["defn"] = enemy["defn"] // 2 if enemy["defn"] != enemy["base_defn"] // 2 else enemy["defn"]
                        chars["jose"]["specials"]["fuck_you"]["turns"] -= 1
                    else:
                        print(f"{enemy['nameColor'] + enemy['name']} \033[0;37;40mhas regained their \033[1;34;40mDEFN\033[0;37;40m!")
                        chars["jose"]["specials"]["fuck_you"]["turns"] = chars["jose"]["specials"]["fuck_you"]["base_turns"]
                        enemy["defn"] = enemy["base_defn"]
                        enemy["effects"].remove("fuck_you")
                        time.sleep(2)

                if "slam_dunk" in enemy["effects"]:
                    if chars["louis"]["specials"]["slam_dunk"]["turns"] > 0:
                        skip_enemy_turn = True
                        enemy["defn"] = enemy["defn"] + (enemy["defn"] // 4) if enemy["defn"] != enemy["base_defn"] + (enemy["base_defn"] // 4) else enemy["defn"]
                        chars["louis"]["specials"]["slam_dunk"]["turns"] -= 1
                    else:
                        skip_enemy_turn = False
                        print(f"{enemy['nameColor'] + enemy['name']} \033[0;37;40mgot out of the sink!")
                        chars["louis"]["specials"]["slam_dunk"]["turns"] = chars["louis"]["specials"]["slam_dunk"]["base_turns"]
                        enemy["defn"] = enemy["base_defn"]
                        enemy["effects"].remove("slam_dunk")
                        time.sleep(2)
                clear()


            
            if len(chars["player"]["effects"]) > 0:
                if "safe_guard" in chars["player"]["effects"]:
                    if chars["aidan"]["spells"]["safe_guard"]["turns"] > 0:
                        chars["aidan"]["spells"]["safe_guard"]["turns"] -= 1
                    else:
                        print(f"{chars['aidan']['nameColor'] + chars['aidan']['name']}'s \033[0;37;40m Safe Guard went down...")
                        chars["aidan"]["spells"]["safe_guard"]["turns"] = chars["aidan"]["spells"]["safe_guard"]["base_turns"]
                        chars["player"]["defn"] = chars["player"]["base_defn"]
                        chars[f"{chars['player']['party'][0]}"]["defn"] = chars[f"{chars['player']['party'][0]}"]["base_defn"]
                        chars[f"{chars['player']['party'][1]}"]["defn"] = chars[f"{chars['player']['party'][1]}"]["base_defn"]
                        chars["player"]["effects"].remove("safe_guard")
                        time.sleep(2)
                clear()

        if chars["player"]["mana"] >= 100:
            chars["player"]["mana"] = 100

        print(f"{enemy['nameColor'] + enemy['name']} \t \033[1;31;40mHP: {printRoman(enemy['hp'])}/{printRoman(enemy['base_hp'])}\033[0;37;40m")
        if settings["debug"]:
            print(f"\033[1;35;40m{enemy['effects']} \t \033[0;31;40mATK: {enemy['atk']}/{enemy['base_atk']} \t \033[1;34;40mDEFN: {enemy['defn']}/{enemy['base_defn']} \t\t \033[1;36;40mSkip turn: {skip_enemy_turn}\033[0;37;40m")
        #normal = choice(enemy["dialogue"])
        
        print(f"\n{dialogue[enemy['name'].casefold()]['intro'] if introDialogue else choice(dialogue[enemy['name'].casefold()]['dialogue'])}")
        introDialogue = False if introDialogue else False
        
        magicCol = "\033[1;35;40m" if player["has_magic"] else "\033[0;31;40m"
        if not player["has_magic"]:
            magicCol = "\033[38;5;242m" if player["specials"] == None else "\033[0;31;40m"

        hpCol = "\033[1;31;40m" if player["hp"] <= player["base_hp"] else "\033[1;32;40m"
        print(f"\n\033[1;31;40m{printRoman(1)}. Attack        {magicCol}{printRoman(2)}. {'Magic' if player['has_magic'] else 'Specials'}{'        ' if player['has_magic'] else '     '}\033[1;32;40m{printRoman(3)}. Items        \033[1;33;40m{printRoman(4)}. Forfeit\033[0;37;40m")
        print(f"{player['nameColor'] + player['name']} \t\t \033[1;32;40mLV: {printRoman(player['lv'])} {hpCol} \t HP: {printRoman(player['hp'])}/{printRoman(player['base_hp'])} \t \033[1;33;40mMana: {printRoman(chars['player']['mana'])}\033[0;37;40m")
        action = input("What to do? (\033[1;34;40mNumber\033[0;37;40m): ")
        match action:
            case action if "1" in action: # 1 in action
                clear()
                attack(player, enemy)
                time.sleep(1)
                if fuckingDied(enemy, enemy, death_sound)[0]:
                    return False
                else:
                    if not skip_enemy_turn:
                        attack(enemy, player)
                        time.sleep(1)
                    dieQuit = fuckingDied(player, enemy, death_sound)
                    match dieQuit:
                        case died if died[0]: # First in tuple is player died, second is will quit or not
                            if dieQuit[1]:
                                return True
                            else:
                                sys.exit()
                        case _:
                            pass

                    went_back = False
                    if partyBattle:
                        playerTurn += 1
                    continue
        
            case action if "2" in action: # 2 in action
                if player["has_magic"]:
                    clear()
                    spellOpts = []
                    actual_names = []
                    spell_num = 1
                    for spell in player["spells"]:
                        print(f"{printRoman(spell_num)}. {player['spells'][spell]['name']}    \033[1;33;40m{printRoman(player['spells'][spell]['mana_cost'])}\033[0;37;40m        ", end="")
                        spellOpts.append(player["spells"][spell]["name"])
                        actual_names.append(spell)
                        spell_num += 1
                    print(f"{printRoman(3)}. \033[1;33;40mGo back")



                    spell_select = input(f"\n\033[0;37;40mWhich two spells should {player['nameColor'] + player['name']} \033[0;37;40mcast? (\033[1;34;40mNumber\033[0;37;40m): ")
                    match spell_select:
                        case spell_select if "1" in spell_select or "2" in spell_select:
                            
                            index = int(spell_select[0]) - 1

                            if chars["player"]["mana"] < player["spells"][actual_names[index]]["mana_cost"]:
                                print("\033[1;31;40mNot enough mana...")
                                time.sleep(0.5)
                                went_back = True
                                continue

                            if player["spells"][f"{actual_names[index]}"]["offensive"]:
                                print()
                                if cast_spell(player, f"{actual_names[index]}", enemy, enemy, death_sound):
                                    return False
                                
                                if player["spells"][f"{actual_names[index]}"]["lingers"] and not actual_names[index] in enemy["effects"]:
                                    enemy["effects"].append(actual_names[index])
                                clear()
                                if not skip_enemy_turn:
                                    attack(enemy, player)
                                    time.sleep(1)
                                dieQuit = fuckingDied(player, enemy, death_sound)
                                match dieQuit:
                                    case died if died[0]: # First in tuple is player died, second is will quit or not
                                        if dieQuit[1]:
                                            return True
                                        else:
                                            sys.exit()
                                    case _:
                                        pass

                                went_back = True
                                if partyBattle:
                                    playerTurn += 1
                                continue
                
                            else:
                                clear()
                                member_1 = chars["player"]["party"][0]
                                member_2 = chars["player"]["party"][1]
                                if not player["spells"][f"{actual_names[index]}"]["partyWide"]:
                                    print(f"{printRoman(1)}. {chars['player']['nameColor'] + chars['player']['name']}    \033[1;31;40mHP: {printRoman(chars['player']['hp'])}/{printRoman(chars['player']['base_hp'])},    \033[0;31;40mATK: {printRoman(chars['player']['atk'])},    \033[1;34;40mDEFN: {printRoman(chars['player']['defn'])}\033[0;37;40m")
                                    print(f"{printRoman(2)}. {chars[member_1]['nameColor'] + chars[member_1]['name']}    \033[1;31;40mHP: {printRoman(chars[member_1]['hp'])}/{printRoman(chars[member_1]['base_hp'])},    \033[0;31;40mATK: {printRoman(chars[member_1]['atk'])},    \033[1;34;40mDEFN: {printRoman(chars[member_1]['defn'])}\033[0;37;40m")
                                    print(f"{printRoman(3)}. {chars[member_2]['nameColor'] + chars[member_2]['name']}    \033[1;31;40mHP: {printRoman(chars[member_2]['hp'])}/{printRoman(chars[member_2]['base_hp'])},    \033[0;31;40mATK: {printRoman(chars[member_2]['atk'])},    \033[1;34;40mDEFN: {printRoman(chars[member_2]['defn'])}\033[0;37;40m")
                                    
                                    help_select = input(f"Who will {player['nameColor'] + player['name']}\033[0;37;40m cast a spell on? (\033[1;34;40mNumber\033[0;37;40m or \033[1;31;40m\"c\" \033[0;37;40mto \033[1;31;40mcancel\033[0;37;40m): ").strip()
                                    match help_select.casefold():
                                        case "c":
                                            went_back = True
                                            continue
                                        
                                        case help_select if "1" in help_select:
                                            helped = chars["player"]
                                        
                                        case help_select if "2" in help_select:
                                            helped = chars["player"]["party"][0]
                                        
                                        case help_select if "3" in help_select:
                                            helped = chars["player"]["party"][1]
                                        
                                        case _:
                                            went_back = True
                                            invalidInput(1500)
                                            time.sleep(1)
                                            continue
                                    print("")
                                    print()
                                    if cast_spell(player, f"{actual_names[index]}", helped, enemy, death_sound):
                                        return True
                                else:
                                    if cast_spell(chars["player"], f"{actual_names[index]}", helped, enemy, death_sound):
                                        return True
                                    if cast_spell(chars[member_1], f"{actual_names[index]}", helped, enemy, death_sound):
                                        return True
                                    if cast_spell(chars[member_2], f"{actual_names[index]}", helped, enemy, death_sound):
                                        return True
                                
                                clear()
                                if not skip_enemy_turn:
                                    attack(enemy, player)
                                    time.sleep(1)
                                dieQuit = fuckingDied(player, enemy, death_sound)
                                match dieQuit:
                                    case died if died[0]: # First in tuple is player died, second is will quit or not
                                        if dieQuit[1]:
                                            return True
                                        else:
                                            sys.exit()
                                    case _:
                                        pass

                                went_back = True
                                if partyBattle:
                                    playerTurn += 1
                                continue
                        
                        case spell_select if "3" in spell_select:
                            went_back = True
                            continue
                        
                        case _:
                            went_back = True
                            # invalidInput(1244)
                            print("\033[1;31;40mPlease pick a \033[1;34;40mnumber \033[1;31;40mfrom \033[1;34;40m1-3.\033[0;37;40m")
                            time.sleep(1)
                            continue   

                else:
                    if player["specials"] == None:
                        print(f"\033[1;31;40m{player['nameColor'] + player['name']} \033[1;31;40mdoesn't have any specials...")
                        time.sleep(1.3)
                        continue
                    specialOpts = []
                    actual_names = []
                    special_num = 1
                    clear()
                    for special in player["specials"]:
                        print(f"{printRoman(special_num)}. {player['specials'][special]['name']}    \033[1;33;40m{printRoman(player['specials'][special]['mana_cost'])}\033[0;37;40m        ", end="")
                        specialOpts.append(player["specials"][special]["name"])
                        actual_names.append(special)
                        special_num += 1
                    print(f"{printRoman(3)}. \033[1;33;40mGo back")

                    special_select = input(f"\n\033[0;37;40mWhich two specials should {player['nameColor'] + player['name']} \033[0;37;40muse? (\033[1;34;40mNumber\033[0;37;40m): ")
                    match special_select:
                        case special_select if "1" in special_select or "2" in special_select:
                            
                            index = int(special_select[0]) - 1

                            if chars["player"]["mana"] < player["specials"][actual_names[index]]["mana_cost"]:
                                print("\033[1;31;40mNot enough mana...")
                                time.sleep(0.5)
                                went_back = True
                                continue
                            if use_special(player, f"{actual_names[index]}", enemy, enemy, death_sound):
                                return True
                            

                            if player["specials"][f"{actual_names[index]}"]["lingers"] and not actual_names[index] in enemy["effects"]:
                                    enemy["effects"].append(actual_names[index])
                            
                            input("\nPress \033[1;33;40m\"Enter\"\033[0;37;40m to continue: ")
                            clear()
                            if not skip_enemy_turn:
                                attack(enemy, player)
                                time.sleep(1)
                            dieQuit = fuckingDied(player, enemy, death_sound)
                            match dieQuit:
                                case died if died[0]: # First in tuple is player died, second is will quit or not
                                    if dieQuit[1]:
                                        return True
                                    else:
                                        sys.exit()
                                case _:
                                    pass

                            went_back = False
                            if partyBattle:
                                playerTurn += 1
                            continue
                        
                        case special_select if "3" in special_select:
                            went_back= True
                            continue

                        case _:
                            invalidInput(1604)
                            time.sleep(1)
                            went_back = True
                            continue

            case action if "3" in action: # 3 in action
                invent_display(0.01)
                print(f"\n\033[1;32;40m{printRoman(1)}. Use    \033[1;34;40m{printRoman(2)}. Inspect    \033[1;33;40m{printRoman(3)}. Go back")
                inventAct = input("\033[0;37;40mWhat to do? (\033[1;34;40mNumber\033[0;37;40m): ")

                match inventAct:
                    case inventAct if "1" in inventAct:
                        clear()
                        invent_display()
                        choose = input("\nWhich would you like to \033[1;32;40muse\033[0;37;40m? (\033[1;34;40mNumber\033[0;37;40m or \033[1;31;40m\"c\" \033[0;37;40mto cancel): ")
                        if choose.isnumeric():
                            choose = int(choose)
                            choose -= 1
                            if 0 <= choose <= 11:
                                itemName = chars["player"]["inventory"][choose]
                                item = chars["player"]["inventory"][choose].casefold()
                                if itemName != "Empty":
                                    print(f"\nYou used the {itemName}.\n")
                                    time.sleep(1)
                                    player["hp"] += items[item]["hp"]
                                    player["base_atk"][0] += items[item]["atk"]
                                    player["base_atk"][1] = player["base_atk"][0] + 5
                                    player["defn"] += items[item]["defn"]

                                    match player["hp"]:
                                        case hp if hp <= 0:
                                            dieQuit = fuckingDied(player, enemy, death_sound)
                                            match dieQuit:
                                                case died if died[0]: # First in tuple is player died, second is will quit or not
                                                    if dieQuit[1]:
                                                        return True
                                                    else:
                                                        sys.exit()
                                                case _:
                                                    pass
                                        case _:
                                            pass
                                    
                                    match items[item]["hp"]:
                                        case hp if hp > 0:
                                            if player["hp"] > player["base_hp"]:
                                                if player["hp"] > player["base_hp"] + (player["base_hp"] // 4):
                                                    print(f"\033[1;32;40mGained {printRoman(items[item]['hp'])} HP! (MAX HP)\033[0;37;40m")
                                                else:
                                                    print(f"\033[1;32;40mGained {printRoman(items[item]['hp'])} HP! ({'OVERHEAL' if player['hp'] > player['base_hp'] else ''})\033[0;37;40m")
                                            else:
                                                print(f"\033[1;32;40mGained {printRoman(items[item]['hp'])} HP!\033[0;37;40m")
                                            time.sleep(0.3)
                                        case _:
                                            if items[item]["hp"] == 0:
                                                pass
                                            if items[item]["hp"] < 0:
                                                print(f"\033[0;31;40mLost {printRoman(items[item]['hp'])} HP...")
                                                time.sleep(0.3)
                                    
                                    match items[item]["atk"]:
                                        case atk if atk > 0:
                                            print(f"\033[1;31;40mGained {printRoman(items[item]['atk'])} ATK!\033[0;37;40m")
                                            time.sleep(0.3)
                                        case _:
                                            pass

                                    match items[item]["defn"]:
                                        case defn if defn > 0:
                                            print(f"\033[1;34;40mGained {printRoman(items[item]['defn'])} DEF!\033[0;37;40m")
                                            time.sleep(0.3)
                                        case _:
                                            pass 
                                    
                                    invent_sub(choose)
                                    input("\nPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")

                                    clear()
                                    if not skip_enemy_turn:
                                        attack(enemy, player)
                                        time.sleep(1)
                                    dieQuit = fuckingDied(player, enemy, death_sound)
                                    match dieQuit:
                                        case died if died[0]: # First in tuple is player died, second is will quit or not
                                            if dieQuit[1]:
                                                return True
                                            else:
                                                sys.exit()
                                        case _:
                                            pass
                                    
                                    went_back = False
                                    if partyBattle:
                                        playerTurn += 1
                                    continue
                                
                                else:
                                    went_back = True
                                    print("\n\033[1;31;40mNo item in slot.")
                                    time.sleep(1)
                                    continue
                            else:
                                went_back = True
                                print("\033[1;31;40mPlease pick a number between 1 to 12.\033[0;37;40m")
                                time.sleep(1)
                                continue

                        else:
                            went_back = True
                            if choose.casefold() == "c":
                                continue 
                            else:
                                print("\033[1;31;40mPlease choose a number.\033[0;37;40m")
                                time.sleep(1)
                                continue

                    case inventAct if "2" in inventAct:
                        clear()
                        invent_display()
                        choose = input("\nWhat would you like to \033[1;34;40minspect\033[0;37;40m? (\033[1;34;40mNumber\033[0;37;40m or \033[1;31;40m\"c\" \033[0;37;40mto cancel): ")
                        if choose.isnumeric():
                            
                            choose = int(choose)
                            choose -= 1
                            if 0 <= choose <= 11:
                                itemName = chars["player"]["inventory"][choose]
                                if itemName != "Empty":
                                    itemName = chars["player"]["inventory"][choose]
                                    thing_inspect(itemName)
                                    time.sleep(1)
                                    input("\n\n\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                                    went_back = True
                                    continue
                                else:
                                    went_back = True
                                    print("\n\033[1;31;40mNo item in slot.")
                                    time.sleep(1)
                                    continue
                            else:
                                went_back = True
                                print("\033[1;31;40mPlease pick a number between 1 to 12.\033[0;37;40m")
                                time.sleep(1)
                                continue

                        else:
                            went_back = True
                            if choose.casefold() == "c":
                                continue
                            else:
                                print("\033[1;31;40mPlease choose a number.\033[0;37;40m")
                                time.sleep(1)
                                continue

                    case inventAct if "3" in inventAct:
                        went_back = True
                        continue

                    case _:
                        went_back = True
                        invalidInput(1763)
                        time.sleep(1)
                        continue
            
            case action if "4" in action: # 4 in action
                clear()
                flee = input("Are you SURE you want to flee? (\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m): ")
                match flee.casefold():
                    case "y":
                        fleeChance = randint(1, 3)
                        if fleeChance == 1 or fleeChance == 2:
                            print(f"\n{player['nameColor'] + player['name']} \033[0;37;40mfled the battle...")
                            musicInOut(1300, 1.35)
                            # I was a victim of magic, apollo, catching my breath as I bled on the ground
                            player["defn"] = player["base_defn"]
                            player["atk"] = player["base_atk"]
                            enemy["hp"] = enemy["base_hp"]
                            enemy["atk"] = enemy["base_atk"][0]
                            enemy["defn"] = enemy["base_defn"]

                            chars["aidan"]["spells"]["safe_guard"]["turns"] = 6
                            chars["jose"]["specials"]["fuck_you_ii"]["turns"] = 6

                            enemy["effects"] = []
                            return
                        else:
                            went_back = True
                            message = randint(1, 15)
                            if message == 9 or message == 4:
                                print("\033[1;31;40m WHO ARE YOU RUNNING FROM?")
                            else:
                                print("\nCouldn't flee!")
                            time.sleep(1)
                            continue
                    
                    case "n":
                        went_back = True
                        print("\nAlright, you can do this!")
                        time.sleep(1)
                        continue

                    case _:
                        went_back = True
                        invalidInput(1809)
                        continue

            case action if "5" in action: # 5 in action
                match action[-1]:
                    case "6":
                        if not skip_enemy_turn:
                            attack(enemy, player)
                        if player["hp"] <= 0:
                            dieQuit = fuckingDied(player, enemy, death_sound)
                            match dieQuit:
                                case died if died[0]: # First in tuple is player died, second is will quit or not
                                    if dieQuit[1]:
                                        return True
                                    else:
                                        sys.exit()
                                case _:
                                    pass
                    
                    case "7":
                        chars["player"]["mana"] = 100

                    case "0":
                        player["hp"] = player["hp"]// 4
                        player["defn"] = 0
                # The package which this comes with is absoluetly not compatible
                # with whatever it is you're using 
                went_back = False
                if partyBattle:
                    playerTurn += 1
                    continue
                else:
                    continue

            case _:
                went_back = True
                invalidInput(1837)
                time.sleep(1.3)
                continue


def saveAll():
    if "sound" in os.getcwd():
        os.chdir("../")
    save("chars.json", chars)
    save("extra_data.json", extra_data)
    save("settings.json", settings)
    save("nodel.json", nodel)

def pogSaver():
    while True:
        ask = input("\033[1;32;40mWould you like to save your progress(\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m)?: ").strip()
        if ask.casefold() == "y":
            clear()
            print("\033[1;32;40mAlright!")
            time.sleep(0.5)
            print("Saving progress...")
            time.sleep(1)
            saveAll()
            print("\nDone!")
            time.sleep(0.5)
            print("Enjoy the demo!")
            input("\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
            return

        if ask.casefold() == "n":
            doubleAsk = input("\033[1;32;40mAre you SURE you don't want to save(\033[1;31;40my\033[0;37;40m/\033[1;32;40mn\033[0;37;40m)?: ").strip()
            if doubleAsk.casefold() == "y":
                clear()
                print("\033[1;32;40mAlright then!")
                time.sleep(1)
                print("Don't come crying to me when you get far and come all the way back to this point!")
                input("\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                return
            
            if doubleAsk.casefold() == "n":
                clear()
                triple = input("Then will you save(\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m)?: ").strip()
                if triple.casefold() == "y":
                    clear()
                    print("\033[1;32;40mSmart choice!")
                    time.sleep(1)
                    print("Okay, saving your progres...")
                    time.sleep(1)
                    saveAll()
                    print("\nDone!")
                    time.sleep(0.5)
                    print("Enjoy the rest of the demo!")
                    input("\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                    return
                
                if triple.casefold() == "n":
                    clear()
                    print("\033[1;32;40mThen why'd you say you unsure in the first-")
                    time.sleep(2)
                    print("...")
                    time.sleep(1)
                    print("...Anyway,")
                    time.sleep(1)
                    print("Just don't come to my doorstep-")
                    time.sleep(0.5)
                    print("-Er, keyboard I guess??-")
                    time.sleep(1)
                    print("Sobbing and complaining to me that you got sent back here.")
                    time.sleep(2.5)
                    
                    input("\nGot it\033[0;37;40m(y/n)?: ")
                    clear()
                    
                    print("\033[1;32;40mDOESN'T MATTER!")
                    time.sleep(1)
                    print("Just, enjoy the demo.")
                    input("\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                    return
                
                else:
                    invalidInput(1917)
                    time.sleep(1)
                    clear()
                    continue
            else:
                invalidInput(1922)
                time.sleep(1)
                clear()
                continue
        else:
            invalidInput(1927)
            time.sleep(1)
            clear()
            continue

def you_suck(player, enemy, partyBattle=False, music=["battle", 0, None]):
    prevInv = chars["player"]["inventory"][:]
    # print(prevInv)
    for i in range(2):
        if battle(player, enemy, partyBattle, music):
            chars["player"]["inventory"] = prevInv
            full_recover()
            spell_turn_reset()

        else:
            spell_turn_reset()
            return False

    if battle(player, enemy, partyBattle, music):
        if randint(1, 64) == 37:
            print("\033[1;32;40m", end="")
            say("\nTOO", 0)
            time.sleep(0.05)
            say(" BAD,", 0)
            time.sleep(0.1)
            say(" bitch.")
            time.sleep(1.3)
            clear()
            sys.exit()
        else:
            print("\033[1;32;40m", end="")
            say("Sorry, three chances only!")
            time.sleep(0.5)
            say("\nTo the beginning of the segment you go.")
            time.sleep(1)
            full_recover()
            spell_turn_reset()
            return True

#################
### SEGMENT 2 ###
#################
def seg_2_end():
    playMusic("credits", ogg=False)
    clear()
    print("\nSeg 2 END")
    clear()
    print("CREDITS:")
    print(f"""\tNON-EXISTANT STORY:
\t\t\033[1;35;40mME\033[0;37;40m

\tCONCEPTUALIZATION:
\t\t\033[1;35;40mME\033[0;37;40m

\tPROGRAMMING:
\t\t\033[1;35;40mME\033[0;37;40m

\tMUSIC:
\t\t99% stolen (sorry/not sorry toby fox, jean-jacques, tally hall and the real zebos)
\t\tOh yeah and sorry/not sorry \033[1;33;40m{myLord('Josie')} \033[0;37;40mfor stealing like less than second of you talking
\t\tabout your dad buying you your guitar or something.
\t\tIt's all just placeholder stuff, don't worry
\t\t(if you don't know what I meant by that, it's the \"voice.ogg\" file in\n\t\tthe \"sound\" folder)


\tLITERALLY EVERYTHING ELSE IN THIS GOD FORESAKEN GAME:
\t\t\033[1;35;40mME\033[0;37;40m
""")
    nodel["times_completed"] += 1
    nodel["prev_name"]= chars["player"]["name"]
    save("nodel.json", nodel)
    save("extra_data.json", extra_data)
    time.sleep(90.2)
    print("k now fuck off")

    sys.exit()

def seg_2_mid():
    clear()
    print("\nSeg 2 mid")
    extra_data["progress"]["seg_2_end"] = True
    if not settings["hard_mode"]:
        pogSaver()
    seg_2_end()
    
def seg_2_beg():
    clear()

    print("\n\n\nSeg 2 beg")
    extra_data["progress"]["seg_2_mid"] = True
    if not settings["hard_mode"]:
        pogSaver()
    seg_2_mid()



#################
### SEGMENT 1 ###
#################
def seg_1_end():
    while True:
        clear()
        chars["player"]["party"][0] = "aidan"
        if you_suck(chars["player"], chars["driver d."], True):
            continue
        
        print("\nSeg 1 END")
        extra_data["progress"]["seg_2_beg"] = True
        if not settings["hard_mode"]:
            pogSaver()
        seg_2_beg()

def seg_1_mid():
    returned = False
    
    while True:
        clear()
        if returned:
            invent_reset(("Dildo", "McIntosh", "Popsicle", "Popsicle"))

        if you_suck(chars["player"], chars[myLord("josie")], True, ["battle", 0, "josie_death.ogg"]):
            returned = True
            continue
        
        say(myLord("Josie dropped her...", 0.05))
        time.sleep(1.5)
        print(censor(" DILDO????"))
        time.sleep(2)
        say("Let's just move on.")
        time.sleep(1.3)
        invent_add(items[censor("dildo")])
        print(censor(myLord(f"\n(Josie's Dildo has been added to your items.)")))
        invent_add(items["mcintosh"])
        invent_add(items["popsicle"])
        invent_add(items["popsicle"])
        time.sleep(2.3)
        clear()
        
        if you_suck(chars["player"], chars["joe hawley"], True, ["battle", 0, "mind_of_simon.ogg"]):
            returned = True
            continue

        print("\nSeg 1 mid")
        extra_data["progress"]["seg_1_end"] = True
        if not settings["hard_mode"]:
            pogSaver()
        seg_1_end()
    
def seg_1_beg():
    returned = False

    while True:
        clear()
        if returned:
            chars["player"]["Inventory"] = ["Empty"] * 12

        invent_add(items["feces"])
        invent_add(items["pizza"])
        invent_add(items["popsicle"])
        invent_add(items["window"])
        
        
        chars["player"]["party"][0], chars["player"]["party"][1] = "jose", "louis"
        if you_suck(chars["player"], chars["monkey"], False, ["gypsy_in_rio", 8.45, None]):
            returned = True
            continue
        
        invent_add(items["popsicle"])
        invent_add(items["apple"])
        invent_add(items["pizza"])
        # print(len(traceback.extract_stack()))
        print("Seg 1 beg")
        extra_data["progress"]["seg_1_mid"] = True
        if not settings["hard_mode"]:
            pogSaver()
        seg_1_mid()



def progress_check():
    if extra_data["progress"]["seg_2_end"]:
        seg_2_end()

    if extra_data["progress"]["seg_2_mid"]:
        seg_2_mid()

    if extra_data["progress"]["seg_2_beg"]:
        seg_2_beg()

    if extra_data["progress"]["seg_1_end"]:
        seg_1_end()

    if extra_data["progress"]["seg_1_mid"]:
        seg_1_mid()

    if extra_data["progress"]["seg_1_beg"]:
        seg_1_beg()
    
    else:
        print("\033[1;31;40mDoes not compute!")
        pprint(extra_data["progress"])


def name_check(name):
    clear()
    forbidden = ("chantal", "marcus", "valerie")
    match name.casefold():
        case "jose":
            time.sleep(0.5)
            say("\033[1;34;40mListen here, bitch:", voice="sans", chrigger=2)
            time.sleep(0.5)
            say("\nI will personally grab your nose,", voice="sans", chrigger=2)
            time.sleep(0.3)
            say(" rip it off your fucking face,", voice="sans", chrigger=2)
            time.sleep(0.3)
            say("\ndip it into soy sauce,", voice="sans", chrigger=2)
            time.sleep(0.3)
            say(" and eat your fucking nose.", voice="sans", chrigger=2)
            time.sleep(0.25)
            say("\n\nThat's right,", voice="sans", chrigger=2),
            time.sleep(0.3)
            say(" I'm gonna eat your nose with soy sauce,", voice="sans", chrigger=2)
            time.sleep(0.3)
            say(" and there's not a\ngod damn thing you can do about it.", voice="sans", chrigger=2)
            time.sleep(0.3)
            say("\nWanna know why?", voice="sans", chrigger=2)
            time.sleep(0.8)
            say(" Because your nose was fucking ripped off.", voice="sans", chrigger=2)
            time.sleep(0.3)
            print("\n\n", end="")
            say("\033[1;36;40mI'M JOSE,", 0.04, "sans", chrigger=2)
            time.sleep(0.2)
            say(" NOT YOU,", 0.015, "sans", chrigger=2)
            time.sleep(0.3)
            say("\nFUCKING NO LIFE LOSER", voice="sans", chrigger=2)
            time.sleep(1)
            return True
    
        case "josie":
            if random() == 1:
                time.sleep(0.3)
                say("Y'know,")
                time.sleep(0.2)
                say(" you're a stupid fucking bitch but")
                say("...", 0.08)
                time.sleep(0.02)
                say("\nI don't COMPLETELY hate you,")
                time.sleep(0.2)
                say(" so I'll let you play.")
                time.sleep(1.2)
                return True
            else:
                say("You acknowledge that from this point onward your life will be made a living hell,")
                time.sleep(0.15)
                say(" correct?")
                time.sleep(1)
                contin = input("\nDo you agree to this(\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m)?: ").strip().casefold()
                if contin == "y":
                    settings["hard_mode"] = True
                    save("settings.json", settings)
                    clear()
                    return False
                if contin == "n":
                    pass
                    return True
                else:
                    invalidInput(2159)
                    return True

        case "ofi":
            time.sleep(0.5)
            print("\033[1;37;40mWait wait, WHAT!?")
            time.sleep(2)
            print("You're naming yourself... MYself???")
            time.sleep(3)
            print()
            for i in range(3):
                say("...")
                time.sleep(0.5)
            time.sleep(1)
            
            clear()
            
            print("N", end="", flush=True)
            say("O"*1024)
            print("!")
            time.sleep(2.5)
            
            clear()

            exclamations = randint(8, 46)
            print("That's MY name WHY would you do that????????", end="")
            say("!" * exclamations, 0.04)
            print("1")

            time.sleep(3.5)

            clear()
            exclamations = randint(3, 16)
            print("I'm not sure if you've heard this, but", end="")
            say("." * exclamations, 0.03)
            time.sleep(5)
            print("I could kill you an instant, do NOT fuck with me.")
            time.sleep(5)
            print("I'll turn into my wolf OC and I'll fill your jiggly wiggly-")
            time.sleep(5.3)
            print("\n\033[0;37;40mHuh?")
            time.sleep(1)
            print("What do you MEAN too extreme??")
            time.sleep(2)
            print("UGH, fine...")
            time.sleep(2)
            print("\033[1;37;40mSorry about that, I was just kidding!")
            time.sleep(2)
            print("Just, name yourself something else and enjoy the demo! :)")
            time.sleep(3.5)
            input("\n\033[0;37;40mwh... Press \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
            return True

        case "diego":
            say("Alright")
            say(" you doughy bitch," if random() == 1 else myLord("josie,"))
            time.sleep(5)
            return True

        case "captain" | "khelian" | "ice" | "virgin":
            say("Leader of the virgin squad, ")
            time.sleep(0.1)
            say("right?")
            time.sleep(1)
            print("\n")
            say("...", 0.1)
            time.sleep(0.5)
            say("Yeah, no.")
            time.sleep(1)
            sys.exit()
            return True

        case "venus":
            sys.exit()
            return True

        case name if name in forbidden:
            time.sleep(0.5)
            say("Oh ew.")
            time.sleep(1)
            say("\nYeah you're not allowed to play.")
            time.sleep(1)
            clear()
            sys.exit()

        case _:
            return False

def nmtn():
    say("All")
    say(" the parts")
    say(" combine")
    say(" to one")
    say(" and all")
    say(" of us")
    say(" around")
    say(" the sun")
    
    say("Ev")
    say("erything")
    say(" will fall")
    say(" away")
    say(" from order")
    say(" to")
    say("the dis")
    say("array")

    say("See")
    say(" the sun")
    say(" the sha")
    say("dows cast")
    say(" from all")
    say(" the times")
    say(" I")
    say(" floa")
    say("ted past")
    
    say("See")
    say(" the o")
    say("cean")
    say("spin")
    say("ning out")
    say(" with all")
    say(" the hope")
    say(" and all")
    say(" the doubt")
    
    say("See")
    say(" the sky")
    say(" and all")
    say(" the land")
    say(" together")
    say(" again")
    
    say("See")
    say(" the way")
    say(" the earth")
    say(" can")
    say(" stay")
    say(" be")
    say("low")

    say("Who do we")
    say(" think")
    say(" we")
    say(" are?")

    say("Everything")
    say(" plays")
    say(" a")
    say(" part")

    say("There are")
    say(" some")
    say(" things")
    say(" we don't")
    say(" under")
    say("stand,")
    say(" rea")
    say("sons")
    say(" on")
    say("the other hand,")

    say("There are")
    say(" some")
    say(" things")
    say(" we are")
    say(" never meant")
    say(" to know")

if __name__ == "__main__":
    def update():
        setAll()
        saveAll()

    ### Checks if any files are missing ### 
    missing_files = []
    files = ("chars.json", "extra_data.json", "settings.json", "nodel.json")
    for file in files:
        if not os.path.exists(file):
            missing_files.append(file)

    if len(missing_files) > 0:
        print("Wow, you really removed the ")
        for index, file in enumerate(missing_files):
            print(f"{file}, " if not index == len(missing_files) - 1 else f"and {file} files?", end=" ")

        time.sleep(2.5)
        insults = ("Asshole.", "Piece of shit.", "Dumbass.")
        print(f"\n{choice(insults)}")
        time.sleep(2)
        clear()
        sys.exit()

    time.sleep(1)
    extra_data["secret"]["interest"] = 0
    match extra_data["secret"]["interest"]:
        case 0:
            '''
            def dona():
                for i in range(3):
                    print()
                print("""
                                  $$$$$$$$$@@@@@
                              $$$$#############$$$$$
                            ####***!!****!*****#*##$$$#
                          ##****!!!=========!!*****#####
                        ******!!==;;;::::::;;;=!!*****###*
                       !****!!==;::~--,,,,--~~:;=!!*****#**
                      =***!!!==::~-.........,-~:;==!*!*****!
                      !!*!!!==;:~,............,~:;==!!*****!
                      !!!!!!==;:-,..        ..,-:;==!!!***!!;
                      !!!!!!!=;:~,.          .,~:;==!!!!*!!!;
                      =!!****!!!!=:          -:;;;=!!!!!!!!=;
                      =!!!*********!~       ;===!!!!!!!!!!!=~
                      :=!!***#####$$###*!************!!!!==;
                       ;=!***###$$$@@@@$$$$$####****!!!!==;-
                       -:=!****##$$$@@@@@$$$$###****!!!=;:~
                         ~;=!****###$$$$$$$###****!!!==;:-
                          ~:;=!*!!****####*****!!!===;:~
                            -~;;=!!****!!**!!!!===;:~-
                              .-~:;;;======;;;;::~-.
                                  ..,--------,,.
                
                

                """)
            if isWindows:
                print("You're running windows? fucking cuck, no spinning donut for you")
                time.sleep(5)
            else:
                time.sleep(1)
                playMusic("DONUT", 2)
                
                os.system(f"cd {os.getcwd()}; {'start donut.exe' if isWindows else './donut.out'}")
                mixer.music.fadeout(2800)
                print("\033[38;5;240m", end ="")
                clear()
                dona()
                time.sleep(1)
                print("\033[38;5;234m", end="")
                clear()
                dona()
                time.sleep(0.8)
        '''
            pass
        

        case 15:
            playMusic("ofi_orgasm")

        case 23:
            playMusic(f"goofy_{randint(0, 3)}" if not randint(1, 23) == 15 else "mind_of_simon")

        case 64:
            if settings["sound"]:
                playMusic("MysteryThemeLoop")
                mixer.music.queue("sound/MysteryTheme.ogg")
                mixer.music.unload()
                clear()
                print("\033[0;35;40m???\033[0;37;40m")
                time.sleep((48*2) + 4)
                clear()

        case _:
            pass
    change_title("Almonds Prototype")
    while True:
        clear()
        try:
            with open("chars.json", "r") as f:
                chars = json.load(f)
            with open("extra_data.json", "r") as f:
                extra_data = json.load(f)
            with open("settings.json", "r") as f:
                settings = json.load(f)
            with open("nodel.json", "r") as f:
                nodel = json.load(f)

            #extra_data = load("extra_data.json")
            #settings = load("settings.json")
            #nodel = load("nodel.json")

            if chars["player"]["name"] == "Melanie":
                raise json.decoder.JSONDecodeError("", "", 0)

            mixer.music.set_volume(settings["musicVolume"])
            space = " " * 36 if not isWindows and defaultSize else " " * 44
            # setAll()

            print(f"\n{space}\033[38;5;130mAlmonds\033[0;37;40m")
            time.sleep(1)
            space = " " * 30 if not isWindows and defaultSize else " " * 39
            print(f"\n{space}{chars['player']['nameColor'] + chars['player']['name']}\n{space}\033[1;32;40mLV: {printRoman(chars['player']['lv'])}\033[0;37;40m")
            
            print(f"{space}{'1.' if not settings['hard_mode'] else 'I.  '} Continue Game\n{space}{'2.' if not settings['hard_mode'] else 'II. '} Clear Save\n{space}{'3.' if not settings['hard_mode'] else 'III.'} Quit\n{space}{'4.' if not settings['hard_mode'] else 'IV. ' } Settings")
            space = " " * 21 if not isWindows and defaultSize else " " * 31

            menuSelect = input(f"\n{space}What would you like to do? (\033[1;34;40mNumber\033[0;37;40m): ")

            if "1" in menuSelect:
                space = None
                base_stat_set()
                full_recover()
                progress_check()
                break
            
            if "2" in menuSelect:
                print("\nDeleting chars.json...")
                with open("chars.json", "w") as f:
                    f.write("")

                # EXCLUSIVE SNEEK PEEK AT THE CODE FOR ALMONDS (not really)
                # I mean it IS the code but is it an exclusive view? Absolutely not, literally ask to look and I'll let you LMAO
                chars["player"]["name"] = "Melanie" # Woah secret name in Almonds WOAHHHHH
                chars["player"]["nameColor"] = "\033[1;32;40m"
                time.sleep(0.2)
                
                print("Deleting extra_data.json...")
                with open("extra_data.json", "w") as f:
                    f.write("")
                
                # extra_data["progress"]["seg_1_beg"] = False
                # extra_data["progress"]["seg_1_mid"] = False
                # extra_data["progress"]["seg_1_end"] = False
                # extra_data["progress"]["seg_2_beg"] = False
                # extra_data["progress"]["seg_2_mid"] = False
                # extra_data["progress"]["seg_2_end"] = False
                # for thing in extra_data["progress"]:
                #     extra_data["progress"][thing] = False

                time.sleep(0.2)

                print("Deleting settings.json...")
                with open("settings.json", "w") as f:
                    f.write("")
                time.sleep(0.2)
                print("\033[1;31;40mSave data erased.")
                time.sleep(1)
                say("\033[1;37;40mPlease restart the game after it closes.", 0.05)
                time.sleep(3)
                update()
                sys.exit()
            
            if "3" in menuSelect:
                clear()
                sys.exit()
            
            if "4" in menuSelect:
                colors = {
                    "bool": {
                        "True": "\033[1;32;40m",
                        "False": "\033[1;31;40m"
                    },

                    "int": "\033[1;34;40m",
                    "float": "\033[1;36;40m"
                }

                hidden = ("debug", "hard_mode")
                dialogue_change = ("naughty")
                access = ""
                while True:
                    clear()
                    if access in dialogue_change:
                        set_items()
                        set_spells()
                        set_specials()
                        for char in dialogue:
                            try:
                                dialogue[char]["intro"] = censor(dialogue[char]["intro"])
                                for line in dialogue[char]["dialogue"]:
                                    dialogue[char]["dialogue"][line] = censor(dialogue[char]["dialogue"][line])
                            except Exception:
                                pass
                        # save("chars.json", chars)
                    save("settings.json", settings)
                    names = []
                    print("Settings: ")
                    for setting in settings:
                        valType = str(type(settings[setting]))
                        forbidden = ("<", ">", "'", " ")
                        for char in forbidden:
                            valType = valType.translate({ord(char):None})
                        valType = valType[5:]

                        names.append(setting)

                        if not setting in hidden:
                            print(f"\t{setting}: {colors[valType] if not valType == 'bool' else colors['bool'][str(settings[setting])]} {settings[setting]}\033[0;37;40m")
                            
                    time.sleep(1)
                    print("\n\033[1;32;40mTo access a setting, \033[1;34;50mtype its name \033[1;31;40mEXACTLY \033[1;32;40mas you see it.")
                    access = input("\033[0;37;40mEnter a setting name (or \033[1;31;40m\"c\" \033[0;37;40mto go back): ")
                    
                    
                    match access:
                        case access if access in names:
                            change = input(f"\nWhat would you like to change {access} to?: ")
                            
                            valType = str(type(settings[access]))
                            for char in forbidden:
                                valType = valType.translate({ord(char):None})
                            valType = valType[5:]

                            match valType:
                                case "bool":
                                    if change.casefold() == "true" or change.casefold() == "false":
                                        settings[access] = True if change.casefold() == "true" else False
                                        continue
                                    else:
                                        print("\n\033[1;31;40mPlease enter \033[1;32;40m\"True\" \033[0;37;40mor \033[0;31;40m\"False.\"\033[0;37;40m")
                                        time.sleep(1.5)
                                        continue
                                
                                case "int":
                                    try:
                                        if change.casefold() == "true" or change.casefold() == "false":
                                            raise ValueError
                                        change = int(change)
                                        settings[access] = change
                                        continue

                                    except ValueError:
                                        print("\n\033[1;31;40mPlease enter a \033[1;34;40mwhole number.\033[0;37;40m")
                                        time.sleep(1)
                                        continue

                                case "float":
                                    try:
                                        if change.casefold() == "true" or change.casefold() == "false":
                                            raise ValueError
                                        change = float(change)
                                        settings[access] = change
                                        continue

                                    except ValueError:
                                        print("\n\033[1;31;40mPlease enter a \033[1;36;40mdecimal number.\033[0;37;40m")
                                        time.sleep(1)
                                        continue
                                case _:
                                    print("impossible burger")

                            continue
                        case "c":
                            break
                        case _:
                            invalidInput(1459)
                            time.sleep(1)
                            continue

                continue

            if "secret" in menuSelect:
                clear()
                print("\033[1;32;40mNo secrets implemented yet,", end="", flush=True)
                time.sleep(1.3)
                print(" sorry.")
                time.sleep(1)
                continue

                print("\033[1;32;40m", end="")
                say("Username: ")
                print("\033[0;37;40m", end="", flush=True)

                if bcrypt.checkpw(bytes(input().casefold(), "utf-8"), b"$2b$12$bIXNyT3fGfeHfNjDdmmbl..gd7WFx.Yb9sC/ViwuBfZhb/Awa0wEq"): # melanie
                    print("\033[1;32;40m", end="", flush=True)
                    say("Password: ")
                    print("\033[0;37;40m", end="", flush=True)
                    passw = bytes(input(), "utf-8")
                    if bcrypt.checkpw(passw, b"$2b$12$2eRQ6r3U4fF56tBEJWrO/OqXGrbw7w6p33KmwO1zM3FWihR2RXLJ6"): # MakeTheRounds
                        subprocess.call([f"{'./secret' if not isWindows else 'secret.exe'}", "O3fMORJEWXBR6rw2$i/O3R6Fq$htwp672zbLU23W2e5QrX$mw61rGb43FJK1", f"{'clear' if not isWindows else 'cls'}"]) # the hash but scrambled + reversed
                        input()
                    else:
                        sys.exit()
                else:
                    sys.exit()

            if "5" in menuSelect:
                while True:
                    clear()
                    save("extra_data.json", extra_data)
                    print(f"Counter: \033[1;33;40m{extra_data['secret']['counter']}\033[0;37;40m")
                    print("(Enter \033[1;35;40m\"r\" \033[0;37;40mto reset)\033[0;37;40m")
                    counter_select = input("\nPress \033[1;33;40m\"Enter\" to increment, \033[0;31;40m\"-\" \033[0;37;40mto decrement, or \033[1;31;40m\"c\" \033[0;37;40m to go back: ").strip().casefold()

                    match counter_select:
                        case "":
                            extra_data["secret"]["counter"] += 1
                            continue
                        
                        case "-":
                            extra_data["secret"]["counter"] -= 1
                            continue
                        
                        case "r":
                            extra_data["secret"]["counter"] = 0
                            continue
                        
                        case "c":
                            break
                        
                        case _:
                            invalidInput(2598)
                            time.sleep(1)
                            continue
                continue
            
            if "name" in menuSelect:
                clear()
                printNames()
                input("\nPress Enter to continue: ")
                continue

            else:
                continue
            
        except json.decoder.JSONDecodeError:#    What are you looking at this comment for, hmmmm?
            with open("nodel.json", "r") as f:
                nodel = json.load(f)
            save("settings.json", settings)
            
            jose_sucks_my_cock_every_sunday_night = True # soooooooooooo true

            coop_is_awesome_for_helping_me_with_saving_data_to_JSON_files = True
            josie_in_almonds_confirmed = "Idk maybe but i WILL add her dildo as an item"
            # These variables are literally months old and have been wasting bytes of memory (or bits??)
            # Also i DID add josie's dildo as an armor, need to update its description, not gross enough

            # ok so i ran sys.getsizeof() and these shits are wasting like 80 bytes total

            
            if nodel["first_boot"]:
                space = " " * 40 if not isWindows else " " * 38
                print(f"""{space}\033[38;5;242m -- INSTRUCTIONS -- \033[0;37;40m
\t\t  When presented with a prompt, type out what it says in the
\t\t\t\t  (parenthesis)/\033[1;34;40mhighlighting\033[0;37;40m,
\t\t\t\tand then press the \033[1;33;40mEnter \033[0;37;40mbutton.""")
                time.sleep(5)
                input("\n\t\t\t\t  Press \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
                nodel["first_boot"] = False
                save("nodel.json", nodel)
                clear()

            if nodel["times_completed"] == 0 and extra_data["progress"]["seg_1_beg"] == False:
                print("\033[1;32;40mWelcome, ")
                time.sleep(1)
                print("...")
                time.sleep(0.5)
                print("What IS your name?... ")
                time.sleep(1)
                name = input("\n\033[0;37;40mEnter a name: ").strip()
                
                if len(name) > 8:
                    print("\n\033[1;31;40mName is too long.")
                    time.sleep(2)
                    continue
                if name == "":
                    print("\n\033[1;31;40mSorry, your name can't be literally nothing!")
                    time.sleep(2)
                    continue
                else:
                    clear()
                    if not name_check(name):
                        if name.casefold() == "persona":
                            settings["debug"] = True
                            save("settings.json", settings)
                        reverse = randint(1, 25)
                        
                        print(f"\033[1;32;40m{name if not reverse == 10 or reverse == 19 else name[::-1]}")

                        nameAssert = input("\nIs this the correct name(\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m)?: ").strip()
                        clear()
                        if nameAssert.casefold() == "y":
                            print("\033[1;32;40mOkay, remembering your name and other things...")
                            time.sleep(2)
                            
                            chars["player"]["name"] = name
                            chars["player"]["nameColor"] = "\033[0;37;40m"
                            chars["player"]["lv"] = 1
                            chars["player"]["money"] = 0
                            chars["player"]["exp"] = 0
                            chars["player"]["inventory"] = ["Empty"] * 12
                            save("chars.json", chars)
                            
                            extra_data["progress"]["seg_1_beg"] = True
                            save("extra_data.json", extra_data)

                            nodel["current_name"] = chars["player"]["name"]
                            save("nodel.json", nodel)
                            
                            while True:
                                clear()
                                soundSet = input("\033[1;32;40mWould you like to have sound on?\033[0;37;40m(\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m): ").strip().casefold()
                                if soundSet == "y":
                                    settings["sound"] = True

                                elif soundSet == "n":
                                    settings["sound"] = False
 
                                else:
                                    print(soundSet)
                                    invalidInput(2534)
                                    time.sleep(0.5)
                                    continue

                                volumeSet = input("\033[1;32;40mPreferred music volume?\033[0;37;40m(pick from 0.0-1.0): ").strip()
                                try:
                                    settings["musicVolume"] = float(volumeSet)
                                    mixer.music.set_volume(settings["musicVolume"])
                                except ValueError:
                                    print("\033[1;31;40mPlease pick a decimal from 0.0-1.0")
                                    time.sleep(1.7)
                                    continue
                                
                                volumeSet = input("\033[1;32;40mPreferred sound effects volume?\033[0;37;40m(pick from 0.0-1.0): ").strip()
                                try:
                                    settings["sfxVolume"] = float(volumeSet)
                                    mixer.music.set_volume(settings["sfxVolume"])
                                    break
                                except ValueError:
                                    print("\033[1;31;40mPlease pick a decimal from 0.0-1.0")
                                    time.sleep(1.7)
                                    continue
                        
                            save("settings.json", settings)

                            base_stat_set()
                            full_recover()
                            progress_check()
                            break

                        if nameAssert.casefold() == "n":
                            print("\033[1;32;40mAlright, one moment.")
                            time.sleep(1.5)
                            print("\nRebooting...\033[0;37;40m")
                            time.sleep(1.5)
                            continue
                        
                        else:
                            invalidInput(2572)
                            time.sleep(1)
                            continue

            else:
                if not extra_data["progress"]["seg_1_beg"]:
                    print(f"\033[1;32;40mWelcome {nodel['prev_name'][:1]}...")
                    time.sleep(1.5)
                    print("You look like someone I've seen, have we met before?")
                    time.sleep(2.3)
                    familiar = input("\033[0;37;40m(HAVE you met before?)(\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m): ").strip()
                    
                    clear()
                    
                    if familiar.casefold() == "y":
                        print("\033[1;32;40mRight!!")
                        time.sleep(0.5)
                        print("How could I forget you?")
                        time.sleep(1.5)
                        print(f"Welcome back, {nodel['prev_name']}\033[1;32;40m!\033[0;37;40m")
                        time.sleep(1.7)
                        clear()
                        chars["player"]["name"] = nodel["prev_name"]
                        chars["player"]["lv"] = 1
                        chars["player"]["money"] = 0
                        chars["player"]["exp"] = 0
                        chars["player"]["inventory"] = ["Empty"] * 12
                        save("chars.json", chars)

                        extra_data["progress"]["seg_1_beg"] = True
                        save("extra_data.json", extra_data)

                        base_stat_set()
                        full_recover()
                        progress_check()
                        break
                    
                    if familiar.casefold() == "n":
                        print("\033[1;32;40mRight, right...")
                        time.sleep(0.7)
                        print("You look a lot like them, you know?")
                        time.sleep(1.7)
                        print("Actually, you look EXACTLY like them...")
                        time.sleep(1.7)
                        print("It's a bit eerie...")
                        time.sleep(1.5)
                        name = input("\nAnyway, what IS your name?: \033[0;37;40m").strip()
                        
                        if len(name) > 8:
                            print("\n\033[1;31;40mName is too long.")
                            time.sleep(2)
                            continue
                        else:
                            if name.casefold() == nodel["prev_name"].casefold():
                                if not name_check(name):
                                    continue
                                else:
                                    clear()
                                    print("\033[1;32;40mWait...")
                                    time.sleep(0.5)
                                    print("Wait wait wait!")
                                    time.sleep(1.3)
                                    print(f"\n{name}")
                                    nameAssert = input("\nIs this ACTUALLY your name?\033[1;37;40m(\033[1;32;40my\033[1;37;40m/\033[1;31;40mn\033[1;37;40m): ")
                                    
                                    clear()
                                    
                                    if nameAssert.casefold() == "y":
                                        print("Of COURSE it's you!")
                                        time.sleep(1)
                                        print("I knew I'd see you again!")
                                        time.sleep(1.3)
                                        print(f"Welcome, {name}, welcome!")
                                        time.sleep(2.3)
                                        
                                        chars["player"]["name"] = nodel["prev_name"]
                                        chars["player"]["lv"] = 1
                                        chars["player"]["money"] = 0
                                        chars["player"]["exp"] = 0
                                        chars["player"]["inventory"] = ["Empty"] * 12
                                        save("chars.json", chars)
                                        
                                        extra_data["progress"]["seg_1_beg"] = True
                                        save("extra_data.json", extra_data)
                                        
                                        base_stat_set()
                                        full_recover()
                                        progress_check()
                                        break

                                    if nameAssert.casefold() == "n":
                                        print("\033[1;32;40mI see.")
                                        time.sleep(1.5)
                                        print("\nRebooting...\033[0;37;40m")
                                        time.sleep(1.5)
                                        continue
                                    else:
                                        invalidInput(26649)
                                        time.sleep(1)
                                        continue
                            
                            else:
                                if not name_check(name):
                                    print("\033[1;32;40m" + name)
                                    time.sleep(1)
                                    nameAssert = input("\nIs this your name?\033[1;37;40m(\033[1;32;40my\033[1;37;40m/\033[1;31;40mn\033[1;37;40m): ")
                                    if nameAssert.casefold() == "y":
                                        print("\n\033[1;32;40mAh, well...")
                                        time.sleep(1)
                                        print(f"Welcome, {name}!\033[0;37;40m")
                                        time.sleep(2.3)

                                        chars["player"]["name"] = nodel["prev_name"]
                                        chars["player"]["lv"] = 1
                                        chars["player"]["money"] = 0
                                        chars["player"]["exp"] = 0
                                        chars["player"]["inventory"] = ["Empty"] * 12
                                        save("chars.json", chars)
                                        
                                        extra_data["progress"]["seg_1_beg"] = True
                                        save("extra_data.json", extra_data)
                                        
                                        base_stat_set()
                                        full_recover()
                                        progress_check()
                                        break

                                    if nameAssert == "n":
                                        print("\033[1;31;40mOkay, one moment please!")
                                        time.sleep(1)
                                        print("\nRebooting...\033[0;37;40m")
                                        time.sleep(1.5)
                                        continue
                                    else:
                                        invalidInput(2324)
                    else:
                        invalidInput(2711)
                        time.sleep(1)
                        continue
                else:
                    continue
