from django.shortcuts import render, get_object_or_404,resolve_url
from django.views.generic import ListView,CreateView ,DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post,Comment
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import PostSerializer

class PostListView(ListView):
     model = Post
     template_name = 'blog/index.html'
     paginate_by = 10

     def get_template_names(self):
          if self.request.is_ajax():
               return ['blog/_post_list.html']
          return ['blog/index.html']


index = PostListView.as_view()
post_new= CreateView.as_view(model=Post, fields='__all__')
post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

class PostDeleteView(DeleteView):
     model = Post
     success_url = reverse_lazy('blog:index')
post_delete = PostDeleteView.as_view()

class CommentCreateView(CreateView):
     model = Comment
     fields = ['message']

     def form_valid(self, form):
          comment = form.save(commit=False)
          comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
          return super().form_valid(form)

     def get_success_url(self):
          return resolve_url(self.object.post)

comment_new = CommentCreateView.as_view()

class CommentUpdateView(UpdateView):
     model = Comment
     fields = ['message']

     def get_success_url(self):
          return resolve_url(self.object.post)

comment_edit = CommentUpdateView.as_view()


class CommentDeleteView(DeleteView):
     model = Comment

     def get_success_url(self):
          return resolve_url(self.object.post)

     success_url = reverse_lazy('blog:index')

comment_delete = CommentDeleteView.as_view()

def post_list_json(request):
     qs = Post.objects.all()

     serializer = PostSerializer(qs, many=True)
     json_utf8_string = JSONRenderer().render(serializer.data)

     return HttpResponse(json_utf8_string, content_type='application/json; charset=utf8')  # 커스텀 지정