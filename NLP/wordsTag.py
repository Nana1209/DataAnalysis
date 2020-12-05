import json

import nltk

with open('D:\REST API\\result\\pathsplit.json', 'r') as f:
  splitresult = json.load(f)

tagresult={}
for apiname,v in splitresult.items():
    pathresults={}
    for pathname,wordlist in v.items():
        resulttemp = []
        for hir in wordlist:
            for word in hir:
                wordtemp=[]
                wordtemp.append(word)
                resulttemp.append(nltk.pos_tag(wordtemp))
        pathresults[pathname] = resulttemp
    tagresult[apiname]=pathresults
json_str = json.dumps(tagresult, indent=4)
with open('D:\REST API\\result\\wordTagWord.json', 'w') as json_file:
    json_file.write(json_str)
