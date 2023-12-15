import requests, shutil, connection

conn = connection.connect()
cur = conn.cursor(buffered=True)

cur.execute('SELECT image, id FROM bbdd')
urls = cur.fetchall()
for url in urls:
    if url[0] != '':
        res = requests.get(url[0])
        if res.status_code == 200:
            with open(f'{url[1]}.jpg','wb') as f:
                shutil.copyfileobj(res.raw, f)
                print(f'Image sucessfully Downloaded: {url[1]}.jpg')
        else:
            print('Image Couldn\'t be retrieved')


connection.disconnect(conn)