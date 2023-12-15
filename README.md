# Recetas
Proyecto python


## Git instructions
git clone https://github.com/Joan404/Recetas.git

git commit -a

git push


## SQL:

CREATE TABLE db_sencilla(
    id INT AUTO_INCREMENT,
    id_recipe INT UNIQUE,
    done BOOLEAN DEFAULT false
    PRIMARY KEY (id)
);

CREATE TABLE bbdd(
    id INT AUTO_INCREMENT,
    id_recipe INT UNIQUE,
    name VARCHAR(255),
    ingredients VARCHAR(255),
    minutes INT,
    servings INT,
    instructions VARCHAR(700),
    vegan BOOLEAN,
    vegetarian BOOLEAN,
    glutenFree BOOLEAN,
    diaryFree BOOLEAN,
    image VARCHAR(255)
    PRIMARY KEY (id)
);

CREATE TABLE recipe_steps(
	id INT AUTO_INCREMENT,
    recipe_id INT NOT NULL,
    step INT,
    instruction VARCHAR(255),
    ingredients VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES bbdd(id_recipe)
);
