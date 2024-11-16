from django.shortcuts import render, redirect
from task.errands import test_func, hello_test


# Create your views here.

def test(request):
    test_func.delay()
    return redirect('home')