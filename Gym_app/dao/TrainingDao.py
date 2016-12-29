from Gym_app.models.classes_models import PersonalTraining


class TrainingDao:
    def get_training_by_id(self, id):
        return PersonalTraining.objects.get(id=id)