from dash import register_page

from page_helpers import dir_page_layout, strat_dir_link_tile

register_page(
    __name__,
    path="/capital-markets/",
    name="Capital Markets",
    title="Capital Markets | TROVE WAM",
)

TILES = [
    {
        "title": "TSR",
        "desc": (
            "Comprehensive TSR analytics enabling peer benchmarking and insights into value creation drivers."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/Capital_Markets_Landing/capital_market_tsr.jpg",
        "href": "mailto:NewDelhiBCNFSWAM@Bain.com",
    },
    {
        "title": "BGW",
        "desc": (
            "Structured BGW analysis classifying companies by growth, operational performance and assess current and future potential."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/Capital_Markets_Landing/capital_market_sp.jpg",
        "href": "mailto:NewDelhiBCNFSWAM@Bain.com",
    },
]

layout = dir_page_layout(
    "Capital Markets: TSR and BGW",
    [
        "Access capital markets analytics for the WAM sector, "
        "combining Total Shareholder Return (TSR) benchmarking with BGW analysis. "
        "These tools provide structured perspectives on market "
        "performance, value creation, strategic positioning, and future growth potential.",
    ],
    [strat_dir_link_tile(t, "Capital Markets") for t in TILES],
)
