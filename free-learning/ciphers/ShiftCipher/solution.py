A = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л",
     "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш",
     "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def list_find(list, value):
    for i, e in enumerate(list):
        if e == value:
            return i
    return -1


def decrypt(value, key, alphabet=None):
    if alphabet is None:
        alphabet = A
    c = []
    sa = set(alphabet)
    for el in value:
        if el not in sa:
            continue
        c.append(alphabet[(list_find(alphabet, el) - key) % len(
            alphabet)])
    return c


def encrypt(value, key, alphabet=None):
    if alphabet is None:
        alphabet = A
    c = []
    sa = set(alphabet)
    for el in value:
        if el not in sa:
            continue
        c.append(alphabet[(list_find(alphabet, el) + key) % len(
            alphabet)])
    return c
print("".join(decrypt('ъуожстеюжлщшёфлщхтгсхиофжфппфхпиъулфппцчптжйжщгофжфплфжклтл', 7)))