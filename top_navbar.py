import dash
from dash import html

header = html.Header(
    html.Div(
        [
            html.A(
                "Trove WAM",
                href=dash.get_relative_path("/"),
                className="top-nav-brand",
            ),
            html.Div(
                [
                    html.Button(
                        [
                            html.I(className="fas fa-bell"),
                            html.Span("What's New"),
                        ],
                        id="btn-whats-new-open",
                        n_clicks=0,
                        className="btn-whats-new",
                        type="button",
                    ),
                    html.A(
                        "Contact us",
                        id="btn-contact-us",
                        href="mailto:NewDelhiBCNFSWAM@Bain.com",
                        className="btn-contact-us",
                    ),
                ],
                className="top-nav-actions",
            ),
        ],
        className="top-nav-inner",
    ),
    className="top-nav",
    id="top-navbar",
)
