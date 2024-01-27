from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = '__all__'
    

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Project
        fields = '__all__'
    
        
class ProjectDetailSerializer(ProjectSerializer):
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

class PledgeDetailSerializer(PledgeSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    def update(self, instance , validated_data):
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.save()
        return instance
   
   
   
   
    