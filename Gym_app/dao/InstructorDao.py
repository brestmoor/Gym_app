from Gym_app.models import Instructor


class InstructorDao:
    def getByEmail(self, email):
        return Instructor.objects.get(username=email)