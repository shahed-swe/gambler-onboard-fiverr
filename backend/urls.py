from django.urls import path
from django.contrib.admin import site as admin_site

from backend.api.views import leaderboard, videos, livestream

urlpatterns = [
    path('admin/', admin_site.urls),

    # content
    path('api/videos', videos.GetVideos.as_view()),
    path('api/livestream', livestream.GetLiveStream.as_view()),

    # leaderboards
    path('api/leaderboards', leaderboard.GetLeaderboards.as_view()),
]
