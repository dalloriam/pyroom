from pyroom.image import Image

import sqlite3


class Catalog(object):

    def __init__(self, catalog_file):
        self._catalog = f'file:{catalog_file}?mode=ro'
        self._conn = sqlite3.connect(self._catalog, uri=True)

        self._root_folders = self._get_root_folders()

    def _get_root_folders(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT id_local, absolutePath from AgLibraryRootFolder
        """)

        return {f_id: path for f_id, path in c.fetchall()}

    def get_by_tag(self, name):
        c = self._conn.cursor()
        c.execute("""
          SELECT AgLibraryFile.idx_filename, AgLibraryFolder.pathFromRoot, AgLibraryFolder.rootFolder, AgLibraryFile.id_local
          FROM AgLibraryFile
          INNER JOIN Adobe_images ON AgLibraryFile.id_local = Adobe_images.rootFile
          INNER JOIN AgLibraryKeywordImage ON Adobe_images.id_local = AgLibraryKeywordImage.image
          INNER JOIN  AgLibraryKeyword ON AgLibraryKeyword.id_local = AgLibraryKeywordImage.tag
          INNER JOIN AgLibraryFolder ON AgLibraryFile.folder = AgLibraryFolder.id_local
          WHERE AgLibraryKeyword.name = ?
        """, (name,))

        images = c.fetchall()

        return [Image(img[0], img[1], self._root_folders[img[2]], img[-1]) for img in images]
