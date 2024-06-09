# this is a decorator nd not a normal function
# this decorator will run for order view
from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        returnUrl=request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login?returnUrl={returnUrl}')
        response = get_response(request)
        # pass request to view
        return response

    return middleware