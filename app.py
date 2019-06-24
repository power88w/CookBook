import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'CookBook'
app.config["MONGO_URI"] = 'mongodb+srv://root:zgadnij12345678910@myfirstcluster-gg70b.mongodb.net/CookBook?retryWrites=true&w=majority'

mongo = PyMongo(app)

#Allergeny
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

@app.route('/')
@app.route('/get_prescription')
def get_prescription():
    return render_template('prescription.html',
                           prescription1=mongo.db.prescription.find().sort('prescription_name', 1),
                           prescription2=mongo.db.prescription.find().sort('prescription_name', 1),
                           prescription3=mongo.db.prescription.find().sort('prescription_name', 1),
                           prescription4=mongo.db.prescription.find().sort('prescription_name', 1),
                           prescription5=mongo.db.prescription.find().sort('prescription_name', 1),
                           prescription6=mongo.db.prescription.find().sort('prescription_name', 1),
                           allergen=mongo.db.allergen.find().sort('allergen_name', 1))




@app.route('/get_prescriptionlist')
def get_prescriptionlist():
    return render_template('prescriptionlist.html',
                            prescriptionlist=mongo.db.prescription.find().sort('prescription_name', 1))


@app.route('/delete_prescription/<prescription_id>')
def delete_prescription(prescription_id):
    mongo.db.prescription.remove({'_id': ObjectId(prescription_id)})
    return redirect(url_for('get_prescriptionlist'))


@app.route('/edit_prescription/<prescription_id>')
def edit_prescription(prescription_id):
    the_prescription = mongo.db.prescription.find_one({"_id": ObjectId(prescription_id)})
    all_allergens = mongo.db.allergen.find()
    all_allergens2 = mongo.db.allergen.find()
    all_allergens3 = mongo.db.allergen.find()
    all_allergens4 = mongo.db.allergen.find()
    all_ingredients1 = mongo.db.ingredients.find()
    all_ingredients2 = mongo.db.ingredients.find()
    all_ingredients3 = mongo.db.ingredients.find()
    all_ingredients4 = mongo.db.ingredients.find()
    all_ingredients5 = mongo.db.ingredients.find()
    all_ingredients6 = mongo.db.ingredients.find()
    all_ingredients7 = mongo.db.ingredients.find()
    all_ingredients8 = mongo.db.ingredients.find()
    all_ingredients9 = mongo.db.ingredients.find()
    all_ingredients10 = mongo.db.ingredients.find()
    all_uom1 = mongo.db.uom.find()
    all_uom2 = mongo.db.uom.find()
    all_uom3 = mongo.db.uom.find()
    all_uom4 = mongo.db.uom.find()
    all_uom5 = mongo.db.uom.find()
    all_uom6 = mongo.db.uom.find()
    all_uom7 = mongo.db.uom.find()
    all_uom8 = mongo.db.uom.find()
    all_uom9 = mongo.db.uom.find()
    all_uom10 = mongo.db.uom.find()
    return render_template('editprescription.html', prescription=the_prescription,
                           allergen=all_allergens, allergen2=all_allergens2,
                           allergen3=all_allergens3, allergen4=all_allergens4,
                           ingredients1=all_ingredients1, ingredients2=all_ingredients2,
                           ingredients3=all_ingredients3, ingredients4=all_ingredients4,
                           ingredients5=all_ingredients5, ingredients6=all_ingredients6,
                           ingredients7=all_ingredients7, ingredients8=all_ingredients8,
                           ingredients9=all_ingredients9, ingredients10=all_ingredients10,
                           uom1=all_uom1, uom2=all_uom2, uom3=all_uom3, uom4=all_uom4, uom5=all_uom5, uom6=all_uom6,
                           uom7=all_uom7, uom8=all_uom8, uom9=all_uom9, uom10=all_uom10)




