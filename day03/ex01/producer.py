from random import randrange
import json
import logging
import redis


def produce_message():
    lower_bound = 10 ** 9
    upper_bound = 10 ** 10

    from_account = randrange(lower_bound, upper_bound)
    to_account = randrange(lower_bound, upper_bound)
    amount = randrange(1, 10) * 1000
    if randrange(5) == 0:
        amount *= -1

    data = {
        'metadata': {
            'from': from_account,
            'to': to_account,
        },
        'amount': amount,
    }
    json_data = json.dumps(data)

    return json_data
        

def main():
    host = 'localhost'
    port = 6379
    radis_db = 0
    n_transactions = 5

    logger = logging.getLogger('producer')
    logging.basicConfig(level=logging.INFO)

    r = redis.Redis(host=host, port=port, db=radis_db)

    for i in range(n_transactions):
        message = produce_message()
        r.publish('transactions', message)
        logger.info(message)


if __name__ == '__main__':
    main()

