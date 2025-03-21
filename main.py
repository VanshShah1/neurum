import Neutron

win = Neutron.Window("Example", size=(600, 400), css="styles.css")
win.display(file="index.html")


def onClick():
    win.getElementById("title").innerHTML = "Hello:" + win.getElementById("search").value

win.getElementById("submit").addEventListener("click", Neutron.event(onClick))

win.show()