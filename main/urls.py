from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id, register, login_user
from main.views import logout_user, edit_product, delete_product, get_product_json, add_product_ajax
from main.views import edit_product_ajax, delete_product_ajax
app_name = 'main'

urlpatterns = [
    path("main/", show_main, name="show_main"),
    path("create-product", create_product, name="create_product"),  
    path("xml", show_xml, name="show_xml"),
    path("json", show_json, name="show_json"),
    path("xml/<int:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>/", show_json_by_id, name="show_json_by_id"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("edit-product/<int:id>/", edit_product, name="edit_product"),
    path("delete-product/<int:id>/", delete_product, name="delete_product"),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('main/delete_product_ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    
]