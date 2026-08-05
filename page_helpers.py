from dash import html, dcc
import dash


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
