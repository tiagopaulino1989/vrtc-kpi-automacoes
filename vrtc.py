from operator import indexOf
import time
import os
import dash 
from dash import Dash, dcc, html, Input, Output

source = [
            'https://app.powerbi.com/reportEmbed?reportId=5befd927-6043-459b-9b95-98e448ef3d51&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',
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
        dcc.Interval (
            id = 'att',
            interval = 40*1000,
            disabled = False
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