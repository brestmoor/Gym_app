from Gym_app.models import Member


class MemberToDtoConverter:
    def convert(self, member: Member) -> {}:
        return {
            'id': member.pk,
            'fullName': member.first_name + " " + member.last_name,
            'email': member.username,
            'trainingPlan': {'description': member.plan.description,
                             'id': member.plan.pk} if member.plan is not None else None,
            'diet': {'description': member.diet.description,
                     'id': member.diet.pk} if member.diet is not None else None
        }

    def convert_extended(self, member: Member) -> {}:
        info = self.convert(member)
        info['achievements'] = member.goal_set.all()[0]
        return info
