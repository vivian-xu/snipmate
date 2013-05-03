from django.shortcuts import render_to_response


def home(request):
    context = dict()
    context['title'] = 'life cycle'
    context['author'] = 'JackonYang'

    return render_to_response('homepage.html', context)
