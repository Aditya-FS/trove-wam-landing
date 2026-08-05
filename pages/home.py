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
        "detail": "KPI Benchmarking, Liquid Asset Dashboard, Market Maps, Market Sizing",
        "hover": "Access wealth and asset management insights for WAM, featuring AM & WM dashboards, Liquid Assets Dashboard, Market Maps, WM decks, and competitive market intelligence.",
        "href": "/strategy/",
        "image": _pick_image("Strategy.jpg"),
    },
    {
        "label": "Capital Markets",
        "detail": "TSR, BGW ",
        "hover": "Comparative analysis of global Wealth & Asset players on capital market metrics such as TSR and BWG.",
        "href": "/capital-markets/",
        "image": _pick_image(
            "Capital Market.jpg"
        ),
    },
    {
        "label": "PI/Cost",
        "detail": "Cost Benchmarking, Cost Compass, IT Investment, Workforce Analysis",
        "hover": "Provides comprehensive analysis for WAM sector in terms of performance improvement via tools such as cost"
                 " benchmarking, cost out compass, IT investment spend analysis, branch rationalization, workforce analysis.",
        "href": "/pi-cost/",
        "image": _pick_image("PICost.jpg"),
    },
    {
        "label": "ET",
        "detail": "ET Regression, Thinker Doer Watcher Analysis  ",
        "hover": "Comparative analysis on ET analysis covering ET regression and Thinker, doer, watcher analysis.",
        "href": "/et/",
        "image": _pick_image("ET.jpg"),
    },
    {
        "label": "Customer",
        "detail": "Coming soon",
        "hover": "Customer modules coming soon.",
        "href": "/customer/",
        "image": _pick_image("Customer.jpg"),
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
                html.Div(
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
                                "WAM Trove is a comprehensive platform offering consolidated data and insights for ",
                                "Wealth & Asset Management markets across key modules including Asset ",
                                "Management KPIs, Wealth Management KPIs, TSR, Sector Analysis, Market Maps and more. ",
                            ],
                            className="home-hero-text",
                        ),
                        html.P(
                            [
                                "Please click ",
                                html.A("here", href="https://iris.bain.com/content-viewer/4H5X64", className="home-hero-link"),
                                " for the credentials deck, You may also reach out to ",
                                html.A("Sukrita Bhatia", href="mailto:Sukrita.Bhatia@Bain.com", className="home-hero-link"),
                                " and ",
                                html.A("Sarang Deva", href="mailto:Sarang.Deva@Bain.com", className="home-hero-link"),
                                " for the further queries ",
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
