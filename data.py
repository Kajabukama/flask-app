
def Articles():
    articles = [
        {
            'id': 1,
            'title':'Article One',
            'content':'Sample content for article one',
            'date':'2017-09-02',
            'author':'Yusuph H. Kajabukama'
        },
        {
            'id': 2,
            'title':'Article Two',
            'content':'Sample content for article three',
            'date':'2017-12-12',
            'author':'Johari H. Kajabukama'
        },
        {
            'id': 3,
            'title':'Article Three',
            'content':'Sample content for article three',
            'date':'2017-02-05',
            'author':'John Doe'
        }
    ]

    return articles

def getItem(id):
    return [item for item in Articles() if item["id"] == id]

def findArticle(id):
    for article in Articles():
        if article['id'] == int(id):
            return article