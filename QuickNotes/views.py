from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Note, User
from .serializers import NoteSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']

    userExists = User.objects.filter(Q(username=username) | Q(email=email)).exists()
    # userExists = UserSerializer(userExists)
    if userExists:
        return Response({"Failed": "Username or Email alreday exists!!!"},status=status.HTTP_409_CONFLICT,)
        
    
    user = User.objects.create(username=username,password=password,email=email)
    user.save()
    user = UserSerializer(user)
    return Response(user.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(Q(email=email))
    # userExists = UserSerializer(userExists)
    if not user.exists():
        return Response({"Failed": "Email does not exists!!!"},status=status.HTTP_409_CONFLICT,)
        
    if password != user.first().password:
        return Response({"Failed": "Invalid Password!!!"},status=status.HTTP_401_UNAUTHORIZED)
    user = UserSerializer(user.first())
    return Response(user.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def getRoutes(request):

    routes = [

        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
        {
            'Endpoint': '/register/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Register a user'
        },
        {
            'Endpoint': '/login/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Login'
        },
    ]

    return Response(routes)


# get all notes
# @api_view(['GET'])
# def getNotes(request):
#     notes = Note.objects.all().order_by('-updated')
#     serializer = NoteSerializer(notes, many=True)  # multiple object
#     return Response(serializer.data)

@api_view(['GET'])
def getNotes(request,email):
    # Filter notes based on the logged-in user
    notes = Note.objects.filter(email=email).order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


# get a single note
@api_view(['GET'])
def getNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False) # single object
    return Response(serializer.data)


# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body = data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    print(data)
    note = Note.objects.create(
        body=data['body'],
        email = data['email'],
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data 
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was Deleted')
