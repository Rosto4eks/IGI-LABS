from django.contrib import admin
from django.urls import path
from pizza.handlers import handlers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('statistics', handlers.statistics),

    path('', handlers.index),
    path('search', handlers.search),
    path('sign-in', handlers.sign_in),
    path('sign-up', handlers.sign_up),

    path('employee', handlers.sign_in_employee),
    path('orders', handlers.orders),
    path('completed', handlers.completed),
    path('complete-order', handlers.complete_order),

    path("add-pizza", handlers.add_pizza),
    path("edit-pizza", handlers.edit_pizza),
    path("delete-pizza", handlers.delete_pizza),

    path('profile', handlers.profile),
    path("add-to-cart", handlers.add_to_cart),
    path("cart", handlers.get_cart),
    path("remove-from-cart", handlers.remove_from_cart),
    path("buy", handlers.buy),

    path('about', handlers.about),
    path('news', handlers.news),
    path('faq', handlers.faq),
    path('contacts', handlers.contacts),
    path('policy', handlers.policy),
    path('vacancies', handlers.vacancies),
    path('reviews', handlers.reviews),
    path('new-review', handlers.new_review),
    path('delete-review', handlers.delete_review),
    path('coupons', handlers.promo),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)