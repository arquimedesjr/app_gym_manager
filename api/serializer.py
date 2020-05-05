from datetime import datetime
from django.core.serializers.python import Serializer

class MySerializer(Serializer):
    def handle_field(self, obj, field):
        value = field.value_from_object(obj)
        if isinstance(value, datetime):
            self._current['created_at'] = value.strftime('%d/%m/%Y')
        else:
            super(MySerializer, self).handle_field(obj, field)

