# class Author:
#     pass


# class Book:
#     pass


# class Contract:
#     pass

# Book class
# class Book:
#     all_books = []

#     def __init__(self, title):
#         self.title = title
#         self._contracts = [] 
#         Book.all_books.append(self)

#     def contracts(self):
#            return self._contracts
    
#     def authors(self):
#         return [contract.author for contract in self._contracts]

#     def add_contract(self, contract):
#         self._contracts.append(contract)

# # Author class
# class Author:
#     all_authors = []
#     def __init__(self, name):
#         self.name = name
#         self._contracts = []
#         Author.all_authors.append(self)
      
            
#     def contracts(self):
#         return self._contracts
#         #  return [contract for contract in Contract.all_contracts if contract.author == self]


#     def total_royalties(self):
#         return sum(contract.royalties for contract in self._contracts) 

#     def contracts(self):
#         return self._contracts

#     def books(self):
#         return [contract.book for contract in self._contracts]

#     def sign_contract(self, book, date, royalties):
#         contract = Contract(self, book, date, royalties)
#         self._contracts.append(contract)
#         return contract

#     def total_royalties(self):
#         return sum(contract.royalties for contract in self._contracts)

# # Contract class
# class Contract:
#     all_contracts = []

#     def __init__(self, author, book, date, royalties):
#         if not isinstance(author, Author):
#             raise Exception("author must be an Author instance")
#         if not isinstance(book, Book):
#             raise Exception("book must be a Book instance")
        
#             if not isinstance(date, str):
#              raise ValueError("Date must be a string")
#         if not isinstance(royalties, int):
#             raise ValueError("Royalties must be an integer")
#     #     class Contract:
#     # def __init__(self, author, book, date, royalties):
#         if not isinstance(date, str):
#             raise TypeError("Date must be a string")
#         self.date = date

#         def contracts_by_date(cls, date):
#          return sorted([contract for contract in cls.all if contract.date == date], key=lambda x: x.date)

#         self.author = author
#         self.book = book
#         self.date = date
#         self.royalties = royalties
#         Contract.all_contracts.append(self)

#     @classmethod
#     def contracts_by_date(cls, date):
#         return [contract for contract in cls.all_contracts if contract.date == date]



class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        # Return all contracts associated with this book
        return [contract for contract in Contract.all_contracts if contract.book == self]
    def authors(self):
        # Return all authors associated with this book
        return [contract.author for contract in Contract.all_contracts if contract.book == self]

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

# class Contract:
#     all_contracts = []

#     def __init__(self, author, book, date, royalties):
#         if not isinstance(author, Author):
#             raise Exception("Invalid author")
#         if not isinstance(book, Book):
#             raise Exception("Invalid book")
#         if not isinstance(date, str):
#             raise Exception("Invalid date")
#         if not isinstance(royalties, int):
#             raise Exception("Invalid royalties")
        
#         self.author = author
#         self.book = book
#         self.date = date
#         self.royalties = royalties
#         Contract.all_contracts.append(self)

#     @classmethod
#     def contracts_by_date(cls, date):
#         return [contract for contract in cls.all_contracts if contract.date == date]

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
