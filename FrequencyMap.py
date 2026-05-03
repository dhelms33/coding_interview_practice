def freq_map(text: str)->dict{str, int}:
    dict_map = {}
    length = len(text)
    for char in text:
        if char in dict_map:
            dict_map[char] += 1
        else:
            dict_map[char] = 1
    return dict_map

def freq_map_opt(text:str)->dict{str, int}:
    return dict(Counter(text))