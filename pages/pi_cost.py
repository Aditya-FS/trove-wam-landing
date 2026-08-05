import os

import dash
from dash import html, register_page

register_page(
    __name__,
    path="/pi-cost/",
    name="PI / Cost",
    title="PI / Cost | TROVE WAM",
)

RED = "#C00000"
GREY_BAR = "#5a5a5a"
_ASSETS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
_BLACK_T = 30

_ICON_CANDIDATES = [
    os.path.join("Icons", "Strat", "Placeholder.png"),
    os.path.join("Icons", "Strat", "placeholder.png"),
    os.path.join("Icons", "strategy icons", "placeholder.png"),
    os.path.join("Icons", "PI_R.png"),
]


def _knock_out_black_to_png(src_path: str, dest_path: str) -> bool:
    try:
        from PIL import Image
    except ImportError:
        return False
    im = Image.open(src_path).convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if r <= _BLACK_T and g <= _BLACK_T and b <= _BLACK_T:
                px[x, y] = (0, 0, 0, 0)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    im.save(dest_path, "PNG")
    return True


def _ensure_clear_png(src_rel: str) -> str:
    src_rel = src_rel.replace("\\", "/")
    src_full = os.path.join(_ASSETS, src_rel.replace("/", os.sep))
    if not os.path.isfile(src_full):
        for rel in _ICON_CANDIDATES:
            if os.path.isfile(os.path.join(_ASSETS, rel)):
                src_rel = rel.replace("\\", "/")
                src_full = os.path.join(_ASSETS, src_rel.replace("/", os.sep))
                break
        else:
            return src_rel if src_rel.lower().endswith(".png") else "Icons/PI_R.png"

    base, _ext = os.path.splitext(src_rel)
    clear_rel = f"{base}_clear.png"
    clear_full = os.path.join(_ASSETS, clear_rel.replace("/", os.sep))
    try:
        need = (not os.path.isfile(clear_full)) or (
            os.path.getmtime(src_full) > os.path.getmtime(clear_full)
        )
    except OSError:
        need = True
    if need and _knock_out_black_to_png(src_full, clear_full):
        return clear_rel
    if os.path.isfile(clear_full):
        return clear_rel
    return src_rel


def _default_icon() -> str:
    for rel in _ICON_CANDIDATES:
        if os.path.isfile(os.path.join(_ASSETS, rel)):
            return rel.replace("\\", "/")
    return "Icons/Strat/Placeholder.png"


DEFAULT_ICON = _default_icon()


def _icon_url(icon_rel: str | None = None) -> str:
    rel = _ensure_clear_png(icon_rel or DEFAULT_ICON)
    assert rel.lower().endswith(".png"), rel
    return dash.get_asset_url(rel).replace(" ", "%20")


