import os
import dash
from dash import html, dcc, register_page

register_page(__name__, path="/", name="Home", title="TROVE WAM")

_ASSETS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "Images_Used")


def _path(route: str) -> str:
    return dash.get_relative_path(route)


def _img(name: str) -> str:
    return dash.get_asset_url(f"Images_Used/{name}")


def _pick_image(*candidates: str) -> str:
    for name in candidates:
        if os.path.isfile(os.path.join(_ASSETS, name)):
            return name
    return candidates[0]


TILES = [
    {
        "label": "Strategy",
        "detail": "KPI Benchmarking, Liquid Assets Dashboard, Market Maps, Alternative Market Sizing, Wealth Management Decks ",
        "hover": "Access a comprehensive suite of WAM strategy and market intelligence resources "
                "including financial KPI benchmarking, liquid asset dashboards, market maps, market sizing, Wealth Management decks, "
                "and competitive market insights. These tools bring together relevant data and perspectives to support benchmarking,"
                " market assessment and strategic decision-making.",
        "href": "/strategy/",
        "image": _pick_image("Strategy.jpg"),
    },
    {
        "label": "Capital Markets",
        "detail": "TSR, BGW ",
        "hover": "Access focused capital markets analytics for the WAM sector, "
                "combining Total Shareholder Return (TSR) benchmarking with BGW analysis. "
                "These tools provide structured perspectives on market "
                "performance, value creation, strategic positioning and future growth potential.",
        "href": "/capital-markets/",
        "image": _pick_image(
            "Capital Market.jpg"
        ),
    },
    {
        "label": "PI/ Cost",
        "detail": "Cost Benchmarking, Cost Out Compass, IT Investment, Workforce Analysis",
        "hover": "Access a comprehensive suite of performance improvement "
                "and cost analytics for the WAM sector, spanning cost benchmarking, "
                "Cost Out Compass, IT investment analysis, and workforce analytics. "
                "These tools support fact-based assessment of efficiency, "
                "investment priorities, and operating model opportunities.",
        "href": "/pi-cost/",
        "image": _pick_image("PICost.jpg"),
    },
    {
        "label": "ET",
        "detail": "ET Regression, Thinker Doer Watcher Analysis  ",
        "hover": "Access targeted performance driver and operating model "
                "analytics for the WAM sector, combining ET Regression with Thinker / Doer / Watcher analysis. "
                "These tools support a structured assessment of performance drivers, "
                "organizational roles, capacity, and decision rights.",
        "href": "/et/",
        "image": _pick_image("ET.jpg"),
    },
    {
        "label": "Customer",
        "detail": "Social Sentiment Analysis",
        "hover": "Access focused customer insight"
                " and market sentiment analytics "
                "for the WAM sector, designed to provide a clearer "
                "understanding of customer perceptions, brand positioning, "
                "and emerging market signals.",
        "href": "/customer/",
        "image": _pick_image("Customer.jpg"),
    },
    {
        "label": "M&A",
        "detail": "Mergers & Acquisitions Tracker",
        "hover": "Access focused M&A analytics for "
                "the WAM sector, providing structured perspectives on transaction activity,"
                " market dynamics, valuations, and strategic "
                "deal trends across Wealth & Asset Management.",
        "href": "/ma/",
        "image": _pick_image("MA.jpg"),
    },
]


def _tile(tile: dict):
    return dcc.Link(
        [
            html.Div(
                [
                    html.Img(
                        src=_img(tile["image"]),
                        alt=tile["label"],
                        className="home-tile-img",
                    ),
                    html.Div(tile["hover"], className="home-tile-hover"),
                ],
                className="home-tile-media",
            ),
            html.Div(
                html.P(
                    [
                        html.Span(f"{tile['label']}: ", className="home-tile-label"),
                        html.Span(tile["detail"], className="home-tile-detail"),
                    ],
                    className="home-tile-footer-text",
                ),
                className="home-tile-footer",
            ),
        ],
        href=_path(tile["href"]),
        className="home-tile",
    )


layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1(
                            [
                                "Integrated data tool for Wealth and Asset",
                                html.Br(),
                                "Management",
                            ],
                            className="home-hero-title",
                        ),
                        html.P(
                            [
                                "WAM Trove is a comprehensive platform that brings together consolidated data, market intelligence "
                                "and actionable insights for the Wealth & Asset Management sector across key modules, including "
                                "Asset Management KPIs, Wealth Management KPIs, TSR, Sector Analysis, Market Maps and more."
,
                            ],
                            className="home-hero-text",
                        ),
                        html.P(
                            [
                                "Please click ",
                                html.A("here", href="https://iris.bain.com/content-viewer/4H5X64", className="home-hero-link"),
                                " for the TROVE WAM credentials deck, You may also reach out to ",
                                html.A("Sukrita Bhatia", href="mailto:Sukrita.Bhatia@Bain.com", className="home-hero-link"),
                                " and ",
                                html.A("Sarang Deva", href="mailto:Sarang.Deva@Bain.com", className="home-hero-link"),
                                " for any further queries ",
                                ".",
                            ],
                            className="home-hero-text",
                        ),
                        html.P(
                            "Click on the Wealth & Asset Management Data Assets key products as shown below:",
                            className="home-hero-prompt",
                        ),
                    ],
                    className="home-hero-copy",
                ),
                html.Div(
                    [
                        html.Div(className="home-hero-accent home-hero-accent-top"),
                        html.Div(
                            html.Img(
                                src=_img("HeroImage.png"),
                                alt="Trove WAM",
                                className="home-hero-img",
                            ),
                            className="home-hero-img-clip",
                        ),
                        html.Div(className="home-hero-accent home-hero-accent-bottom"),
                    ],
                    className="home-hero-visual",
                ),
            ],
            className="home-hero",
        ),
        html.Div([_tile(t) for t in TILES], className="home-tile-grid"),
    ],
    className="home-page",
)
