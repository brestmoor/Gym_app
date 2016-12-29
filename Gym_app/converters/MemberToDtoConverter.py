from Gym_app.dto.MemberDto import MemberDto
from Gym_app.models import Member


class MemberToDtoConverter:
    def convert(self, member: Member) -> MemberDto:
        return MemberDto(member.first_name, member.last_name)