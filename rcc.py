import sys
import unicodedata

file2 = open(sys.argv[2], 'w')
file1 = open(sys.argv[1], 'r')
 
while True:
    line = file1.readline()
    if not line:
        # reached EOF
        break
    nocc = "".join(ch for c in line if unicodedata.category(c)[0]!="C")
    file2.write(nocc + "\n")

file1.close()
file2.close()

