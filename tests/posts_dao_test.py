import pytest
from json import JSONDecodeError
from config import PATH_TO_DATA, FILE_NAME_DATA
import os.path
from dao.posts_dao import PostsList


class TestCommentsList:

    @pytest.fixture()
    def post_list(self):
        return PostsList()

    @pytest.fixture()
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk", "mark"}

    def test_load_posts(self, post_list):
        """ проверка загрузки из JSON файла """
        assert type(post_list.load_posts()) == list, 'Список постов дожен быть типа list'
        assert type(post_list.load_posts()[0]) == dict, 'Пост дожен быть типа dict'

    def test_get_all_posts(self, post_list, keys_expected):
        """ проверка загрузки всех постов"""
        for post in post_list.get_all_posts([]):
            assert set(post.keys()) == keys_expected, 'Неверный список ключей в файле с постами'

    parameters_post_id  = [1,2,3,4,5,6,7,8]
    @pytest.mark.parametrize('post_id', parameters_post_id)
    def test_get_post_by_post_id(self, post_list, keys_expected,post_id):
        """ проверка выбора поста по id поста"""
        post = post_list.get_post_by_post_id(post_list.get_all_posts([]), post_id)
        assert post['pk'] == post_id, 'Неверное значение post_id'
        assert set(post.keys()) == keys_expected, 'Неверный список ключей в файле с постами'

    parameters_by_user = [('leo', {1,5}), ('johnny', {2,6}), ('hank', {3,7}), ('larry', {4,8})]
    @pytest.mark.parametrize('poster_name, pk_correct', parameters_by_user)
    def test_get_posts_by_user(self, post_list, poster_name, pk_correct):
        """ проверка загрузки постов по имени автора"""
        posts = post_list.get_posts_by_user(poster_name, post_list.get_all_posts([]))
        post_pks = set()
        for post in posts:
            post_pks.add(post['pk'])
        assert post_pks == pk_correct, 'Выбранные авторы не совпадают с заданными'

    parameters_search = [('еда', {1}), ('пока', {2,8}), ('вижу', {4})]
    @pytest.mark.parametrize('word, pk_correct', parameters_search)
    def test_search_for_posts(self, post_list, word, pk_correct):
        """ проверка постов по поиску"""
        posts = post_list.search_for_posts(word, post_list.get_all_posts([]))
        post_pks = set()
        for post in posts:
            post_pks.add(post['pk'])
        assert post_pks == pk_correct, 'Выбранные посты не совпадают с заданными'
