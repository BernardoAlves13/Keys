from wiki import ExtractKeysFromWiki

kws = ExtractKeysFromWiki("Coronavírus")
for kw in kws:
    print(kw[0])