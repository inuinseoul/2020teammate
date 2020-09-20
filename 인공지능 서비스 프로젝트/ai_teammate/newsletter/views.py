from django.shortcuts import render
from django_pandas.io import read_frame
from users.models import Customer
from newsletter.models import News

# [ '공통','문화/예술', '경제', '건강', '사회', '기술']


def news_all_list(request):
    page = 10
    if request.method == "POST":
        page = int(request.POST["page"]) + 10

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data = df0.loc[
        :,
        [
            "link",
            "title",
            "date",
            "content",
            "tag",
            "team_category",
        ],
    ]

    news = news_data[news_data.team_category == "공통"]
    news.reset_index(drop=True, inplace=True)

    all_list = []
    if news.shape[0] < page:
        for i in range(page - news.shape[0]):
            all_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )
    else:
        for i in range(10):
            all_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )

    context = {"all_list": all_list, "page": page, "news_num": news.shape[0]}

    return render(request, "newsletter_all.html", context)


def news_art_list(request):
    page = 10
    if request.method == "POST":
        page = int(request.POST["page"]) + 10

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data = df0.loc[
        :,
        [
            "link",
            "title",
            "date",
            "content",
            "tag",
            "team_category",
        ],
    ]

    news = news_data[news_data.team_category == "문화/예술"]
    news.reset_index(drop=True, inplace=True)

    art_list = []
    if news.shape[0] < page:
        for i in range(page - news.shape[0]):
            art_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )
    else:
        for i in range(10):
            art_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )

    context = {"art_list": art_list, "page": page, "news_num": news.shape[0]}

    return render(request, "newsletter_art.html", context)


def news_economy_list(request):
    page = 10
    if request.method == "POST":
        page = int(request.POST["page"]) + 10
    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data = df0.loc[
        :,
        [
            "link",
            "title",
            "date",
            "content",
            "tag",
            "team_category",
        ],
    ]

    news = news_data[news_data.team_category == "경제"]
    news.reset_index(drop=True, inplace=True)

    economy_list = []
    if news.shape[0] < page:
        for i in range(page - news.shape[0]):
            economy_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )
    else:
        for i in range(10):
            economy_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )
    context = {"economy_list": economy_list, "page": page, "news_num": news.shape[0]}

    return render(request, "newsletter_economy.html", context)


def news_health_list(request):
    page = 10
    if request.method == "POST":
        page = int(request.POST["page"]) + 10
    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data = df0.loc[
        :,
        [
            "link",
            "title",
            "date",
            "content",
            "tag",
            "team_category",
        ],
    ]

    news = news_data[news_data.team_category == "건강"]
    news.reset_index(drop=True, inplace=True)

    health_list = []
    if news.shape[0] < page:
        for i in range(page - news.shape[0]):
            health_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )

    else:
        for i in range(10):
            health_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )
    print(len(health_list))
    print(page)
    context = {"health_list": health_list, "page": page, "news_num": news.shape[0]}
    return render(request, "newsletter_health.html", context)


def news_social_list(request):
    page = 10
    if request.method == "POST":
        page = int(request.POST["page"]) + 10
    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data = df0.loc[
        :,
        [
            "link",
            "title",
            "date",
            "content",
            "tag",
            "team_category",
        ],
    ]

    news = news_data[news_data.team_category == "사회"]
    news.reset_index(drop=True, inplace=True)

    social_list = []
    if news.shape[0] < page:
        for i in range(page - news.shape[0]):
            social_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )
    else:
        for i in range(10):
            social_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )

    context = {"social_list": social_list, "page": page, "news_num": news.shape[0]}

    return render(request, "newsletter_social.html", context)


def news_tech_list(request):
    page = 10
    if request.method == "POST":
        page = int(request.POST["page"]) + 10
    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data = df0.loc[
        :,
        [
            "link",
            "title",
            "date",
            "content",
            "tag",
            "team_category",
        ],
    ]

    news = news_data[news_data.team_category == "기술"]
    news.reset_index(drop=True, inplace=True)

    tech_list = []
    if news.shape[0] < page:
        for i in range(page - news.shape[0]):
            tech_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )
    else:
        for i in range(10):
            tech_list.append(
                {
                    "link": news["link"][page + i - 10],
                    "title": news["title"][page + i - 10],
                    "date": news["date"][page + i - 10],
                    "category": news["team_category"][page + i - 10],
                    "tag": news["tag"][page + i - 10],
                }
            )

    context = {"tech_list": tech_list, "page": page, "news_num": news.shape[0]}

    return render(request, "newsletter_tech.html", context)
