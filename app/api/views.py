from flask import Blueprint
from dao.posts_dao import PostsList
from dao.comments_dao import CommentsList
from flask import jsonify

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')

# API возвращает полный список постов в виде JSON-списка
@api_blueprint.route('/api/posts')
def get_all_posts_to_json():
    posts_list = PostsList()
    posts = posts_list.get_all_posts([])
    comment_list = CommentsList()
    comments = comment_list.get_all_comments()
    data_json = {'posts': posts, 'comments': comments}
    return jsonify(data_json)


# API возвращает  пост по ID в виде JSON
@api_blueprint.route('/api/posts/<int:post_id>')
def get_post_to_json(post_id):
    posts_list = PostsList()
    posts = posts_list.get_all_posts([])
    post = posts_list.get_post_by_post_id(posts, post_id)
    comment_list = CommentsList()
    comments = comment_list.get_comments_by_post_id(post_id)
    data_json = {'post': post, 'comments': comments}
    return jsonify(data_json)