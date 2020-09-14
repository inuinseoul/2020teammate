from django.shortcuts import render,redirect
from users.models import Customer, Domain, Score, Role
from django.contrib.auth.models import User
from django.contrib import auth

#정보수정
def info_edit(request, customer_pk):
    if request.method == 'POST':
        Customer.objects.filter(pk=customer_pk).update(
            name=request.POST['name'],
            email=request.POST['email'],
            phone_num=request.POST['phone_num']
            )

        return redirect('home')
    
    customer = Customer.objects.get(pk=customer_pk)

    context = {'customer' : customer}

    return render(request, 'edit/info_edit.html',context)

#설문조사정보수정
def survey_edit(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    if request.method == 'POST':

        Domain.objects.filter(foreignkey=customer).update(
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

        Score.objects.filter(foreignkey=customer).update(
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

        Role.objects.filter(foreignkey=customer).update(
            analysis_hearts=request.POST['analysis_hearts'],
            web_hearts=request.POST['web_hearts'],
            design_hearts=request.POST['design_hearts'],
            modeling_hearts=request.POST['modeling_hearts'],
        )

        print("수정완료")


        return redirect('home')            
    
    domain = Domain.objects.get(foreignkey=customer)
    score = Score.objects.get(foreignkey=customer)
    role = Role.objects.get(foreignkey=customer)

    context = {'customer' : customer, 'domain' : domain, 'score' : score, 'role' : role}

    return render(request, 'edit/survey_edit.html',context)