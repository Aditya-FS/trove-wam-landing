from dash import register_page

from page_helpers import dir_page_layout, strat_dir_link_tile

register_page(
    __name__,
    path="/pi-cost/",
    name="PI / Cost",
    title="PI / Cost | TROVE WAM",
)

TILES = [
    {
        "title": "Cost Benchmarking",
        "desc": (
            "Peer-based WAM cost benchmarking across cost-to-income, operating expenses, and efficiency metrics to identify performance gaps and improvement opportunities."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "PICost_Landing/Picture3.png",
        "href": "mailto:NewDelhiBCNFSWAM@Bain.com",
    },
    {
        "title": "Cost Out Compass",
        "desc": (
            "A comprehensive cost transformation tool providing benchmarked cost reduction ranges to identify and prioritize efficiency opportunities."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "Iris",
        "meta": " ",
        "icon": "Icons/PICost_Landing/capital_market_cds.jpg",
        "href": "https://iris.bain.com/content-viewer/03SRJJ",
    },
    {
        "title": "IT Investment",
        "desc": (
            "Structured WAM technology spend analytics enabling peer benchmarking across portfolio mix, run-versus-change expenditure, and investment priorities."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/PICost_Landing/it-investment-spend-icon.jpg",
        "href": "mailto:NewDelhiBCNFSWAM@Bain.com",
    },
    {
        "title": "Workforce Analytics",
        "desc": (
            "Comparative workforce analytics across FTE levels, workforce trends, hiring, attrition, and diversity to support workforce planning and organizational assessment."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/PICost_Landing/workforce-icon.jpg",
        "href": "https://bainandcompany-my.sharepoint.com/:p:/g/personal/aditya_a_bain_com/IQA83Qy7U8DdSZmAH11F8UpGATcwsJY57nf1Fk04D-8YcXY?e=GmVMFzm",
    },
]

layout = dir_page_layout(
    "PI / Cost: Benchmarking, Compass, IT Investment & Workforce Analysis",
    [
        "Access a comprehensive suite of performance improvement "
        "and cost analytics for the WAM sector, spanning cost benchmarking, "
        "Cost Out Compass, IT investment analysis, and workforce analytics. "
        "These tools support fact-based assessment of efficiency, "
        "investment priorities, and operating model opportunities.",
    ],
    [strat_dir_link_tile(t, "PI / Cost") for t in TILES],
)
