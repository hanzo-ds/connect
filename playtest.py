import datastore_connect


def main():
    print(f'\nDatastore Connect installed version: {datastore_connect.version()}')
    client = datastore_connect.get_client(host='play.hanzo.ai',
                                           username='play',
                                           password='datastore',
                                           port=443)
    print(f'Datastore Play current version and timezone: {client.server_version} ({client.server_tz})')
    result = client.query('SHOW DATABASES')
    print('Datastore play Databases:')
    for row in result.result_set:
        print(f'  {row[0]}')
    client.close()


if __name__ == '__main__':
    main()
