from django.shortcuts import render,redirect
from .models import Customer, Domain, Score, Role
from django.contrib.auth.models import User
from django.contrib import auth

ERROR_MSG = {
    'ID_EXIST' : '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST' : '존재하지 않는 아이디 입니다.',
    'ID_PW_MISSING' : '아이디와 비밀번호를 다시 한번 확인해주세요.',
    'PW_CHECK' : '비밀번호가 일치하지 않습니다.',
}

# 회원가입
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
                    return render(request, 'users/signup2.html')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
    
    return render(request, 'users/signup.html', context)

#회원가입2 - 흥미(건강~기술)
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
        
        
        return render(request,'users/signup3.html')

    return render(request, 'users/signup2.html')

#회원가입3 - 실력테스트(각분야에대한 점수)
def signup3(request, customer_pk):
    if request.method == 'POST':
        web = request.POST['web']
        design = request.POST['design']
        machine_learning = request.POST['machine_learning']
        statistics = request.POST['statistics']
        deep_learning  = request.POST['deep_learning']
        algorithm = request.POST['algorithm']
        nlp = request.POST['nlp']
        data_score = round(int(web)*0.5 + int(design)*0.5)
        modeling_score = round(int(machine_learning)*0.25+int(deep_learning)*0.25+int(algorithm)*0.25+int(nlp)*0.25)

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
            data_score = data_score,
            modeling_score = modeling_score,
        )
        
        
        return render(request,'users/signup4.html')

    return render(request, 'users/signup3.html')

#회원가입4 - 선호역할
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
        
        
        return render(request,'users/signup5.html')

    return render(request, 'users/signup4.html')

#관심있는 스터디
def signup5(request, customer_pk):
    return redirect('home')

#로그인
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
    
    return render(request,'users/login.html',context)

#로그아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('home')
        