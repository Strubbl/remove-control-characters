import sys
import unicodedata

file2 = open(sys.argv[2], 'w')
file1 = open(sys.argv[1], 'r')
 
while True:
    line = file1.readline()
    if not line:
        # reached EOF
        break
    nocc = "".join(c for c in line if unicodedata.category(c)[0]!="C" or unicodedata.category(c)=="Cc")
    file2.write(nocc)

file1.close()
file2.close()

