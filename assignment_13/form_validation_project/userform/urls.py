from django.urls import path

from userform.views import submit_view, submit_page

urlpatterns = [
    # path('/', )
    path('submit_view/', submit_view, name='submit'),
    path('submit_page/', submit_page, name='submit_page'),
]
