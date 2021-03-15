class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.page = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages = photos_count // 4)

    def add_photo(self, label: str):
        photos_per_page = 4
        try:
            if len(self.photos[self.page]) < photos_per_page:
                self.photos[self.page].append(label)
                return f"{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}"
            else:
                self.page += 1
                self.photos[self.page].append(label)
                return f"{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}"
        except:
            return f"No more free spots"

    def display(self):
        res = ""
        for sublist in range(len(self.photos)):
            res += f"-----------\n"
            res += " ".join(["[]" for _ in range(len(self.photos[sublist]))])
            res += "\n"
        res += "-----------\n"
        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())

import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free spots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------\n")


if __name__ == "__main__":
    unittest.main()
