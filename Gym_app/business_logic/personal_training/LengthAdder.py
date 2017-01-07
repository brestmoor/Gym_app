from Gym_app.business_logic.personal_training.LengthCalculator import LengthCalculator


class LengthAdder():
    def addFor(self, plans):
        for plan in plans:
            plan['maxLength'] = LengthCalculator().calculate_max_length(plan['exercises'])

