import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'CookBook'
app.config["MONGO_URI"] = 'mongodb+srv://root:zgadnij12345678910@myfirstcluster-gg70b.mongodb.net/CookBook?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/get_prescription')
def get_prescription():
    return render_template('prescription.html',
                           prescription=mongo.db.prescription.find())


@app.route('/add_prescription')
def add_prescription():
    return render_template('addprescription.html',
                           prescription=mongo.db.prescription.find(),
                           allergen=mongo.db.allergen.find(),
                           allergen2=mongo.db.allergen.find(),
                           allergen3=mongo.db.allergen.find(),
                           allergen4=mongo.db.allergen.find(),
                           uom1=mongo.db.uom.find(),
                           uom2=mongo.db.uom.find(),
                           uom3=mongo.db.uom.find(),
                           uom4=mongo.db.uom.find(),
                           uom5=mongo.db.uom.find(),
                           uom6=mongo.db.uom.find(),
                           uom7=mongo.db.uom.find(),
                           uom8=mongo.db.uom.find(),
                           uom9=mongo.db.uom.find(),
                           uom10=mongo.db.uom.find(),
                           ingredients1=mongo.db.ingredients.find(),
                           ingredients2=mongo.db.ingredients.find(),
                           ingredients3=mongo.db.ingredients.find(),
                           ingredients4=mongo.db.ingredients.find(),
                           ingredients5=mongo.db.ingredients.find(),
                           ingredients6=mongo.db.ingredients.find(),
                           ingredients7=mongo.db.ingredients.find(),
                           ingredients8=mongo.db.ingredients.find(),
                           ingredients9=mongo.db.ingredients.find(),
                           ingredients10=mongo.db.ingredients.find())


@app.route('/insert_prescription', methods=['POST'])
def insert_prescription():
    prescription =  mongo.db.prescription
    prescription.insert_one(request.form.to_dict())
    return redirect(url_for('get_prescription'))





@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'task_name':request.form.get('task_name'),
        'category_name':request.form.get('category_name'),
        'task_description': request.form.get('task_description'),
        'due_date': request.form.get('due_date'),
        'is_urgent':request.form.get('is_urgent')
    })
    return redirect(url_for('get_tasks'))




#Allergeny
@app.route('/')
@app.route('/get_allergen')
def get_allergen():
    return render_template('allergen.html',
                            allergen=mongo.db.allergen.find().sort('allergen_name', 1))



@app.route('/delete_allergen/<allergen_id>')
def delete_allergen(allergen_id):
    mongo.db.allergen.remove({'_id': ObjectId(allergen_id)})
    return redirect(url_for('get_allergen'))

@app.route('/edit_allergen/<allergen_id>')
def edit_allergen(allergen_id):
    return render_template('editallergen.html',
                           allergen=mongo.db.allergen.find_one(
                           {'_id': ObjectId(allergen_id)}))

@app.route('/update_allergen/<allergen_id>', methods=['POST'])
def update_allergen(allergen_id):
    mongo.db.allergen.update(
        {'_id': ObjectId(allergen_id)},
        {'allergen_name': request.form.get('allergen_name')})
    return redirect(url_for('get_allergen'))

@app.route('/insert_allergen', methods=['POST'])
def insert_allergen():
    allergen = mongo.db.allergen
    allergen_doc = {'allergen_name': request.form.get('allergen_name')}
    allergen.insert_one(allergen_doc)
    return redirect(url_for('get_allergen'))

@app.route('/new_allergen')
def new_allergen():
    return render_template('addallergen.html')

#Koniec Allergenów

#UOM

@app.route('/get_uom')
def get_uom():
    return render_template('uom.html',
                            uom=mongo.db.uom.find())

@app.route('/delete_uom/<uom_id>')
def delete_uom(uom_id):
    mongo.db.uom.remove({'_id': ObjectId(uom_id)})
    return redirect(url_for('get_uom'))

@app.route('/edit_uom/<uom_id>')
def edit_uom(uom_id):
    return render_template('edituom.html',
                           uom=mongo.db.uom.find_one(
                           {'_id': ObjectId(uom_id)}))

@app.route('/update_uom/<uom_id>', methods=['POST'])
def update_uom(uom_id):
    mongo.db.uom.update(
        {'_id': ObjectId(uom_id)},
        {'uom_name': request.form.get('uom_name')})
    return redirect(url_for('get_uom'))

@app.route('/insert_uom', methods=['POST'])
def insert_uom():
    uom = mongo.db.uom
    uom_doc = {'uom_name': request.form.get('uom_name')}
    uom.insert_one(uom_doc)
    return redirect(url_for('get_uom'))

@app.route('/new_uom')
def new_uom():
    return render_template('adduom.html')


# Finish UOM


# Ingredients


@app.route('/get_ingredients')
def get_ingredients():
    return render_template('ingredients.html',
                            ingredients=mongo.db.ingredients.find().sort('ingredients_name', 1))

@app.route('/delete_ingredients/<ingredients_id>')
def delete_ingredients(ingredients_id):
    mongo.db.ingredients.remove({'_id': ObjectId(ingredients_id)})
    return redirect(url_for('get_ingredients'))

@app.route('/edit_ingredients/<ingredients_id>')
def edit_ingredients(ingredients_id):
    return render_template('editingredients.html',
                           ingredients=mongo.db.ingredients.find_one(
                           {'_id': ObjectId(ingredients_id)}))

@app.route('/update_ingredients/<ingredients_id>', methods=['POST'])
def update_ingredients(ingredients_id):
    mongo.db.ingredients.update(
        {'_id': ObjectId(ingredients_id)},
        {'ingredients_name': request.form.get('ingredients_name')})
    return redirect(url_for('get_ingredients'))

@app.route('/insert_ingredients', methods=['POST'])
def insert_ingredients():
    ingredients = mongo.db.ingredients
    ingredients_doc = {'ingredients_name': request.form.get('ingredients_name')}
    ingredients_doc2 = {'ingredients_name': request.form.get('ingredients_name2')}
    ingredients_doc3 = {'ingredients_name': request.form.get('ingredients_name3')}
    ingredients_doc4 = {'ingredients_name': request.form.get('ingredients_name4')}
    ingredients_doc5 = {'ingredients_name': request.form.get('ingredients_name5')}
    ingredients_doc6 = {'ingredients_name': request.form.get('ingredients_name6')}
    ingredients_doc7 = {'ingredients_name': request.form.get('ingredients_name7')}
    ingredients_doc8 = {'ingredients_name': request.form.get('ingredients_name8')}
    ingredients_doc9 = {'ingredients_name': request.form.get('ingredients_name9')}
    ingredients_doc10 = {'ingredients_name': request.form.get('ingredients_name10')}
    ingredients.insert_one(ingredients_doc)
    ingredients.insert_one(ingredients_doc2)
    ingredients.insert_one(ingredients_doc3)
    ingredients.insert_one(ingredients_doc4)
    ingredients.insert_one(ingredients_doc5)
    ingredients.insert_one(ingredients_doc6)
    ingredients.insert_one(ingredients_doc7)
    ingredients.insert_one(ingredients_doc8)
    ingredients.insert_one(ingredients_doc9)
    ingredients.insert_one(ingredients_doc10)
    return redirect(url_for('get_ingredients'))


@app.route('/new_ingredients')
def new_ingredients():
    return render_template('addingredients.html')


#Koniec Ingredients


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)





