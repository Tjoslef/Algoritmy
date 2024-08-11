import numpy
def isNStraightHand(hand, groupSize):
    hand.sort()
    if len(hand) % groupSize != 0:
        return False
    
    nArray = []
    sublist = [hand[0]]

    for i in range(1, len(hand)):
        if hand[i] == hand[i - 1] + 1:
            sublist.append(hand[i])
        else:
            nArray.append(sublist)
            sublist = [hand[i]]

    nArray.append(sublist)
    count = 0
    for sublist in nArray:
        sublist_mean = sum(sublist) / len(sublist)
        sublist_median = sublist[len(sublist) // 2]
        if sublist_mean != sublist_median:
            count += 1

    if count > 0:
        return False
    else:
        return True

groupSize = 1
print(isNStraightHand(hand, groupSize))

           
    

    




