
from django.shortcuts import render
from django import forms
import pywhatkit


class DetailsForm(forms.Form):
    phone_number = forms.CharField(
        label="Phone Number (including country code)",
        max_length=13,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., +917032491677', 'class': 'form-control'})
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'placeholder': 'Type your message here...', 'class': 'form-control'})
    )
    time = forms.TimeField(
        label="Time (24 Hours Format)",input_formats=['%H:%M'],
        widget=forms.TimeInput(attrs={'placeholder': 'e.g, 19:30', 'class': 'form-control'})

    )



def send_message(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)  # Initialize form with POST data
        if form.is_valid():  # Check if form is valid inside the POST request
            number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            time = form.cleaned_data['time']



            # Send WhatsApp message
            pywhatkit.sendwhatmsg(number, message, time.hour, time.minute)




            return render(request, 'send_message.html', {'form': form, 'success': True})
    else:
        form = DetailsForm()  # Initialize an empty form for GET request

    return render(request, 'send_message.html', {'form': form})