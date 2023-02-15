# quiz game to learn hex values
import pyttsx3
import random

# initialisation of text to speach
engine = pyttsx3.init()
engine.setProperty('rate', 148)

number = 0
hex_version = ''
num_list=[]
[num_list.append(i) for i in range(255)]

def prCyan(skk):
    print("\033[96m {}\033[00m" .format(skk))


def prRed(skk):
    print("\033[91m {}\033[00m".format(skk))


def get_nums():
    global number
    global hex_version
    number = random.choice(num_list)
    hex_version = (str(hex(number)))
    hex_version = hex_version[2:]

def say_hex():
    global hex_version
    talk_hex = []
    [talk_hex.append(i) for i in hex_version]
    print(f'The Hex is {hex_version}.')
    engine.say(f'The Hex is {talk_hex}')
    engine.runAndWait()

while True:
    get_nums()
    print(f'The number is {number}.')
    engine.say(f'The number is {number}.')
    engine.say('What is the hex val u?')
    engine.runAndWait()
    # print(f'The Hex is {hex_version}.')
    user_hex = input('What is the Hex value?\n:')

    if user_hex == hex_version:
        prCyan('Correct!')
        engine.say('Correct.')
        say_hex()
    else:
        prRed('Incorrect')
        engine.say('Incorrect.')
        say_hex()

    again_yn = input('Play again?')
    if again_yn in ['no', 'nope', 'quit', 'die', 'no thanks', 'piss off', 'exit','n','N']:
        break
    else:
        continue

engine.say('Good bye?')
engine.runAndWait()
print('~~~~ GOODBYE! ~~~~')
