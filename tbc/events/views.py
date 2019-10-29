from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.db.models import Q


# Create your views here.

def host_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'events/ack.html', {'form': form})

    else:
        form = EventForm()

    return render(request, 'events/host_event.html', {'form': form})



def view_events(request):
    events = Event.objects.values() # Returns all events
    eventsobj = Event.objects.all()
    someevent = Event.objects.filter(Q(show_name__icontains="Show B")) # Returns a specific event based on our search
    print(someevent)
    somecomedian = someevent[0].comedians # Returns the comedian associated with that event
    print("\n")
    print(somecomedian.firstname)
    return render(request, 'events/view_events.html', {'events': events, 'eventsobj': eventsobj})
