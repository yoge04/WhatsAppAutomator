

# WhatsAppAutomator

This project allows you to send automated WhatsApp messages using a simple web interface built with Django. Users can input the recipient's phone number, message content, and the time to send the message. The project uses the `pywhatkit` library to handle WhatsApp message automation.

## Features

- Simple form to input the phone number, message, and time for the WhatsApp message.
- Bootstrap-based design for a responsive user interface.
- Pop-up alerts for success messages and reminders.
- Real-time feedback on message scheduling.
- **Ensure WhatsApp Web is logged in** before sending a message.

## Prerequisites

- **Python 3.12** or higher
- **Django 5.1.1**
- **pywhatkit** for message automation
- A WhatsApp account logged into WhatsApp Web

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yoge04/WhatsAppAutomator.git
   cd WhatsAppAutomator
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install django==5.1.1 pywhatkit==5.4

   ```

4. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Access the app at `http://127.0.0.1:8000/` on your browser.

## How to Use

1. **Open the Web Interface**:
   Enter the recipient's phone number (including country code), message, and the time (in 24-hour format) when you want to send the message.

2. **Pop-up Reminders**:
   A pop-up reminder will appear when you first access the site, reminding you to log in to WhatsApp Web.

3. **Success Feedback**:
   After the message is sent, a pop-up message will notify you that the message was successfully sent.

## Requirements

- Django==5.1.1
- pywhatkit==5.4
- Bootstrap (for styling)

## Project Structure

- `views.py`: Contains the form logic and handles sending messages using `pywhatkit`.
- `templates/`: HTML files with integrated Bootstrap for user interaction.
- `static/`: CSS for additional styling and JavaScript for handling modals and pop-ups.

## License

This project is licensed under the MIT License.

---

### Customization Instructions
- Replace `yoge04` with your GitHub username if necessary.
- Ensure all sections accurately reflect your project's details.

Feel free to copy and paste this text into your `README.md` file on your GitHub repository! Let me know if you need any more adjustments or additions!
