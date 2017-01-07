from Gym_app.dao.InstructorDao import InstructorDao
from Gym_app.dao.MealDao import MealDao
from Gym_app.models import Diet


class DietDao:
    def getAllForTrainer(self, email):
        instructor = InstructorDao().getByEmail(email)
        return Diet.objects.filter(trainer=instructor)

    def getAllForMember(self, email):
        pass

    def createAndFill(self, meals, name, email):
        diet = Diet()
        diet.description = name
        diet.trainer = InstructorDao().getByEmail(email)
        diet.save()
        MealDao().createMultiple(meals, diet)