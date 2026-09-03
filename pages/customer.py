from dash import register_page

from page_helpers import dir_page_layout, strat_mixed_link_tile

register_page(__name__, path="/customer/", name="Customer", title="Customer | TROVE WAM")

TILES = [
    {
        "title": "Social Sentiment Analysis",
        "desc": (
            "Structured WAM social sentiment analysis providing insights into brand perception, customer voice, and emerging market signals across digital channels."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/Module_Aura.png",
        "href": "https://bainandcompany-my.sharepoint.com/:p:/g/personal/aditya_a_bain_com/IQCaDQj5AUL6QZXZbvNBjLDiAZt95urw4VBmUcvCkg2avLY?e=dfBkTa",
    },
    {
        "title": "Coming Soon",
        "desc": (
            "Additional customer analytics modules are currently "
            "under development and will be introduced to "
            "further expand the range of customer insights "
            "available through the platform."
        ),
        "extra_label": "Status:",
        "extra_value": " In development.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "",
        "href": "#",
    },
]

layout = dir_page_layout(
    "Customer: Social Sentiment Analysis",
    [
        "Access focused customer insight"
        " and market sentiment analytics "
        "for the WAM sector, designed to provide a clearer "
        "understanding of customer perceptions, brand positioning, "
        "and emerging market signals.",
    ],
    [strat_mixed_link_tile(t, "Customer") for t in TILES],
)
