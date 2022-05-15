import json
from config import PATH_TO_DATA, FILE_NAME_COMMENTS
from json import JSONDecodeError
import os.path
from logger import logger_app


class CommentsList:
    """
    Оперирует с данными из внешнего фала JSON с комментами к постам
    """
    def __init__(self):
        self.file_comments = os.path.join(PATH_TO_DATA, FILE_NAME_COMMENTS)

    def load_comments(self):
        try:
            with open(self.file_comments, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError():
            logger_app.debug('Файл с данными о комментах не найден (comments)')
            raise FileNotFoundError('Файл с данными о комментах не найден')
        except JSONDecodeError():
            logger_app.debug('Файл с данными о комментах представлен не в формате JSON (comments)')
            raise  JSONDecodeError('Файл с данными о комментах представлен не в формате JSON')

    def get_all_comments(self):
        return self.load_comments()

    def get_comments_by_post_id(self, post_id):
        comments_list = self.get_all_comments()
        comments = []
        for comment in comments_list:
            if comment['post_id'] == post_id:
                comments.append(comment)
        return comments
