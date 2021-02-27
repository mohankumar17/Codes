class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,key):
        p=self.root
        n=len(key)
        for i in range(n):
            ind=ord(key[i])-ord('a')
            if p.children[ind] is None:
                p.children[ind]=TrieNode()  #creating Node
            p=p.children[ind]
        p.isEndOfWord=True

    def search(self,key):
        p=self.root
        n=len(key)
        for i in range(n):
            ind=ord(key[i])-ord('a')
            if p.children[ind] is None:
                return False
            p=p.children[ind]
        return p!=None and p.isEndOfWord

#########################################################
keys = ['act','dog','god','tac','cat']
t = Trie()

for key in keys:
    t.insert(key)

print(t.search("act"))
print(t.search("dog"))
print(t.search("god"))
print(t.search("tac"))
