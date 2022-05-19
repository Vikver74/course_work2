import pytest
from dao.comments_dao import CommentsList

class TestCommentsList:

    @pytest.fixture()
    def comments_list(self):
        return CommentsList()

    @pytest.fixture()
    def keys_expected(self):
        return {"post_id", "commenter_name", "comment", "pk"}

    def test_load_posts(self, comments_list):
        """ проверка загрузки из JSON файла """
        assert type(comments_list.load_comments()) == list, 'Список комментов дожен быть типа list'
        assert type(comments_list.load_comments()[0]) == dict, 'Коммент дожен быть типа dict'

    def test_get_all_comments(self, comments_list, keys_expected):
        """ проверка загрузки всех комментов"""
        for comment in comments_list.get_all_comments():
            assert set(comment.keys()) == keys_expected, 'Неверный список ключей в файле с комментами'

    parameters_post_id = [1, 2, 3, 4, 5, 6, 7, 8]
    @pytest.mark.parametrize('post_id', parameters_post_id)
    def test_get_comments_by_post_id(self, comments_list, keys_expected, post_id):
        """ проверка выбора коммента по id поста"""
        comments = comments_list.get_comments_by_post_id(post_id)
        for comment in comments:
            assert comment['post_id'] == post_id, 'Неверное значение pk в комменте'
            assert set(comment.keys()) == keys_expected, 'Неверный список ключей в файле с комментами'