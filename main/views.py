from django.shortcuts import render , HttpResponse
# Create your views here.

#Important Notes
s='The session frameworks lets you store and retreive arbitrary data \
    it stores data on the server side and does the sending and receiving of cookies \
    <br> \
    Cookies in this case will contain the session id aonly and not the data\
    data is kept at server and an id is stored in browser  a session key/id is matched with data\
    So jab bhi client ko data chaiye to session id ke saath fetch karna hoga \
    <br> \
    By default Django stores sessions in our database \
    <br> The djangose'
def home(request):
    return HttpResponse('<h1>{}</h1>'.format(s))

def getSession(request):
    return render(request,'main/getsession.html')
