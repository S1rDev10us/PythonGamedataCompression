import os
import zipfile


archive=zipfile.ZipFile('Index.zap','r')
with archive as z:
    newstrings=[]
    for filename in z.namelist():
        print(filename=='Index.py')
        if not os.path.isdir(filename):
            pass
            newstring=''
            for line in z.open(filename):
                newstring+=line.decode('utf-8')
                # print(line.decode('utf-8'))
            newstrings.append(newstring)
    print(newstrings)