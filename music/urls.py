
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from music import views as view
import music

extra_patterns = [
    path('blog-details/<slug:the_slug>', view.blog_info),
    
] 

urlpatterns = [
    path('', view.index, name="home"),
    path('blog-home', view.blog_home, name="blog-home"),
    path('test', view.blog_home),
    path('words', view.words, name="wisdom"),
    path('', include(extra_patterns), name="view_info"),
    path('etv', view.emmanuel_tv, name="emmanuel"),
    path('about-me', view.aboutMe, name="about"),
]