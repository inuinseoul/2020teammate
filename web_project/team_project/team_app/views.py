from django.shortcuts import render,redirect
from .models import Customer
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):

    return render(request,'home.html')

ERROR_MSG = {
    'ID_EXIST' : '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST' : '존재하지 않는 아이디 입니다.',
    'ID_PW_MISSING' : '아이디와 비밀번호를 다시 한번 확인해주세요.',
    'PW_CHECK' : '비밀번호가 일치하지 않습니다.',
}

def signup(request):
    context = {
        'error' : {'state':False, 'msg':''}
    }
    
    if request.method == 'POST':

        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']
        name = request.POST['name']

        if user_id and user_pw:
            user = User.objects.filter(username=user_id)
            if len(user) ==0:
                if user_pw == user_pw_check:

                    created_user = User.objects.create_user(
                        username = user_id,
                        password = user_pw
                    )

                    Customer.objects.create(
                        user = created_user,
                        name = name
                    )

                    auth.login(request, created_user)
                    return render(request, 'signup2.html')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
    
    return render(request, 'signup.html',context)

def signup2(request):
    if request.method == 'POST':
        # Customer.objects.filter(pk=customer_pk)
        
        return render(request,'signup2.html')

    return render(request, 'signup3.html')

def signup3(request):
    return redirect('home')



def login(request):
    context = {
        'error':{'state': False, 'msg':''}
    }
    if request.method == 'POST':

        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        if (user_id and user_pw):
            user = User.objects.filter(username=user_id)

            if len(user) !=0:

                user = auth.authenticate(
                    username=user_id,
                    password=user_pw
                )
                
                if user != None : 

                    auth.login(request, user) 

                    return redirect('home')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
    
    return render(request,'login.html',context)

def edit(request, customer_pk):
    if request.method == 'POST':
        Customer.objects.filter(pk=customer_pk).update(
            name=request.POST['name'],
        )
        
        return redirect('home')
            
    customer = Customer.objects.get(pk=customer_pk)

    context = {'customer' : customer}

    return render(request, 'edit.html',context)




def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('home')

def rec(request,customer_pk):
    customer_list = Customer.objects.all()

    context = {
        'customer_list' : customer_list
    }
    return render(request, 'rec.html', context)


def grp(request, customer_pk):
    customer_list = Customer.objects.all()

    context = {
        'customer_list' : customer_list
    }
    return render(request, 'grp.html', context)

#알리미
def alarm(request, customer_pk):
    customer_alarm = Customer.objects.get(pk=customer_pk)

    context = {
        'customer_alarm' : customer_alarm
    }

    return render(request, 'alarm.html', context )