import dash
import wikipedia
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from navbar import create_navbar
from app import app
from datetime import datetime as dt
import yfinance as yf
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# model
from model import prediction
from sklearn.svm import SVR


d = pd.read_csv(
    r"https://docs.google.com/spreadsheets/d/e/2PACX-1vTwKy5v8cpuqw_zf7eD2Gz1y9_2pGczVjnchAQqAWMX8KeTw4uCqE8fB6dvSeiyq42gCQu8e4XN1_F7/pub?gid=454164262&single=true&output=csv"
)


nse_n = d["NAME"].tolist()

nse_p = d["%CHNG"].tolist()

nse_h = d["HIGH"].tolist()

nse_l = d["LOW"].tolist()

nse_c = d["CURRENT"].tolist()


nse = ".NS"


def get_stock_price_fig(df):

    fig = px.line(
        df, x="Date", y=["Close", "Open"], title="Closing and Openning Price vs Date"
    )

    return fig


def get_more(df):
    df["EWA_20"] = df["Close"].ewm(span=20, adjust=False).mean()
    fig = px.scatter(
        df, x="Date", y="EWA_20", title="Exponential Moving Average vs Date"
    )
    fig.update_traces(mode="lines+markers")
    return fig


nav = create_navbar()

header = html.Div(
    children=[
        html.Div(
            children=[
                html.P(
                    children=[
                        html.Img(
                            src="assets/img/slogo.png",
                            style={"height": "50%", "width": "50%"},
                        ),
                        html.Br([]),
                        "Stock Scrutinizer",
                    ],
                    className="logo",
                ),
                html.A(
                    [
                        html.I(
                            [" " " " " " " " "Dashboard"],
                            className="fa fa-dashboard icons",
                        )
                    ],
                    href="",
                    className="icon-a",
                ),
                dcc.Link(
                    [html.I([" " " " " " " " "Home"], className="fa fa-users icons")],
                    href="/",
                    className="icon-a",
                ),
                html.A(
                    [
                        html.I(
                            [" " " " " " " " "Forecast"], className="fa fa-list icons"
                        )
                    ],
                    href="",
                    className="icon-a",
                ),
                html.A(
                    [
                        html.I(
                            [" " " " " " " " "Analysis"], className="fa fa-tasks icons"
                        ),
                    ],
                    href="/page-3",
                    className="icon-a",
                ),
            ],
            id="mySidenav",
            className="sidenav",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Span(
                                    [
                                        "NSE INDICES",
                                    ],
                                    className="nav",
                                    style={
                                        "font-size": "30px",
                                        "cursor": "pointer",
                                        "color": "white",
                                    },
                                ),
                            ],
                            className="col-div-6",
                        ),
                        html.Div([], className="clearfix"),
                    ],
                    className="head",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.Span([nse_n[0]]),
                                        html.P(
                                            [
                                                html.Span([nse_c[0]]),
                                                html.Span(" ("),
                                                html.Span([nse_p[0]]),
                                            ]
                                        ),
                                        html.Span(") "),
                                    ]
                                ),
                            ],
                            className="box",
                        ),
                    ],
                    className="col-div-3",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.Span([nse_n[1]]),
                                        html.P(
                                            [
                                                html.Span([nse_c[1]]),
                                                html.Span(" ("),
                                                html.Span([nse_p[1]]),
                                            ]
                                        ),
                                        html.Span(") "),
                                    ]
                                ),
                            ],
                            className="box",
                        ),
                    ],
                    className="col-div-3",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.Span([nse_n[2]]),
                                        html.P(
                                            [
                                                html.Span([nse_c[2]]),
                                                html.Span(" ("),
                                                html.Span([nse_p[2]]),
                                            ]
                                        ),
                                        html.Span(") "),
                                    ]
                                ),
                            ],
                            className="box",
                        ),
                    ],
                    className="col-div-3",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.Span([nse_n[3]]),
                                        html.P(
                                            [
                                                html.Span([nse_c[3]]),
                                                html.Span(" ("),
                                                html.Span([nse_p[3]]),
                                            ]
                                        ),
                                        html.Span(") "),
                                    ]
                                ),
                            ],
                            className="box",
                        ),
                    ],
                    className="col-div-3",
                ),
                html.Div([], className="clearfix"),
                html.Br([]),
                html.Br([]),
                html.Div([], className="clearfix"),
                html.Br(),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Span(
                                    [
                                        "Company Info",
                                    ],
                                    className="nav",
                                    style={
                                        "font-size": "30px",
                                        "cursor": "pointer",
                                        "color": "white",
                                    },
                                ),
                            ],
                            className="col-div-2",
                        ),
                        html.Div([], className="clearfix"),
                    ],
                    className="head",
                ),
                html.Div(
                    [
                        html.P("Input stock code: "),
                        html.Div(
                            [
                                dcc.Input(id="dropdown_tickers", type="text"),
                                html.Button("Submit", id="submit"),
                            ],
                            className="form",
                        ),
                    ],
                    className="input-place",
                ),
                html.Div(
                    [
                        dcc.DatePickerRange(
                            id="my-date-picker-range",
                            min_date_allowed=dt(1995, 8, 5),
                            max_date_allowed=dt.now(),
                            initial_visible_month=dt.now(),
                            end_date=dt.now().date(),
                        ),
                    ],
                    className="date",
                ),
                html.Div(
                    [
                        html.Button("Stock Price", className="stock-btn", id="stock"),
                        html.Button(
                            "Indicators", className="indicators-btn", id="indicators"
                        ),
                        dcc.Input(
                            id="n_days", type="text", placeholder="Number of Days"
                        ),
                        html.Button(
                            "Forecast", className="forecast-btn", id="forecast"
                        ),
                    ],
                    className="buttons",
                ),
                html.Div(
                    [
                        html.Div(
                            [html.Img(id="logo"), html.P(id="ticker")],  # header
                            className="header",
                        ),
                        html.Br(),
                        html.Div(id="description", className="decription_ticker"),
                        html.Br(),
                        html.Div([], id="graphs-content"),
                        html.Br(),
                        html.Div([], id="main-content"),
                        html.Br(),
                        html.Div([], id="forecast-content"),
                    ],
                    className="content",
                ),
            ],
            id="main",
        ),
    ],
    className="dashboard",
)


