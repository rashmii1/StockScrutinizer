from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.Div(
    [
        html.Img(src="assets/img/dash.jpg", style={"height": "100%", "width": "100%"}),
        html.Div(
            [
                html.H6(
                    "When it comes to investing, we want our money to grow with the highest rates of return, and the lowest risk possible. While there are no shortcuts to getting rich, there are smart ways to go about it."
                ),
                html.H1(
                    "We helps you in investing at the right place by reducing the risk!"
                ),
            ],
            className="context",
        ),
        html.Div(
            html.Ul(
                [
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                    html.Li(),
                ],
                className="circles",
            ),
            className="area",
        ),
        html.Section(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H2(
                                                    "New to the Stock Market?",
                                                    className="mb-3 text-white",
                                                ),
                                                html.H6(
                                                    "The stock market broadly refers to the collection of exchanges and other venues where the buying, selling, and issuance of shares of publicly held companies take place. ",
                                                    className="mb-4 text-white",
                                                ),
                                                html.P(
                                                    "Most of the trading in the Indian stock market takes place on its two stock exchanges: the Bombay Stock Exchange (BSE) and the National Stock Exchange (NSE)."
                                                ),
                                            ],
                                            className="d-flex flex-column justify-content-center ml-lg-auto mr-lg-5 col-lg-5 col-md-6 col-12",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Img(
                                                            src="assets/img/stck.jpg",
                                                            style={
                                                                "width": "150%",
                                                                "height": "100%",
                                                            },
                                                        ),
                                                    ],
                                                    className="about-working-hours",
                                                ),
                                            ],
                                            className="mr-lg-auto mt-3 col-lg-4 col-md-6 col-12",
                                        ),
                                    ],
                                    className="row",
                                )
                            ]
                        ),
                    ],
                    className="c",
                )
            ],
            className="sv",
            id="sv",
        ),
        html.Section(
            [
                html.A(
                    [
                        html.Button(
                            "N S E",
                            type="button",
                            className="glow-on-hover",
                            style={"margin-right": "17px"},
                        )
                    ],
                    href="https://www.nseindia.com/",
                ),
                html.Br(),
                html.Br(),
                html.A(
                    [
                        html.Button(
                            "B S E",
                            type="button",
                            className="glow-on-hover",
                            style={"margin-right": "17px"},
                        )
                    ],
                    href="https://www.bseindia.com/",
                ),
                html.Br(),
                html.Br(),
                html.A(
                    [
                        html.Button(
                            "GOOGLE FINANCE",
                            type="button",
                            className="glow-on-hover",
                            style={"margin-right": "17px"},
                        )
                    ],
                    href="https://www.google.com/finance/",
                ),
                html.Br(),
                html.Br(),
                html.A(
                    [
                        html.Button(
                            "YAHOO FINANCE", type="button", className="glow-on-hover"
                        )
                    ],
                    href="https://finance.yahoo.com/",
                ),
            ],
            className="redirect",
        ),
        html.Section(
            [
                html.H1("Analising the Stock Data", className="atext"),
                html.P(
                    "Stock market analysis enables investors to identify the intrinsic worth of a security even before investing in it. Stock market analysis is a vital part of any investor's portfolio, as it allows them to identify the worth of a security even before they make an investment. It also helps traders and investors make informed decisions.",
                    className="atext",
                ),
                html.Br(),
                html.P(
                    "Doing a proper research before investing is a must. Doing so helps you make informed decisions and maximize your returns. It is similar to buying a car or phone, you conduct due diligence to ensure that the investment is worth the money.",
                    className="atext",
                ),
                html.Div([], className="clearfix"),
                html.Br(),
                html.H2("Fundamental Research", className="atext"),
                html.P(
                    "In fundamental research, A fundamental research study is a process that involves trying to find out the value of an equity share using the company's financial statements. This step is carried out by analyzing the various aspects of the business, such as financial soundness, competitive advantage, and management style. The investor tries to analyse various aspects of the business like competitive advantage, financial soundness, quality of management and competition. The main aim is to ascertain the relative attractiveness of the underlying business. Here, it is assumed that the market price doesn’t reflect the true value of the company due to some uncontrollable external factors like investor sentiments. As the market will attain equilibrium, the real value will be equal to its market price in the long run. It believes that paying a higher price for a stock will affect return on investment adversely. Thus, by means of financial ratios, investors try to arrive at the true value at which a stock should ideally trade in the market.",
                    className="atext",
                ),
                html.H2("Indicators for Fundamental Research", className="atext"),
                html.Br(),
                html.H3("Return On Equity (ROE)", className="atext"),
                html.P(
                    "Return On Equity tells you about how much does a company earns on shareholders’ equity.A company’s return on equity shows how much it makes from its shareholders’ equity. It lets you know how efficient the company is in running its operations. Return On Equity = [(Income – Preference Dividend)/ (Average Shareholders’ Equity)]*100.",
                    className="atext",
                ),
                html.H3("Debt-Equity Ratio (DER)", className="atext"),
                html.P(
                    "Debt-Equity Ratio shows the proportion of assets which is being used to finance the assets of the company.A debt-equity ratio shows how much of the company's assets are used to finance its operations. It can be used to compare the relative performance of different companies within the same industry. Debt-Equity (D/E) Ratio = Total Debt/Total Equity",
                    className="atext",
                ),
                html.H3("Price to Earning Ratio (PER)", className="atext"),
                html.P(
                    "Price to Earning Ratio compares the current market price of the share with the earnings per share. Price to Earning Ratio is a simple and quick way to evaluate a company's share price. It tells you the current market price and the earnings per share. Price to Earning Ratio = Current Share Price/Earning Per Share. This ratio also indicates the number of years that will be required to get back the initial invested capital by way of returns. ",
                    className="atext",
                ),
                html.H3("Earning Per Share (EPS)", className="atext"),
                html.P(
                    "Earning Per Share is one such useful measure which the investors look for all the time. Earning Per Share is a great measure to evaluate a company's performance. It shows the amount of money that the company is making on every share. It can be used to compare a company's performance against that of other firms in the same industry. It can be easily used to compare performance across industries.",
                    className="atext",
                ),
                html.Div([], className="clearfix"),
                html.Br(),
                html.H2("Technical Research", className="atext"),
                html.P(
                    "Technical research relates to the study of past stock prices to predict the trend of prices in future. As the stock prices are dependent on investor psychology which keeps changing according to news and events, technical research emphasises the use of Stop-losses. It will save investors from suffering a big loss in future. Technical research is an instrument used to predict the future trend of a stock. It shows you the direction of the share price. It is not dependent on the news or events that have already been incorporated in the share price. Technical research focuses on the use of Stop-losses to prevent potential losses. It saves investors from suffering huge losses in the future due to the volatility of the stock prices.Weekly / monthly charts are used by medium/long term traders to ascertain the probability to earn higher more in the long run.",
                    className="atext",
                ),
                html.H2("Visualizing for Technical Research", className="atext"),
                html.Br(),
                html.H3("Candlestick Charts", className="atext"),
                html.P(
                    " Candlestick charts are used for technical analysis and can help decide the Buy, Sell, or Hold strategy.",
                    className="atext",
                ),
                html.H3("Line Charts", className="atext"),
                html.P(
                    "Line Charts are the conventional charts and most commonly used one. They are used by most of the fundamental and technical analysts to decide strategies.",
                    className="atext",
                ),
                html.H3("OHLC Charts", className="atext"),
                html.P(
                    "OHLC(Open, High, Low, and Close) charts are similar to candlestick charts and are important as they work on the closing price.",
                    className="atext",
                ),
            ],
            className="analysis",
        ),
        # html.Section([
        # ], className="stocknews"),
        html.Footer(
            [
                html.Img(
                    src="assets/img/slogo.png",
                    style={"height": "50%", "width": "20%"},
                ),
                html.P(
                    "Upcoming with Analysis Prediction Tools! .... Stay Tuened!.....",
                    className="foottext",
                    style={"color": "#fff"},
                ),
                html.P(
                    "“The best way to measure your investing success is not by whether you’re beating the market but by whether you’ve put in place a financial plan and a behavioral discipline that are likely to get you where you want to go.” Benjamin Graham",
                    className="foottext",
                    style={"padding-right": "3%", "color": "#fff"},
                ),
            ],
            className="fixed-footer",
        ),
    ],
    className="news",
)


def create_page_3():
    layout = html.Div(
        [
            nav,
            header,
        ]
    )
    return layout
