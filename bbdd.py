import connection, requests, re

conn = connection.connect()
cur = conn.cursor(buffered=True)

try:
    cur.execute('SELECT * FROM db_sencilla')
    for bd in cur.fetchall():
        print(bd)
        if bd[2] == 0:
            url = f'https://api.spoonacular.com/recipes/{bd[1]}/information?apiKey=097afe44aca74010895efa6139eba2b5'
            res = requests.get(url)
            data = res.json()
            if not data.get('instructions'):
                data['instructions'] = None
            if data['instructions'] != None:
                if not data.get('image'):
                    data['image'] = ''
                ingr = ''
                for ingrs in data['extendedIngredients']:
                    ingr = f'{ingr} / {ingrs["originalName"]}'
                ingr.strip()
                ingr = re.sub(r'\"', '', ingr)
                ins = re.sub(r'\"', '', data['instructions'])
                title = re.sub(r'\"', '', data['title'])
                string = 'INSERT INTO bbdd (id_recipe, name, ingredients, minutes, servings, instructions, vegan, vegetarian, glutenFree, diaryFree, image) VALUES(%d, "%s", "%s", %d, %d, "%s", %s, %s, %s, %s, "%s");' % (data["id"], title, ingr, data["readyInMinutes"], data["servings"], ins, data["vegan"], data["vegetarian"], data["glutenFree"], data["dairyFree"], data["image"])
                # print(string)
                cur.execute(string)
                conn.commit()
                for insts in data['analyzedInstructions'][0]['steps']:
                    ingredient = ''
                    for ingredients in insts['ingredients']:
                        step = re.sub(r'\"', '', insts["step"])
                        ingredient = f'{ingredient}, {ingredients["name"]}'
                        ingredient = re.sub(r'\"', '', ingredient)
                    cur.execute(f'INSERT INTO recipe_steps (recipe_id, step, instruction, ingredients) VALUES({bd[1]}, {insts["number"]}, "{step}", "{ingredient}");')
                    conn.commit()
                cur.execute(f'UPDATE db_sencilla SET done = true WHERE id = {bd[0]};')
                conn.commit()
except Exception as e:
    print(e)

connection.disconnect(conn)