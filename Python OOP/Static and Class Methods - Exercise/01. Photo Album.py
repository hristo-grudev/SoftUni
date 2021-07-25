class PhotoAlbum:
    PAGE_PHOTOS = 4
    FAILED = "No more free slots"
    DASHES = f"{11 * '-'}\n"

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.page_index = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // cls.PAGE_PHOTOS
        return cls(pages)

    def is_space(self):
        return self.page_index < self.pages and len(self.photos[self.page_index]) < self.PAGE_PHOTOS

    def new_page(self):
        if len(self.photos[self.page_index]) == self.PAGE_PHOTOS:
            self.page_index += 1
        return self.page_index

    def add_photo(self, label):
        if not self.is_space():
            return self.FAILED
        self.photos[self.page_index].append(label)
        page_added = f"{label} photo added successfully on page {self.page_index + 1} slot {len(self.photos[self.page_index])}"
        self.new_page()
        return page_added

    def display(self):
        data = self.DASHES
        for _ in self.photos:
            if _:
                data += "".join('[] ' for p in range(len(_))).strip()
            data += f"\n{self.DASHES}"
        return data


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
