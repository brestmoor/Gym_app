from Gym_app.dao.TrainingDao import TrainingDao
from Gym_app.dao.user.UserDao import UserDao


class TrainingAttendanceManager():
    def sign_up_for_class(self, class_id, email):
        user_dao = UserDao()
        training = TrainingDao().get_training_by_id(class_id)
        training.attendee = user_dao.get_by_email(email)
        training.save()

    def resign_from_class(self, email, class_id):
        training = TrainingDao().get_training_by_id(class_id)
        if email == training.attendee.email:
            training.attendee = None
            training.save()
