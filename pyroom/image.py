import os


class Image(object):

    def __init__(self, filename, path_from_root, root_folder, img_id):
        self.id = img_id
        self.path = os.path.join(root_folder, path_from_root, filename)

    @property
    def exists(self):
        return os

    def __str__(self):
        return f'<Image id="{self.id}" path="{self.path}">'
