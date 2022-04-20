from django.shortcuts import render
from .models import user


# Create your views here.

def userData(request):

    users = user.objects.all().values()
    #users1 = user.objects.filter(user_name__startswith='a').values()
    #print("filter",users1)
    print(users[0].get('id'))
    print(users[0])
    userlist = []

    for i in users[0].values():
        userlist.append(i)

    print("user list ",userlist)
  
  
    context = {
        'users': userlist
    }
    return render(request,'orm/userdata.html',context)