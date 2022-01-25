import dash
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.LUX,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    ],
    external_scripts=[
        "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
    ],
    title="Stock Scrutinizer",
)
app._favicon = "favico.ico"
server = app.server
