from flask import Blueprint
from dao.posts_dao import PostsList
from dao.marked_dao import MarkedPostsList
from dao.comments_dao import CommentsList
from flask import render_template, request, redirect
from logger import logger_app
from json import JSONDecodeError

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates', static_folder='/app/posts/static')

@post_blueprint.route('/')
def main_page():
    """ главная страница"""
    marked_list = MarkedPostsList()
    marked_posts_list = marked_list.get_all_markers()
    posts_list = PostsList()
    try:
        posts = posts_list.get_all_posts(marked_posts_list)
    except FileNotFoundError:
        logger_app.debug('Файл JSON с постами не найден')
        return "Файл с постами не найден"
    except JSONDecodeError:
        logger_app.debug('Файл с постами не JSON формата')
        return "Файл с постами не JSON формата"
    return render_template('index.html', posts=posts, post_count=len(posts), marked_count= len(marked_posts_list))


@post_blueprint.route('/posts/<int:post_id>', methods=['get'])
def get_post_by_id(post_id):
    """ отображает выбранный пост"""
    marked_list = MarkedPostsList()
    marked_posts_list = marked_list.get_all_markers()
    posts_list = PostsList()
    posts = posts_list.get_all_posts(marked_posts_list)
    post = posts_list.get_post_by_post_id(posts, post_id)
    content_lst = post['content'].split(' ')
    post['content'] = posts_list.modify_content_with_tags(content_lst)
    comment_list = CommentsList()
    try:
        comments = comment_list.get_comments_by_post_id(post_id)
        comments_count = len(comments)
        return render_template('post.html', post=post, comments=comments,
                           comments_count=comments_count)
    except FileNotFoundError:
        logger_app.debug('Файл JSON с комментами не найден')
        return "Файл с комментами не найден"
    except JSONDecodeError:
        logger_app.debug('Файл с комментами не JSON формата')
        return "Файл с с комментами не JSON формата"


@post_blueprint.route('/search')
def search_by_words():
    """ посик постов по вхождению ключевого слова в текст поста"""
    marked_list = MarkedPostsList()
    marked_posts_list = marked_list.get_all_markers()
    posts_list = PostsList()
    posts_with_mark = posts_list.get_all_posts(marked_posts_list)
    word = request.args.get('word')
    posts = posts_list.search_for_posts(word, posts_with_mark)
    if len(word.strip()) > 0:
        return render_template('search.html', posts=posts, post_count=len(posts))
    else:
        return redirect('/', code=302)


@post_blueprint.route('/users/<username>', methods=['get'])
def search_by_user(username):
    """ поиcк постов по автору"""
    marked_list = MarkedPostsList()
    marked_posts_list = marked_list.get_all_markers()
    posts_list = PostsList()
    posts_with_mark = posts_list.get_all_posts(marked_posts_list)
    posts = posts_list.get_posts_by_user(username, posts_with_mark)
    return render_template("user-feed.html", posts=posts)


@post_blueprint.route('/bookmarks')
def get_marked_posts():
    """ отображает список постов из закладок"""
    marked_list = MarkedPostsList()
    marked_posts_list = marked_list.get_all_markers()
    posts_list = PostsList()
    posts = posts_list.get_all_posts(marked_posts_list)
    posts_marked = marked_list.get_all_marked_posts(posts)
    if len(posts_marked) > 0:
        return render_template("bookmarks.html", posts=posts_marked)
    else:
        return redirect("/", code=302)


@post_blueprint.route('/bookmarks/add/<int:post_id>')
def add_post_to_marked(post_id):
    """ добавляет пост в закладки"""
    marked_list = MarkedPostsList()
    marked_list.add_post_to_marked(post_id)
    return redirect("/", code = 302)


@post_blueprint.route('/bookmarks/remove/<int:post_id>')
def dell_post_from_marked(post_id):
    """ удаляет пост из закладок"""
    marked_list = MarkedPostsList()
    marked_posts_list = marked_list.remove_post_from_marked(post_id)
    if  marked_posts_list > 0:
        return redirect("/bookmarks", code=302)
    else:
        return redirect("/", code=302)


@post_blueprint.route('/tag/<tagname>')
def search_by_hashtag(tagname):
    """ поиск постов по хэштэгу"""
    logger_app.debug(f' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    logger_app.debug(f'tagname     {tagname}')
    marked_list = MarkedPostsList()
    marked_posts_list = marked_list.get_all_markers()
    posts_list = PostsList()
    posts_with_tag = posts_list.get_all_posts(marked_posts_list)
    posts = posts_list.search_for_tag(tagname, posts_with_tag)
    return render_template('tag.html', posts=posts, tagname=tagname)
