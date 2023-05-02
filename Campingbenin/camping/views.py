from django.shortcuts import redirect, render, get_object_or_404

from .forms import EventForm, ReservationForm
from django.contrib import messages
from .models import Event
from django.utils import timezone


# from .forms import ReservationForm

from .models import Reservation, ReservationConfirmation
# Create your views here.


def index(request):
    return render(request, 'Campingbenin/index.html')

def reservation(request):
    return render(request, 'Campingbenin/reservation.html')

def event_create(request):
    return render(request, 'Campingbenin/event_create.html')


def event_details(request):
    return render(request, 'Campingbenin/event_details.html')


#Créez une vue pour afficher le formulaire de création d'événement :
def event_create_view(request):
    form = EventForm()
    return render(request, 'event_create.html', {'form': form})


# Créez une vue pour enregistrer l'événement créé :
def event_create_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre événement a été créé avec succès.')
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form': form})



def event_list_view(request):
    events = Event.objects.all()
    return render(request, 'Campingbenin/event_list.html', {'events': events})

   # Créez une vue pour afficher les détails de l'événement :

def event_detail_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

# Créez une vue pour afficher tous les événements à venir :
def events_view(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events.html', {'events': events})


# Ajoutez une vue pour confirmer la réservation :

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            confirmation_number = 'ABC123' # Remplacez par une logique pour générer un numéro de confirmation unique
            confirmation = ReservationConfirmation(reservation=reservation, confirmation_number=confirmation_number)
            confirmation.save()
            messages.success(request, 'Votre réservation a été confirmée avec succès.')
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})




def reservation_view(request):
    event = get_object_or_404(Event, pk=1)  # Récupérer l'événement concerné par la réservation
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            num_reserved = form.cleaned_data['num_of_people']
            if num_reserved <= event.num_of_seats:
                reservation = form.save()
                confirmation_number = 'ABC123'  # Remplacez par une logique pour générer un numéro de confirmation unique
                confirmation = ReservationConfirmation(reservation=reservation, confirmation_number=confirmation_number)
                confirmation.save()
                # Mettre à jour le nombre de places disponibles pour l'événement
                event.num_of_seats -= num_reserved
                event.save()
                messages.success(request, 'Votre réservation a été confirmée avec succès.')
                return redirect('home')
            else:
                messages.error(request, 'Le nombre de places restantes est insuffisant pour votre réservation.')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})



#  Ajoutez une vue pour afficher les réservations à venir :

def reservations_view(request):
    reservations = Reservation.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'reservations.html', {'reservations': reservations})