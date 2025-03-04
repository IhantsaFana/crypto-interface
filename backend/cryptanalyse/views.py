from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import caesar_cipher, vigenere_cipher, aes_encrypt, aes_decrypt

@api_view(['POST'])
def caesar_encrypt(request):
    text = request.data.get("text", "")
    shift = int(request.data.get("shift", 3))
    result = caesar_cipher(text, shift)
    return Response({"result": result})

@api_view(['POST'])
def vigenere_encrypt(request):
    text = request.data.get("text", "")
    key = request.data.get("key", "defaultkey")
    result = vigenere_cipher(text, key)
    return Response({"result": result})

@api_view(['POST'])
def aes_encrypt_view(request):
    text = request.data.get("text", "")
    key = request.data.get("key", "defaultkey").ljust(32)[:32]  # Ajuster la clé AES
    encrypt = request.data.get("encrypt", True)

    if encrypt:
        result = aes_encrypt(text, key)
    else:
        result = aes_decrypt(text, key)

    return Response({"result": result})
