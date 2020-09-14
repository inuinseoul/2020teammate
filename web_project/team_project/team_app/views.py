from django.shortcuts import render,redirect
from .models import Customer, Domain, Score, Role, Message
from django.contrib.auth.models import User
from django.contrib import auth
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame
import numpy as np
import pandas as pd


# 홈
def home(request):

    return render(request,'home.html')

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
        email = request.POST['email']
        phone_num = request.POST['phone_num']

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
                        name = name,
                        email = email,
                        phone_num = phone_num,
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
        
        
        return render(request,'signup3.html')

    return render(request, 'signup2.html')

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
        
        
        return render(request,'signup4.html')

    return render(request, 'signup3.html')

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
        
        
        return render(request,'signup5.html')

    return render(request, 'signup4.html')

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
    
    return render(request,'login.html',context)

#정보수정
def edit(request, customer_pk):
    if request.method == 'POST':
        Customer.objects.filter(pk=customer_pk).update(
            name=request.POST['name'],
            email=request.POST['email'],
            phone_num=request.POST['phone_num']
            )

        return redirect('edit',customer_pk)
    
    customer = Customer.objects.get(pk=customer_pk)

    context = {'customer' : customer}

    return render(request, 'edit.html',context)

#설문조사정보수정
def edit2(request, customer_pk):
    if request.method == 'POST':

        Domain.objects.filter(pk=customer_pk).update(
            health=request.POST['health'],
            economy=request.POST['economy'],
            culture_art=request.POST['culture_art'],
            education=request.POST['education'],
            society=request.POST['society'],
            technology=request.POST['technology'],
        )
        
        web = request.POST['web']
        design = request.POST['design']
        machine_learning = request.POST['machine_learning']
        statistics = request.POST['statistics']
        deep_learning  = request.POST['deep_learning']
        algorithm = request.POST['algorithm']
        nlp = request.POST['nlp']
        data_score = round(int(web)*0.5 + int(design)*0.5)
        modeling_score = round(int(machine_learning)*0.25+int(deep_learning)*0.25+int(algorithm)*0.25+int(nlp)*0.25)

        Score.objects.filter(pk=customer_pk).update(
            web=request.POST['web'],
            design=request.POST['design'],
            machine_learning=request.POST['machine_learning'],
            statistics=request.POST['statistics'],
            deep_learning=request.POST['deep_learning'],
            algorithm=request.POST['algorithm'],
            nlp=request.POST['nlp'],
            data_score = data_score,
            modeling_score = modeling_score,
        )

        Role.objects.filter(pk=customer_pk).update(
            analysis_hearts=request.POST['analysis_hearts'],
            web_hearts=request.POST['web_hearts'],
            design_hearts=request.POST['design_hearts'],
            modeling_hearts=request.POST['modeling_hearts'],
        )


        return redirect('edit2',customer_pk)
            
    customer = Customer.objects.get(pk=customer_pk)
    domain = Domain.objects.get(pk=customer_pk)
    score = Score.objects.get(pk=customer_pk)
    role = Role.objects.get(pk=customer_pk)

    context = {'customer' : customer, 'domain' : domain, 'score' : score, 'role' : role}

    return render(request, 'edit2.html',context)


#로그아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('home')

#팀메이트 추천시스템
def rec(request,customer_pk):
    customer_list = Customer.objects.all()
    score_list = Score.objects.all()
    domain_list = Domain.objects.all()
    role_list = Role.objects.all()    
    df0 = read_frame(customer_list)
    df1 = read_frame(score_list)
    df2 = read_frame(domain_list)
    df3 = read_frame(role_list)
    customer_score = df1.loc[:,['web', 'design', 'data_score', 'modeling_score']]
    customer_score_sum = customer_score.sum(axis=1)
    customer_domain = df2.loc[:,['health', 'economy', 'culture_art', 'education', 'society', 'technology']]
    customer_role = df3.loc[:,['analysis_hearts', 'web_hearts','design_hearts', 'modeling_hearts']]   

    my_num = df0[df0['user'] == customer_pk].index.tolist()[0]

    # 각 유사도측정
    score_similarity = cosine_similarity(customer_score, customer_score)
    domain_similarity = cosine_similarity(customer_domain, customer_domain)
    role_similarity = cosine_similarity(customer_role, customer_role)

    grade_subs = np.abs(customer_score_sum - customer_score_sum[my_num]) * 0.1
    evaluation_value = score_similarity[my_num-1] + grade_subs - domain_similarity[my_num-1] + role_similarity[my_num-1]
    recommend_id_list = evaluation_value.sort_values().index.tolist()
    if my_num in recommend_id_list:
        recommend_id_list.remove(my_num)
    recommend_pk_list = df0.iloc[recommend_id_list].id

    recommend_customer_list = []
    recommend_customer_score_list = []
    recommend_customer_domain_list = []
    recommend_customer_role_list = []

    for i in recommend_pk_list:
        recommend_customer_list.append(Customer.objects.get(pk=int(i)))
        recommend_customer_score_list.append(Score.objects.get(pk=int(i)))
        recommend_customer_domain_list.append(Domain.objects.get(pk=int(i)))
        recommend_customer_role_list.append(Role.objects.get(pk=int(i)))

    context = {
        'recommend_customer_list' : recommend_customer_list,
        'recommend_customer_score_list' : recommend_customer_score_list,
        'recommend_customer_domain_list' : recommend_customer_domain_list,
        'recommend_customer_role_list' : recommend_customer_role_list
    }
    return render(request, 'rec.html', context)

#추천회원 정보보기
def rec_customer(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    domain = Domain.objects.get(pk=customer_pk)
    score = Score.objects.get(pk=customer_pk)
    role = Role.objects.get(pk=customer_pk)

    context = {'customer' : customer, 'domain' : domain, 'score' : score, 'role' : role}

    return render(request, 'rec_customer.html', context)


#스터디그룹 추천시스템
def grp(request, customer_pk):
    customer_list = Customer.objects.all()

    context = {
        'customer_list' : customer_list
    }
    return render(request, 'grp.html', context)

#알리미
def alarm(request, customer_pk):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=customer_pk)
        sender = request.user

        Message.objects.create(
                            sender = sender.customer.name,
                            recipient = customer.name,
                        )

        return redirect('rec', sender.pk)
    
    message_list = Message.objects.all()

    context = {'message_list' : message_list}

    return render(request, 'alarm.html',context)

#알림삭제
def alarm2(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    message.delete()
    message_list = Message.objects.all()

    context = {'message_list' : message_list}

    return render(request, 'alarm.html',context)