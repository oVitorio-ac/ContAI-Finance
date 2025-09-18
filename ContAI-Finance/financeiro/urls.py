from django.urls import path
from . import views
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def debug_view(request):
    return JsonResponse({
        'method': request.method,
        'status': 'OK',
        'data': dict(request.POST) if request.method == 'POST' else None
    })

urlpatterns = [
    path('', views.upload_view, name='home'),
    path('upload/', views.upload_view, name='upload'),
    path('chat/', views.chat_view, name='chat'),
    path('test/', views.test_view, name='test'),
    path('debug/', debug_view, name='debug'),
]