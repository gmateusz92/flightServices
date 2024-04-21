from django.shortcuts import render
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity = request.data['departureCity'], arrivalCity = request.data['arrivalCity'], dateOfDeparture = request.data['dateOfDeparture'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()
    
    return Response(status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['departureCity', 'arrivalCity', 'dateOfDeparture']
    permission_classes = (IsAuthenticated, )

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer 

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def find_flights(request):
    if request.method == 'POST':
        departure_city = request.POST.get('departureCity')
        arrival_city = request.POST.get('arrivalCity')
        date_of_departure = request.POST.get('dateOfDeparture')
        
        response = requests.post('http://localhost:8000/api/find_flights/', data={
            'departureCity': departure_city,
            'arrivalCity': arrival_city,
            'dateOfDeparture': date_of_departure
        })
        
        flights = response.json()
        
        return render(request, 'flights.html', {'flights': flights})
    return render(request, 'find_flights.html')

def save_reservation(request):
    if request.method == 'POST':
        flight_id = request.POST.get('flightId')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        middle_name = request.POST.get('middleName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        response = requests.post('http://localhost:8000/api/save_reservation/', data={
            'flightId': flight_id,
            'firstName': first_name,
            'lastName': last_name,
            'middleName': middle_name,
            'email': email,
            'phone': phone
        })
        
        if response.status_code == 201:
            return render(request, 'reservation_success.html')
        else:
            return render(request, 'reservation_failure.html')
    return render(request, 'save_reservation.html')


def index(request):
    return render(request, 'index.html')
