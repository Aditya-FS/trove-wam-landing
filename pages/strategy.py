import dash
from dash import register_page

from page_helpers import dir_page_layout, strat_dir_link_tile

register_page(__name__, path="/strategy/", name="Strategy", title="Strategy | TROVE WAM")

TILES = [
    {
        "title": "Asset Management Financial KPIs Benchmark",
        "desc": (
            "An interactive dashboard benchmarking key AM metrics across peers, ownership types, detailed cost structures and more. "
        ),
        "extra_label": "Areas of Analysis:",
        "extra_value": " AM Peer Benchmarking ",
        "live": True,
        "badge": "Live",
        "meta": " ",
        "icon": "Icons/Strategy_Landing/branch-icon.jpg",
        "href": "https://us-east-1.online.tableau.com/#/site/casepracticeproduct/views/AMDashboard2018-2023/Cover?:iid=1",
    },
    {
        "title": "Wealth Management Financial KPIs Benchmark",
        "desc": (
            "An interactive dashboard benchmarking key WM metrics across peers, ownership types, detailed cost structures and more. "
        ),
        "extra_label": "Areas of Analysis:",
        "extra_value": " WM Peer Benchmarking ",
        "live": True,
        "badge": "Live",
        "meta": " ",
        "icon": "Icons/Strategy_Landing/it-investment-spend-icon.jpg",
        "href": "https://us-east-1.online.tableau.com/#/site/casepracticeproduct/views/WealthManagementFinancialKPIsbenchmark2017-2024/Cover?:iid=1",
    },
    {
        "title": "Asset Management Market Maps",
        "desc": (
            "A structured view of the AM landscape, highlighting market structure, key participants, and opportunity pools across the regions- Americas, APAC & EMEA."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "Iris",
        "meta": " ",
        "icon": "Icons/Strategy_Landing/market-overview-mm.jpg",
        "href": dash.get_relative_path("/strategy/market-maps/"),
    },
    {
        "title": "Wealth Management Decks",
        "desc": (
            "A comprehensive view of country-specific WM insights, covering market dynamics, revenues, AUM, profitability, key trends, and performance benchmarks."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "Iris",
        "meta": " ",
        "icon": "Icons/Strategy_Landing/capital_market_cds.jpg",
        "href": dash.get_relative_path("/strategy/wealth-management-decks/"),
    },
    {
        "title": "Liquid Assets Dashboard",
        "desc": (
            "An interactive Liquid Assets dashboard enabling data classification by asset class, region, customer segment and other dimensions."
        ),
        "extra_label": "Areas of Analysis:",
        "extra_value": " Liquid Assets",
        "live": True,
        "badge": "Live",
        "meta": " ",
        "icon": "Icons/Strategy_Landing/Liquid Assets.png",
        "href": "https://us-east-1.online.tableau.com/#/site/casepracticeproduct/views/WealthManagementMarketInsights/Cover?:iid=1",
    },
    {
        "title": "Alternative Market Sizing",
        "desc": (
            "A deep dive into the Alternatives market providing an L2 product-level insights to assess market size, growth, and opportunities across key segments."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/Strategy_Landing/capital_market_tsr.jpg",
        "href": "https://bainandcompany-my.sharepoint.com/:p:/g/personal/aditya_a_bain_com/IQAweI8rRKcJRIz9rQ1okajwAejgJCiI5YHNvyKAF55GmxE?e=1nsyrJ",
    },
]

layout = dir_page_layout(
    "Strategy: KPI Benchmarking, Liquid Asset Dashboard, Market Maps & Market Sizing",
    [
        "Access a comprehensive suite of WAM strategy and market intelligence resources, "
        "including Financial KPI benchmarking, Liquid Assets Dashboards, Market Maps, Market Sizing, Wealth Management Decks, "
        "and Competitive Market Insights. These tools bring together relevant data and perspectives to support benchmarking,"
        " market assessment, and strategic decision-making.",
    ],
    [strat_dir_link_tile(t, "Strategy") for t in TILES],
)
