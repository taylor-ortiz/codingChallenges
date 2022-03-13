import re

def to_camel_case(text):
    res = re.split('_|-', text)
    for i in range(len(res)):
        if i != 0:
            text += res[i][:1].upper() + res[i][1:]
        else:
            text = res[i]
    return text
