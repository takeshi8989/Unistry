from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import School, Chat, Profile, Message, Event, Team

class SchoolSerializer(ModelSerializer):
    num_of_events = serializers.SerializerMethodField()
    num_of_members = serializers.SerializerMethodField()
    # ten_member_images

    class Meta:
        model = School
        fields = ('id', 'name','location','url', 'image', 'num_of_events', 'num_of_members')

    def get_num_of_events(self, instance):
        return instance.event_set.count()

    def get_num_of_members(self, instance):
        return instance.profile_set.count()

class EventSerializer(ModelSerializer):
    members = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()
    school_id = serializers.SerializerMethodField()
    teams = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = ('id', 'title', 'organizers', 'members', 'school', 'school_id', 'teams', 'description', 'created_at')

    def get_members(self, instance):
        profile_list = instance.members.all()
        result = []
        for profile in profile_list:
            # image
            result.append(profile.user.username)
        return result

    def get_school(self, instance):
        return instance.school.name

    def get_school_id(self, instance):
        return instance.school.id
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")

    def get_teams(self, instance):
        teams = instance.team_set.all()
        result = []
        for team in teams:
            team_members = team.members.all().values_list('id', flat=True)
            result.append({'team': team.id, 'members': team_members})
        return result

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'