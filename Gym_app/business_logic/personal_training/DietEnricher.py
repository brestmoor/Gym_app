from collections import OrderedDict


class DietEnricher:
    def addCalories(self, diet):
        diet['calories'] = self.calculateCalories(diet['meals'])
        return diet

    def calculateCalories(self, meals_ordered):
        enriched_diet = OrderedDict([('Poniedziałek', 0), ('Wtorek', 0), ('Środa', 0),
                                     ('Czwartek', 0), ('Piątek', 0), ('Sobota', 0),
                                     ('Niedziela', 0)])
        for (row, meals) in meals_ordered.items():
            for meal in meals:
                if meal is not None:
                    enriched_diet[meal.day] += meal.calories

        return enriched_diet