from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyCustomUserModel
from rest_framework import status


@api_view(['POST'])
def create(request):
    try:
        email = request.data.get("email")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        gender = request.data.get("gender")
        if None in [email, password, first_name, last_name, gender]:
            raise ValueError("All fields are required")
        gender = int(gender)
        created_data = MyCustomUserModel.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
        )
        if not created_data:
            raise ValueError("Error during user creation")
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_list(request):
    data = MyCustomUserModel.objects.all()
    response_data = [
        {"id": i.id, "email": i.email, "first_name": i.first_name, "last_name": i.last_name, "gender": i.gender}
        for i in data
    ]
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_detail(request, id):
    data = MyCustomUserModel.objects.get(id=id)
    email = data.email
    first_name = data.first_name
    last_name = data.last_name
    gender = data.gender
    return Response({"email": email, "first_name": first_name, "last_name": last_name, "gender": gender})


@api_view(['PUT'])
def user_update(request, id):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    gender = request.data.get('gender')
    MyCustomUserModel.objects.filter(id=id).update(first_name=first_name, last_name=last_name,
                                                                  gender=gender)
    updated_data = MyCustomUserModel.objects.get(id=id)
    return Response(
        {"email": updated_data.email, "first_name": updated_data.first_name, "last_name": updated_data.last_name,
         "gender": updated_data.gender})


@api_view(['DELETE'])
def user_delete(request, id):
    MyCustomUserModel.objects.filter(id=id).delete()
    return Response({"message": "Successfully deleted"})
