import datetime

import pandas as pd

from handlers.s3_handler import read_from_s3, write_to_s3
from handlers.quinto_andar_handler import get_filtered_apartments
from handlers.telegram_handler import send_all_messages


def dataframe_exclusion(df, df_to_exclude):
    df_ids = set(df['id'].values) if not df.empty else set()
    ids_to_exclude = set(map(str, df_to_exclude['id'].values)) if not df_to_exclude.empty else set()
    remaining_ids = df_ids - ids_to_exclude
    print('Retrieved {} ids: {}'.format(len(df_ids), sorted(df_ids)))

    print('Had {} ids from past data: {}'.format(len(ids_to_exclude), sorted(ids_to_exclude)))
    print('{} ids remained'.format(len(remaining_ids)))

    return df[df['id'].isin(remaining_ids)] if not df.empty else pd.DataFrame()


def run():
    previous_apartments_df = read_from_s3()

    current_apartments_df = get_filtered_apartments()

    new_apartments_df = dataframe_exclusion(current_apartments_df, previous_apartments_df)

    aggregated_df = pd.concat([previous_apartments_df, new_apartments_df], sort=True)
    send_all_messages(new_apartments_df)
    write_to_s3(aggregated_df)


def main():
    import time
    while True:
        print('Started running at {}'.format(datetime.datetime.now()))
        run()
        print('Time sleep of 5 minutes')
        time.sleep(300)  # Delay for 1 minute (60 seconds).


if __name__ == '__main__':
    main()
