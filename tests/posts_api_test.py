import pytest
from run import app


def test_get_post_to_json():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200, 'API не отдал JSON файл (get_post_to_json)'
    assert isinstance(response.json, dict), 'Неверный формат JSON файла (get_post_to_json)'
    assert 'comments' in response.json.keys(), 'Неверный ключ get_post_to_json'
    assert 'post' in response.json.keys(), 'Неверный ключ get_post_to_json'

    keys_post = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count','likes_count','pk']
    keys_post_ = response.json['post'].keys()
    for key_ in keys_post:
        assert key_ in keys_post_, 'Неверный ключ get_post_to_json (post)'

    keys_comments = ['post_id', 'commenter_name','comment', 'pk']
    keys_comments_ = response.json['comments'][0].keys()
    for key_ in keys_comments:
        assert key_ in keys_comments_, 'Неверный ключ get_post_to_json (comments)'


def test_get_all_posts_to_json():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200, 'API не отдал JSON файл (get_all_posts_to_json)'
    assert isinstance(response.json, dict), 'Неверный формат JSON файла (get_all_posts_to_json)'
    assert 'comments' in response.json.keys(), 'Неверный ключ get_all_posts_to_json'
    assert 'posts' in response.json.keys(), 'Неверный ключ get_all_posts_to_json'

    keys_posts = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    keys_posts_ = response.json['posts'][0].keys()
    for key_ in keys_posts:
        assert key_ in keys_posts_, 'Неверный ключ get_post_to_json (post)'

    keys_comments = ['post_id', 'commenter_name', 'comment', 'pk']
    keys_comments_ = response.json['comments'][0].keys()
    for key_ in keys_comments:
        assert key_ in keys_comments_, 'Неверный ключ get_post_to_json (comments)'