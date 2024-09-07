from django.http import HttpResponse, HttpResponseRedirect


def return_something(request, username, **kwargs):
    return HttpResponse(f"my name is {username} and {kwargs}")


def return_something(request):
    return HttpResponseRedirect("will_return_something", kwargs={"foo": "bar"})
