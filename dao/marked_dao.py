import json
from config import PATH_TO_DATA, FILE_NAME_BOOKMARKS
from json import JSONDecodeError
import os.path
from logger import logger_app


class MarkedPostsList:
    """
    Оперирует с данными из внешнего фала JSON с закладками
    """
    def __init__(self):
        self.file_data = os.path.join(PATH_TO_DATA, FILE_NAME_BOOKMARKS)

    def load_markers(self):
        try:
            with open(self.file_data, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            marked_post_list = []
            return marked_post_list
        except JSONDecodeError:
            marked_post_list = []
            return marked_post_list

    def get_all_markers(self):
        return  self.load_markers()

    def get_all_marked_posts(self, posts):
        posts_marked =[]
        for post in posts:
            if post['mark'] == 'active':
                posts_marked.append(post)
        return posts_marked

    def add_post_to_marked(self, post_id):
        marked_post_list = self.get_all_markers()
        marked_post_list.append(post_id)
        marked_verifyed = list(set(marked_post_list))
        with open(self.file_data, 'w', encoding='utf-8') as file:
            json.dump(marked_verifyed, file)
        return

    def remove_post_from_marked(self, post_id):
        marked_post_list = self.get_all_markers()
        marked_post_list.remove(post_id)
        with open(self.file_data, 'w', encoding='utf-8') as file:
            json.dump(marked_post_list, file)
        return len(marked_post_list)
