from imp import source_from_cache
import time
import os
import dash 
from dash import Dash, dcc, html, Input, Output


"""
GLOBAL CONFIGS

"""

# URLS CONFIG FOR ROTATE TABS
# url = {
    
#     "Comparativo de Uso - Monittora": 
#     "https://app.powerbi.com/groups/35336e6c-ae7b-456f-b382-d557def8fa6e/reports/29a6a265-0368-4bdb-ae9e-e86af3da47cb?chromeless=True",

#     "Comparativo de Uso - Valida": 
#     "https://app.powerbi.com/groups/35336e6c-ae7b-456f-b382-d557def8fa6e/reports/29a6a265-0368-4bdb-ae9e-e86af3da47cb/ReportSectionbf046b7d50740a01b3d6?chromeless=True",

#     "Comparativo de Uso - Novos Clientes":
#     "https://app.powerbi.com/groups/35336e6c-ae7b-456f-b382-d557def8fa6e/reports/29a6a265-0368-4bdb-ae9e-e86af3da47cb/ReportSectionb0cfdc025e90ed8f547b?chromeless=True"

#     }


# while True: 
#     for key, value in url.items():
#         print(key)
#         time.sleep(timer)
#     time.sleep(5)
source = [
            'https://app.powerbi.com/reportEmbed?reportId=5befd927-6043-459b-9b95-98e448ef3d51&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5',
            'https://app.powerbi.com/reportEmbed?reportId=f028225b-8ade-4e88-a50d-77cb4c731df5&autoAuth=true&ctid=aa047146-a58c-4fad-80ec-052475368fb5', 
        ]

global pg

pg = 0

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
        dcc.Interval (
            id = 'att',
            interval = 30,
            n_intervals = 0
        ),
        html.Iframe(
            id='iframe', 
            src=source[pg], 
            style={"height": "1080px", "width": "100%"}
        ),
    ]
)

@app.callback( 
    Output('iframe', 'src'), 
    [ Input('src', 'att') ] 
) 
def setPage():
    if pg < len(source):
        pg += 1
        return source[pg]
    else:
        pg = 0
        
if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False, port=8051)