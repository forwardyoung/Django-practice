from django.urls import path
app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create')
]