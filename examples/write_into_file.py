import datastore_connect

if __name__ == '__main__':
    client = datastore_connect.get_client()
    query = 'SELECT number, toString(number) AS number_as_str FROM system.numbers LIMIT 5'
    fmt = 'CSVWithNames'  # or any other format, see https://docs.hanzo.ai/datastore/en/interfaces/formats
    stream = client.raw_stream(query=query, fmt=fmt)
    with open("output.csv", "wb") as f:
        for chunk in stream:
            f.write(chunk)
