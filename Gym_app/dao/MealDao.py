from Gym_app.models import Meal


class MealDao:
    def createMultiple(self, meals, plan):
        for meal in meals:
            new_meal = Meal()
            new_meal.day = meal['day']
            new_meal.name = meal['name']
            new_meal.order = meal['order']
            new_meal.quantity = meal['quantity']
            new_meal.calories = meal['calories']
            new_meal.plan = plan
            new_meal.save()