from dash import register_page
from page_helpers import module_page

register_page(__name__, path="/customer/", name="Customer", title="Customer | TROVE WAM")

layout = module_page(
    "Customer",
    note="Coming soon — Customer modules will be available here.",
)
