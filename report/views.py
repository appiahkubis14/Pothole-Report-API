from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PotholeReport
from .serializers import PotholeReportSerializer

class PotholeReportView(APIView):
    renderer_classes = [JSONRenderer]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        reports = PotholeReport.objects.all()
        serializer = PotholeReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PotholeReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log or print the validation errors to debug
            print(serializer.errors)  # Use logging in production
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

