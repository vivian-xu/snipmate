from django.shortcuts import render_to_response


def home(request):
    print("method: {}".format(request.method))
    print('post: {}'.format(request.POST))
    print("request: {}".format(request.REQUEST))
    print("get: {}".format(request.GET))
    paras = dict()
    paras['author'] = 'JackonYang'

    return render_to_response('homepage.html', paras)
