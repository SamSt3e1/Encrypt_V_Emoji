print (" █▀▀ █▀▄▀█ █▀▀█   ▀  ▀    █▀▀ █▀▀█ █  █ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▀█ █  █ █  █ ")
print (" █▀▀ █ ▀ █ █  █   █ ▀█▀   █   █▄▄▀ █▄▄█ █  █   █   █  █ █ ▀█ █▄▄▀ █▄▄█ █  █ █▀▀█ █▄▄█ ")
print (" ▀▀▀ ▀   ▀ ▀▀▀▀ █▄█ ▀▀▀   ▀▀▀ ▀ ▀▀ ▄▄▄█ █▀▀▀   ▀   ▀▀▀▀ ▀▀▀▀ ▀ ▀▀ ▀  ▀ █▀▀▀ ▀  ▀ ▄▄▄█ ")

print ("Made by SamSteel")
dictionary = {
"a":"🙄", "b":"😏", "c":"😣", "d":"😥", "e":"😮", "f":"🤐", "g":"😯", "h":"😪", "i":"😫", "j":"🥱", "k":"😴", "l":"😌", "m":"😛", "n":"😜", "o":"😝", "p":"🤤", "q":"😒", "r":"😓", "s":"😔", "t":"😕", "u":"🙃", "v":"🤑", "w":"😲", "x":"🙁", "y":"😖", "z":"😞"
}

def convertText(emoji):
    result = ""
    for i in emoji:
        for key, value in dictionary.items():
            if(value == i):
                result+=key
    return result


def frot13(emoji):
    emojis = "🙄😏😣😥😮🤐😯😪😫🥱😴😌😛😜😝🤤😒😓😔😕🙃🤑😲🙁😖😞"
    words = "abcdefghijklmnopqrstuvwxyz"
    trans = words[13:]+words[:13]
    rot_char = lambda c: trans[emojis.find(c)] if emojis.find(c)>-1 else c
    return ''.join( rot_char(c) for c in word )
word = input("emojini daxil edin: ")
emoji = convertText(word)
reEmoji = convertText(word)
rot13 = frot13(word)
reRot13 = frot13(rot13)


print("emoji    : "+word)
print("cipher   : "+emoji)
print("plain text   : "+rot13)