# callback for company info
@app.callback(
    [
        Output("description", "children"),
        Output("logo", "src"),
        Output("ticker", "children"),
        Output("stock", "n_clicks"),
        Output("indicators", "n_clicks"),
        Output("forecast", "n_clicks"),
    ],
    [Input("submit", "n_clicks")],
    [State("dropdown_tickers", "value")],
)
def update_data(n, val):  # inpur parameter(s)
    if n == None:
        return (
            html.H4(
                "Hey there! Please enter a legitimate stock code to get details.",
                style={"color": "#fff", "padding-left": "10%", "margin-top": "-110px"},
            ),
            None,
            None,
            None,
            None,
            None,
        )
        # raise PreventUpdate
    else:
        if val == None:
            raise PreventUpdate
        else:
            ticker = yf.Ticker(val + nse)
            inf = ticker.info
            df = pd.DataFrame().from_dict(inf, orient="index").T
            df[["logo_url", "shortName", "longBusinessSummary"]]
            return (
                df["longBusinessSummary"].values[0],
                df["logo_url"].values[0],
                df["shortName"].values[0],
                None,
                None,
                None,
            )


# callback for stocks graphs
@app.callback(
    [
        Output("graphs-content", "children"),
    ],
    [
        Input("stock", "n_clicks"),
        Input("my-date-picker-range", "start_date"),
        Input("my-date-picker-range", "end_date"),
    ],
    [State("dropdown_tickers", "value")],
)
def stock_price(n, start_date, end_date, val):
    if n == None:
        return [""]
        # raise PreventUpdate
    if val == None:
        raise PreventUpdate
    else:
        if start_date != None:
            df = yf.download(val + nse, str(start_date), str(end_date))
        else:
            df = yf.download(val + nse)

    df.reset_index(inplace=True)
    fig = get_stock_price_fig(df)
    return [dcc.Graph(figure=fig)]


# callback for indicators
@app.callback(
    [Output("main-content", "children")],
    [
        Input("indicators", "n_clicks"),
        Input("my-date-picker-range", "start_date"),
        Input("my-date-picker-range", "end_date"),
    ],
    [State("dropdown_tickers", "value")],
)
def indicators(n, start_date, end_date, val):
    if n == None:
        return [""]
    if val == None:
        return [""]

    if start_date == None:
        df_more = yf.download(val + nse)
    else:
        df_more = yf.download(val + nse, str(start_date), str(end_date))

    df_more.reset_index(inplace=True)
    fig = get_more(df_more)
    return [dcc.Graph(figure=fig)]


# callback for forecast
@app.callback(
    [Output("forecast-content", "children")],
    [Input("forecast", "n_clicks")],
    [State("n_days", "value"), State("dropdown_tickers", "value")],
)
def forecast(n, n_days, val):
    if n == None:
        return [""]
    if val == None:
        raise PreventUpdate
    fig = prediction(val + nse, int(n_days) + 1)
    return [dcc.Graph(figure=fig)]


def create_page_2():
    layout = html.Div(
        [
            header,
        ]
    )
    return layout
