
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import glob

regex = r"(<title>.*?)  · GitBook(<\/title>)"

for f in glob.glob("*.[ch]"):
    with open(f, "r") as inputfile:
        subst = "\\1 | Pierre Deboissy\\2"
        result = re.sub(regex, subst, f, 0, re.MULTILINE)
        newText = inputfile.read().replace('Version1', result)

    with open(f, "w") as outputfile:
        outputfile.write(newText)

for filename in glob.iglob('_book/' + '**/*.html', recursive=True):
    with open(filename, 'w') as f:
      subst = "\\1 | Pierre Deboissy\\2"
      result = re.sub(regex, subst, f, 0, re.MULTILINE)
      if result:
        print (result)
      



      
