def isWordinDict(d,word):
    if word in d:
        return True
    else:
        return False

def word_break(d,word):
    if len(word)==0:
        return True
    for i in range(1,len(word)+1):
        if isWordinDict(d,word[0:i]) and word_break(d,word[i:]):
            return True
    return False

'''def word_breakDP(d,word):
    n=len(word)
    if n==0:
        return True
    ans=[False]*(n+1)
    if word[0] in d:
        ans[0]=True

    for i in range(1,n+1):
        if ans[i]==False and isWordinDict(d,word[0:i+1]):
            ans[i]=True

        if ans[i]==True:
            if i==n:
                return True
            for j in range(i+1,n+1):
                if ans[j]==False and isWordinDict(d,word[i:j-i+1]):
                    ans[j]=True
                if j==n and ans[j]==True:
                    return True
    return False'''

d={'i','am','ace','a'}
word='iamacea'
print(word_break(d,word))
#print(word_breakDP(d,word))
