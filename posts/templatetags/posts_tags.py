from django.template import Library, Node
from posts.models import Post

register = Library()

@register.tag
def get_latest_posts(parser, token):
    """
    {% get_latest_posts %}
    """
    return LatestPostsNode()

class LatestPostsNode(Node):
    def render(self, context):
        context['latest_posts'] = Post.objects.order_by('-created_at')[:5]
        return ''
