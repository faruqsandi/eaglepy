from .application import Application
from .folder import Folder
from .item import Item
from .library import Library


class EagleClient:
    def __init__(self, base_url):
        self.application = Application(base_url)
        self.folder = Folder(base_url)
        self.item = Item(base_url)
        self.library = Library(base_url)
