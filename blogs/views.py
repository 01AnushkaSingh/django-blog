from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog,Category

# Create your views here.
def posts_by_category(request,category_id):

    # fetch the posts that belongs to the category with the id category_id
    posts =Blog.objects.filter(status='Published',category=category_id)
    #use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category= Category.objects.get(pk=category_id)
    # except:
    #     #redirect user to homepage
    #     return redirect('home')
    
    #use this when you want to show the 404 error page if category does'nt exists
    category= get_object_or_404(Category,pk=category_id)
    context={
        'posts': posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)