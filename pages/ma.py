from dash import register_page

from page_helpers import dir_page_layout, strat_mixed_link_tile

register_page(__name__, path="/ma/", name="M&A", title="M&A | TROVE WAM")

TILES = [
    {
        "title": "M&A Tracker",
        "desc": (
            "A structured M&A assessment identifying priority acquisition candidates and providing a strategic roadmap to evaluate and execute potential transactions."
        ),
        "extra_label": " ",
        "extra_value": " ",
        "live": False,
        "badge": "Claude Artifact",
        "meta": " ",
        "icon": "Icons/market-overview-wbrp.jpg",
        "href": "https://claude.ai/artifacts/latest/4716e4c5-0f7a-4dbf-a8f9-054a28bbe26e",
    },
    {
        "title": "Coming Soon",
        "desc": (
            "Additional M&A analytics modules are currently"
            " under development and will be introduced to broaden "
            "the range of transaction insights available through the platform."
        ),
        "extra_label": "Status:",
        "extra_value": " In development.",
        "live": False,
        "badge": "",
        "meta": "",
        "icon": "",
        "href": "",
    },
]

layout = dir_page_layout(
    "M&A: Mergers & Acquisitions",
    [
        "Access focused M&A analytics for "
        "the WAM sector, providing structured perspectives on transaction activity,"
        " market dynamics, valuations, and strategic "
        "deal trends across Wealth & Asset Management. ",
    ],
    [strat_mixed_link_tile(t, "M&A") for t in TILES],
)
