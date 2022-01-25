import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href="/"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Dashboard", href="/page-2"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Analysis", href="/page-3"),
                ],
            ),
        ],
        brand="Stock Scrutinizer",
        brand_href="/",
        sticky="top",
        color="black",
        dark=True,
    )

    return navbar
