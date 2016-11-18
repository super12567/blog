from django.shortcuts import render

from article.models import Article, Comment

def article(request):
    '''
    Render the article page
    '''
    
    articles = Article.objects.all()
    itemsList=[]
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'article/article.html',context)