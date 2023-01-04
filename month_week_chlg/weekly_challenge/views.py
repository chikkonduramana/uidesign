from django.shortcuts import render

# Create your views here.

challenge_dict = {
    'monday' : 'Welcome to our 8-Week Tidy Challenge! Review the basics.',
    'tuesday' : 'Imagine Your Ideal Living Space: What does your dream home look like?',
    'wedneday' : 'Imagine Your Ideal Emotional State: How do you want to feel after this challenge?',
    'thrusday' : 'Write down your visions in a journal.',
    'friday' : 'Make a vision board.',
    'saturday' : 'Take "before" pictures of your space!',
    'sunday' : 'Continue taking "before" pictures of your space.',
}


def index_week(request):
    week_names = list(challenge_dict.keys())
    context = {'week_names':week_names}
    return render(request,'weekly_challenge/index.html',context)


def week_challenge(request,week_name):
    try:
        challenge = challenge_dict[week_name]

        context = {'week_name':week_name, 'challenge':challenge}

    except KeyError:
        context = {'week_name':week_name, 'challenge':'week Name Found'}

    return render(request,'weekly_challenge/week.html',context)
    


