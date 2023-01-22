from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Chat, School, Profile, Message, Event, Team
from .serializers import SchoolSerializer, ChatSerializer, MessageSerializer, EventSerializer, TeamSerializer ,ProfileSerializer
from . import utils


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/schools/',
            'method': 'GET, POST',
            'body': None,
            'description': 'Returns an array of schools or creates a new school'
        },
        {
            'Endpoint': '/schools/school_id/',
            'method': 'GET, POST, DELETE',
            'body': None,
            'description': 'Returns, updates, or delete a single school object'
        },
        {
            'Endpoint': '/events/',
            'method': 'GET, POST',
            'body': None,
            'description': 'Returns an array of events or creates a new event'
        },
        {
            'Endpoint': '/events/event_id/',
            'method': 'GET, POST, DELETE',
            'body': {'body': ""},
            'description': 'Returns, updates, or delete a single event object'
        },
        {
            'Endpoint': 'events/school/school_id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns all events a user has attended or organized'
        },
        {
            'Endpoint': 'events/user/user_id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns all events from a school'
        },
        {
            'Endpoint': '/teams/',
            'method': 'GET, POST',
            'body': None,
            'description': 'Returns an array of team or create a new team'
        },
        {
            'Endpoint': '/teams/team_id/',
            'method': 'GET, DELETE, POST',
            'body': {'body': ""},
            'description': 'Returns, delete, or update a single team'
        },
        {
            'Endpoint': 'teams/event/event_id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns all the teams in the event'
        },
        {
            'Endpoint': '/chats',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of chats'
        },
        {
            'Endpoint': '/chats/chat_id',
            'method': 'GET POST',
            'body': None,
            'description': 'Returns or update a single chat'
        },
        {
            'Endpoint': '/chats/user/user_id',
            'method': 'GET',
            'body': None,
            'description': 'Returns all the chats used by a user'
        },
        {
            'Endpoint': 'messages/chat_id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of messages in a chat'
        },
        {
            'Endpoint': '/profiles/',
            'method': 'GET, POST',
            'body': None,
            'description': 'Returns an array of profiles or creates a new profile'
        },
        {
            'Endpoint': '/profiles/profile_id/',
            'method': 'GET, POST, DELETE',
            'body': {'body': ""},
            'description': 'Returns, updates, or delete a single profile object'
        },
        {
            'Endpoint': 'profiles/school/school_id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns all members in a school'
        },
        {
            'Endpoint': 'profiles/event/event_id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns all members in an event'
        },
        {
            'Endpoint': 'profiles/team/team_id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns all members in a team'
        },
        {
            'Endpoint': 'profiles/chat/chat_id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns all members in a chat'
        },
        {
            'Endpoint': 'profiles/school/user_id/school_id/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Change user school and remove from the chat'
        },
        {
            'Endpoint': 'profiles/event/user_id/event_id/',
            'method': 'PUT, DELETE',
            'body': {'body': ""},
            'description': 'ADD or DELETE user from the event and from the chat'
        },
        {
            'Endpoint': 'profiles/team/team_id/',
            'method': 'PUT, DELETE',
            'body': {'body': ""},
            'description': 'ADD or DELETE user from the team and from the chat'
        },
    ]
    return Response(routes)

# School
class SchoolViews(APIView):
    model = School
    serializer_class = SchoolSerializer
    def get(self, request, school_id):
        return utils.get_single_object(School, SchoolSerializer, school_id)

    def post(self, request, school_id):
        return utils.update_school(school_id, request.data)

    def delete(self, request, school_id):
        return utils.delete_object(School, 'school', school_id)

class SchoolListViews(APIView):
    model = School
    serializer_class = SchoolSerializer
    def get(self, request):
        return utils.get_object_list(School, SchoolSerializer)

    def post(self, request):
        return utils.post_school(request.data)


# Event
class EventViews(APIView):
    model = Event
    serializer_class = EventSerializer
    def get(self, request, event_id):
        return utils.get_single_object(Event, EventSerializer, event_id)

    def post(self, request, event_id):
        return utils.update_event(event_id, request.data)
    
    def delete(self, request, event_id):
        return utils.delete_object(Event, 'event', event_id)

