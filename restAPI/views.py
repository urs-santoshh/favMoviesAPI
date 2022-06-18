from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movies
from .serializers import MoviesSerializers

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Api Overview':'/api/',
        'Movies List':'/movies/',
        'Movies Detail':'/movies/<pk>/',
    }
    return Response(api_urls)

@api_view(['GET','POST'])
def moviesListView(request):
    if request.method == 'GET':
        movies = Movies.objects.all()
        serializer = MoviesSerializers(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MoviesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def moviesDetailView(request,pk):
    try:
        movies = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MoviesSerializers(movies)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MoviesSerializers(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

