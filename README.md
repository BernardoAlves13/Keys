This package allow  users to extract keywords from wikipedia articles given an input subjuct
```bash
from wiki import ExtractKeysFromWiki

kws = ExtractKeysFromWiki("Coronavírus")
for kw in kws:
    print(kw[0])
```