# Convert each card combination into a numeric value. Then, compare numbers.
# Each poker hand is rapresented by a number which encodes rank and cards value.
# i.e:  [ ## , ## ## ## ## ## ]. The first two digits are representative of the
# ranked hand (high card, straight, flush, ...), the other five double digits
# stand for card values.

cards_pts = {'2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14}

combo_pts = {'high': 0,
        '1pair': 1,
        '2pairs': 2,
        'three': 3,
        'straight': 4,
        'flush': 5,
        'full': 6,
        'four': 7,
        'straight_flush': 8,
        'royal_flush': 9}

def process_one_pair(mult):
    other_cards = []
    value_cards = []
    for card, amount in mult.items():
        if amount == 2:
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
        else:
            other_cards.append(str(cards_pts[card]).zfill(2))
    total = ['1.'] + value_cards + sorted(other_cards, reverse=True)
    return float(''.join(total))

def process_two_pairs(mult):
    other_cards = []
    value_cards = []
    for card, amount in mult.items():
        if amount == 2:
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
        else:
            other_cards.append(str(cards_pts[card]).zfill(2))
    total = ['2.'] + sorted(value_cards, reverse=True) + other_cards
    return float(''.join(total))

def process_three(mult):
    other_cards = []
    value_cards = []
    for card, amount in mult.items():
        if amount == 3:
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
        else:
            other_cards.append(str(cards_pts[card]).zfill(2))
    total = ['3.'] + value_cards + sorted(other_cards, reverse=True)
    return float(''.join(total))

def process_full(mult):
    value_cards = []
    other_cards = []
    for card, amount in mult.items():
        if amount == 3:
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
        else:
            other_cards.append(str(cards_pts[card]).zfill(2))
            other_cards.append(str(cards_pts[card]).zfill(2))
    total = ['6.'] + value_cards + other_cards
    return float(''.join(total))

def process_four(mult):
    value_cards = []
    other_cards = []
    for card, amount in mult.items():
        if amount == 4:
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
            value_cards.append(str(cards_pts[card]).zfill(2))
        else:
            other_cards.append(str(cards_pts[card]).zfill(2))
    total = ['7.'] + value_cards + other_cards
    return float(''.join(total))

def is_straight(h):
    # TODO: l'asso può andare prima del 2?
    h_new = []
    for card in h:
        h_new.append(cards_pts[card])
    h_new.sort()
    for i in range(len(h_new) - 1):
        if h_new[i + 1] - h_new[i] != 1:
            return False
    return True

def process_straight(h):
    h_new = []
    for card in h:
        h_new.append(cards_pts[card])
    h_new.sort(reverse=True)
    m = max(h_new)
    decimals = []
    for c in range(m, m - 5, -1):
        decimals.append(str(c).zfill(2))
    return ''.join(decimals)

def is_flush(h):
    if len(set(h)) == 1:
        return True
    else:
        return False

def process_high(h):
    h_new = []
    for card in h:
        h_new.append(cards_pts[card])
    h_new.sort(reverse=True)
    decimals= []
    for c in h_new:
        decimals.append(str(c).zfill(2))
    return ''.join(decimals)

def is_pair(h):
    # Check if there is at least a pair in the list 'h'
    # returns True for pair, False otherwise
    if len(set(h)) < len(h):
        return True
    else:
        return False

def check_pairs(h):
    mult = {}
    for card in h:
        if card in mult:
            mult[card] += 1
        else:
            mult[card] = 1
    if max(mult.values()) == 4:
        # four of a kind
        return process_four(mult)
    elif max(mult.values()) == 3:
        if sorted(mult.values())[-2] == 2:
            # full house
            return process_full(mult)
        else:
            # three of a kind
            return process_three(mult)
    elif max(mult.values()) == 2:
        if sorted(mult.values())[-2] == 2:
            # two pairs
            return process_two_pairs(mult)
        else:
            # one pair
            return process_one_pair(mult)


def process_hand(h, f):
    if is_pair(h):
        return check_pairs(h)
    else:
        straight = is_straight(h)
        flush = is_flush(f)
        if straight and flush:
            # straight flush
            return float('8.' + process_straight(h))
        elif straight and not flush:
            # straihgt
            return float('4.' + process_straight(h))
        elif not straight and flush:
            # flush)
            return float('5.' + process_high(h))
        else:
            # high card
            return float('0.' + process_high(h))


def compare_hands(h_1, h_2, f_1, f_2):
    # h_1, h_2, f_1, f_2: lists of chars
    # returns True if h_1 wins, False otherwise
    p_1 = process_hand(h_1, f_1)
    p_2 = process_hand(h_2, f_2)
    if p_1 > p_2:
        return True
    else:
        return False


def parse_line(line):
    # line: string with ten consecutive cards symbols (five for each player),
    # separated by whitespaces
    # returns two chars-based lists, one for each player
    
    idx = 0
    h_1 = []
    h_2 = []
    f_1 = [] # check flush
    f_2 = []
    for card in line.split(' '):
        if idx < 5:
            h_1.append(card[0])
            f_1.append(card[1])
        else:
            h_2.append(card[0])
            f_2.append(card[1])
        idx += 1

    return h_1, h_2, f_1, f_2

player_1_wins = 0

with open('p054_poker.txt') as poker_hands:
    for line in poker_hands:
        h_1, h_2, f_1, f_2 = parse_line(line)
        if compare_hands(h_1, h_2, f_1, f_2):
            player_1_wins += 1
    print(player_1_wins)
