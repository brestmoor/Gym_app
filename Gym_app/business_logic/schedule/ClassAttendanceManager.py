from Gym_app.dao.GroupClassDao import GroupClassDao
from Gym_app.dao.user.MemberDao import MemberDao
from Gym_app.models import GroupClass
from Gym_app.models import Member


class ClassAttendanceManager:
    def sign_up_for_class(self, classId, email):
        user_dao = MemberDao()
        clazz = GroupClassDao().get_class_by_id(classId)
        clazz.attendees.add(user_dao.get_by_email(email))

    def get_classes_for_user(self, email):
        user = MemberDao().get_by_email(email)
        classes = user.groupclass_set.all()
        if classes is None:
            return []
        else:
            return classes

    def get_ids_for_user(self, email):
        user = MemberDao().get_by_email(email)
        ids = user.groupclass_set.values_list('pk', flat=True)
        if ids is None:
            return []
        else:
            return list(ids)

    def resign_from_class(self, email, class_id):
        clazz = GroupClassDao().get_class_by_id(class_id)
        user = MemberDao().get_by_email(email)
        user.groupclass_set.remove(clazz)

    def get_attendees_for_class(self, class_id):
        clazz = GroupClassDao().get_class_by_id(class_id)
        if clazz.attendees.all() is None:
            return []
        else:
            return list(clazz.attendees.all())