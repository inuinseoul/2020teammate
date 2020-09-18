from django.shortcuts import render
from django_pandas.io import read_frame
from users.models import Customer
from newsletter.models import News

#[ '공통','문화/예술', '경제', '건강', '사회', '기술']

# Create your views here.
def news_select(request):
    return render(request, "news_select.html")

def news_all_list(request) : 

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data=df0.loc[:,
        [
            'link',
            'title',
            'date',
            'content',
            'tag',
            'team_category',
        ]]

    art=news_data[news_data.team_category == '공통']
    art.reset_index(drop=True,inplace=True)

    all_list = []


    for i in range(10) :
        all_list.append({'link':art['link'][i],'title':art['title'][i],'date': art['date'][i],'category': art['team_category'][i],'tag' : art['tag'][i]})#,art['title'][i],art['team_category'][i]})
        # art_tag.append(art['tag'][i])
        # art_headline.append(art['title'][i])
        # art_category.append(art['team_category'][i])


    context = {
        'all_list':all_list,
        }
        
    return render(request, "newsletter_all.html", context)

def news_art_list(request) : 

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data=df0.loc[:,
        [
            'link',
            'title',
            'date',
            'content',
            'tag',
            'team_category',
        ]]

    art=news_data[news_data.team_category == '문화/예술']
    art.reset_index(drop=True,inplace=True)

    art_list = []


    for i in range(10) :
        art_list.append({'link':art['link'][i],'tag' : art['tag'][i],'title':art['title'][i],'date': art['date'][i],'category': art['team_category'][i]})#,art['title'][i],art['team_category'][i]})
        # art_tag.append(art['tag'][i])
        # art_headline.append(art['title'][i])
        # art_category.append(art['team_category'][i])


    context = {
        'art_list':art_list,
        }
        
    return render(request, "newsletter_art.html", context)

def news_economy_list(request) : 

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data=df0.loc[:,
        [
            'link',
            'title',
            'date',
            'content',
            'tag',
            'team_category',
        ]]

    art=news_data[news_data.team_category == '경제']
    art.reset_index(drop=True,inplace=True)

    economy_list = []


    for i in range(10) :
        economy_list.append({'tag' : art['tag'][i],'link':art['link'][i],'title':art['title'][i],'date': art['date'][i],'category': art['team_category'][i]})#,art['title'][i],art['team_category'][i]})
        # art_tag.append(art['tag'][i])
        # art_headline.append(art['title'][i])
        # art_category.append(art['team_category'][i])


    context = {
        'economy_list':economy_list,
        }
        
    return render(request, "newsletter_economy.html", context)

def news_health_list(request) : 

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data=df0.loc[:,
        [
            'link',
            'title',
            'date',
            'content',
            'tag',
            'team_category',
        ]]

    art=news_data[news_data.team_category == '건강']
    art.reset_index(drop=True,inplace=True)

    art_list = []


    for i in range(10) :
        art_list.append({'tag' : art['tag'][i],'link':art['link'][i],'title':art['title'][i],'date': art['date'][i],'category': art['team_category'][i]})#,art['title'][i],art['team_category'][i]})
        # art_tag.append(art['tag'][i])
        # art_headline.append(art['title'][i])
        # art_category.append(art['team_category'][i])


    context = {
        'health_list':art_list,
        }
        
    return render(request, "newsletter_health.html", context)

def news_social_list(request) : 

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data=df0.loc[:,
        [
            'link',
            'title',
            'date',
            'content',
            'tag',
            'team_category',
        ]]

    art=news_data[news_data.team_category == '사회']
    art.reset_index(drop=True,inplace=True)

    art_list = []


    for i in range(10) :
        art_list.append({'tag' : art['tag'][i],'link':art['link'][i],'title':art['title'][i],'date': art['date'][i],'category': art['team_category'][i]})#,art['title'][i],art['team_category'][i]})
        # art_tag.append(art['tag'][i])
        # art_headline.append(art['title'][i])
        # art_category.append(art['team_category'][i])


    context = {
        'social_list':art_list,
        }
        
    return render(request, "newsletter_social.html", context)

def news_tech_list(request) : 

    news_data = News.objects.all()
    df0 = read_frame(news_data)

    news_data=df0.loc[:,
        [
            'link',
            'title',
            'date',
            'content',
            'tag',
            'team_category',
        ]]

    art=news_data[news_data.team_category == '기술']
    art.reset_index(drop=True,inplace=True)

    art_list = []


    for i in range(10) :
        art_list.append({'tag' : art['tag'][i],'link':art['link'][i],'title':art['title'][i],'date': art['date'][i],'category': art['team_category'][i]})#,art['title'][i],art['team_category'][i]})
        # art_tag.append(art['tag'][i])
        # art_headline.append(art['title'][i])
        # art_category.append(art['team_category'][i])


    context = {
        'tech_list':art_list,
        }
        
    return render(request, "newsletter_tech.html", context)
