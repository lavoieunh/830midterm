import csv
import pandas as pd

sortingbooks = pd.read_csv("BookSheet.csv")

class ReturnList(object):

    def Author_List(self):
        authors =  sortingbooks
        author_books = authors.sort_values(['Author'], ascending=[True])
        print(author_books)

    def Title_List(self):
        titles =  sortingbooks
        titles_books = titles.sort_values(['Title'], ascending=[True])
        print(titles_books)

    def Year_Published(self):
        yearpub =  sortingbooks
        year_pub = yearpub.sort_values(['YearPublished'], ascending=[True])
        print(year_pub)

    def Book_Summary(self):
        booksum =  sortingbooks
        book_summary = booksum.sort_values(['Summary'], ascending=[True])
        print(book_summary)
