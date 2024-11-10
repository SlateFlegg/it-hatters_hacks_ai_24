import dash
from dash import dcc, html, Input, Output, State
from dash.exceptions import PreventUpdate
import base64
import os
import uuid
import pandas as pd
import dash_html_components as dhc

df = pd.read_excel('C:/Users/Maria Smirnova/Desktop/Проекты/межнар/it-hatters_hacks_ai_24/интерфейс_dash/User_list.xlsx')

app = dash.Dash(__name__)


red_button_style = {'background': "#0a0a23",
                    'color': 'white',
                    'height': '10px',
                    'width': '20px',
                    'margin-top': '10px',
                    'margin-left': '10px'}

app.layout = html.Div([
    #html.Img(src=app.get_asset_url('vprodakshion.png'), style={'width': '100%', 'height': '100%'}),
    html.Form([
        dcc.Input(id='username', type='text', placeholder='Введите логин', debounce=True,className='input-big'),
        html.Br(),
        dcc.Input(id='password', type='text', placeholder='Введите пароль', debounce=True, className='input-big'),
        ], 
        id='login_form', className='centered-block'),
    
    html.Div(id='upload_video',  style={"display": "none"}, children=[
        html.H1(id='text_box', children='Привет!', className='american-captain-header'),
        html.P(id='text_box2', children='Хочешь работать с близкими по духу людьми? Загружай визитку! Получи шанс на лучшую работу', className='montserrat-text'),
        html.P(id='text_box3', children='Загружай свою свою видео-визитку, а наши умные алгоритмы подскажут, как найти работу быстрее', className='montserrat-text'),
        html.Br(),
        html.Br(),
        dcc.Upload(
            id='video-uploader',
            children=html.Div([
                html.Div('Перетащите файл сюда или ', className='upload-message'),
                html.A('выберите файл', className='upload-link')
            ], className='upload-container'),
            multiple=False,
            accept="video/*",
        ),
        html.Br(),
        html.Br(),
        html.Hr(),
        html.P(id='text_box3', children='Не знаешь как снять классную визитку, которую хочется всем показывать? Не беда - читай инструкцию и действуй!', className='montserrat-text'),
        html.H1('Как создать видео-визитку'),

        html.H2('Шаг 1: Подготовка сценария',className='american-captain-header'),
        html.Ul([
            html.Li('Определись с целью: Чего ты хочешь достичь? Это может быть представление себя как профессионала, демонстрация своих навыков или просто краткое знакомство.', className='montserrat-text'),
            html.Li('Напиши сценарий:', className='montserrat-text'), 
                html.Ol([
                    html.Li('Вступление: Приветствие и короткое представление (имя, должность).'),
                    html.Li('Основная часть: Кратко расскажи о своем опыте работы, ключевых навыках и достижениях. Можно упомянуть проекты, над которыми работал(-а), и результаты.'),
                    html.Li('Заключение: Заверши видео фразой, подчеркивающей твою готовность к сотрудничеству и контактной информацией (например, электронная почта или номер телефона).'),
                ], className='montserrat-text'),
                html.P('Придерживайся хронометража: Оптимальная длина видео – около 1–2 минут. Важно быть лаконичным и структурированным.', className='montserrat-text')
        ]),

        html.H2('Шаг 2: Подбор оборудования',className='american-captain-header'),
        html.Ul([
            html.Li('Камера: Используй камеру хорошего качества (смартфон, веб-камеру или зеркальный фотоаппарат). Убедись, что картинка четкая и яркая.'),
            html.Li('Микрофон: Если есть возможность, используй внешний микрофон для записи звука. Это улучшит качество аудио.'),
            html.Li('Освещение: Снимай при хорошем освещении. Естественный свет от окна – отличный вариант. Избегай резких теней и слишком темных участков.'),
            html.Li('Фон: Выбери нейтральный фон без лишних деталей. Например, однотонная стена или аккуратный рабочий стол.')
        ], className='montserrat-text'),

        html.H2('Шаг 3: Запись видео',className='american-captain-header'),
        html.Ul([
            html.Li('Репетиция: Прочитай свой сценарий несколько раз вслух, чтобы привыкнуть к тексту и звучать естественно.'),
            html.Li('Запись: Начни запись, следуя сценарию. Постарайся говорить уверенно и смотреть прямо в камеру. Если допустил ошибку, начни заново.'),
            html.Li('Несколько дублей: Сделай несколько попыток, чтобы выбрать лучший вариант.')
        ],className='montserrat-text'),

        html.H2('Шаг 4: Монтаж',className='american-captain-header'),
        html.Ul([
            html.Li('Редактирование: Обрежь ненужные моменты, добавь вступительные и заключительные титры. Можно использовать программы вроде Adobe Premiere Pro, Final Cut Pro или бесплатные аналоги (например, DaVinci Resolve).'),
            html.Li('Добавление музыки: При желании можно добавить фоновую музыку, но она должна быть ненавязчивой и соответствовать общему настроению видео.'),
            html.Li('Проверка: Просмотри готовое видео несколько раз, убедившись, что все выглядит и звучит хорошо.')
        ],className='montserrat-text'),

        html.H2('Шаг 5: Публикация',className='american-captain-header'),
        html.Ul([
            html.Li('Загрузка: Загрузи видео на платформу, которую выберешь для отправки работодателю. Это может быть YouTube, Vimeo или любой другой видеохостинг.'),
            html.Li('Ссылка: Отправь ссылку на видео вместе с резюме или сопроводительным письмом. Убедись, что ссылка работает корректно.')
        ],className='montserrat-text'),

        html.H3('Советы:',className='american-captain-header'),
        html.Ul([
            html.Li('Будь собой: Натуральность и искренность всегда ценятся больше, чем идеально выученный текст.'),
            html.Li('Улыбка: Немного улыбки придаст видео дружелюбия и открытости.'),
            html.Li('Качество важнее количества: Лучше сделать одно качественное видео, чем несколько посредственных.')
        ],className='montserrat-text'),

        html.P('Следуя этим шагам, ты сможешь создать впечатляющую видео-визитку, которая выделит тебя среди других кандидатов. Удачи!',className='montserrat-text'),
        html.Div(id='video-path'),        
    ]),
    
    
    html.Div(id='user_data', style={"display": "none"}, children=[
        html.A(html.Button('Выйти', className='exit-button'),href='/'),
        html.Br(),
        html.Img(src=app.get_asset_url('photo.jpg'), height=100),

        html.H3('Surname birthdate and other'),
        html.H3('Result of our model')
    ]),
    
    
    html.Div(id='admin_panel', style={"display": "none"}, children=[
        html.A(html.Button('Выйти', className='exit-button'),href='/'),
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
    ], 
   )

def show_hide_element(username, password):
    if (df[df.user_login==username].empty): 
        return {'display': 'none'}, {'display': 'none'}, \
                {'display': 'none'}, {'display': 'block'}
    elif df[df.user_login==username]['user_password'].values[0]==password:
        is_admin = df[df.user_login==username]['is_admin'].values[0]
        if is_admin:
            return {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
        is_video_uploaded = df[df.user_login==username]['is_video_uploaded'].values[0]
        if is_video_uploaded:
            return {'display': 'none'}, {'display': 'block'},{'display': 'none'}, {'display': 'none'}
        return {'display': 'none'},{'display': 'none'}, {'display': 'block'}, {'display': 'none'}

    return  {'display': 'none'}, {'display': 'none'}, \
                {'display': 'none'}, {'display': 'block'}

    
@app.callback(Output('video-path', 'children'),Output('upload_video', 'style',allow_duplicate=True),  Output('user_data', 'style',allow_duplicate=True), Input('video-uploader', 'contents'), prevent_initial_call=True)
def save_and_display_path(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        
        # Создаем уникальную строку для имени файла
        file_name = f"{uuid.uuid4().hex}.mp4"
        
        # Путь к папке для сохранения файлов
        upload_folder = r'C:\Users\Maria Smirnova\Desktop\Проекты\межнар\it-hatters_hacks_ai_24\интерфейс_dash\\'#os.path.join(os.getcwd(), 'User')
        
        # Проверяем наличие папки, создаем ее, если нет
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        # Сохраняем файл
        file_path = os.path.join(upload_folder, file_name)
        with open(file_path, 'wb') as f:
            f.write(decoded)
        
        return f"Видео сохранено по пути: {file_path}", {'display': 'none'}, {'display': 'block'}
    

if __name__ == '__main__':
    app.run_server(debug=True)