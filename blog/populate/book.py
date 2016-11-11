from populate import base

import random
import datetime


from article.models import Book



def  populate():
    print('Populating Book', end='')
    titles = ['如何像電腦科學家一樣思考', '10 分鐘內學好 Python2', '簡單學習 Django2',
              '如何像電腦科學家一樣思考2', '10 分鐘內學好 Python3', '簡單學習 Django3',
              '如何像電腦科學家一樣思考3', '10 分鐘內學好 Python4', '簡單學習 Django4',
              '如何像電腦科學家一樣思考4']
    authors = ['w1','w2','w3','w4','w5']
    
    Book.objects.all().delete()
    
    for title in titles:
        book = Book()
        book.titles = title
        n = random.randint(0, len(authors)-1)
        book.author=authors[n]
        book.publisher = book.author
        book.publicationdate = datetime.datetime.today()
        book.version = '1'
        book.price = 1000
        book.save()
        
    print('done')
    
if __name__ == '__main__':
    populate()  