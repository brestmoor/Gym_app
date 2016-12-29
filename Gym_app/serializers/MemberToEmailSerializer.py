from datetime import date, time

from Gym_app.models import Member


class MemberToEmailSerializer:
    def serialize(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, date):
            serial = obj.isoformat()
            return serial

        if isinstance(obj, time):
            serial = obj.isoformat()
            return serial

        if isinstance(obj, Member):
            serial = obj.email
            return serial

        return obj.__dict__