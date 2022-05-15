import json
from config import PATH_TO_DATA, FILE_NAME_DATA
from json import JSONDecodeError
import os.path
from logger import logger_app


class PostsList:
    """
    Оперирует с данными из внешнего файла JSON с постами
    """
    def __init__(self,):
        self.file_data = os.path.join(PATH_TO_DATA, FILE_NAME_DATA)

    def load_posts(self):
        try:
            with open(self.file_data, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logger_app.debug('Файл JSON с постами не найден')
            raise FileNotFoundError("Файл с постами не найден")
        except JSONDecodeError:
            logger_app.debug('Файл с постами не JSON формата')
            raise JSONDecodeError("Файл с постами не JSON формата")

    def get_all_posts(self, marked):
        posts_marked = []
        for post in self.load_posts():
            if post['pk'] in marked:
                post['mark'] = 'active'
            else:
                post['mark'] = ''
            posts_marked.append(post)
        return posts_marked

    def get_post_by_post_id(self, posts_list, post_id):
        for post in posts_list:
            if post['pk'] == post_id:
                return post

    def get_posts_by_user(self, user, posts_list):
        posts = []
        for post in posts_list:
            if post['poster_name'].lower() == user.lower():
                posts.append(post)
        return posts

    def search_for_posts(self, word, posts_list):
        posts = []
        post_counter = 0
        for post in posts_list:
            if word.lower() in post['content'].lower():
                posts.append(post)
            post_counter += 1
            if post_counter >= 10: break
        return posts

