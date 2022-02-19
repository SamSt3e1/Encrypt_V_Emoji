print (" █▀▀ █▀▄▀█ █▀▀█   ▀  ▀    █▀▀ █▀▀█ █  █ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▀█ █  █ █  █ ")
print (" █▀▀ █ ▀ █ █  █   █ ▀█▀   █   █▄▄▀ █▄▄█ █  █   █   █  █ █ ▀█ █▄▄▀ █▄▄█ █  █ █▀▀█ █▄▄█ ")
print (" ▀▀▀ ▀   ▀ ▀▀▀▀ █▄█ ▀▀▀   ▀▀▀ ▀ ▀▀ ▄▄▄█ █▀▀▀   ▀   ▀▀▀▀ ▀▀▀▀ ▀ ▀▀ ▀  ▀ █▀▀▀ ▀  ▀ ▄▄▄█ ")

print ("Made by SamSteel")

dictionary = {
"a":"🙄", "b":"😏", "c":"😣", "d":"😥", "e":"😮", "f":"🤐", "g":"😯", "h":"😪", "i":"😫", "j":"🥱", "k":"😴", "l":"😌", "m":"😛", "n":"😜", "o":"😝", "p":"🤤", "q":"😒", "r":"😓", "s":"😔", "t":"😕", "u":"🙃", "v":"🤑", "w":"😲", "x":"🙁", "y":"😖", "z":"😞"
}

def convertEmoji(word):
    result = ""
    for i in word:
        result+=dictionary[i]
    return result


def frot13(word):
    emojis = "🙄😏😣😥😮🤐😯😪😫🥱😴😌😛😜😝🤤😒😓😔😕🙃🤑😲🙁😖😞"
    trans = emojis[13:]+emojis[:13]
    rot_char = lambda c: trans[emojis.find(c)] if emojis.find(c)>-1 else c
    return ''.join( rot_char(c) for c in word )
word = input("Insert word to encrypt here: ")
emoji = convertEmoji(word)
rot13 = frot13(emoji)


print("word    : "+word)
print("emoji   : "+emoji)
print("rot13   : "+rot13)
