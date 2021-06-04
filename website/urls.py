from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('carnes', views.carnes_page_view, name='carnes'),
    path('doces', views.doces_page_view, name='doces'),
    path('opiniao', views.opiniao_page_view, name='opiniao'),
    path('peixe', views.peixe_page_view, name='peixe'),
    path('veggie', views.veggie_page_view, name='veggie'),
    path('veggieReceita', views.veggieR_page_view, name='veggieReceita'),
    path('carnesReceita', views.carnesR_page_view, name='carnesReceita'),
    path('peixeReceita', views.peixeR_page_view, name='peixeReceita'),
    path('docesReceita', views.docesR_page_view, name='docesReceita'),
    path('videos', views.videos_page_view, name='videos'),
    path('quemSomos', views.quemSomos_page_view, name='quemSomos'),
    path('receitaNova', views.receitaNova_page_view, name='receitaNova'),
    path('contactos', views.contactos_page_view, name='contactos'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('quizz_resultados/<int:id>',views.quizz_resultados,name="quizz_resultados"),
    path('edita/<int:contacto_id>', views.edita_contactos_view, name='edita'),
    path('apaga/<int:contacto_id>', views.apaga_contactos_view, name='apaga'),
]