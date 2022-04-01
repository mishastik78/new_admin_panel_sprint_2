from rest_framework import routers

from movies.api.v1 import views

router = routers.SimpleRouter()
router.register(r'movies', views.MoviesViewSet)
urlpatterns = router.urls
