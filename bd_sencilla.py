import connection, requests

meals = ['main course', 'snack', 'dessert', 'breakfast']
diets = ['vegetarian', 'omnivore', 'vegan', 'gluten free', 'diary free']

conn = connection.connect()

for meal in meals:
    for diet in diets:
        url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey=097afe44aca74010895efa6139eba2b5&diet={diet}&number=100&type={meal}'
        # print(url)

        res = requests.get(url)
        data = res.json()

        cur = conn.cursor()

        for dada in data['results']:
            print(dada['id'])
            try:
                cur.execute(f'INSERT INTO db_sencilla (id_recipe) VALUES({dada["id"]})')
                conn.commit()
            except Exception as e:
                print(e)

connection.disconnect(conn)