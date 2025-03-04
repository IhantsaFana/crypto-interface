from django.urls import path
from .views import caesar_encrypt, vigenere_encrypt, aes_encrypt_view

urlpatterns = [
    path('caesar/', caesar_encrypt, name='caesar_encrypt'),
    path('vigenere/', vigenere_encrypt, name='vigenere_encrypt'),
    path('aes/', aes_encrypt_view, name='aes_encrypt'),
]
