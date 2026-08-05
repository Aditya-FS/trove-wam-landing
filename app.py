from python_compat import patch_pkgutil_find_loader

patch_pkgutil_find_loader()

try:
    from fix_icon_bg import main as _fix_icons

    _fix_icons()
except Exception as _icon_err:
    print(f"icon fix skipped: {_icon_err}")

import dash
from dash import html, dcc, Input, Output, callback
from flask import request
import dash_bootstrap_components as dbc

from whats_new_popup import (
    ENABLE_WHATS_NEW_AUTO_OPEN,
    build_whats_new_body_children,
    build_whats_new_popup,
    get_active_whats_new_content,
    has_ip_seen_whats_new_version,
)

app = dash.Dash(
    __name__,
    use_pages=True,
    requests_pathname_prefix="/wam/",
    routes_pathname_prefix="/wam/",
    title="TROVE WAM",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
    ],
)

from top_navbar import header
from navigation_bar import nav_bar, build_side_nav_items

app.config.suppress_callback_exceptions = True
server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div([header]),
        build_whats_new_popup(),
        html.Div([nav_bar], id="container_body", className="no-breadcrumbs"),
        dcc.Store(id="store_visitor_info", storage_type="session"),
    ]
)


@callback(
    Output("side-nav-items", "children"),
    Input("url", "pathname"),
)
def sync_side_nav_active_icons(pathname):
    return build_side_nav_items(pathname or "/")


@callback(
    Output("store_whats_new_popup_content", "data"),
    Input("url", "pathname"),
)
def load_whats_new_popup_content(_pathname):
    return get_active_whats_new_content()


@callback(
    Output("whats-new-popup-title", "children"),
    Output("whats-new-popup-subtitle", "children"),
    Output("whats-new-popup-body", "children"),
    Output("btn-whats-new-open", "style"),
    Input("store_whats_new_popup_content", "data"),
)
def render_whats_new_popup_content(content):
    content = content or {}
    has_active_version = bool(content.get("has_active_version"))
    trigger_style = {} if has_active_version else {"display": "none"}
    return (
        content.get("title") or "New Features!",
        content.get("subtitle") or "No active updates are available right now.",
        build_whats_new_body_children(content),
        trigger_style,
    )


@callback(
    Output("store_whats_new_popup_state", "data"),
    [
        Input("url", "pathname"),
        Input("store_whats_new_popup_content", "data"),
        Input("btn-whats-new-open", "n_clicks_timestamp"),
    ],
    prevent_initial_call=False,
)
def update_whats_new_popup_state(pathname, popup_content, open_click_timestamp):
    popup_content = popup_content or {}
    has_active_version = bool(popup_content.get("has_active_version"))
    popup_version_id = popup_content.get("id")
    ctx = dash.callback_context

    normalized = (pathname or "").rstrip("/")
    home_paths = {"", "/wam", dash.get_relative_path(""), dash.get_relative_path("/")}
    is_home = normalized in {(p or "").rstrip("/") for p in home_paths}

    if not ctx.triggered:
        seen = False
        if has_active_version and popup_version_id:
            seen = has_ip_seen_whats_new_version(request.remote_addr, popup_version_id)
        return {
            "open": ENABLE_WHATS_NEW_AUTO_OPEN
            and has_active_version
            and is_home
            and not seen
        }

    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == "btn-whats-new-open" and open_click_timestamp:
        return {"open": has_active_version}

    if trigger_id in {"url", "store_whats_new_popup_content"}:
        seen = False
        if has_active_version and popup_version_id:
            seen = has_ip_seen_whats_new_version(request.remote_addr, popup_version_id)
        return {
            "open": ENABLE_WHATS_NEW_AUTO_OPEN
            and has_active_version
            and is_home
            and not seen
        }

    return dash.no_update


@callback(
    Output("store_whats_new_popup_state", "data", allow_duplicate=True),
    [
        Input("btn-whats-new-close", "n_clicks_timestamp"),
        Input("btn-whats-new-footer-close", "n_clicks_timestamp"),
    ],
    prevent_initial_call=True,
)
def close_whats_new_popup(_close_ts, _footer_ts):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if trigger_id in {"btn-whats-new-close", "btn-whats-new-footer-close"}:
        return {"open": False}
    return dash.no_update


@callback(
    Output("whats-new-popup", "className"),
    Input("store_whats_new_popup_state", "data"),
)
def toggle_whats_new_popup_visibility(popup_state):
    if popup_state and popup_state.get("open"):
        return "whats-new-popup-shell is-open"
    return "whats-new-popup-shell"


if __name__ == "__main__":
    import threading
    import webbrowser

    APP_URL = "http://127.0.0.1:8000/wam/"

    def _open_browser():
        webbrowser.open(APP_URL)

    threading.Timer(1.25, _open_browser).start()
    app.run(host="0.0.0.0", port=8000, debug=False)
