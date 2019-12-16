from Actions.ItemActions import ItemActions


class ItemService:

    def __init__(self, db_session):

        self.session = db_session

    def create_item(self, title: str, price: float, user_id: int, category_id: int):
        return ItemActions(self.session).create_item(title=title, price=price,
                                                     user_id=user_id, category_id=category_id)

    def get_all_users_items(self, user_id):
        return ItemActions(self.session).get_items_for_user(user_id)