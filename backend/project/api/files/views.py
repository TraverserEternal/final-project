import rest_framework.generics as generics
from project.api.files.serializers import FileSerializer
from project.base.apps.trackers.models.file import File


class FilesFromSessions(generics.ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(session__id=self.kwargs.get('pk')).order_by('created')


class MapFileToMember(generics.RetrieveUpdateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
