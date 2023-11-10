from django.urls import path, re_path, register_converter
from .views import post_list, post_detail, archives_year


class YearConverter:
    regex = r'20\d{2}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'year')


app_name = 'instagram'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail),
    # path('archives/<int:year>/', archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', archives_year),
    path('archives/<year:year>/', archives_year),
]
