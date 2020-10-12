from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
	title = 'My blog'
	link = reverse_lazy('blog:post_list')
	description = 'My Latest Posts Feeds'


	def items(self):
		return  Post.published.all()[:5]

	def item_title(self, post):
		return post.title

	def item_description(self, post):
		return truncatewords(post.body, 30)