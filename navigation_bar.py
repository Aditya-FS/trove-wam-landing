import dash
from dash import html, dcc, page_container


def _path(route: str) -> str:
    return dash.get_relative_path(route)


def _icon(name: str) -> str:
    return dash.get_asset_url(f"Icons/{name}")


NAV_SECTIONS = [
    {
        "id": "home",
        "label": "Home",
        "href": "/",
        "icon_r": "Home_R.png",
        "icon_s": "Home_S.png",
        "exact_home": True,
        "path_prefixes": [],
    },
    {
        "id": "strategy",
        "label": "Strategy",
        "href": "/strategy/",
        "icon_r": "Strategy_R.png",
        "icon_s": "Strategy_S.png",
        "path_prefixes": ["/strategy"],
    },
    {
        "id": "cm",
        "label": "Capital Markets",
        "href": "/capital-markets/",
        "icon_r": "Capital_R.png",
        "icon_s": "Capital_S.png",
        "path_prefixes": ["/capital-markets"],
    },
    {
        "id": "pi-cost",
        "label": "Cost / PI",
        "href": "/pi-cost/",
        "icon_r": "PI_R.png",
        "icon_s": "PI_S.png",
        "path_prefixes": ["/pi-cost"],
    },
    {
        "id": "et",
        "label": "ET",
        "href": "/et/",
        "icon_r": "ET_R.png",
        "icon_s": "ET_S.png",
        "path_prefixes": ["/et"],
    },
    {
        "id": "customer",
        "label": "Customer",
        "href": "/customer/",
        "icon_r": "Customer_R.png",
        "icon_s": "Customer_S.png",
        "path_prefixes": ["/customer"],
    },
]


def _normalize_path(pathname: str) -> str:
    if not pathname:
        return "/"
    p = pathname.replace("\\", "/")
    if p.startswith("/wam"):
        p = p[4:] or "/"
    if not p.startswith("/"):
        p = "/" + p
    if len(p) > 1 and p.endswith("/"):
        p = p.rstrip("/")
    return p or "/"


def active_section_id(pathname: str) -> str:
    p = _normalize_path(pathname)
    if p in {"", "/"}:
        return "home"
    for section in NAV_SECTIONS:
        if section.get("exact_home"):
            continue
        for prefix in section["path_prefixes"]:
            pref = prefix.rstrip("/") or "/"
            if p == pref or p.startswith(pref + "/"):
                return section["id"]
    return "home"


def _nav_item(section: dict, is_active: bool = False):
    classes = "side-nav-item"
    if is_active:
        classes += " is-active"
    if section["id"] == "home":
        classes += " is-home"

    return html.Div(
        dcc.Link(
            [
                html.Div(
                    [
                        html.Img(
                            src=_icon(section["icon_s"]),
                            className="side-nav-icon side-nav-icon-s",
                            alt="",
                        ),
                        html.Img(
                            src=_icon(section["icon_r"]),
                            className="side-nav-icon side-nav-icon-r",
                            alt="",
                        ),
                    ],
                    className="side-nav-icon-wrap"
                    + (" is-round" if section["id"] == "home" else ""),
                ),
                html.Span(section["label"], className="side-nav-label"),
            ],
            href=_path(section["href"]),
            className="side-nav-row",
        ),
        className=classes,
        id=f"side-nav-{section['id']}",
    )


def build_side_nav_items(pathname: str = "/"):
    active = active_section_id(pathname)
    return [_nav_item(s, is_active=(s["id"] == active)) for s in NAV_SECTIONS]


nav_bar = html.Aside(
    [
        html.Div(
            [
                html.Button(
                    html.I(className="fas fa-chevron-left"),
                    id="side-nav-toggle",
                    className="side-nav-toggle",
                    type="button",
                    title="Collapse / expand menu",
                    n_clicks=0,
                ),
                html.Div(
                    build_side_nav_items("/"),
                    id="side-nav-items",
                    className="side-nav-items",
                ),
            ],
            className="side-nav-inner",
            id="side-nav-inner",
        ),
        html.Div(
            [page_container],
            className="main-page-wrap",
            id="nav_Bar_global",
        ),
    ],
    className="side-nav",
    id="side-nav",
)
