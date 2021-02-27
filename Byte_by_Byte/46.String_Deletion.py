import sys
def stringDeletion(d,query):
    n=len(query)
    m=sys.maxsize
    for i in d:
        c=0
        if len(i)==n:
            for j in range(0,len(i)):
                if query[j]!=i[j]:
                    c=c+1
            if c<m:
                m=c
    return m

d=['a','aa','aaa']
query='abc'
print(stringDeletion(d,query))
