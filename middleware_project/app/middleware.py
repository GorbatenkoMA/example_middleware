from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

# https://www.agiliq.com/blog/2015/07/understanding-django-middlewares/

class AppMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('AppMiddleware executed')
        print(request.user)
        # another AnotherMiddleware.process_request will not be executed anymore
        # return HttpResponse('some response')

    def process_response(self, request, response):
        print('AppMiddleware process_response executed')
        return response


class AnotherMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('Another Middleware executed')

    def process_response(self, request, response):
        print('AnotherMiddleware process_response executed')
        return response
