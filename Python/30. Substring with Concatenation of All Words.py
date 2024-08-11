
import itertools
def findSubstring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    total_len = word_len * len(words)
    permutations = itertools.permutations(words)
    iList = []

    for pr in permutations:
        fwords = ''.join(pr)
        start = 0
        
        while start <= len(s) - total_len:
            finex = s.find(fwords, start)
            if finex == -1:
                break
            if finex not in iList:
                iList.append(finex)
            start = finex + 1
    
    return iList
                        
                        

print(findSubstring("barfoothefoobarman",["foo","bar"]))

                
