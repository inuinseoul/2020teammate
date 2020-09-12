from sklearn.metrics.pairwise import cosine_similarity

# 각 유사도측정


def rec(request,customer_pk):
    customer_list = Customer.objects.all()
    score_list = Score.objects.all()
    domain_list = Domain.objects.all()
    role_list = Role.objects.all()

    # df 형태로 불러오기
    customer_score = ''
    customer_domain = ''
    customer_role = ''

    grade_similarity = cosine_similarity(customer_score, customer_score)
    interest_similarity = cosine_similarity(customer_domain, customer_domain)
    preference_role_similarity = cosine_similarity(customer_role, customer_role)

    input_num = customer_pk
    grade_subs = np.abs(customer_score_sum - customer_score_sum[input_num]) * 0.1
    evaluation_value = grade_similarity[input_num-1] + grade_subs - (interest_similarity[input_num-1]) + preference_role_similarity[input_num-1]

    context = {
        'customer_list' : customer_list
    }
    return render(request, 'rec.html', context)