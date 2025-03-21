import Neutron
from g4f.client import Client
import re

client = Client()

win = Neutron.Window("Neurum", size=(600, 400), css="styles.css")
win.display(file="index.html")

def onSearch():
    query = win.getElementById("searchInput").value
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": query}]
        )
    content = response.choices[0].message.content
    win.getElementById("result").innerHTML = f"Search result for: {content}"

win.getElementById("searchButton").addEventListener("click", Neutron.event(onSearch))

win.show()