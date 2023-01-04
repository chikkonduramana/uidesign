from django.shortcuts import render

# Create your views here.


challenge_dict = {
    'january' : 'Wake Up at 6',
    'february' : 'Read Django for 2 hours daily',
    'march' : 'Read python for exam',
    'april' : 'Run 10 KMs daily',
    'may' : 'Read Java',
    'june' : 'Read C++',
    'july' : 'sleep by 10',
    'august' : 'Read novels daily',
    'september' : 'Create templates',
    'october' : 'Complete the project',
    'november' : 'Plan for a Trip',
    'december' : 'Try not to Die',
}


def index(request):
    month_names = list(challenge_dict.keys())
    context = {'month_names':month_names}
    return render(request,'monthly_challenge/index.html',context)


def get_challenge(request,month_name):
    try:
        challenge = challenge_dict[month_name]

        context = {'month_name':month_name, 'challenge':challenge}

    except KeyError:
        context = {'month_name':month_name, 'challenge':'Month Name Found'}

    return render(request,'monthly_challenge/month.html',context)
    