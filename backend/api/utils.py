from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Chat, School, Profile, Message, Event, Team
from .serializers import SchoolSerializer, ChatSerializer, MessageSerializer, EventSerializer, ProfileSerializer, TeamSerializer
from rest_framework import status


# GET
def get_single_object(model, modelSerializer, id):
    obj = model.objects.get(id=id)
    serializer = modelSerializer(obj, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def get_object_list(model, serializer):
    queryset = model.objects.all()
    serializer = serializer(queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def get_user_chats(user_id):
    user = Profile.objects.get(id=user_id)
    chats = user.chat_set.all()
    serializer = ChatSerializer(chats, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def get_messages(chat_id):
    chat = Chat.objects.get(id=chat_id)
    messages = chat.message_set.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def get_members(model, id):
    obj = model.objects.get(id=id)
    members = obj.members.all()
    serializer = ProfileSerializer(members, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# POST
def post_school(data):
    new_school = School.objects.create(name=data['name'], location=data['location'], url=data['url'])
    school_chat = Chat.objects.create(is_public=True)
    school_chat.school = new_school
    school_chat.save()
    serializer = SchoolSerializer(data=new_school, many=False)
    if serializer.is_valid():
        serializer.save()
        school_chat.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

def post_event(data):
    event_chat = Chat.objects.create(is_public=False)
    new_event = Event.objects.create(title=data['title'], school=School.objects.get(id=data['school']), description=data['description'])
    organizers = data['organizers']
    for organizer in organizers:
        user = Profile.objects.get(id=organizer)
        if user is not None:
            new_event.organizers.add(user)
    event_chat.event = new_event
    event_chat.save()
    new_event.save()
    serializer = EventSerializer(data=new_event, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

def post_team(data):
    team_chat = Chat.objects.create(is_public=False)
    new_team = Team.objects.create(name=data['name'], event=Event.objects.get(id=data['event']))
    team_chat.team = new_team
    team_chat.save()
    serializer = TeamSerializer(data=new_team, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

def post_profile(data):
    new_user = User.objects.create(username=data['username'], email=data['email'], password=data['password'])
    new_profile = new_user.profile
    new_profile.save()
    serializer = ProfileSerializer(data=new_profile, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# PUT
def update_school(school_id, data):
    school = School.objects.get(id=school_id)
    school.name = data['name']
    school.location = data['location']
    school.url = data['url']
    school.save()
    serializer = SchoolSerializer(data=school, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def update_event(event_id, data):
    event = Event.objects.get(id=event_id)
    event.title = data['title']
    event.description = data['description']
    event.save()
    serializer = EventSerializer(data=event, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def update_team(team_id, data):
    team = Team.objects.get(id=team_id)
    team.name = data['name']
    team.save()
    serializer = TeamSerializer(data=team, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def update_chat(chat_id, data):
    chat = Chat.objects.get(id=chat_id)
    chat.is_public = data['is_public']
    chat.save()
    serializer = ChatSerializer(data=chat, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def update_profile(user_id, data):
    profile = Profile.objects.get(id=user_id)
    user = profile.user
    user.email = data['email']
    profile.link = data['link']
    profile.info = data['info']
    if profile.school is None or profile.school.id != data['school']:
        change_school(profile, data['school'])
    user.save()
    profile.save()
    serializer = ProfileSerializer(data=profile, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# Add or Remove member
def change_school(profile, school_id):
    new_school = School.objects.get(id=school_id)
    if profile.school is not None:
        profile.chat_set.remove(profile.school.chat)
    profile.school = new_school
    profile.chat_set.add(new_school.chat)
    profile.save()

def add_member(model, user_id, id):
    obj = model.objects.get(id=id)
    profile = Profile.objects.get(id=user_id)
    obj.members.add(profile)
    profile.chat_set.add(obj.chat)
    profile.save()
    obj.save()
    serializer = ProfileSerializer(data=profile, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def remove_member(model, user_id, id):
    obj = model.objects.get(id=id)
    profile = Profile.objects.get(id=user_id)
    obj.members.remove(profile)
    profile.chat_set.remove(obj.chat)
    profile.save()
    obj.save()
    serializer = ProfileSerializer(data=profile, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)

# DELETE
def delete_object(model, model_name, id):
    obj = model.objects.get(id=id)
    obj.delete()
    return Response("The " + model_name + " is deleted!")