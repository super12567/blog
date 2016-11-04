from populate import base
from article.models import Article, Comment
import random


def populate():
    print('Populating Article and Comment...', end='')
    titles = ['如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django']
    contents = titles
    comments = ['文章真棒', '並不認同您的觀點', '借分享', '學好一個程式語言或框架並不容易']
    Article.objects.all().delete()
    Comment.objects.all().delete()
    for i in range(len(titles)):
        article = Article()
        article.title = titles[i]
        for j in range(50):
            article.content += contents[i] + '\n'
        article.views = random.randint(0, 20)
        article.likes = random.randint(0, 20)
        article.save()
        for j in range(len(comments)):
            Comment.objects.create(article=article, content=comments[j])
    print('done')
    
if __name__ == '__main__':
    populate()  