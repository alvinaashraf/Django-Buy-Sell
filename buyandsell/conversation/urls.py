from django.urls import path,include
from .import views

app_name='conversation'

urlpatterns=[
    path('',views.inbox,name="inbox"),
    path('<int:pk>',views.detail_inbox,name="detail_inbox"),
    path('new/<int:item_pk>/',views.newConversation,name="new")
]