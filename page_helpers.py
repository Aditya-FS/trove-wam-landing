from dash import html
import dash

RED = "#c00"
GREY_BAR = "#5a5a5a"

_DIR_PAGE_STYLE = {
    "height": "calc(100vh - 64px - 36px)",
    "maxHeight": "calc(100vh - 64px - 36px)",
    "overflow": "hidden",
    "display": "flex",
    "flexDirection": "column",
    "padding": "10px 28px 14px 8px",
    "boxSizing": "border-box",
    "background": "#fff",
}

_DIR_GRID_STYLE = {
    "flex": "1 1 auto",
    "minHeight": "0",
    "display": "grid",
    "gridTemplateColumns": "repeat(3, 1fr)",
    "gridTemplateRows": "1fr 1fr",
    "gap": "22px",
    "alignContent": "stretch",
}

_DIR_TITLE_STYLE = {
    "fontSize": "clamp(1.25rem, 1.85vw, 1.55rem)",
    "fontWeight": "700",
    "color": "#111",
    "margin": "0",
    "lineHeight": "1.3",
    "letterSpacing": "-0.01em",
}

_DIR_INTRO_STYLE = {
    "color": "#777",
    "fontSize": "0.98rem",
    "lineHeight": "1.55",
    "margin": "22px 0 22px",
    "maxWidth": "75%",
}

_DIR_TILE_LINK_STYLE = {
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

_DIR_TILE_RIBBON_LINK_STYLE = {
    "display": "flex",
    "flexDirection": "column",
    "textDecoration": "none",
    "color": "inherit",
    "minHeight": "0",
    "height": "100%",
}


def coming_soon_ribbon(label="COMING SOON"):
    return html.Div(
        html.Div(label, className="strat-coming-soon-ribbon"),
        className="strat-coming-soon-ribbon-wrap",
    )


def tile_icon_url(icon_rel: str) -> str:
    rel = icon_rel.replace("\\", "/")
    return dash.get_asset_url(rel).replace(" ", "%20")


def strat_dir_icon(icon_url: str, alt: str = "Module"):
    return html.Div(
        html.Img(src=icon_url, alt=alt, className="strat-dir-icon-img"),
        className="strat-dir-icon-wrap",
    )


def strat_dir_title(text: str):
    return html.H3(text, className="strat-dir-tile-title")


def strat_dir_desc(text: str):
    return html.P(text, className="strat-dir-tile-desc")


def strat_dir_extra(label: str, value: str):
    return html.P(
        [
            html.Span(label, className="strat-dir-tile-extra-label"),
            html.Span(value, className="strat-dir-tile-extra-value"),
        ],
        className="strat-dir-tile-extra",
    )


def strat_dir_copy_wrap(*children):
    return html.Div(list(children), className="strat-dir-copy-wrap")


def strat_dir_row(*children):
    return html.Div(list(children), className="strat-dir-tile-row")


def strat_dir_badge_footer(live: bool, badge: str, meta: str):
    return html.Div(
        [
            html.Span(
                badge,
                style={
                    "display": "inline-flex",
                    "alignItems": "center",
                    "padding": "7px 16px",
                    "fontSize": "0.8rem",
                    "fontWeight": "700",
                    "color": "#fff",
                    "background": RED if live else GREY_BAR,
                    "borderRadius": "0 10px 0 0",
                },
            ),
            html.Span(
                meta,
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "padding": "0 14px",
                    "fontSize": "0.78rem",
                    "color": "#999",
                    "whiteSpace": "nowrap",
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


def strat_dir_link_tile(t: dict, icon_alt: str):
    return html.A(
        [
            strat_dir_row(
                strat_dir_icon(tile_icon_url(t["icon"]), icon_alt),
                strat_dir_copy_wrap(
                    strat_dir_title(t["title"]),
                    strat_dir_desc(t["desc"]),
                    strat_dir_extra(t["extra_label"], t["extra_value"]),
                ),
            ),
            strat_dir_badge_footer(t["live"], t["badge"], t["meta"]),
        ],
        href=t.get("href", "#"),
        style=_DIR_TILE_LINK_STYLE,
    )


def strat_ribbon_link_tile(t: dict, icon_alt: str):
    ribbon_label = t.get("ribbon", "COMING SOON")
    return html.A(
        html.Div(
            [
                coming_soon_ribbon(ribbon_label),
                strat_dir_row(
                    strat_dir_icon(tile_icon_url(t["icon"]), icon_alt),
                    strat_dir_copy_wrap(
                        strat_dir_title(t["title"]),
                        strat_dir_desc(t["desc"]),
                        strat_dir_extra(t["extra_label"], t["extra_value"]),
                    ),
                ),
            ],
            className="strat-tile-inner",
        ),
        href=t.get("href", "#"),
        className="strat-tile-has-ribbon",
        style=_DIR_TILE_RIBBON_LINK_STYLE,
    )


def strat_mixed_link_tile(t: dict, icon_alt: str, *, coming_soon_title: str = "Coming Soon"):
    is_coming_soon = t.get("title") == coming_soon_title

    copy_children = []
    if not is_coming_soon:
        copy_children.append(strat_dir_title(t["title"]))
    copy_children.extend(
        [
            strat_dir_desc(t["desc"]),
            strat_dir_extra(t["extra_label"], t["extra_value"]),
        ]
    )

    copy_class = "strat-dir-copy-wrap"
    if is_coming_soon:
        copy_class = "strat-dir-copy-wrap strat-dir-copy-wrap-full"

    row_children = []
    if not is_coming_soon and t.get("icon"):
        row_children.append(strat_dir_icon(tile_icon_url(t["icon"]), icon_alt))
    row_children.append(html.Div(copy_children, className=copy_class))

    tile_body = [html.Div(row_children, className="strat-dir-tile-row")]
    if not is_coming_soon:
        tile_body.append(strat_dir_badge_footer(t["live"], t["badge"], t["meta"]))

    if is_coming_soon:
        return html.A(
            html.Div(
                [coming_soon_ribbon(), *tile_body],
                className="strat-tile-inner",
            ),
            href=t.get("href", "#"),
            className="strat-tile-has-ribbon",
            style=_DIR_TILE_RIBBON_LINK_STYLE,
        )

    return html.A(tile_body, href=t.get("href", "#"), style=_DIR_TILE_LINK_STYLE)


def dir_page_layout(title: str, intro, tiles, *, page_class=None):
    intro_children = intro if isinstance(intro, (list, tuple)) else [intro]
    return html.Div(
        [
            html.H1(title, style=_DIR_TITLE_STYLE),
            html.P(intro_children, style=_DIR_INTRO_STYLE),
            html.Div(tiles, style=_DIR_GRID_STYLE),
        ],
        style=_DIR_PAGE_STYLE,
        className=page_class,
    )
