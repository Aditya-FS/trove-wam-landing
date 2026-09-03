from dash import register_page

from page_helpers import dir_page_layout, strat_mixed_link_tile

register_page(
    __name__,
    path="/strategy/wealth-management-decks/",
    name="Wealth Management Decks",
    title="Wealth Management Decks | TROVE WAM",
)

TILES = [
    {
        "title": "UK Wealth Management Deck",
        "desc": (
            "A comprehensive view of the UK WM market, covering key players, market structure, emerging trends, and strategic positioning."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "Iris",
        "meta": " ",
        "icon": "Strategy_Landing/Picture4.png",
        "href": "https://iris.bain.com/content-viewer/CPUGMO",
    },
    {
        "title": "DACH Wealth Management Deck",
        "desc": (
            "A comprehensive view of the DACH WM market, covering key players, market structure, emerging trends, and strategic positioning."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "Iris",
        "meta": " ",
        "icon": "Strategy_Landing/Picture5.png",
        "href": "https://iris.bain.com/content-viewer/474IV5",
    },
    {
        "title": "Coming Soon",
        "desc": (
            "Additional Wealth Management decks across regions and product"
            " areas are currently under development and will be made "
            "available soon, expanding the breadth of market "
            "perspectives and insights available through the platform."
        ),
        "extra_label": "Status:",
        "extra_value": "In development",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/Strategy_Landing/capital_market_cds.jpg",
        "href": "#",
    },
]

layout = dir_page_layout(
    "Wealth Management Decks",
    "Explore wealth management decks by geography.",
    [strat_mixed_link_tile(t, "Wealth Management Decks") for t in TILES],
    page_class="wealth-decks-page",
)
