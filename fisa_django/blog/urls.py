from django.urls import path
from . import views

# 앞으로 현재 프로젝트 내에서 blog/ 안에 있는 경로는 모두 blog_app
app_name= 'blog_app'  # blog_app:blog  -> localhost:8000/blog/post-list
# url 'blog_app:about_me'  localhost:8000/blog/about-me 
urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    # path('', views.index), # localhost:8000/blog 경로, 경로를 호출하면 실행할 함수의 위치
    path('post-list/', views.PostList.as_view(), name='post_list'), #  name= 개발자가 이 주소를 부를 이름
    path('', views.about_me, name='about_me'), # blog_app:about_me     blog/
    path('<int:pk>', views.PostDetail.as_view()), # <자료형:필드명> 
    path('create-post/', views.PostCreate.as_view(), name="create"),  # blog_app:create
    # update, delete는 이미 있는 글을 수정/삭제하므로 글번호가 필요합니다. 
    path('edit-post/<int:pk>', views.PostUpdate.as_view(), name='update'),
    path('delete-post/<int:pk>', views.PostDelete.as_view(), name='delete'),



    path('user-delete/', views.user_delete, name='user_delete'), # blog_app:user_delete
    # 같은 tag를 가진 글끼리 게시판에 보여주기
    path('tag/<str:slug>', views.tag_posts, name="tag"), # <자료형:필드명> 
]