@app.route('/update_prescription/<prescription_id>', methods=["POST"])
def update_prescription(prescription_id):
    prescription = mongo.db.prescription
    prescription.update({'_id': ObjectId(prescription_id)},
    {
        'disp_name':request.form.get('disp_name'),
        'origin_country':request.form.get('origin_country'),
        'prescription_name':request.form.get('prescription_name'),
        'prep_time':request.form.get('prep_time'),
        'cook_time':request.form.get('cook_time'),
        'allergen_name': request.form.get('allergen_name'),
        'alle_01': request.form.get('alle_01'),
        'alle_02': request.form.get('alle_02'),
        'alle_03': request.form.get('alle_03'),
        'alle_04': request.form.get('alle_04'),
        'step_01a': request.form.get('step_01a'),
        'step_01b': request.form.get('step_01b'),
        'step_02a': request.form.get('step_02a'),
        'step_02b': request.form.get('step_02b'),
        'step_03a': request.form.get('step_03a'),
        'step_03b': request.form.get('step_03b'),
        'step_04a': request.form.get('step_04a'),
        'step_04b': request.form.get('step_04b'),
        'pcs_01': request.form.get('pcs_01'),
        'pcs_02': request.form.get('pcs_02'),
        'pcs_03': request.form.get('pcs_03'),
        'pcs_04': request.form.get('pcs_04'),
        'pcs_05': request.form.get('pcs_05'),
        'pcs_06': request.form.get('pcs_06'),
        'pcs_07': request.form.get('pcs_07'),
        'pcs_08': request.form.get('pcs_08'),
        'pcs_09': request.form.get('pcs_09'),
        'pcs_10': request.form.get('pcs_10'),
        'uom_01': request.form.get('uom_01'),
        'uom_02': request.form.get('uom_02'),
        'uom_03': request.form.get('uom_03'),
        'uom_04': request.form.get('uom_04'),
        'uom_05': request.form.get('uom_05'),
        'uom_06': request.form.get('uom_06'),
        'uom_07': request.form.get('uom_07'),
        'uom_08': request.form.get('uom_08'),
        'uom_09': request.form.get('uom_09'),
        'uom_10': request.form.get('uom_10'),
        'ing_01': request.form.get('ing_01'),
        'ing_02': request.form.get('ing_02'),
        'ing_03': request.form.get('ing_03'),
        'ing_04': request.form.get('ing_04'),
        'ing_05': request.form.get('ing_05'),
        'ing_06': request.form.get('ing_06'),
        'ing_07': request.form.get('ing_07'),
        'ing_08': request.form.get('ing_08'),
        'ing_09': request.form.get('ing_09'),
        'ing_10': request.form.get('ing_10'),
        'prescription_pic01': request.form.get('prescription_pic01'),
        'prescription_pic02': request.form.get('prescription_pic02')
    })

    mongo.db.prescription.update_many({'disp_name': None}, {'$set': {'disp_name': ''}})
    mongo.db.prescription.update_many({'origin_country': None}, {'$set': {'origin_country': ''}})
    mongo.db.prescription.update_many({'prescription_name': None}, {'$set': {'prescription_name': ''}})
    mongo.db.prescription.update_many({'prep_time': None}, {'$set': {'prep_time': ''}})
    mongo.db.prescription.update_many({'cook_time': None}, {'$set': {'cook_time': ''}})
    mongo.db.prescription.update_many({'allergen_name': None}, {'$set': {'allergen_name': ''}})
    mongo.db.prescription.update_many({'alle_01': None}, {'$set': {'alle_01': ''}})
    mongo.db.prescription.update_many({'alle_02': None}, {'$set': {'alle_02': ''}})
    mongo.db.prescription.update_many({'alle_03': None}, {'$set': {'alle_03': ''}})
    mongo.db.prescription.update_many({'alle_04': None}, {'$set': {'alle_04': ''}})
    mongo.db.prescription.update_many({'step_01a': None}, {'$set': {'step_01a': ''}})
    mongo.db.prescription.update_many({'step_01b': None}, {'$set': {'step_02a': ''}})
    mongo.db.prescription.update_many({'step_02a': None}, {'$set': {'step_02a': ''}})
    mongo.db.prescription.update_many({'step_02b': None}, {'$set': {'step_02b': ''}})
    mongo.db.prescription.update_many({'step_03a': None}, {'$set': {'step_03a': ''}})
    mongo.db.prescription.update_many({'step_03b': None}, {'$set': {'step_03b': ''}})
    mongo.db.prescription.update_many({'step_04a': None}, {'$set': {'step_04a': ''}})
    mongo.db.prescription.update_many({'step_04b': None}, {'$set': {'step_04b': ''}})
    mongo.db.prescription.update_many({'pcs_01': None}, {'$set': {'pcs_01': ''}})
    mongo.db.prescription.update_many({'pcs_02': None}, {'$set': {'pcs_02': ''}})
    mongo.db.prescription.update_many({'pcs_03': None}, {'$set': {'pcs_03': ''}})
    mongo.db.prescription.update_many({'pcs_04': None}, {'$set': {'pcs_04': ''}})
    mongo.db.prescription.update_many({'pcs_05': None}, {'$set': {'pcs_05': ''}})
    mongo.db.prescription.update_many({'pcs_06': None}, {'$set': {'pcs_06': ''}})
    mongo.db.prescription.update_many({'pcs_07': None}, {'$set': {'pcs_07': ''}})
    mongo.db.prescription.update_many({'pcs_08': None}, {'$set': {'pcs_08': ''}})
    mongo.db.prescription.update_many({'pcs_09': None}, {'$set': {'pcs_09': ''}})
    mongo.db.prescription.update_many({'pcs_10': None}, {'$set': {'pcs_10': ''}})
    mongo.db.prescription.update_many({'uom_01': None}, {'$set': {'uom_01': ''}})
    mongo.db.prescription.update_many({'uom_02': None}, {'$set': {'uom_02': ''}})
    mongo.db.prescription.update_many({'uom_03': None}, {'$set': {'uom_03': ''}})
    mongo.db.prescription.update_many({'uom_04': None}, {'$set': {'uom_04': ''}})
    mongo.db.prescription.update_many({'uom_05': None}, {'$set': {'uom_05': ''}})
    mongo.db.prescription.update_many({'uom_06': None}, {'$set': {'uom_06': ''}})
    mongo.db.prescription.update_many({'uom_07': None}, {'$set': {'uom_07': ''}})
    mongo.db.prescription.update_many({'uom_08': None}, {'$set': {'uom_08': ''}})
    mongo.db.prescription.update_many({'uom_09': None}, {'$set': {'uom_09': ''}})
    mongo.db.prescription.update_many({'uom_10': None}, {'$set': {'uom_10': ''}})
    mongo.db.prescription.update_many({'ing_01': None}, {'$set': {'ing_01': ''}})
    mongo.db.prescription.update_many({'ing_02': None}, {'$set': {'ing_02': ''}})
    mongo.db.prescription.update_many({'ing_03': None}, {'$set': {'ing_03': ''}})
    mongo.db.prescription.update_many({'ing_04': None}, {'$set': {'ing_04': ''}})
    mongo.db.prescription.update_many({'ing_05': None}, {'$set': {'ing_05': ''}})
    mongo.db.prescription.update_many({'ing_06': None}, {'$set': {'ing_06': ''}})
    mongo.db.prescription.update_many({'ing_07': None}, {'$set': {'ing_07': ''}})
    mongo.db.prescription.update_many({'ing_08': None}, {'$set': {'ing_08': ''}})
    mongo.db.prescription.update_many({'ing_09': None}, {'$set': {'ing_09': ''}})
    mongo.db.prescription.update_many({'ing_10': None}, {'$set': {'ing_10': ''}})
    mongo.db.prescription.update_many({'prescription_pic01': None}, {'$set': {'prescription_pic01': ''}})
    mongo.db.prescription.update_many({'prescription_pic02': None}, {'$set': {'prescription_pic02': ''}})

    return redirect(url_for('get_prescription'))

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





