from django.urls import path
from . import views

app_name = 'polls' # 앱의 이름공간을 설정해준다. 다른 앱과 구분하기 위해.
urlpatterns = [
    # 제너릭 뷰 사용. detail, results, index 비슷한 페이지들 중복되는 부분 제거하고 함께 쓰자.
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# url 함수에 넘겨야하는 인수
# regex(필수) 정규표현식. 너무 복잡하게 쓰지는 말자. 느려진다.
# view(필수)
# kwargs(선택) 파라미터인듯? 딕셔너리 형태
# name(선택) URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다. 
# 이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와줍니다.