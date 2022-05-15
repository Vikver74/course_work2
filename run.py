from flask import Flask, render_template, request, jsonify, redirect
# from dao.posts_dao import PostsList
# from dao.marked_dao import MarkedPostsList
# from dao.comments_dao import CommentsList
# from logger import logger_app
# from json import JSONDecodeError
from app.api.views import api_blueprint
from app.posts.views import post_blueprint


app = Flask(__name__)

app.register_blueprint(api_blueprint)
app.register_blueprint(post_blueprint)

app.config['JSON_AS_ASCII'] = False


# # главная страница
# @app.route('/')
# def main_page():
#
#     marked_list = MarkedPostsList()
#     marked_posts_list = marked_list.get_all_markers()
#     posts_list = PostsList()
#     try:
#         posts = posts_list.get_all_posts(marked_posts_list)
#     except FileNotFoundError:
#         logger_app.debug('Файл JSON с постами не найден')
#         return "Файл с постами не найден"
#     except JSONDecodeError:
#         logger_app.debug('Файл с постами не JSON формата')
#         return "Файл с постами не JSON формата"
#     return render_template('index.html', posts=posts, post_count=len(posts), marked_count= len(marked_posts_list))
#
#
# # отображает выбранный пост
# @app.route('/posts/<int:post_id>', methods=['get'])
# def get_post_by_id(post_id):
#     marked_list = MarkedPostsList()
#     marked_posts_list = marked_list.get_all_markers()
#     posts_list = PostsList()
#     posts = posts_list.get_all_posts(marked_posts_list)
#     post = posts_list.get_post_by_post_id(posts, post_id)
#     comment_list = CommentsList()
#     try:
#         comments = comment_list.get_comments_by_post_id(post_id)
#         comments_count = len(comments)
#         return render_template('post.html', post=post, comments=comments,
#                            comments_count=comments_count)
#     except FileNotFoundError:
#         logger_app.debug('Файл JSON с комментами не найден')
#         return "Файл с комментами не найден"
#     except JSONDecodeError:
#         logger_app.debug('Файл с комментами не JSON формата')
#         return "Файл с с комментами не JSON формата"
#
#
# # посик постов по вхождению ключевого слово в текст поста
# @app.route('/search')
# def search_by_words():
#     marked_list = MarkedPostsList()
#     marked_posts_list = marked_list.get_all_markers()
#     posts_list = PostsList()
#     posts_with_mark = posts_list.get_all_posts(marked_posts_list)
#     word = request.args.get('word')
#     posts = posts_list.search_for_posts(word, posts_with_mark)
#     return render_template('search.html', posts=posts, post_count=len(posts))
#
#
# # поиcк постов по автору
# @app.route('/users/<username>', methods=['get'])
# def search_by_user(username):
#     marked_list = MarkedPostsList()
#     marked_posts_list = marked_list.get_all_markers()
#     posts_list = PostsList()
#     posts_with_mark = posts_list.get_all_posts(marked_posts_list)
#     posts = posts_list.get_posts_by_user(username, posts_with_mark)
#     return render_template("user-feed.html", posts=posts)


# # API возвращает полный список постов в виде JSON-списка
# @app.route('/api/posts')
# def get_all_posts_to_json():
#     posts_list = PostsList()
#     posts = posts_list.get_all_posts([])
#     comment_list = CommentsList()
#     comments = comment_list.get_all_comments()
#     data_json = {'posts': posts, 'comments': comments}
#     return jsonify(data_json)
#
#
# # API возвращает  пост по ID в виде JSON
# @app.route('/api/posts/<int:post_id>')
# def get_post_to_json(post_id):
#     posts_list = PostsList()
#     posts = posts_list.get_all_posts([])
#     post = posts_list.get_post_by_post_id(posts, post_id)
#     comment_list = CommentsList()
#     comments = comment_list.get_comments_by_post_id(post_id)
#     data_json = {'post': post, 'comments': comments}
#     return jsonify(data_json)


# # отображает список постов из закладок
# @app.route('/bookmarks')
# def get_marked_posts():
#     marked_list = MarkedPostsList()
#     marked_posts_list = marked_list.get_all_markers()
#     posts_list = PostsList()
#     posts = posts_list.get_all_posts(marked_posts_list)
#     posts_marked = marked_list.get_all_marked_posts(posts)
#     if len(posts_marked) > 0:
#         return render_template("bookmarks.html", posts=posts_marked)
#     else:
#         return redirect("/", code=302)
#
#
# # добавляет пост в закладки
# @app.route('/bookmarks/add/<int:post_id>')
# def add_post_to_marked(post_id):
#     marked_list = MarkedPostsList()
#     marked_list.add_post_to_marked(post_id)
#     return redirect("/", code = 302)
#
#
# # удаляет пост из закладок
# @app.route('/bookmarks/remove/<int:post_id>')
# def dell_post_from_marked(post_id):
#     marked_list = MarkedPostsList()
#     marked_posts_list = marked_list.remove_post_from_marked(post_id)
#     if  marked_posts_list > 0:
#         return redirect("/bookmarks", code=302)
#     else:
#         return redirect("/", code=302)


if __name__ == '__main__':
    app.run()