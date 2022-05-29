from . import views
from django.urls import path

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('mim', views.mim_page_view, name='mim'),
    path('educacao', views.educacao_page_view, name='educacao'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('website', views.website_page_view, name='website'),
    path('noticias', views.noticias_page_view, name='noticias'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('blog', views.blog_page_view, name='blog'),
    path('new/', views.new_post_view, name='new'),
    path('edit/<int:post_id>', views.edit_post_view, name='edit'),
    path('delete/<int:post_id>', views.delete_post_view, name='delete'),
]
