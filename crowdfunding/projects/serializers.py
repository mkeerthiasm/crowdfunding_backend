from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = '__all__'
    # id = serializers.ReadOnlyField()
    # amount = serializers.IntegerField()
    # comment = serializers.CharField(max_length=200)
    # anonymous = serializers.BooleanField()
    # project = serializers.IntegerField()
    # supporter = serializers.CharField(max_length = 250)


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Project
        fields = '__all__'
    # id = serializers.ReadOnlyField()
    # title = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=None)
    # goal = serializers.IntegerField()
    # image = serializers.URLField()
    # is_open = serializers.BooleanField()
    # date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length = 250)
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    def update(self, instance , validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data('goal', instance.goal)
        instance.image = validated_data('image', instance.image)
        instance.is_open = validated_data('is_open', instance.is_open)
        instance.date_created = validated_data('date_created', instance.date_created)
        instance.owner = validated_data('owner', instance.owner)
        instance.save()
        return instance

   
   
   
   
   
    