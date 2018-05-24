import sys

count=0
codes=0

for f in sys.argv[1:]:
    fp = open(f)
    code = False
    for line in fp:
        if line.startswith("\\end{lstlisting}"):
            code = False
            print(count)
        if code and not line.isspace():
            count+=1
        if line.startswith("\\begin{lstlisting}"):
            code = True
            codes += 1

print(count)
print(codes)