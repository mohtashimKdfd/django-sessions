from django.shortcuts import render , HttpResponse, resolve_url
from .models import Users
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

def setSession(request):
    request.session['name']='Mohtashim'
    return render(request,'main/setsession.html')

def getsession(request):
    name = request.session.get('name')
    return render(request,'main/getsession.html',{'name':name})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'main/delsession.html')

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Users.objects.filter(username=username).exists():
            target = Users.objects.get(username=username)
            if (target.password == request.POST.get('password')):
                request.session['name']=username
                return render(request,'main/login.html',{'status':'Session Established'})
            else:
                return render(request,'main/login.html',{'status':'Incorrect Password'})
            
        else:
            return render(request,'main/signup.html',{'status':'No user found! Want to sign up?'})
    return render(request,'main/login.html',{'status':''})    

def signup(request):
    if 'name' in request.session:
        return render(request,'main/userpage.html',{'name':request.session.get('name')})
    else:
        return render(request,'main/signup.html',{'status':'Sign Up Page'})



def addnewUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Users.objects.filter(username=username).exists():
            return render(request,'main/login.html',{'status':'user already exsists| Try login '})
        
        else:
            new_user = Users(username=username,password=password)
            new_user.save()
            return render(request,'main/signup.html',{'status':'New user created'})
    return render(request,'main/signup.html',{'status':'Sign Up Page'})

def login(request):
    if 'name' in request.session:
                return render(request,'main/userpage.html',{'name':request.session.get('name')})
    return render(request,'main/login.html')

def user(request):
    name = request.session.get('name','Guest')
    if name == 'Guest':
        return render(request,'main/userpage.html',{'name':'User not Logged in!'})
    else:
        return render(request,'main/userpage.html',{'name':name})

def logout(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'main/userpage.html',{'name':'User not Logged in!'})
