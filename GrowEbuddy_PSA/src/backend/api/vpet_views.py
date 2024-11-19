# src/backend/api/vpet_views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from prisma import Prisma  # Import the Prisma client
from .serializers import VpetSerializer  # Import the serializer

prisma = Prisma()  # Initialize the Prisma client

@api_view(['POST'])
async def create_vpet(request):
    """
    Create a new Vpet.
    """
    serializer = VpetSerializer(data=request.data)  # Validate input data
    if serializer.is_valid():
        try:
            vpet = await prisma.vpet.create(data=serializer.validated_data)  # Create the Vpet using validated data
            return Response(VpetSerializer(vpet).data, status=status.HTTP_201_CREATED)  # Return the created Vpet data
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)  # Handle any errors during creation
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

@api_view(['GET'])
async def get_vpets(request):
    """
    Retrieve all Vpets.
    """
    try:
        vpets = await prisma.vpet.find_many()  # Fetch all Vpets from the database
        return Response(VpetSerializer(vpets, many=True).data)  # Serialize and return the Vpets
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Handle any errors

@api_view(['GET'])
async def get_vpet(request, vpet_id):
    """
    Retrieve a specific Vpet by ID.
    """
    try:
        vpet = await prisma.vpet.find_unique(where={'vpet_id': vpet_id})  # Fetch the Vpet by ID
        if not vpet:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found
        return Response(VpetSerializer(vpet).data)  # Serialize and return the Vpet
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Handle any errors

@api_view(['PUT'])
async def update_vpet(request, vpet_id):
    """
    Update a specific Vpet by ID.
    """
    try:
        vpet = await prisma.vpet.find_unique(where={'vpet_id': vpet_id})  # Fetch the Vpet by ID
        if not vpet:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found

        serializer = VpetSerializer(data=request.data)  # Validate input data
        if serializer.is_valid():
            updated_vpet = await prisma.vpet.update(
                where={'vpet_id': vpet_id},
                data=serializer.validated_data  # Update the Vpet using validated data
            )
            return Response(VpetSerializer(updated_vpet).data)  # Serialize and return the updated Vpet
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Handle any errors

@api_view(['DELETE'])
async def delete_vpet(request, vpet_id):
    """
    Delete a specific Vpet by ID.
    """
    try:
        await prisma.vpet.delete(where={'vpet_id': vpet_id})  # Delete the Vpet by ID
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Handle any errors