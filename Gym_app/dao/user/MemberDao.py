from Gym_app.dao.DietDao import DietDao
from Gym_app.dao.PlansDao import PlansDao
from Gym_app.models import Goal
from Gym_app.models import Instructor
from Gym_app.models import Member


class MemberDao:
    def insert(self, user_data):
        new_member = Member.objects.create_user(user_data['email'], user_data['email'], user_data['password'])
        new_member.last_name = user_data['lastName']
        new_member.first_name = user_data['name']
        new_member.groups.addFor(4)
        new_member.save()

    def get_by_email(self, email):

        return Member.objects.get(email=email)

    def get_by_id(self, id):
        return Member.objects.get(pk=id)

    def get_all_for_trainer(self, email):
        instructor = Instructor.objects.get(username=email)
        members = instructor.member_set.all()
        if members is None:
            return []
        else:
            return members

    def update(self, newMemberData):
        member = self.get_by_email(newMemberData['email'])
        member.diet = DietDao().getById(newMemberData['diet']['id'])
        member.plan = PlansDao().getById(newMemberData['trainingPlan']['id'])
        member.save()

    def get_goal_for_member(self, member):
        return Goal.objects.get(member=member)