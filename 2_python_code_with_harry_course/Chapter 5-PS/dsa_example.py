
def get_card_position_linear_search(card_list, frequency):
    card_list.sort()
    position = 0
    while position < len(card_list):
        if card_list[position] == frequency:
            return position
        position +=1
    return -1

def get_card_position_binary_search(card_list, frequency):
    card_list.sort()
    lo, hi = 0, (len(card_list)-1)
    while lo < hi:
        mid = (lo + hi) // 2
        if frequency == card_list[mid]:
            return mid
        elif frequency < card_list[mid]:
            hi = mid
        elif frequency > card_list[mid]:
            lo = mid
    return -1

card_list = [5, 6, 9, 12, 15, 21, 25, 30, 32]
frequency = 25

#print(get_card_position_linear_search(card_list, frequency))
print(get_card_position_binary_search(card_list, frequency))
