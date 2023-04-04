import json
import os
import subprocess
import sys
import time
print("\033[1;32;40mLoading...")
try:
    import bcrypt
    # import keyboard

    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

    from pprint import pprint
    from random import choice, randint, random

    from pygame import mixer
    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init()

except ModuleNotFoundError:
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;31;40mHOLD IT!!!")
    time.sleep(1.5)
    print("\033[1;32;40mSome things are missing.")
    time.sleep(1.5)
    print(f"Try running the \033[1;33;40m{'windows_install.bat' if os.name == 'nt' else 'unix_install.sh'} \033[1;32;40mfile,", end="", flush=True)
    time.sleep(1.5)
    print(" THEN try starting the game up again.")
    time.sleep(1.5)
    input("\nPress \033[1;33;40m\"Enter\" \033[0;37;40mto exit: ")
    sys.exit()

isWindows = os.name == "nt"
clearCom = "cls" if isWindows else "clear"
home_dir = os.environ["HOMEPATH"] if isWindows else os.environ["HOME"]
defaultSize = False if len(sys.argv) > 1 else True
colors = [f"\\033[38;5;{i}m" for i in range(256)]

naughty = True
JOSIX_compliant = True

def clear():
    os.system(clearCom)

def change_title(title):
    if isWindows:
        os.system(f"title {title}")
    else:
        os.system(f"echo -n -e 033]{title}007")

def resize(rows, columns, default_sz=False):
    if isWindows:
        subprocess.call(["windows_resize.bat", [f"{default_sz}"]])
    else:
        subprocess.call(["./unix_resize.sh", [f"{default_sz}"]])

def invalidInput(line):
    print(f"\033[1;33;40mLine {line}: \033[1;31;40mInvalid input, please try again.\033[0;37;40m")

def save(file, thing):
    with open(file, "w") as f:
        json.dump(thing, f)

def load(file):
    with open(file, "r") as f:
        return json.load(f)

def printNames():
    for char in chars:
        print(f"{chars[char]['nameColor']}{chars[char]['name']}")

def printRoman(num):
    return num

def censor(phrase):
    if not naughty: # replace with ```if not settings["naughty"]```
        print("clean")
        nono_words = ("fuck", "fucks", "shit", "shat", "bitch", "bitches", "dildo", "dumbass")
        replacements = ("fuss", "fusses", "shucks", "poo'd", "female dog", "female dogs", "mystery item", "smooth brain")
        
        spl_cln_phrase = phrase.split() # "spl" = "split", "cln" = "clean"

        for index, word in enumerate(spl_cln_phrase):
            for ind, cuss in enumerate(nono_words):
                if cuss in word.casefold():
                    spl_cln_phrase[index] = word.casefold().replace(cuss, replacements[ind])
        phrase = " ".join(spl_cln_phrase)
    return phrase

def myLord(phrase):
    if JOSIX_compliant:
        spl_cln_phrase = phrase.split()
        gonna_get_executed = ("josie", "marcus")
        josie_happy = ("no one in particular", "kim jung un")
        
        for index, word in enumerate(spl_cln_phrase):
            for ind, bad in enumerate(gonna_get_executed):
                if bad in word.casefold():
                    spl_cln_phrase[index] = word.casefold().replace(bad, josie_happy[ind])
        phrase = " ".join(spl_cln_phrase)
    return phrase











