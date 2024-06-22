from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactsForm
import requests

class ContactViewPage(View):
    def get(self, request):
        form = ContactsForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactsForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Ma'lumotlarni DB ga saqlash
            try:
                self.send_telegram_message(contact)  # Telegram botga yuborish
                return redirect('success')
            except Exception as e:
                # Handle error when sending message to Telegram
                error_message = str(e)
                return render(request, 'contact.html', {'form': form, 'error_message': error_message})
        else:
            print('asdasdkj')
            return render(request, 'contact.html', {'form': form})
        
        return render(request, 'contact.html', {'form': form})

    def send_telegram_message(self, contact):
        try:
            token = '7225811705:AAH8vhezqKy47PpMbcxP7e8GtlZTJiRAh7c'
            chat_id = '2143611445'
            message = f"User Contact:\n\nName: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}"
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            data = {'chat_id': chat_id, 'text': message}
            response = requests.post(url, data=data)
            response.raise_for_status()
            # Optionally, you can log the success response
            print(f"Message sent to Telegram bot, response: {response.text}")
        except requests.exceptions.RequestException as e:
            # Handle requests exceptions
            raise Exception(f"Failed to send message to Telegram bot: {e}")
        except Exception as e:
            # Handle any other exceptions
            raise Exception(f"An error occurred: {e}")

class SuccessView(View):
    def get(self, request):
        return render(request, 'contact.html')