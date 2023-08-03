from rest_framework.serializers import ModelSerializer
from .models import Note 


# serializer for a particular model
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
