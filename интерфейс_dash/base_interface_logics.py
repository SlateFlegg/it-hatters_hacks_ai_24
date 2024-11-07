import dash
from dash import dcc, html, Input, Output, State
from dash.exceptions import PreventUpdate
import base64
import os
import uuid
import pandas as pd

df = pd.read_excel('C:/Users/Maria Smirnova/Desktop/Проекты/межнар/интерфейс_dash/User_list.xlsx')


red_button_style = {'background': "#0a0a23",
                    'color': 'white',
                    'height': '10px',
                    'width': '20px',
                    'margin-top': '10px',
                    'margin-left': '10px'}

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Form([
        dcc.Input(id='username', type='text', placeholder='Введите логин', debounce=True),
        dcc.Input(id='password', type='text', placeholder='Введите пароль', debounce=True),
        ], 
        id='login_form',style={"display": "block"},
    ),
    html.Div(id='upload_video',  style={"display": "none"}, children=[
        html.H1(id='text_box', children='text'),
        dcc.Upload(
            id='video-uploader',
            children=html.Div(['Перетащите файл сюда или ', html.A('выберите файл')]),
            multiple=False,
            accept="video/*",
        ),
        html.Hr(),
        html.Div(id='video-path'),
    ]),
    html.Div(id='user_data', style={"display": "none"}, children=[
        html.A(html.Button('Выйти'),href='/', style=red_button_style),
        html.Br(),
        html.Img(src=app.get_asset_url('photo.jpg'), height=70),
        html.H3('Name Surname birthdate and other'),
        html.H3('Result of our model')
    ]),
    html.Div(id='admin_panel', style={"display": "none"}, children=[
        html.A(html.Button('Выйти'),href='/', style=red_button_style),
        html.Br(),
        html.H1('The admin panel will be here')
    ])
])

@app.callback(
   Output(component_id='admin_panel', component_property='style'),
   Output(component_id='user_data', component_property='style'),
   Output(component_id='upload_video', component_property='style'),
   Output(component_id='login_form', component_property='style'),
   [Input(component_id='username', component_property='value'),
    Input(component_id='password', component_property='value'),
    ])

def show_hide_element(username, password):
    if (df[df.user_login==username].empty): #| (df[df.user_login==username]['user_password'].any()!=password)
        return {'display': 'none'}, {'display': 'none'}, \
                {'display': 'none'}, {'display': 'block'}
    elif df[df.user_login==username]['user_password'].values[0]==password:
        print('im here')
        is_admin = df[df.user_login==username]['is_admin'].values[0]
        if is_admin:
            return {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
        is_video_uploaded = df[df.user_login==username]['is_video_uploaded'].values[0]
        if is_video_uploaded:
            return {'display': 'none'}, {'display': 'block'},{'display': 'none'}, {'display': 'none'}
        return {'display': 'none'},{'display': 'none'}, {'display': 'block'}, {'display': 'none'}
    
    print('nope', df[df.user_login==username]['user_password'])
    return {'display': 'none'}, {'display': 'none'}, \
                {'display': 'none'}, {'display': 'block'}

    
@app.callback(Output('video-path', 'children'), Output('user_data', 'style',allow_duplicate=True), Input('video-uploader', 'contents'), prevent_initial_call=True)
def save_and_display_path(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        
        # Создаем уникальную строку для имени файла
        file_name = f"{uuid.uuid4().hex}.mp4"
        
        # Путь к папке для сохранения файлов
        upload_folder = r'C:\Users\Maria Smirnova\Desktop\Проекты\межнар\интерфейс_dash\\'#os.path.join(os.getcwd(), 'User')
        
        # Проверяем наличие папки, создаем ее, если нет
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        # Сохраняем файл
        file_path = os.path.join(upload_folder, file_name)
        with open(file_path, 'wb') as f:
            f.write(decoded)
        
        return f"Видео сохранено по пути: {file_path}", {'display': 'block'}



if __name__ == '__main__':
    app.run_server(debug=True)