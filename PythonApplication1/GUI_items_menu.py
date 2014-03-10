from GUI_factory import Category_UI
class GUI_items_menu(Category_UI):
    """description of class"""
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Starting items', first_header='Not used', second_header='Items available', third_header='Description', list_width=50)
        self.f1.destroy()
        self.items = []
        self.populate_box(self.box_list, self.items, 'source/starting_items.txt')
        self.set_dictionaries(filepath_descriptions='source/items_descriptions.txt', sep='_')
        self.name='items'

