
class LengthCalculator():
    def calculate_max_length(self, exercises):
        max_length = 0
        for day, values in exercises.items():
            if len(values) > max_length:
                max_length = len(values)

        return max_length