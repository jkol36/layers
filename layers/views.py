from django.shortcuts import render, redirect


def handle404(request):
	return render(request, '404.jade')