from django.shortcuts import render_to_response
import vm


def home(request):
    context = dict()
    context['title'] = 'life cycle'
    context['author'] = 'JackonYang'
    context['vmstate'] = vm.do(1, 2, 3)

    start = {'value': 'start',
             'type': 'submit',
             'title': 'start a vm'}
    stop = {'value': 'stop',
            'type': 'submit',
            'title': 'stop a vm',
            'onclick': "return confirm('are you sure to stop?')"}

    context['actions'] = [start, stop]

    print(context)

    return render_to_response('homepage.html', context)
