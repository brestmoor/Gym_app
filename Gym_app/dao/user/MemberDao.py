from Gym_app.models import Member


class MemberDao:
    def insert(self, user_data):
        new_member = Member.objects.create_user(user_data['email'], user_data['email'], user_data['password'])
        new_member.last_name = user_data['lastName']
        new_member.first_name = user_data['name']
        new_member.groups.addFor(4)
        new_member.save()

    def get_by_full_name(self, name, last_name):
        return Member.objects.filter(first_name=name, last_name=last_name)

    def get_by_email(self, email):
        return Member.objects.get(email=email)
