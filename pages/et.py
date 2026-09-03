from dash import register_page

from page_helpers import dir_page_layout, strat_dir_link_tile

register_page(__name__, path="/et/", name="ET", title="ET | TROVE WAM")

TILES = [
    {
        "title": "ET Regression",
        "desc": (
            "Enterprise Technology (ET) Regression analysis across WAM players to assess performance trends and relationships across key metrics."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "Iris",
        "meta": " ",
        "icon": "Icons/ET_Landing/Module_CostOI.png",
        "href": "https://iris.bain.com/content-viewer/EJDSCV",
    },
    {
        "title": "Thinker, Doer, Watcher Analysis",
        "desc": (
            "A structured WAM operating model diagnostic assessing role archetypes, organizational capacity, and decision rights to identify improvement opportunities."
        ),
        "extra_label": "Contact",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "Iris",
        "meta": " ",
        "icon": "Icons/ET_Landing/connecting-icon.jpg",
        "href": "https://iris.bain.com/content-viewer/I15L1J",
    },
]

layout = dir_page_layout(
    "ET: Regression and Thinker / Doer / Watcher",
    [
        "Access targeted performance driver and operating model "
        "analytics for the WAM sector, combining ET Regression with Thinker / Doer / Watcher analysis. "
        "These tools support a structured assessment of performance drivers, "
        "organizational roles, capacity, and decision rights.",
    ],
    [strat_dir_link_tile(t, "ET") for t in TILES],
)
