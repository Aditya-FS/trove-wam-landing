from dash import html, dcc
import dash_bootstrap_components as dbc

ENABLE_WHATS_NEW_AUTO_OPEN = False


def get_active_whats_new_content():
    return {
        "id": 1,
        "has_active_version": True,
        "title": "New Features!",
        "subtitle": "Latest updates for Trove WAM",
        "body": [
            "Wealth Management module landing is live.",
            "Asset Management and Capital Markets tiles are ready.",
        ],
    }


def build_whats_new_body_children(content):
    content = content or {}
    items = content.get("body") or []
    if not items:
        return html.P("No active updates are available right now.")
    return html.Ul([html.Li(item) for item in items], className="whats-new-list")


def build_whats_new_popup():
    return html.Div(
        [
            dcc.Store(id="store_whats_new_popup_content"),
            dcc.Store(id="store_whats_new_popup_state", data={"open": False}),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H2(id="whats-new-popup-title", children="New Features!"),
                                    html.Button(
                                        "×",
                                        id="btn-whats-new-close",
                                        n_clicks=0,
                                        className="whats-new-close",
                                    ),
                                ],
                                className="whats-new-header",
                            ),
                            html.P(id="whats-new-popup-subtitle", className="whats-new-subtitle"),
                            html.Div(id="whats-new-popup-body", className="whats-new-body"),
                            html.Div(
                                dbc.Button(
                                    "Close",
                                    id="btn-whats-new-footer-close",
                                    n_clicks=0,
                                    className="btn-contact-us",
                                ),
                                className="whats-new-footer",
                            ),
                        ],
                        className="whats-new-dialog",
                    )
                ],
                id="whats-new-popup",
                className="whats-new-popup-shell",
            ),
        ]
    )


def has_ip_seen_whats_new_version(ip_address, version_id):
    return False
