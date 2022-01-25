from dash.html.H5 import H5
from dash import html
from navbar import create_navbar

nav = create_navbar()


header = html.Div(
    [
        html.Section(
            [
                html.Div(
                    [
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(className="cube"),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P(
                                            "You must start investing as early as possible. Yesterday was"
                                        ),
                                        html.P(
                                            "better than today, and today is better than tomorrow. Don’t"
                                        ),
                                        html.P("wait for a significant market drop!"),
                                    ],
                                    className="title",
                                ),
                                html.Div(
                                    ["Don’t be late, Investing is great!"],
                                    className="sub_title",
                                ),
                                html.Div(
                                    [
                                      html.A ( [html.Button("Get Started"),], href="/page-2"),
                                        html.Span(),
                                        html.A([html.Button("Learn More"),], href="/page-3")
                                    ],
                                    className="btns",
                                ),
                            ],
                            className="center",
                        ),
                    ],
                    className="cubes",
                ),
            ],
            className="vor",
        ),
        html.Section(
            [
                html.Div(
                    [
                        html.H2("The Crux of Stock Market", className="section-title"),
                        html.Div(
                            [
                                html.A(
                                    [
                                        html.Img(
                                            src="assets/img/img1.png",
                                            className="featured__img",
                                        ),
                                        html.P(
                                            [
                                                html.Span(
                                                    "Buy Stocks That You Catch",
                                                    className="price",
                                                ),
                                                html.P(
                                                    "Investing in equities be prepared for losses exit at correct."
                                                ),
                                            ],
                                            className="featured__details",
                                        ),
                                    ],
                                    className="featured__item",
                                ),
                                html.A(
                                    [
                                        html.Img(
                                            src="assets/img/img2.png",
                                            className="featured__img",
                                        ),
                                        html.P(
                                            [
                                                html.Span(
                                                    "Be Realistic For Profit",
                                                    className="price",
                                                ),
                                                html.P(
                                                    "One to stay within their circle of competence."
                                                ),
                                            ],
                                            className="featured__details",
                                        ),
                                    ],
                                    className="featured__item",
                                ),
                                html.A(
                                    [
                                        html.Img(
                                            src="assets/img/img3.png",
                                            className="featured__img",
                                        ),
                                        html.P(
                                            [
                                                html.Span(
                                                    "Do Your Own Research",
                                                    className="price",
                                                ),
                                                html.P(
                                                    "One to stay within their circle of competence."
                                                ),
                                            ],
                                            className="featured__details",
                                        ),
                                    ],
                                    className="featured__item",
                                ),
                            ],
                            className="split",
                        ),
                        html.Div(
                            [
                                html.A(
                                    [
                                        html.Img(
                                            src="assets/img/img4.png",
                                            className="featured__img",
                                        ),
                                        html.P(
                                            [
                                                html.Span(
                                                    "Avoid Individual Stocks",
                                                    className="price",
                                                ),
                                                html.P(
                                                    "Buying only one individual stock, is like having all your eggs in one basket increasing risk."
                                                ),
                                            ],
                                            className="featured__details",
                                        ),
                                    ],
                                    className="featured__item",
                                ),
                                html.A(
                                    [
                                        html.Img(
                                            src="assets/img/img5.png",
                                            className="featured__img",
                                        ),
                                        html.P(
                                            [
                                                html.Span(
                                                    "Create Diversified Portfolio",
                                                    className="price",
                                                ),
                                                html.P(
                                                    "Reduces the risk of any one stock in the portfolio hurting the overall performance."
                                                ),
                                            ],
                                            className="featured__details",
                                        ),
                                    ],
                                    className="featured__item",
                                ),
                                html.A(
                                    [
                                        html.Img(
                                            src="assets/img/img6.png",
                                            className="featured__img",
                                        ),
                                        html.P(
                                            [
                                                html.Span(
                                                    "Avoid Short-term Trading",
                                                    className="price",
                                                ),
                                                html.P(
                                                    "Sometimes short-term investors can have unrealistic expectations about growing their money."
                                                ),
                                            ],
                                            className="featured__details",
                                        ),
                                    ],
                                    className="featured__item",
                                ),
                            ],
                            className="split",
                        ),
                    ],
                    className="container",
                )
            ],
            className="featured",
        ),
        html.Div(
            [
                html.Section(
                    [
                        html.Div(
                            [
                                html.Div(className="cube"),
                                html.Div(className="cube"),
                                html.Div(className="cube"),
                                html.Div(className="cube"),
                                html.Div(className="cube"),
                                html.Div(className="cube"),
                            ],
                            className="cubes",
                        ),
                        html.Div(
                            [
                                html.H2("Our products", className="cubes-title"),
                                html.Br(),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                    ],
                                    className="cubes",
                                ),
                                html.Article(
                                    [
                                        html.Img(
                                            src="assets/img/dash.jpg",
                                            className="product__image",
                                        ),
                                        html.H3(
                                            "DASH BOARD", className="product__title"
                                        ),
                                        html.P(
                                            "“The person who starts simply with the idea of getting rich won’t succeed; you must have a larger ambition.”",
                                            className="product__description",
                                        ),
                                        html.H4(" - John D. Rockefeller"),
                                        html.A(
                                            "Check Now", href="/page-2", className="btn"
                                        ),
                                    ],
                                    className="product shoe-red spacing",
                                ),
                                html.Div(
                                    [
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                    ],
                                    className="cubes",
                                ),
                                html.Article(
                                    [
                                        html.Img(
                                            src="assets/img/img7.png",
                                            className="product__image",
                                        ),
                                        html.H5(
                                            "STOCK FORSEE", className="product__title"
                                        ),
                                        html.P(
                                            "“You never know what kind of setup market will present to you, your objective should be to find opportunity where risk reward ratio is best.”",
                                            className="product__description",
                                        ),
                                        html.H4(" - Jaymin Shah"),
                                        html.A(
                                            "Check Now", href="/page-2", className="btn"
                                        ),
                                    ],
                                    className="product shoe-white shoe-left spacing",
                                ),
                                html.Div(
                                    [
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                        html.Div(className="cube"),
                                    ],
                                    className="cubes",
                                ),
                                html.Article(
                                    [
                                        html.Img(
                                            src="assets/img/b.jpg",
                                            className="product__image",
                                        ),
                                        html.H3(
                                            "KNOW STOCKS", className="product__title"
                                        ),
                                        html.P(
                                            "“If you have more than 120 or 130 I.Q. points, you can afford to give the rest away. You don’t need extraordinary intelligence to succeed as an investor.”",
                                            className="product__description",
                                        ),
                                        html.H4(" - Warren Buffet"),
                                        html.A(
                                            "Check Now", href="/page-3", className="btn"
                                        ),
                                    ],
                                    className="product shoe-blue spacing",
                                ),
                            ],
                            className="container",
                        ),
                    ],
                    className="our-products",
                ),
                html.Div(className="cube"),
                html.Div(className="cube"),
                html.Div(className="cube"),
                html.Div(className="cube"),
                html.Div(className="cube"),
                html.Div(className="cube"),
            ],
            className="cubes",
        ),
        html.Section(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Img(
                                            src="assets/img/h.jpg",
                                            style={"height": "75%", "width": "55%"},
                                            className="img-fluid",
                                        )
                                    ],
                                    className="d-flex flex-column justify-content-center ml-lg-auto mr-lg-5 col-lg-5 col-md-6 col-12",
                                ),
                                html.Div(
                                    [
                                        html.H2(
                                            "Hey! Don't you know about us? We Are Here For You..",
                                            style={"color": "#fff"},
                                            className="mb-4",
                                        ),
                                        html.P(
                                            "Stock Scrutinizer is a platform for providing its users personalized experience based on what they seek. This platform basically will be visualizing, forecasting & suggesting stocks platform for traders, investors to get a visualized idea about growth rate of the companies add on with brief information about the company they want to invest in.",
                                            style={"color": "#fff"},
                                        ),
                                        html.P(
                                            "We reduce the risk of loss, By providing the prediction of stocks. ",
                                            style={"color": "#fff"},
                                        ),
                                    ],
                                    className="mr-lg-auto mt-3 col-lg-5 col-md-6 col-12",
                                ),
                                #     html.Img(src="assets/img/x.png", style={"height":"95%", "width":"75%", "padding":"-30%","margin-left":"30%","bottom":"0%"}, className="footimg"),
                            ],
                            className="row",
                        )
                    ],
                    className="c",
                ),
            ],
            className="about_section",
            id="about",
        ),
        html.Footer(
            [
                html.P(
                    "Stocks Scrutinizer is a web application which will help to enhance the Stock Market experience by providing its users company information which are registered with NSE, stock related information of the firms and will give forecast of the price of future rates of the stock of company in market. Information is provided 'as is' and solely for informational purposes.",
                    className="foottext",
                ),
                html.P(
                    html.Img(
                        src="assets/img/slogo.png",
                        style={"height": "50%", "width": "50%"},
                    ),
                    className="footlogo",
                ),
            ],
            className="fixed-footer",
        ),
    ],
    className="home",
)


def create_page_home():
    layout = html.Div(
        [
            nav,
            header,
        ]
    )
    return layout
