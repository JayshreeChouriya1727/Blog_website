from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from blog_app.models import Post, Comment,Category
from .forms import NewCommentForm
from django.views.generic import ListView


def home(request):
    all_posts = Post.objects.all() # this all_post  variable fetch the all  data from Post models
    return render(request, 'home.html', {'posts': all_posts}) # we use all data of Post models  in home.html template.(GUI)



def post_single(request, post):  # post is a slug name
    post = get_object_or_404(Post, slug=post)
    comments = post.comments.filter(status=True)
    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(
        request,
        'post_single.html',
        {
            'post': post,
            'comments': user_comment,
            'comments': comments,
            'comment_form': comment_form,
        },
    )

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts':Post.objects.filter(category__name=self.kwargs['category'])
        }
        return content

def category_list(request):
    category_list = Category.objects.exclude(name="default")
    context={
        "category_list":category_list,
    }
    return context

    