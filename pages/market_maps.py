from dash import register_page

from page_helpers import dir_page_layout, strat_ribbon_link_tile

register_page(
    __name__,
    path="/strategy/market-maps/",
    name="Asset Management Market Maps",
    title="Asset Management Market Maps | TROVE WAM",
)

TILES = [
    {
        "title": "EMEA",
        "ribbon": "W.I.P",
        "desc": (
            "A comprehensive view of the EMEA AM landscape, covering key players, market segments, emerging trends and strategic positioning."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "icon": "Strategy_Landing/Globe.png",
        "href": "https://bainandcompany-my.sharepoint.com/:p:/g/personal/prachi_jain_bain_com/IQCyz2_kVgvyQpHWhrZsxS4mAcrYIoM2xtX7X6uSUN3IRDQ?e=LS7gBW",
    },
    {
        "title": "Americas",
        "ribbon": "COMING SOON",
        "desc": (
            "A comprehensive view of the Americas AM landscape, covering key players, market segments, emerging trends and strategic positioning."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "icon": "Strategy_Landing/Picture2.png",
        "href": "#",
    },
    {
        "title": "APAC",
        "ribbon": "COMING SOON",
        "desc": (
            "A comprehensive view of the APAC AM landscape, covering key players, market segments, emerging trends and strategic positioning."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "icon": "Strategy_Landing/Globe.png",
        "href": "#",
    },
]

layout = dir_page_layout(
    "Asset Management Market Maps",
    [
        "A structured view of the Asset Management landscape, providing insights into market structure,"
        " key participants, and opportunity pools across regions. "
        "Designed to support market assessment, competitive understanding, and opportunity identification.",
    ],
    [strat_ribbon_link_tile(t, "Market Maps") for t in TILES],
)
