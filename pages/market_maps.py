import os

import dash
from dash import html, register_page

from page_helpers import coming_soon_ribbon

register_page(
    __name__,
    path="/strategy/market-maps/",
    name="Asset Management Market Maps",
    title="Asset Management Market Maps | TROVE WAM",
)

RED = "#C00000"
_ASSETS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
_BLACK_T = 30

_ICON_CANDIDATES = [
    os.path.join("Icons", "Strat", "Placeholder.png"),
    os.path.join("Icons", "Strat", "placeholder.png"),
    os.path.join("Icons", "Strategy_Landing", "market-overview-mm.jpg"),
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
            return src_rel

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
        "title": "EMEA",
        "ribbon": "W.I.P",
        "desc": (
            "A comprehensive view of the EMEA Asset Management landscape,"
            " highlighting key players, market segments, emerging trends,"
            " and strategic positioning across the region."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "icon": "Icons/Strategy_Landing/market-overview-mm.jpg",
        "href": "https://bainandcompany-my.sharepoint.com/:p:/g/personal/prachi_jain_bain_com/IQCyz2_kVgvyQpHWhrZsxS4mAcrYIoM2xtX7X6uSUN3IRDQ?e=LS7gBW",
    },
    {
        "title": "Americas",
        "ribbon": "COMING SOON",
        "desc": (
            "A comprehensive view of the Americas Asset Management landscape,"
            " highlighting key players, market segments, emerging trends,"
            " and strategic positioning across the region."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "icon": "Icons/Strategy_Landing/market-overview-mm.jpg",
        "href": "#",
    },
    {
        "title": "APAC",
        "ribbon": "COMING SOON",
        "desc": (
            "A comprehensive view of the APAC Asset Management landscape,"
            " highlighting key players, market segments, emerging trends,"
            " and strategic positioning across the region."
        ),
        "extra_label": "Contact:",
        "extra_value": " Please reach out to NewDelhiBCNFSWAM@bain.com for customized analysis.",
        "icon": "Icons/Strategy_Landing/market-overview-mm.jpg",
        "href": "#",
    },
]


def _tile(t: dict):
    ribbon_label = t.get("ribbon", "COMING SOON")

    tile_body = [
        html.Div(
            [
                html.Div(
                    html.Img(
                        src=_icon_url(t.get("icon")),
                        alt="Market Maps",
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
    ]

    return html.A(
        html.Div(
            [coming_soon_ribbon(ribbon_label), *tile_body],
            className="strat-tile-inner",
        ),
        href=t.get("href", "#"),
        className="strat-tile-has-ribbon",
        style={
            "display": "flex",
            "flexDirection": "column",
            "textDecoration": "none",
            "color": "inherit",
            "minHeight": "0",
            "height": "100%",
        },
    )


layout = html.Div(
    [
        html.H1(
            "Asset Management Market Maps",
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
                "A structured view of the Asset Management landscape, providing insights into market structure,"
            " key participants, and opportunity pools across regions. "
            "Designed to support market assessment, competitive understanding, and opportunity identification.",
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
