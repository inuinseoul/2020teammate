from django.shortcuts import render, redirect
from users.models import Customer, Domain, Score, Role
from django.contrib.auth.models import User
from django.contrib import auth

# 정보수정
def info_edit(request, customer_pk):
    if request.method == "POST":
        Customer.objects.filter(pk=customer_pk).update(
            name=request.POST["name"],
            email=request.POST["email"],
            phone_num=request.POST["phone_num"],
        )

        return redirect("home")

    customer = Customer.objects.get(pk=customer_pk)

    context = {"customer": customer}

    return render(request, "edit/info_edit.html", context)


# 설문조사정보수정
def survey_edit(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    if request.method == "POST":

        health = request.POST["health"]
        economy = request.POST["economy"]
        culture_art = request.POST["culture_art"]
        education = request.POST["education"]
        society = request.POST["society"]
        technology = request.POST["technology"]

        Domain.objects.filter(foreignkey=customer).update(
            health=request.POST["health"],
            economy=request.POST["economy"],
            culture_art=request.POST["culture_art"],
            education=request.POST["education"],
            society=request.POST["society"],
            technology=request.POST["technology"],
            domain_sum=int(health)
            + int(economy)
            + int(culture_art)
            + int(education)
            + int(society)
            + int(technology),
        )

        web = request.POST["web"]
        design = request.POST["design"]
        machine_learning = request.POST["machine_learning"]
        statistics = request.POST["statistics"]
        deep_learning = request.POST["deep_learning"]
        algorithm = request.POST["algorithm"]
        nlp = request.POST["nlp"]
        data_score = round(int(statistics) * 0.5 + int(machine_learning) * 0.5)
        modeling_score = round(
            int(machine_learning) * 0.25
            + int(deep_learning) * 0.25
            + int(algorithm) * 0.25
            + int(nlp) * 0.25
        )

        Score.objects.filter(foreignkey=customer).update(
            web=request.POST["web"],
            design=request.POST["design"],
            machine_learning=request.POST["machine_learning"],
            statistics=request.POST["statistics"],
            deep_learning=request.POST["deep_learning"],
            algorithm=request.POST["algorithm"],
            nlp=request.POST["nlp"],
            data_score=data_score,
            modeling_score=modeling_score,
            score_sum=int(web)
            + int(design)
            + int(machine_learning)
            + int(statistics)
            + int(deep_learning)
            + int(algorithm)
            + int(nlp)
            + int(data_score)
            + int(modeling_score),
        )

        analysis_hearts = request.POST["analysis_hearts"]
        web_hearts = request.POST["web_hearts"]
        design_hearts = request.POST["design_hearts"]
        modeling_hearts = request.POST["modeling_hearts"]

        Role.objects.filter(foreignkey=customer).update(
            analysis_hearts=request.POST["analysis_hearts"],
            web_hearts=request.POST["web_hearts"],
            design_hearts=request.POST["design_hearts"],
            modeling_hearts=request.POST["modeling_hearts"],
            role_sum=int(analysis_hearts)
            + int(web_hearts)
            + int(design_hearts)
            + int(modeling_hearts),
        )

        print("수정완료")

        return redirect("home")

    domain = Domain.objects.get(foreignkey=customer)
    score = Score.objects.get(foreignkey=customer)
    role = Role.objects.get(foreignkey=customer)

    context = {"customer": customer, "domain": domain, "score": score, "role": role}

    return render(request, "edit/survey_edit.html", context)
