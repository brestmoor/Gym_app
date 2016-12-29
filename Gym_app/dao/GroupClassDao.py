from Gym_app.models import GroupClass


class GroupClassDao:
    def get_class_by_id(self, id):
        return GroupClass.objects.get(id=id)
