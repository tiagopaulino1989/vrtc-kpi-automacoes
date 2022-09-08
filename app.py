from operator import indexOf
import time
import os
import dash 
from dash import Dash, dcc, html, Input, Output


"""
CONFIGURAÇÕES DE AMBIENTE & CONJUNTOS DE TELAS 
"""

timing = 60

# PAINÉIS DO VALIDA
dir_tela_01 = [ 
    # GESTÃO DE CADASTRO E CONSULTAS
    'https://app.powerbi.com/reportEmbed?reportId=5befd927-6043-459b-9b95-98e448ef3d51&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5&pageName=ReportSection46ac17ba842ce96ffa8c',

    # GESTÃO DE DIVERGENTES
    'https://app.powerbi.com/reportEmbed?reportId=5befd927-6043-459b-9b95-98e448ef3d51&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5&pageName=ReportSection1643a733f2fdd815e5f2',

    # OPERACIONAL VALIDA
    'https://app.powerbi.com/reportEmbed?reportId=5d5f1cef-915a-4c16-8113-8ae2fb2a0daf&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',
]

dir_tela_02 = [
    
]

dir_tela_03 = [

]

dir_tela_04 = [
    
]

dir_tela_05 = [

]

source = [
            # GESTÃO DE DIVERGENTES 
            'https://app.powerbi.com/reportEmbed?reportId=5befd927-6043-459b-9b95-98e448ef3d51&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',
            # AUDITORIA VALIDA
            'https://app.powerbi.com/reportEmbed?reportId=f028225b-8ade-4e88-a50d-77cb4c731df5&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5', 
        ]


def proximoNaFila(valores:list, atual):
    if valores.index(atual)+1<len(valores):
        return valores[valores.index(atual)+1]
    else:
        return valores[0]

app = Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)


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
        dcc.Dropdown(
            id = 'selecao-tela',
            options = ['Diretoria: Tela 1', 'Diretoria: Tela 2', 'Diretoria: Tela 3', 'Diretoria: Tela 4', 'Diretoria: Tela 5']
        ),
    ]
)

@app.callback( 
    Output('iframe', 'src'), 
    [Input('att', 'n_intervals'),Input('iframe','src')] 
)
def setPage(n_intervals,src):
    return proximoNaFila(source,src)
    
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)