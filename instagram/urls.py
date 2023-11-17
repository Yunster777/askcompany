from django.urls import path, re_path, register_converter

from .views import (
    post_list,
    post_detail,
    post_archive,
    post_archive_year,
    post_archive_month,
    post_archive_day,
)

from .converters import YearConverter, MonthConverter, DayConverter


register_converter(YearConverter, "year")
register_converter(MonthConverter, "month")
register_converter(DayConverter, "day")


app_name = "instagram"
urlpatterns = [
    path("", post_list, name="post_list"),
    path("<int:pk>/", post_detail, name="post_detail"),
    # path('archives/<int:year>/', archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', archives_year),
    # path('archives/<year:year>/', archives_year),
    path("archives/", post_archive, name="post_archive"),
    path("archives/<year:year>/", post_archive_year, name="post_archive_year"),
    path(
        "archives/<year:year>/<month:month>/",
        post_archive_month,
        name="post_archive_month",
    ),
    path(
        "archives/<year:year>/<month:month>/<day:day>/",
        post_archive_day,
        name="post_archive_day",
    ),
]
