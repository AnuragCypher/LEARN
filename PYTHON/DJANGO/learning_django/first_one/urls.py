from django.urls import path
from first_one import views

urlpatterns = [
    path(
        "test/<str:username>",
        views.return_something,
        {"foo": "bar"},
        name="will_return_something",
    )
]
