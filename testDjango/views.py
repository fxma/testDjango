from django.http import HttpResponse,Http404
import time
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
import MySQLdb

# def hello(request):
#     return HttpResponse("hello world!")

def hello(request):
    context = dict()
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def current_time(request):
    # return HttpResponse("Current time is: "+time.strftime('%Y-%m-%d %H:%M:%S'))
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def book_list(request):
    db = MySQLdb.connect(user='test', db='testdb', passwd='test', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})