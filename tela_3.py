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

timing = 40

source  = [ 

    # COMPARATIVO MONITTORA
    'https://app.powerbi.com/reportEmbed?reportId=29a6a265-0368-4bdb-ae9e-e86af3da47cb&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # COMPARATIVO VALIDA
    'https://app.powerbi.com/reportEmbed?reportId=29a6a265-0368-4bdb-ae9e-e86af3da47cb&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5&pageName=ReportSectionbf046b7d50740a01b3d6',

    # NOVOS CLIENTES
    'https://app.powerbi.com/reportEmbed?reportId=29a6a265-0368-4bdb-ae9e-e86af3da47cb&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5&pageName=ReportSectionb0cfdc025e90ed8f547b',

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
    # app.run_server(debug=True, port=8053, use_reloader=True)