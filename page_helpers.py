from dash import html, dcc
import dash


def coming_soon_ribbon(label="COMING SOON"):
    return html.Div(
        html.Div(label, className="strat-coming-soon-ribbon"),
        className="strat-coming-soon-ribbon-wrap",
    )


def module_page(title: str, links=None, note=None):
    links = links or []
    children = [
        html.H2(title),
        html.P(note or "Placeholder redirect page — wire your module content here."),
    ]
    if links:
        children.append(
            html.Ul(
                [
                    html.Li(
                        dcc.Link(
                            label,
                            href=dash.get_relative_path(href),
                        )
                    )
                    for label, href in links
                ]
            )
        )
    children.append(
        html.P(
            dcc.Link("← Back to Home", href=dash.get_relative_path("/")),
            className="module-back",
        )
    )
    return html.Div(children, className="module-placeholder")
