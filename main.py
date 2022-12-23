import PySimpleGUI as sg

active_sites = ["Vinted", "Depop", "Amazon", "Weekday", "Urban Outfitters", "Idealo"]
inactive_sites = []

layout = [
    [sg.Text("Keyword:"), sg.Input(key="-KEYWORD-"), sg.Button("Search")],
    [
        sg.Listbox(active_sites, size=(15, len(active_sites)), key="-ACTIVE-"),
        sg.Button("Deactivate"),
        sg.Listbox(
            inactive_sites,
            size=(15, len(active_sites)),
            key="-INACTIVE-",
        ),
    ],
    [sg.Text("Active websites"), sg.Text("Inactive websites")],
]

window = sg.Window("Fabian's Website Query", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Deactivate":
        if values["-ACTIVE-"]:
            picked_website = values["-ACTIVE-"][0]
            inactive_sites.append(picked_website)
            active_sites.remove(picked_website)
            window["-ACTIVE-"].update(active_sites)
            window["-INACTIVE-"].update(inactive_sites)

window.close()
