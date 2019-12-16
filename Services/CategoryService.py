from Actions.CategoryActions import CategoryActions


class CategorySevice:

    def __init__(self, db_session):
        self.session = db_session

    def add_category(self, title: str, user_id: int):
        return CategoryActions(self.session).add_category(title=title, user_id=user_id)

    def get_all_users_categories(self, user_id):
        return CategoryActions(self.session).get_all_categories_for_user(user_id)