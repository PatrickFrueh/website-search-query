import PySimpleGUI as sg

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
keyword = ""

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

    if event == "Search":
        if values["-KEYWORD-"]:
            print(values["-KEYWORD-"])
            print(active_websites)

window.close()