class EventListViews(APIView):
    model = Event
    serializer_class = EventSerializer
    def get(self, request):
        return utils.get_object_list(Event, EventSerializer)
    
    def post(self, request):
        return utils.post_event(request.data)

class SchoolEventsView(APIView):
    def get(self, request, school_id):
        school = School.objects.get(id=school_id)
        queryset = school.event_set.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

class UserEventsView(APIView):
    def get(self, request, user_id):
        profile = Profile.objects.get(id=user_id)
        attended_events = profile.event_members.all()
        organized_events = profile.event_organizers.all()
        queryset = (attended_events | organized_events).distinct()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)



# Team
class TeamViews(APIView):
    model = Team
    serializer_class = TeamSerializer
    def get(self, request, team_id):
        return utils.get_single_object(Team, TeamSerializer, team_id)

    def post(self, request, team_id):
        return utils.update_team(team_id, request.data)

    def delete(self, request, team_id):
        return utils.delete_object(Team, 'team', team_id)

class TeamListViews(APIView):
    model = Team
    serializer_class = TeamSerializer
    def get(self, request):
        return utils.get_object_list(Team, TeamSerializer)
    
    def post(self, request):
        return utils.post_team(request.data)

class EventTeams(APIView):
    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        queryset = event.team_set.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)




# Chat
class ChatViews(APIView):
    model = Chat
    serializer_class = ChatSerializer
    def get(self, request, chat_id):
        return utils.get_single_object(Chat, ChatSerializer, chat_id)

    def post(self, request, chat_id):
        return utils.update_chat(chat_id, request.data)

class ChatListViews(APIView):
    model = Chat
    serializer_class = ChatSerializer
    def get(self, request):
        return utils.get_object_list(Chat, ChatSerializer)

class UserChatViews(APIView):
    model = Chat
    serializer_class = ChatSerializer
    def get(self, request, user_id):
        return utils.get_user_chats(user_id)


# Message
class MessageView(APIView):
    model = Message
    serializer_class = MessageSerializer
    def get(self, request, chat_id):
        return utils.get_messages(chat_id)


# Profile
class ProfileView(APIView):
    model = Profile
    serializer_class = ProfileSerializer
    def get(self, request, user_id):
        return utils.get_single_object(Profile, ProfileSerializer, user_id)
    
    def post(self, request, user_id):
        return utils.update_profile(user_id, request.data)

    def delete(self, request, user_id):
        return utils.delete_object(Profile, 'profile', user_id)

class ProfileListViews(APIView):
    model = Profile
    serializer_class = ProfileSerializer
    def get(self, request):
        return utils.get_object_list(Profile, ProfileSerializer)
    
    def post(self, request):
        return utils.post_profile(request.data)

class SchoolMemberView(APIView):
    model = Profile
    serializer_class = ProfileSerializer
    def get(self, request, school_id):
        school = School.objects.get(id=school_id)
        members = school.profile_set.all()
        serializer = ProfileSerializer(members, many=True)
        return Response(serializer.data)

class EventMemberView(APIView):
    model = Profile
    serializer_class = ProfileSerializer
    def get(self, request, event_id):
        return utils.get_members(Event, event_id)

class TeamMemberView(APIView):
    model = Profile
    serializer_class = ProfileSerializer
    def get(self, request, team_id):
        return utils.get_members(Team, team_id)

class ChatMemberView(APIView):
    model = Profile
    serializer_class = ProfileSerializer
    def get(self, request, chat_id):
        return utils.get_members(Chat, chat_id)


# Add or Remove Member
class ChangeEventMemberView(APIView):
    model = Profile
    serializer = ProfileSerializer
    def put(self, request, user_id, event_id):
        return utils.add_member(Event, user_id, event_id)
    def delete(self, request, user_id, event_id):
        return utils.remove_member(Event, user_id, event_id)

class ChangeTeamMemberView(APIView):
    model = Profile
    serializer = ProfileSerializer
    def put(self, request, user_id, team_id):
        return utils.add_member(Team, user_id, team_id)
    def delete(self, request, user_id, team_id):
        return utils.remove_member(Team, user_id, team_id)