TILES = [
    {
        "title": "Cost Benchmarking",
        "desc": (
            "Peer cost benchmarking across WAM functions compare cost-to-income, "
            "operating expense ratios, and efficiency levers against relevant peers."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/PICost_Landing/market-overview-mm.jpg",
        "href": "mailto:NewDelhiBCNFSWAM@Bain.com",
    },
    {
        "title": "Cost Compass",
        "desc": (
            "Comprehensive cost-out tool that combines global Financial Services experience,"
            " making cost-out sizing for proposals faster and higher quality."
            " Contains full potential cost out ranges (% of cost saved) in a MECE taxonomy."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/PICost_Landing/capital_market_cds.jpg",
        "href": "mailto:NewDelhiBCNFSWAM@Bain.com",
    },
    {
        "title": "IT Investment",
        "desc": (
            "IT investment and technology spend analytics for wealth and asset "
            "managers portfolio mix, run-vs-change and peer technology intensity."
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
            "Comparative analysis to understand FTE trends across"
            " different support functions. Also provides multiple other"
            " FTE trends such as hiring, attrition, gender diversity etc."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "live": False,
        "badge": "On Demand",
        "meta": " ",
        "icon": "Icons/PICost_Landing/workforce-icon.jpg",
        "href": "mailto:NewDelhiBCNFSWAM@Bain.com",
    },
]


def _tile(t: dict):
    live = t["live"]
    return html.A(
        [
            html.Div(
                [
                    html.Div(
                        html.Img(
                            src=_icon_url(t.get("icon")),
                            alt="PI / Cost",
                            style={
                                "width": "120px",
                                "height": "120px",
                                "objectFit": "contain",
                                "display": "block",
                                "flexShrink": "0",
                                "background": "transparent",
                            },
                        ),
                        style={
                            "flex": "0 0 40%",
                            "width": "40%",
                            "maxWidth": "40%",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "alignSelf": "stretch",
                            "minHeight": "140px",
                            "boxSizing": "border-box",
                            "background": "transparent",
                            "marginRight": "8px",
                            "overflow": "hidden",
                        },
                    ),
                    html.Div(
                        [
                            html.H3(
                                t["title"],
                                style={
                                    "margin": "0 0 10px",
                                    "fontSize": "1.08rem",
                                    "fontWeight": "800",
                                    "color": RED,
                                    "lineHeight": "1.25",
                                    "fontFamily": "Arial, Helvetica, sans-serif",
                                },
                            ),
                            html.P(
                                t["desc"],
                                style={
                                    "margin": "0 0 12px",
                                    "fontSize": "0.86rem",
                                    "color": "#555",
                                    "lineHeight": "1.45",
                                    "fontFamily": "Arial, Helvetica, sans-serif",
                                },
                            ),
                            html.P(
                                [
                                    html.Span(
                                        t["extra_label"],
                                        style={
                                            "fontWeight": "700",
                                            "color": "#444",
                                            "fontStyle": "normal",
                                        },
                                    ),
                                    html.Span(
                                        t["extra_value"],
                                        style={"fontStyle": "italic", "color": "#555"},
                                    ),
                                ],
                                style={
                                    "margin": "0",
                                    "fontSize": "0.8rem",
                                    "lineHeight": "1.4",
                                },
                            ),
                        ],
                        style={
                            "flex": "1 1 60%",
                            "width": "60%",
                            "maxWidth": "60%",
                            "minWidth": "0",
                            "paddingLeft": "10px",
                            "paddingRight": "4px",
                            "boxSizing": "border-box",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "flexDirection": "row",
                    "alignItems": "center",
                    "gap": "4px",
                    "padding": "20px 16px 14px",
                    "flex": "1 1 auto",
                    "minHeight": "0",
                },
            ),
            html.Div(
                [
                    html.Span(
                        t["badge"],
                        style={
                            "display": "inline-flex",
                            "alignItems": "center",
                            "padding": "7px 16px",
                            "fontSize": "0.8rem",
                            "fontWeight": "700",
                            "color": "#fff",
                            "background": RED if live else GREY_BAR,
                            "borderRadius": "0 10px 0 0",
                            "fontFamily": "Arial, Helvetica, sans-serif",
                        },
                    ),
                    html.Span(
                        t["meta"],
                        style={
                            "display": "flex",
                            "alignItems": "center",
                            "padding": "0 14px",
                            "fontSize": "0.78rem",
                            "color": "#999",
                            "whiteSpace": "nowrap",
                            "fontFamily": "Arial, Helvetica, sans-serif",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "stretch",
                    "justifyContent": "space-between",
                    "minHeight": "34px",
                    "marginTop": "auto",
                },
            ),
        ],
        href=t.get("href", "#"),
        style={
            "display": "flex",
            "flexDirection": "column",
            "background": "#fff",
            "border": "1px solid #e0e0e0",
            "borderRadius": "24px",
            "boxShadow": "0 2px 10px rgba(0,0,0,0.10)",
            "overflow": "hidden",
            "textDecoration": "none",
            "color": "inherit",
            "minHeight": "0",
            "height": "100%",
        },
    )


layout = html.Div(
    [
        html.H1(
            "PI / Cost: Benchmarking, Compass, IT Investment & Workforce Analysis",
            style={
                "fontSize": "clamp(1.25rem, 1.85vw, 1.55rem)",
                "fontWeight": "800",
                "color": "#111",
                "margin": "0",
                "lineHeight": "1.3",
                "letterSpacing": "-0.01em",
                "fontFamily": "Arial, Helvetica, sans-serif",
            },
        ),
        html.P(
            [
                "Provides comprehensive analysis for WAM sector in terms "
                "of performance improvement via tools such as cost benchmarking, "
                "cost out compass, IT investment spend analysis, "
                "branch rationalization, workforce analysis.",
            ],
            style={
                "color": "#777",
                "fontSize": "0.98rem",
                "lineHeight": "1.55",
                "margin": "22px 0 22px",
                "maxWidth": "75%",
                "fontFamily": "Arial, Helvetica, sans-serif",
            },
        ),
        html.Div(
            [_tile(t) for t in TILES],
            style={
                "flex": "1 1 auto",
                "minHeight": "0",
                "display": "grid",
                "gridTemplateColumns": "repeat(3, 1fr)",
                "gridTemplateRows": "1fr 1fr",
                "gap": "22px",
                "alignContent": "stretch",
            },
        ),
    ],
    style={
        "height": "calc(100vh - 64px - 36px)",
        "maxHeight": "calc(100vh - 64px - 36px)",
        "overflow": "hidden",
        "display": "flex",
        "flexDirection": "column",
        "padding": "10px 28px 14px 8px",
        "boxSizing": "border-box",
        "background": "#fff",
    },
)
