import redis
import re
import json
import argparse
import logging


def change_transaction(message, bad_accounts):
    data = json.loads(message)
    to_account = data['metadata']['to']
    from_account = data['metadata']['from']
    amount = data['amount']

    if from_account not in bad_accounts and \
            to_account in bad_accounts and amount > 0:
        data['metadata']['from'] = to_account
        data['metadata']['to'] = from_account

    return data


def main():
    host = 'localhost'
    port = 6379
    radis_db = 0

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        help="is a parameter receiving a list of bad guys account numbers",
        type=lambda x: re.split(r'[\s+|,]\s*', x),
        action='append',
    )
    args = parser.parse_args()
    try:
        bad_accounts = {
            int(bad_account)
            for alist in args.e for bad_account in alist
        }
    except ValueError:
        print('Argument must be an integer.')
        exit()

    logger = logging.getLogger('consumer')
    logging.basicConfig(level=logging.INFO)

    r = redis.Redis(host=host, port=port, db=radis_db)
    pubsub = r.pubsub()

    try:
        pubsub.subscribe('transactions')

        for message in pubsub.listen():
            if message['type'] == 'message':
                data = change_transaction(message['data'], bad_accounts)
                logger.info(data)
    except Exception as e:
        logger.info(e)


if __name__ == '__main__':
    main()
