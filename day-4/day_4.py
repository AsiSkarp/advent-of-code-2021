with open('bingo_input.txt') as f:
    lines = f.readlines()

#  Part One

#  Loading the game:

def load_bingo_numbers(strings):
    drawn_numbers = []
    for index, line in enumerate(strings):
        if len(line.strip()) == 0 :
            return drawn_numbers, index + 1
        else:
            row = line.strip().split(',')
            drawn_numbers.append(parse_string_to_int(row))
            #drawn_numbers.append(line.strip().split(','))


def load_bingo_cards(strings, start_index):
    bingo_card = []
    row = []
    for index, line in enumerate(strings[start_index:]):

        if len(line.strip()) == 0:
            return bingo_card, index + start_index + 1
        elif (index + start_index) == (len(strings) - 1):
            row = line.strip().split()
            bingo_card.append(parse_string_to_int(row))
            return bingo_card, index + start_index + 1
        else:
            row = line.strip().split()
            bingo_card.append(parse_string_to_int(row))


def parse_string_to_int(line):
    return_list = []
    for item in line:
        return_list.append(int(item))
    return return_list


def load_game(strings):
    drawn_numbers, start_index = load_bingo_numbers(strings)
    bingo_cards = []
    for _ in range (start_index, len(strings)):
        if start_index >= len(strings):
            break
        bingo_card, next_index = load_bingo_cards(strings, start_index)
        bingo_cards.append(bingo_card)
        start_index = next_index
    return drawn_numbers, bingo_cards


def print_game(numbers, bingo_cards):
    print('Drawn numbers: \n'  + str(numbers[0]))

    print("\n")
    for index, card in enumerate(bingo_cards):
        print('Card #{}'.format(index + 1))
        for row in card:
            print(row)
        print("\n")


def mark_number(bingo_card, bingo_number):
    for i, row in enumerate(bingo_card):
        #print("Checking number: {} \t in row #{}".format(bingo_number, i))
        #print(row)
        for j, number in enumerate(row):
            if number == bingo_number:
                #print('Number: {} is a match at row {} column {}'.format(number, i + 1, j + 1))
                bingo_card[i][j] = 'X'



def check_matches(bingo_card):
    bingo = False
    for i, row in enumerate(bingo_card):
        bingo = check_row(row)
        #print("Bingo in row? {}".format(bingo))
        if bingo:
            break
        bingo = check_column(bingo_card, i)
        #print("Bingo in column? {}".format(bingo))
        if bingo:
            break
    return bingo    



def check_row(row):
    return all(i == 'X' for i in row)


def check_column(card, index):
    return all([row[index] == 'X' for row in card]) 


def calculate_score(bingo_card, bingo_number):
    score = 0
    for row in bingo_card:
        for number in row:
            if number != "X":
                score += number
    
    return score * bingo_number


def play_bingo(bingo_cards, numbers):
    # bingo = False
    for ind, number in enumerate(numbers[0]):
        for iteration, card in enumerate(bingo_cards):
            mark_number(card, number)
            '''
            bingo = check_matches(card)
            if bingo:
                print('BINGO!')
                print_game(numbers, bingo_cards)
                break    
            '''
            #print("Checking card #{}".format(iteration + 1))
            #print("Bingo?: {}".format(check_matches(card)))
            bingo = check_matches(card)
            
            if bingo:
                print('BINGO!')
                print('Card #{} is the winner!'.format(iteration + 1))
                print("Final score is : {}".format(calculate_score(card, number)))
                break
        
        if bingo:
            print("----FINAL RESULT ----")
            #print_game(numbers, bingo_cards)
            break
        print("\n")
        print("Round #{}".format(ind + 1))
        print("\n")
        print_game(numbers, bingo_cards)    
            


numbers, bingo_cards = load_game(lines)

#print_game(numbers, bingo_cards)

play_bingo(bingo_cards, numbers)
#print(load_bingo_numbers(lines))
# print(load_bingo_cards(lines, 8))


