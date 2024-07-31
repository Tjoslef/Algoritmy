def replaceWords(dictionary, sentence):
    wList = sentence.split()
    count = 0
    Index = 0
    order = []
    for word in wList:
        shortest_match = None
        for substring in dictionary:
            if word.startswith(substring):
                if shortest_match is None or len(substring) < len(shortest_match):
                    shortest_match = substring
        if shortest_match:
            order.append(shortest_match)
        else:
            order.append(word)
    result = ' '.join(order)            
    return result
replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery")
            