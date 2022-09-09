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

    # GESTÃO DE COLETAS E ENTREGAS
    'https://app.powerbi.com/reportEmbed?reportId=78541a58-9172-4834-bd3c-680677b31fb4&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # GESTÃO DE FROTA
    'https://app.powerbi.com/reportEmbed?reportId=9af87f9b-efeb-4313-9374-473049fb2a3d&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # GESTÃO DE LEADTIME
    'https://app.powerbi.com/reportEmbed?reportId=3d96ac3f-6ec9-4db7-9194-91083cdee1b5&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # GESTÃO DE PARADAS
    'https://app.powerbi.com/reportEmbed?reportId=f70c3114-b75c-4f55-8bc2-6a902b0ead21&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # GESTÃO DE RASTREADORES
    'https://app.powerbi.com/reportEmbed?reportId=fc145d66-a4fd-442b-b0cd-789fd8df3056&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',


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
    # app.run_server(debug=True, port=8055, use_reloader=True)