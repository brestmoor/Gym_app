from Gym_app.models import Exercise


class ExercisesDao:
    def getAll(self):
        return Exercise.objects.all()

    def get_by_name(self, name):
        return Exercise.objects.get(name=name)