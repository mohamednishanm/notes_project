from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response

#this all are class based views

# 1-Basic ViewSet
class BasicNoteViewSet(viewsets.ViewSet):
    queryset = Note.objects.all()

    def list(self, request):
        # get all notes
        serializer = NoteSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # get individual note by id
        note = get_object_or_404(self.queryset, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def create(self, request):
        # Create note
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        # Delete a note by ID
        note = get_object_or_404(self.queryset, pk=pk)
        note.delete()
        return Response(status=204)


# 2-Generic ViewSet
class GenericNoteViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# 3-Model ViewSet
class ModelNoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
