"""
    Project by: Rushikesh Patl
    Project: A notifing program which notifies to drink water using python
"""

import time
from plyer import notification

notification.notify(
    title = "Please drink water now",
    message = "It will keep your health fit",
    app_icon = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.iconscout.com%2Ficon%2Ffree%2Fpng-512%2Fwater-glass-2-486115.png&imgrefurl=https%3A%2F%2Ficonscout.com%2Ficon%2Fwater-glass-2&tbnid=4jJWb4xwrnmXVM&vet=12ahUKEwio-cTt7ZHwAhWbAHIKHVVyDXAQMygEegUIARDxAQ..i&docid=0AilENyNHKK0NM&w=512&h=512&q=glass%20icon%20pic&ved=2ahUKEwio-cTt7ZHwAhWbAHIKHVVyDXAQMygEegUIARDxAQ",
    timeout = 30
)