
class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Book:
    def __init__(self, name, release_date, author):
        self.name = name
        self.release_date = release_date
        self.authors = [author]
        self.authors_amount = 1

    def addAuthor(self, author):
        self.authors_amount +=1
        authors.append(author)

    def getName(self):
        return self.name

    def setName(self, name):
        self.mame = name

    def printBookInfo(self):
        temp_string = ""
        for x in range(self.authors_amount):
            if(x != 0): 
                temp_string = temp_string + ", "
            temp_string += self.authors[x].getName()
        print("book: " + str(self.name) + " " +  str(self.release_date) + " authors: " + temp_string)


class Deck:
    def __init__(self, size, type):
        self.size = size
        self.type = type
        self.cards = []

    def getSize(self):
        return self.size

    def setSize(self, name):
        self.name = name

    def getType(self):
        return self.type

    def AddCards(self, cards):
        self.cards = cards

    def AddCard(self, card):
        self.cards.append(card)

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def getName(self):
        return self.name


author_test = Author("J. R. R. Tolkien", 81);
book_test = Book("Lord of the Rings", "1954", author_test)

book_test.printBookInfo()

card1 = Card("ace", 1)
card2 = Card("snake", 2)
card3 = Card("tripple", 3)
card4 = Card("queen", 12)

deck1 = Deck( 4 , "smalldeck")
deck1.AddCard(card1)
deck1.AddCard(card2)
deck1.AddCard(card3)
deck1.AddCard(card4)

