import random

player_cards = []
robot_cards = []
deck = []

def game_menu():
    # Display the menu options
    print("Menu:")
    print("1. Start Game")
    print("2. Pick a Card")
    print("3. Shuffle Deck")
    print("4. Show My Cards")
    print("5. Check Win/Lose")
    print("6. Exit")


def create_deck(suits, values):
    global deck
    for suit in suits:
        for value in values:
            card = value + " of " + suit
            deck.append(card)
    print(deck)
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    # Find the indices of the A, Q, and K cards in the shuffled deck
    a_index = next((i for i, card in enumerate(deck) if card.startswith('A')), None)
    q_index = next((i for i, card in enumerate(deck) if card.startswith('Q')), None)
    k_index = next((i for i, card in enumerate(deck) if card.startswith('K')), None)
    # Swap the A, Q, and K cards with their respective positions in the deck
    deck[a_index], deck[0] = deck[0], deck[a_index]
    deck[q_index], deck[len(deck)//2] = deck[len(deck)//2], deck[q_index]
    deck[k_index], deck[-1] = deck[-1], deck[k_index]
    # Display the shuffled deck
    print('Shuffled deck:')
    for card in deck:
        print(card)


def pick_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    cardR = random.choice(deck)
    deck.remove(cardR)
    global player_cards
    player_cards.append(card)
    global robot_cards
    robot_cards.append(cardR)
    return card


def show_cards(player_cards):
    if len(player_cards) == 0:
        print("You have not picked a card yet")
    else:
        print("Your cards:")
        for card in player_cards:
            print(card)


def check_result(player_cards, robot_cards, suits):
    # Rule 1: Check if player has same value card for all suits
    for suit in suits:
        suit_cards = [card for card in player_cards if suit in card]
        if len(suit_cards) == len(player_cards) / len(suits):
            return True

    # Rule 2: Check if player has same value for at least total suits - 1
    for card in player_cards:
        same_value_cards = [c for c in player_cards if c[:-2] == card[:-2]]
        if len(same_value_cards) >= len(suits) - 1:
            return True

    # Rule 3: Check if player has more cards from second suit than robot
    second_suit = suits[1]
    player_second_suit_cards = [card for card in player_cards if second_suit in card]
    robot_second_suit_cards = [card for card in robot_cards if second_suit in card]
    if len(player_second_suit_cards) > len(robot_second_suit_cards):
        return True

    # Rule 4: Check if player has higher average card value than robot
    player_avg_value = sum([card_value(card[:-2]) for card in player_cards]) / len(player_cards)
    robot_avg_value = sum([card_value(card[:-2]) for card in robot_cards]) / len(robot_cards)
    if player_avg_value > robot_avg_value:
        return True

    # Player loses if none of the above conditions are met
    return False


def card_value(card):
    if card.isdigit():
        return int(card)
    elif card == 'A':
        return 1
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 11
    else:
        return 10


def play_game():
    print("Welcome to the card game!")

    suits1 = ["♥", "♦", "♣", "♠"]
    suits2 = ["😃", "😈", "😵", "🤢", "😨"]
    suits3 = ["🤡", "👹", "👺", "👻", "👽", "👾", "🤖"]

    print("Suit 1 : ", suits1)
    print("Suit 2 : ", suits2)
    print("Suit 3 : ", suits3)

    # Get the user's choice of suit
    suit_choice = input("Enter the number corresponding to your desired suit: ")


    # Validate the suit choice
    while suit_choice not in ["1", "2", "3"]:
        print("Invalid input. Please enter a number between 1 and 3.")
        suit_choice = input("Enter the number corresponding to your desired suit: ")

    # Convert the suit choice to the corresponding string
    if suit_choice == "1":
        suit = suits1
    elif suit_choice == "2":
        suit = suits2
    else:
        suit = suits3

    menu_choice = 1
    while menu_choice != None:
        game_menu()
        print("Enter the number corresponding to your desired menu option: ")
        # Get the user's choice of menu option
        menu_choice = input()


        # Validate the menu choice
        while menu_choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid input. Please enter a number between 1 and 6.")
            menu_choice = input("Enter the number corresponding to your desired menu option: ")


        deck = create_deck(suit, values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "K", "Q"])
        # Execute the selected menu option

        if len(player_cards) >= 6:
            print("You can't add more than 6 cards.")
            show_cards(player_cards)
            print("Checking win/lose...")
            if check_result(player_cards, robot_cards, suit_choice):
                print("Player won")
            else:
                print("Robot won")
            # break

        elif menu_choice == "1":
            print("Starting game...")

        elif menu_choice == "2":
            print("Picking a card...")
            card = pick_card(deck)
            print(card)
        elif menu_choice == "3":
            print("Shuffling deck...")
            shuffle_deck(deck)

        elif menu_choice == "4":
            print("Showing my cards...")
            show_cards(player_cards)

        elif menu_choice == "5":
            print("Checking win/lose...")
            if check_result(player_cards, robot_cards, suit_choice):
                print("Player won")
            else:
                print("Robot won")

        else:
            print("Exiting game...")
            break

play_game()