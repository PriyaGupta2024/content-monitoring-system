from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone 
from .utils import calculate_score, should_create_flag

from .models import *
from .serializers import *

# Create your views here.
class KeywordCreateView(APIView):
    def post(self, request):
        serializer = KeywordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
from django.utils import timezone    
    
class ScanView(APIView):
    def post(self, request):

        keywords = Keyword.objects.all()

        # MOCK DATA (simple)
        data = [
            {
                "title": "Learn Django Fast",
                "body": "Django is powerful",
                "source": "blog",
                "last_updated": timezone.now()
            }
        ]

        for item in data:
            content = ContentItem.objects.create(**item)

            for keyword in keywords:
                score = calculate_score(keyword.name, content)

                if score > 0 and should_create_flag(keyword, content):
                    Flag.objects.create(
                        keyword=keyword,
                        content_item=content,
                        score=score
                    )

        return Response({"message": "Scan complete"})
    

class FlagListView(APIView):
    def get(self, request):
        flags = Flag.objects.all()
        serializer = FlagSerializer(flags, many=True)
        return Response(serializer.data)    
        
    
    
class FlagUpdateView(APIView):
    def patch(self, request, id):
        flag = Flag.objects.get(id=id)

        status = request.data.get("status")

        if status not in ['pending', 'relevant', 'irrelevant']:
            return Response({"error": "Invalid status"}, status=400)

        flag.status = status
        flag.save()

        return Response({"message": "Updated"})