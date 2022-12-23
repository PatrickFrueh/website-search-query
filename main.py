import PySimpleGUI as sg
import webbrowser as wb

# Initialize variables
active_websites = [
    "Vinted",
    "Depop",
    "Amazon",
    "Weekday",
    "Urban Outfitters",
    "Idealo",
    "eBay",
    "eBay Kleinanzeigen",
]
inactive_websites = []


# PySimpleGUI Layout
layout = [
    [sg.Text("Keyword:"), sg.Input(key="-KEYWORD-"), sg.Button("Search")],
    [
        sg.Listbox(active_websites, size=(15, len(active_websites)), key="-ACTIVE-"),
        sg.Button("Deactivate"),
        sg.Listbox(
            inactive_websites,
            size=(15, len(active_websites)),
            key="-INACTIVE-",
        ),
    ],
    [sg.Text("Active websites"), sg.Text("Inactive websites")],
]

window = sg.Window("Website Query", layout)

# Checking for changes inside the GUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Deactivate":
        if values["-ACTIVE-"]:
            picked_website = values["-ACTIVE-"][0]
            inactive_websites.append(picked_website)
            active_websites.remove(picked_website)
            window["-ACTIVE-"].update(active_websites)
            window["-INACTIVE-"].update(inactive_websites)

    # Check if the search button is pressed
    # Upon pressing check active websites and open them
    if event == "Search":
        if values["-KEYWORD-"]:
            keyword = values["-KEYWORD-"]
            keyword = keyword.replace(" ", "+")

            # Needed link structure to query the entered keyword
            link_websites_query = {
                "Vinted": f"https://www.vinted.de/catalog?search_text={keyword}",
                "Depop": f"https://www.depop.com/search/?q={keyword}",
                "Amazon": f"https://www.amazon.de/s?k={keyword}",
                "Weekday": f"https://www.weekday.com/de_de/search.html?q={keyword}",
                "Urban Outfitters": f"https://www.urbanoutfitters.com/de-de/search?q={keyword}",
                "Idealo": f"https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q={keyword}",
                "eBay": f"https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2510209.m570.l1313&_nkw={keyword}&_sacat=0",
                "eBay Kleinanzeigen": f"https://www.ebay-kleinanzeigen.de/s-{keyword}/k0",
            }
            for current_website in active_websites:
                if current_website in link_websites_query:
                    wb.open(link_websites_query[f"{current_website}"])

window.close()
