from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Prompt
from .serializers import PromptSerializer


@api_view(['GET', 'POST'])
def prompt_list(request):
    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def prompt_detail(request, id):
    try:
        prompt = Prompt.objects.get(id=id)
    except Prompt.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return Response(PromptSerializer(prompt).data)

    elif request.method == 'PUT':
        serializer = PromptSerializer(prompt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        prompt.delete()
        return Response({'message': 'Deleted'})