import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):

        self.library = []
        
        for i in range(len(texts)):
            merge_sort(texts[i]) # Sort 
            text = texts[i] 
            new_text = []
            for j in range(len(text)):
                if j == 0 :
                    new_text.append(text[j])
                elif(text[j]!=new_text[-1]):
                    new_text.append(text[j])
            texts[i] = new_text

        for i in range(len(book_titles)):
            book = (book_titles[i],texts[i])
            self.library.append(book)

        merge_sort(book_titles) # Sort to be done
        self.books = book_titles
        merge_sort(self.library)
         
    def distinct_words(self, book_title):
        index = self.books.index(book_title)
        words = self.library[index][1][:]
        return words
    
    def count_distinct_words(self, book_title):
        index = self.books.index(book_title)
        words = self.library[index][1]
        return len(words)
    
    def search_keyword(self, keyword):
        books = []
        for book in self.library:
            try:
                index = book[1].index(keyword)
                if index != -1:
                    books.append(book[0])
            except ValueError:
                pass
        return books
    
    def print_books(self):
        for book in self.library:
            words = " | ".join(book[1])
            print(book[0]+ ': ' + words)

def merge(S1, S2, S):
    if isinstance(S[0],tuple):
        i=j=0
        while i+j < len(S):
            if j == len(S2) or (i < len(S1) and S1[i][0] < S2[j][0]):
                S[i+j] = S1[i] # copy ith element of S1 as next item of S
                i += 1
            else:
                S[i+j] = S2[j] # copy jth element of S2 as next item of S
                j += 1
    else:
        i=j=0
        while i+j < len(S):
            if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
                S[i+j] = S1[i] # copy ith element of S1 as next item of S
                i += 1
            else:
                S[i+j] = S2[j] # copy jth element of S2 as next item of S
                j += 1

def merge_sort(S):
    n = len(S)
    if n < 2:
        return 
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n] 
    merge_sort(S1) 
    merge_sort(S2) 
    merge(S1, S2, S)

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.params = params 
        match name:
            case 'Jobs':
                self.library = ht.HashMap('Chain',params)
            case 'Gates':
                self.library = ht.HashMap('Linear',params)
            case 'Bezos':
                self.library = ht.HashMap('Double',params)
        
    def add_book(self, book_title, text):
        distinct_words = ht.HashSet(self.library.collision_type,self.params)
        for word in text:
            distinct_words.insert(word)
        key = (book_title, distinct_words)
        self.library.insert(key)
    
    def distinct_words(self, book_title):
        book = self.library.find(book_title)
        distinct_words = []
        if self.library.collision_type == 'Chain':
            for slot in book.table:
                for word in slot:
                    distinct_words.append(word)
        else:
            for word in book.table:
                if word is not None:
                    distinct_words.append(word)
        return distinct_words 
    
    def count_distinct_words(self, book_title):
        book = self.library.find(book_title)
        return(book.size)
        
    
    def search_keyword(self, keyword):
        books = []
        if self.library.collision_type == 'Chain':
            for slot in self.library.table:
                for book in slot:
                    if book[1].find(keyword):
                        books.append(book[0])
        else:
            for book in self.library.table:
                if book is not None and book[1].find(keyword):
                    books.append(book[0]) 
        return books
    
    def print_books(self):
        if self.library.collision_type == 'Chain':
            for slot in self.library.table:
                for book in slot:
                        formatted_slots = []
                        for slot in book[1].table:
                            if slot:  # Non-Empty slot
                                # Format each element in the chain and join with semicolons
                                elements = [str(elem) for elem in slot]
                                formatted_slots.append(" ; ".join(elements))
                            else:
                                formatted_slots.append('<EMPTY>')
                        string = " | ".join(formatted_slots)
                        print(book[0] + ': ' + string )
        else:
            for book in self.library.table: 
                    if book is not None:
                        formatted_slots = []
                        for element in book[1].table:
                                formatted_slots.append(self._format_element(element))
                        string = " | ".join(formatted_slots)
                        print(book[0] + ': ' + string )

    def _format_element(self, element):
        if element is None:
            return "<EMPTY>"
        if isinstance(element, tuple):
            # For HashMap entries
            return f"({element[0]}, {element[1]})"
        # For HashSet entries
        return str(element)    