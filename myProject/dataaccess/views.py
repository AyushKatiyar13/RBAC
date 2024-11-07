from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import PassengerData
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def load_csv_to_db(request):
    try:
        file_path = os.path.join(settings.BASE_DIR, 'test.csv')

        df = pd.read_csv(file_path)

        with transaction.atomic():
            for _, row in df.iterrows():
                PassengerData.objects.create(
                    PassengerId=row['PassengerId'], Pclass=row['Pclass'], 
                    Name=row['Name'], Sex=row['Sex'], Age=row['Age'], 
                    SibSp=row['SibSp'], Parch=row['Parch'], Ticket=row['Ticket'], Fare=row['Fare'],
                    Cabin=row['Cabin'], Embarked=row['Embarked']
                )

        return Response({'message': 'Data loaded successfully!'})

    except Exception as e:
        return Response({'error': str(e)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def access_data(request):
    user = request.user
    if user.role == 'Admin' or user.can_view_both:
        data = PassengerData.objects.all()
    elif user.role == 'Male':
        data = PassengerData.objects.filter(Sex='male')
    elif user.role == 'Female':
        data = PassengerData.objects.filter(Sex='female')
    else:
        return Response({'error': 'No valid role'})
    
    response_data = [{'PassengerId': p.PassengerId, 'Name': p.Name, 'Sex': p.Sex} for p in data]
    return Response(response_data)