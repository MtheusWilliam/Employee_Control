from django.urls import path
from .views import *

urlpatterns = [
	path('', listing),
	path('listing/', listing),
	path('listing/<int:id>/', selection),
	path('query/', query),
	path('sort/<str:field>/', sort),
	path('insertion/', insertion),
	path('save_insertion/', save_insertion),
	path('update/<int:id>/', update),
	path('save_update/', save_update),
	path('delete/<int:id>/', delete),
	path('save_delete/', save_delete),
	path('graphics/', graphics),
]

