from itertools import chain

from django.db.models import ForeignKey


class DeepMapper:
    def model_to_dict(self, instance, fields=None, exclude=None):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
            if not getattr(f, 'editable', False):
                continue
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ForeignKey):
                data[f.name] = self.model_to_dict(f.related_model.objects.filter(pk=f.value_from_object(instance))[0])
                continue
            data[f.name] = f.value_from_object(instance)
        return data
