from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('schools/', views.SchoolListViews.as_view(), name='schools'),
    path('schools/<str:school_id>/', views.SchoolViews.as_view(), name='school'),

    path('events/', views.EventListViews.as_view(), name='events'),
    path('events/<str:event_id>/', views.EventViews.as_view(), name='event'),
    path('events/school/<str:school_id>/', views.SchoolEventsView.as_view(), name='school_events'),
    path('events/user/<str:user_id>/', views.UserEventsView.as_view(), name='user_events'),

    path('teams/', views.TeamListViews.as_view(), name='teams'),
    path('teams/<str:team_id>/', views.TeamViews.as_view(), name='team'),
    path('teams/event/<str:event_id>/', views.EventTeams.as_view(), name='event_teams'),

    path('chats/', views.ChatListViews.as_view(), name='chats'),
    path('chats/<str:chat_id>/', views.ChatViews.as_view(), name='chat'),
    path('chats/user/<str:user_id>/', views.UserChatViews.as_view(), name='user_chats'),

    path('messages/<str:chat_id>/', views.MessageView.as_view(), name='chat_messages'),

    path('profiles/', views.ProfileListViews.as_view(), name='profiles'),
    path('profiles/<str:user_id>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/school/<str:school_id>/', views.SchoolMemberView.as_view(), name='school_members'),
    path('profiles/event/<str:event_id>/', views.EventMemberView.as_view(), name='event_members'),
    path('profiles/team/<str:team_id>/', views.TeamMemberView.as_view(), name='team_members'),
    path('profiles/chat/<str:chat_id>/', views.TeamMemberView.as_view(), name='chat_members'),

    path('profiles/event/<str:user_id>/<str:event_id>/', views.ChangeEventMemberView.as_view(), name='change_event_member'),
    path('profiles/team/<str:user_id>/<str:team_id>/', views.ChangeTeamMemberView.as_view(), name='change_team_member'),
]