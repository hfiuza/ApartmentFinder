import random

from constants import TELEGRAM_TOKEN
from users.config import USERS

from handlers.requests_helper import make_get_request


def create_bot_messages(new_apartments_df, user_name):
    if not new_apartments_df.empty:
        return [
            'Hi {}, we found the following new apartments'.format(user_name),
            *[
                'Region: {}, Address: {}, Rent: {} reais, Total costs: {} reais, Area: {}m2, Type: {}. https://www.quintoandar.com.br/imovel/{}'.format(*[apartment[field] for field in ['regiao_nome', 'endereco', 'aluguel', 'custo', 'area', 'tipo', 'id']]) for apartment in new_apartments_df.to_dict(orient='records')
            ]
        ]
    else:
        return ['No new apartments'] if random.random() < 0.1 else []


def send_message(bot_chatID, bot_message):
    send_text = 'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message

    make_get_request(send_text)


def send_messages(new_apartments_df, chat_id, user_name):
    for message in create_bot_messages(new_apartments_df, user_name):
        send_message(chat_id, message)


def send_all_messages(new_apartments_df):
    for user in USERS:
        user_apartments_df = new_apartments_df[
            new_apartments_df['area_id'].isin([str(area_id) for area_id in user['areas_ids']])
        ]
        # remove duplicates
        unique_apartment_ids = set(user_apartments_df['id'].values)
        user_apartments_df = user_apartments_df[
            user_apartments_df['id'].isin(unique_apartment_ids)
        ]
        send_messages(user_apartments_df, user['chat_id'], user['name'])
