from django.core.exceptions import ValidationError

from Gym_app.dao.user.UserDao import UserDao


class UserRegistrationValidator:
    def __init__(self):
        self.user_dao = UserDao()

    def validate(self, user_data):
        self.__are_all_fields_provided(user_data)
        self.__is_email_unique(user_data['email'])

    def __are_all_fields_provided(self, user_data):
        if 'name' not in user_data or user_data['name'] == "":
            raise ValidationError("Name must be provided")
        if 'lastName' not in user_data or user_data['lastName'] == "":
            raise ValidationError("Last name must be provided")
        if 'email' not in user_data or user_data['email'] == "":
            raise ValidationError("Email name must be provided")
        if 'password' not in user_data or user_data['password'] == "":
            raise ValidationError("Password name must be provided")

    def __is_email_unique(self, email):
        if self.user_dao.get_by_email(email):
            raise ValidationError("Provided email is already in database")
