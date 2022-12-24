import PySimpleGUI as sg
import webbrowser as wb
import json

sg.theme("Topanga")
# sg.theme("LightGreen3")

# Initialize variables - read current site names
with open("links.json", "r") as json_file:
    links = json.load(json_file)
    active_websites = list(links["links"].keys())
# active_websites = [
#     "Vinted",
#     "Depop",
#     "Amazon",
#     "Weekday",
#     "Urban Outfitters",
#     "Idealo",
#     "eBay",
#     "Kleinanzeigen",
# ]
inactive_websites = []

# PySimpleGUI Layout
layout = [
    [
        sg.Text("Keyword:"),
        sg.Input(key="-KEYWORD-", size=25),
        sg.Button("Search"),
    ],
    [sg.Text("                ")],
    [
        sg.Listbox(active_websites, size=(15, 8), key="-ACTIVE-"),
        sg.Button("⇄", size=(len("Switch On/Off"), 2), font=(15)),
        sg.Listbox(
            inactive_websites,
            size=(15, 8),
            key="-INACTIVE-",
        ),
    ],
    [
        sg.Text("        Active"),
        sg.Stretch(),
        sg.Text("Inactive          "),
    ],
    [sg.Text("─────────────────────────────")],
    [
        sg.Text("Add Link:"),
        sg.Input(
            key="-NEWLINK-",
            size=25,
        ),
        sg.Button("＋"),
        sg.Button("?"),
    ],
]

window = sg.Window("Website Query", layout, element_justification="c")

# Checking for changes inside the GUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Switch contents of active to inactive and vice versa
    if event == "⇄":
        if values["-ACTIVE-"]:
            picked_website = values["-ACTIVE-"][0]
            inactive_websites.append(picked_website)
            active_websites.remove(picked_website)
            window["-ACTIVE-"].update(active_websites)
            window["-INACTIVE-"].update(inactive_websites)

        if values["-INACTIVE-"]:
            picked_website = values["-INACTIVE-"][0]
            active_websites.append(picked_website)
            inactive_websites.remove(picked_website)
            window["-ACTIVE-"].update(active_websites)
            window["-INACTIVE-"].update(inactive_websites)

    # Check if the search button is pressed
    # Upon pressing check active websites and open them
    if event == "Search":
        if values["-KEYWORD-"]:
            keyword = values["-KEYWORD-"]
            keyword = keyword.replace(" ", "+")

            # Load JSON-file to access links
            with open("links.json") as json_file:
                links = json.load(json_file)
                for current_website in active_websites:
                    if current_website in links["links"]:
                        link = links["links"][current_website]
                        link = link.replace("{keyword}", keyword)
                        wb.open(link)

    # Add a link to the JSON-file using the button
    if event == "＋":
        if values["-NEWLINK-"]:
            with open("links.json", "r") as json_file:
                links = json.load(json_file)

            # print(values["-NEWLINK-"])
            new_link = values["-NEWLINK-"]
            new_link = new_link.split(":")
            active_websites.append(new_link[0])

            # Update JSON-file with the new link
            website_dictionary = {f"{new_link[0]}": f"{new_link[1]}"}
            links["links"].update(website_dictionary)

            # Update listbox
            window["-ACTIVE-"].update(active_websites)
            window["-INACTIVE-"].update(inactive_websites)

            with open("links.json", "w") as json_file:
                json.dump(links, json_file)

    if event == "?":
        sg.PopupScrolled(
            "\n",
            "To add a link, use the following format: ",
            "\nWEBSITE_NAME:https//www.website.com/search={keyword}",
            "\n",
            "E.g.:",
            "\nVinted:https://www.vinted.de/catalog?search_text={keyword}",
        )

        # Pop out explanation how to input new link
        pass

window.close()
