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

    # CARREGADOS
    'https://app.powerbi.com/reportEmbed?reportId=3b840a48-107c-456e-b836-e00f90d1693d&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # VAZIOS
    'https://app.powerbi.com/reportEmbed?reportId=0927ee70-4e1d-4ab8-aacd-4ca32792ced5&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # BASE 01
    'https://app.powerbi.com/reportEmbed?reportId=b6c50271-3884-400e-a251-2d456b1c494a&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # BASE 02
    'https://app.powerbi.com/reportEmbed?reportId=0b77fd45-b1cf-418b-a17f-9adba2dbda31&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # BASE CT
    'https://app.powerbi.com/reportEmbed?reportId=be91a282-1e47-44d9-ba56-681e3769d2fb&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',


    # BASE LEALES
    'https://app.powerbi.com/reportEmbed?reportId=33e946c3-b560-4a71-ab3f-e1934aca9a6f&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # BASE TRANSVALE
    'https://app.powerbi.com/reportEmbed?reportId=0b7282a2-7362-47f6-aa77-b5b875e2b8d1&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # BASE INSERT
    'https://app.powerbi.com/reportEmbed?reportId=d399cde9-2c32-44f5-a522-17ca563a7f86&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # ALTO RISCO
    'https://app.powerbi.com/reportEmbed?reportId=6da17e20-100d-4cf8-89cd-3b3d0044b238&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # MEDIO RISCO
    'https://app.powerbi.com/reportEmbed?reportId=b2d6efcb-87f8-4dfa-a6d7-0e5b693bd9a7&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',

    # BAIXO RISCO
    'https://app.powerbi.com/reportEmbed?reportId=51424b7a-ca8e-4b52-8ce3-aafce32558b8&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',


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
    # app.run_server(debug=True, port=8054, use_reloader=True)