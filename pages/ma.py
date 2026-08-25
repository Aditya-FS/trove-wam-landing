import os

import dash
from dash import html, register_page

from page_helpers import coming_soon_ribbon

register_page(__name__, path="/ma/", name="M&A", title="M&A | TROVE WAM")

RED = "#C00000"
GREY_BAR = "#5a5a5a"
_ASSETS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
_BLACK_T = 30

_ICON_CANDIDATES = [
    os.path.join("Icons", "Strat", "Placeholder.png"),
    os.path.join("Icons", "Strat", "placeholder.png"),
    os.path.join("Icons", "MA_R.png"),
    os.path.join("Icons", "strategy icons", "placeholder.png"),
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
            return src_rel if src_rel.lower().endswith(".png") else "Icons/Strat/Placeholder.png"

    base, ext = os.path.splitext(src_rel)
    if ext.lower() in (".png", ".jpg", ".jpeg"):
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
    return dash.get_asset_url(rel).replace(" ", "%20")


TILES = [
    {
        "title": "M&A Tracker",
        "desc": (
            "A structured view of mergers and acquisitions"
            " activity across Wealth & Asset Management, covering deal flow, "
            "transaction valuations, and strategic rationale. The tracker "
            "supports the assessment of market activity, "
            "consolidation trends, and evolving strategic priorities across the sector."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
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


def _tile(t: dict):
    live = t["live"]
    is_coming_soon = t.get("title") == "Coming Soon"

    copy_children = []
    if not is_coming_soon:
        copy_children.append(
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
            )
        )
    copy_children.extend(
        [
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
        ]
    )

    copy_style = {
        "flex": "1 1 60%",
        "width": "60%",
        "maxWidth": "60%",
        "minWidth": "0",
        "paddingLeft": "10px",
        "paddingRight": "4px",
        "boxSizing": "border-box",
    }
    if is_coming_soon:
        copy_style = {
            "flex": "1 1 auto",
            "width": "100%",
            "maxWidth": "100%",
            "minWidth": "0",
            "paddingLeft": "18px",
            "paddingRight": "18px",
            "boxSizing": "border-box",
        }

    row_children = []
    if not is_coming_soon:
        row_children.append(
            html.Div(
                html.Img(
                    src=_icon_url(t.get("icon")),
                    alt="M&A",
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
            )
        )
    row_children.append(html.Div(copy_children, style=copy_style))

    tile_body = [
        html.Div(
            row_children,
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
    ]
    if not is_coming_soon:
        tile_body.append(
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
            )
        )

    if is_coming_soon:
        tile_children = [
            html.Div(
                [coming_soon_ribbon(), *tile_body],
                className="strat-tile-inner",
            ),
        ]
        tile_style = {
            "display": "flex",
            "flexDirection": "column",
            "textDecoration": "none",
            "color": "inherit",
            "minHeight": "0",
            "height": "100%",
        }
        tile_class = "strat-tile-has-ribbon"
    else:
        tile_children = tile_body
        tile_style = {
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
        }
        tile_class = None

    return html.A(
        tile_children,
        href=t.get("href", "#"),
        className=tile_class,
        style=tile_style,
    )


layout = html.Div(
    [
        html.H1(
            "M&A: Mergers & Acquisitions",
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
                "Access focused M&A analytics for "
                "the WAM sector, providing structured perspectives on transaction activity,"
                " market dynamics, valuations, and strategic "
                "deal trends across Wealth & Asset Management. ",
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
