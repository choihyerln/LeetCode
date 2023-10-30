        left = 0
        sub_arr = [cards[0]]

        for i in range(left+1, len(cards)):
            if cards[left] != cards[i]:
                sub_arr.append(cards[i])
                print(sub_arr)
            
            if cards[left] == cards[i]:
                sub_arr.append(cards[i])
                break

        return len(sub_arr) if cards != sub_arr else -1