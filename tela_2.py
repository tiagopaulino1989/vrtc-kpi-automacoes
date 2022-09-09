from imp import reload
from operator import indexOf
import time
import os
from urllib.parse import uses_params
import dash 
from dash import Dash, dcc, html, Input, Output


"""
CONFIGURAÇÕES DE AMBIENTE & CONJUNTOS DE TELAS 
"""

timing = 45

source  = [ 

    # GESTÃO DE CHECKLIST
    'https://app.powerbi.com/reportEmbed?reportId=8a54e054-d7a7-4f98-b8a9-8172adbf923c&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # PRÉ-VIAGEM
    'https://app.powerbi.com/reportEmbed?reportId=c2d8e9e2-33b7-4915-a99d-2680a4ca8910&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # GRID CHECKLIST
    'https://app.powerbi.com/reportEmbed?reportId=ea79cd38-a833-4713-a9a2-c2e0368387ca&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

]


def nextPage(valores:list, atual):
    try:
        if valores.index(atual)+1<len(valores):
            return valores[valores.index(atual)+1]
        else:
            return valores[0]
    except:
        return valores[0]


app = Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

"""
APP LAYOUT
"""


app.title = "vrtc"

server = app.server

app.layout = html.Div(
    id="root",
    children=[
        html.Iframe(
            id='iframe', 
            src=source[0], 
            style={"height": "1095px", "width": "100%"}
        ),
        dcc.Interval(
            id = 'att',
            interval = timing*1000,
            disabled = False
        ),
    ]
)

# TEMPORIZADOR DAS PÁGINAS
@app.callback( 
    Output('iframe', 'src'), 
    [
        Input('att', 'n_intervals'),
        Input('iframe','src'),
    ] 
)
def setPage(n_intervals,src):
    return nextPage(source,src)
    
"""
SERVER-START 
"""

if __name__ == "__main__":
    app.run_server(debug=False)
    # app.run_server(debug=True, port=8052, use_reloader=True)