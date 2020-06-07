import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

LOGO = "assets/me.jpg"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=LOGO, height="100px"
                                )
                            ],
                        ),
                        dbc.Col(
                            [
                                dbc.Row(
                                    [
                                        html.H3("I AM KEK MEI TZY")
                                    ]
                                ),
                                dbc.Row(
                                    [
                                        html.H3("A MOM WHO CODE 👩‍💻 & COOK 👩‍🍳", className="card-title")
                                    ]
                                )
                            ],
                            width="auto"
                        ),
                    ],
                    align="center",
                )
            ),
            html.P(
                dbc.Button(
                    "View on Github",
                    href="https://github.com/MeiTzy222",
                    target="_blank",
                    color="primary"
                )
            )
        ]
    ),
    className="mb-3"
)


app.layout = html.Div(
    [
        navbar
    ]
)

app.run_server(debug=True, port=8051)
