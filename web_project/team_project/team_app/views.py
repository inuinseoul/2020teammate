from django.shortcuts import render,redirect
from .models import Customer, Domain, Score, Role
from django.contrib.auth.models import User
from django.contrib import auth
from django_pandas.io import read_frame

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

def signup2(request, customer_pk):
    if request.method == 'POST':
        health = request.POST['health']
        economy = request.POST['economy']
        culture_art = request.POST['culture_art']
        education = request.POST['education']
        society  = request.POST['society']
        technology = request.POST['technology']

        customer = Customer.objects.get(pk=customer_pk)

        Domain.objects.create(
            foreignkey=customer,
            health = health,
            economy = economy,
            culture_art = culture_art,
            education = education,
            society = society,
            technology = technology,
        )
        
        
        return render(request,'signup3.html')

    return render(request, 'signup2.html')

def signup3(request, customer_pk):
    if request.method == 'POST':
        web = request.POST['web']
        design = request.POST['design']
        machine_learning = request.POST['machine_learning']
        statistics = request.POST['statistics']
        deep_learning  = request.POST['deep_learning']
        algorithm = request.POST['algorithm']
        nlp = request.POST['nlp']

        customer = Customer.objects.get(pk=customer_pk)

        Score.objects.create(
            foreignkey=customer,
            web = web,
            design = design,
            machine_learning = machine_learning,
            statistics = statistics,
            deep_learning = deep_learning,
            algorithm = algorithm,
            nlp = nlp,
        )
        
        
        return render(request,'signup4.html')

    return render(request, 'signup3.html')

def signup4(request, customer_pk):
    if request.method == 'POST':
        analysis_hearts = request.POST['analysis_hearts']
        web_hearts = request.POST['web_hearts']
        design_hearts = request.POST['design_hearts']
        modeling_hearts = request.POST['modeling_hearts']

        customer = Customer.objects.get(pk=customer_pk)

        Role.objects.create(
            foreignkey=customer,
            analysis_hearts = analysis_hearts,
            web_hearts = web_hearts,
            design_hearts = design_hearts,
            modeling_hearts = modeling_hearts,
        )
        
        
        return render(request,'signup5.html')

    return render(request, 'signup4.html')

def signup5(request, customer_pk):
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

        Domain.objects.filter(pk=customer_pk).update(
            health=request.POST['health'],
            economy=request.POST['economy'],
            culture_art=request.POST['culture_art'],
            education=request.POST['education'],
            society=request.POST['society'],
            technology=request.POST['technology'],
        )
        
        Score.objects.filter(pk=customer_pk).update(
            web=request.POST['web'],
            design=request.POST['design'],
            machine_learning=request.POST['machine_learning'],
            statistics=request.POST['statistics'],
            deep_learning=request.POST['deep_learning'],
            algorithm=request.POST['algorithm'],
            nlp=request.POST['nlp'],
        )

        Role.objects.filter(pk=customer_pk).update(
            analysis_hearts=request.POST['analysis_hearts'],
            web_hearts=request.POST['web_hearts'],
            design_hearts=request.POST['design_hearts'],
            modeling_hearts=request.POST['modeling_hearts'],
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