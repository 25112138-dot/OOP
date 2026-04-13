import random

# Lớp lá bài
class Card:
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


# Lớp bộ bài
class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in Card.suits for r in Card.ranks]
        random.shuffle(self.cards)

    def deal(self, num=1):
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt


# Lớp tay bài
class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def __str__(self):
        return " ".join(str(c) for c in self.cards)


# Lớp người chơi
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def receive_cards(self, cards):
        self.hand.add_cards(cards)

    def show_hand(self):
        print(f"{self.name}: {self.hand}")


# Lớp trò chơi Poker
class PokerGame:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(name) for name in players]

    def deal_cards(self):
        for player in self.players:
            player.receive_cards(self.deck.deal(2))  # mỗi người 2 lá

    def show_players(self):
        for player in self.players:
            player.show_hand()


# Ví dụ chạy game
game = PokerGame(["Nguyen Van A", "Tran Thi B", "Le Van C"])
game.deal_cards()
game.show_players()
