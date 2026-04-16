from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Prompt
from .serializers import PromptSerializer


# =========================
# GET ALL + CREATE
# =========================
@api_view(['GET', 'POST'])
def prompt_list(request):

    # GET ALL
    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data)

    # CREATE
    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# GET ONE + UPDATE + DELETE
# =========================
@api_view(['GET', 'PUT', 'DELETE'])
def prompt_detail(request, id):   # ⭐ IMPORTANT: id (not pk)

    try:
        prompt = Prompt.objects.get(id=id)   # ⭐ match id
    except Prompt.DoesNotExist:
        return Response(
            {"error": "Prompt not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET ONE
    if request.method == 'GET':
        serializer = PromptSerializer(prompt)
        return Response(serializer.data)

    # UPDATE
    elif request.method == 'PUT':
        serializer = PromptSerializer(prompt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE ⭐ FINAL FIX
    elif request.method == 'DELETE':
        prompt.delete()
        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_200_OK
        )