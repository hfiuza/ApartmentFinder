import pandas as pd

from handlers.requests_helper import make_get_request
from areas.config import AREAS


def parse_apartment(apartment_json, area_id):
    return {
        'id': apartment_json['id'],
        'area_id': area_id,
        **{
            field: apartment_json['fields'].get(field)
            for field in ['tipo', 'area', 'aluguel', 'custo', 'visit_status', 'endereco', 'regiao_nome', 'listing_tags']
        }
    }


def parse(response_json, area_id):
    apartments = response_json['hits']['hit']
    print('Found {} apartments for area id {}'.format(len(apartments), area_id))
    return [parse_apartment(apartment_json, area_id) for apartment_json in apartments]


def get_apartments(area):
    urls = area['requests']

    apartments = []
    for url in urls:
        response = make_get_request(url)

        if response is not None and response.status_code == 200:
            parsed_apartments = parse(response.json(), area['id'])
            if len(parsed_apartments):
                apartments.extend(parsed_apartments)
            else:
                break
        else:
            import pdb; pdb.set_trace()
            return []
    return apartments


def get_all_apartments():
    return [apartment for area in AREAS for apartment in get_apartments(area)]


def filter_apartment(apartment):
    return (apartment['listing_tags'] is not None) and ('NEW_AD' in apartment['listing_tags'])


def get_filtered_apartments():
    return pd.DataFrame(
     [
         {
             key: value
             for key, value in apartment.items()
             if key != 'listing_tags'
         }
         for apartment in get_all_apartments()
         if filter_apartment(apartment)
      ]
    )