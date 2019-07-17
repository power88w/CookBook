# CookBook
	CookBook It should be a simple web application to create a book of recipes that will use MongoDb to store data, 
	where the user has the option of adding delete or edit recipes.

### Desktop

<img src="https://github.com/power88w/CookBook/blob/master/static/img/overview.JPG?raw=true"/> <br>

### Mobile

<img src="https://github.com/power88w/CookBook/blob/master/static/img/mobile.JPG?raw=true"/> <br>

## User Stories

As a user:


- User Story: as a user, I want to have access to the recipes.
- User Story: as a user, want to have a readable culinary recipe steps, ingredients, allergens.
- User Story: as a user, want to see a picture of the dish.
- User Story: as a user, want to be able to filter recipes due to the main ingredient.
- User Story: as a user, want to be able to filter recipes for allergens.
- User Story: as a user, want to be able to filter recipes on the country of origin or author.
- User Story: as a user, want to be able to add new recipes, edit or delete.
- User Story: as a user, want to be able to add new allergen, edit or delete.
- User Story: as a user, want to be able to add new unit of mesure, edit or delete.

## Technologies Used:

- HTML5 - used to create a website structure.

- [SASS](https://sass-lang.com/) - used to stylize Html.

- [Jquery](https://jquery.com/) - used for the filters on website.

- [Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/) - allows displaying the website in different resolutions

- [Delicious](https://bootstrapmade.com/demo/Delicious/) - free bootstrap template.

- [googlefonts](https://fonts.google.com/) - it allowed me to display a beautiful font.

- [Adobe XD](https://www.adobe.com/pl/products/xd.html) - was used to create a wireframe.

- [MongoDB](https://www.mongodb.com/) - was used to create database.

- [Python with Flask](https://www.fullstackpython.com/flask.html) - main logic and responsive of app.


## Features 




<img src="https://github.com/power88w/CookBook/blob/master/static/img/recipe.JPG?raw=true" width="400" />

### Features left to be implement in future development:


- Simple registering and login in the site.
- Possibility of voting on recipes.
- Possibility of commenting.


## Database schema

Example recipe:

```
	{
	{"_id":{"$oid":"5d110da7c98ec9cd0942c031"},"disp_name":"Marek",
	"origin_country":"China",
	"prescription_name":" Pulled Hoisin Chicken & Sesame Noodles",
	"prep_time":"15 min",
	"cook_time":"20 min",
	"allergen_name":"",
	"alle_01":"Sesame",
	"alle_02":"Barlaey",
	"alle_03":"Soy",
	"alle_04":"Wheat",
	"step_01a":"01.",
	"step_01b":
	"Heat a large, wide-based pan (preferably non-stick) with a matching lid with a drizzle of vegetable oil over a high heat
	Once hot, add the chicken thighs with a generous pinch of both salt and pepper and cook for 3 min on each side or until they're browned
	Meanwhile, peel (scrape the skin off with a teaspoon) and finely chop (or grate) the ginger
	Cut a few chilli rounds (set them aside for garnish) then cut the remaining red chilli[es] in half lengthways, 
	deseed (scrape the seeds out with a teaspoon) and chop ﬁnely
	Peel and finely chop (or grate) the garlic ",
	"step_02a":"02.",
	"step_02b":
	"Boil a kettle
	nOnce the chicken is browned, reduce the heat to medium-low and add a splash of water
	Cover with a lid and cook for 5-6 min or until the chicken is cooked through (no pink meat!)
	While the chicken is cooking, add the wholewheat noodles to a pot and cover them with boiled water until they're fully submerged
	nBring to the boil over a high heat and cook for 5-7 min or until tender with a slight bite, then drain and set aside in a bowl but keep the pot to use later",
	"step_03a":"03.",
	"step_03b":
	"Meanwhile, rip the leaves off the seasonal greens and discard the tough stalks
	Layer the leaves over each other, roll them up and slice into thin strips
	Trim, then slice the spring onions finely 
	Meanwhile, rip the leaves off the seasonal greens and discard the tough stalks
	nLayer the leaves over each other, roll them up and slice into thin strips
	Trim, then slice the spring onions finely ",
	"step_04a":"04.",
	"step_04b":
	"Meanwhile, return the reserved pot to a medium heat with a drizzle of vegetable oil
	Once hot, add the sliced seasonal greens, chopped garlic and a generous pinch of salt and cook for 1 min or until starting to wilt
	Add a splash of water and cook, covered, for 2 min or until completely wilted, then stir in the cooked noodles, toasted sesame oil and remaining soy sauce – these are your sesame noodles
	Serve the pulled hoisin chicken over the sesame noodles
	Garnish with the toasted sesame seeds, chilli rounds (remember to go easy if you don’t like heat) and sliced spring onion Enjoy!",
	"pcs_01":"320",
	"pcs_02":"15","pcs_03":"1",
	"pcs_04":"1",
	"pcs_05":"150","pcs_06":"0.5",
	"pcs_07":"5",
	"pcs_08":"2","pcs_09":"30",
	"pcs_10":"","uom_01":"gram(s)",
	"uom_02":"gram(s)","uom_03":"piece(s)",
	"uom_04":"piece(s)",
	"uom_05":"gram(s)",
	"uom_06":"liter(s)",
	"uom_07":"gram(s)",
	"uom_08":"piece(s)",
	"uom_09":"mililiter(s)",
	"uom_10":"","ing_01":"chicken thighs",
	"ing_02":"root ginger","ing_03":"garlic cloves",
	"ing_04":"red chilli",
	"ing_05":"spring onions",
	"ing_06":"sesame oil",
	"ing_07":"sesame seeds",
	"ing_08":"Wholewheat Noodle Nests",
	"ing_09":"hoisin sauce",
	"ing_10":"",
	"prescription_pic01":"https://www.alaskafromscratch.com/wp-content/uploads/2014/05/IMG_0165.jpg",
	"prescription_pic02":"https://smittenkitchendotcom.files.wordpress.com/2012/06/cold-rice-noodles-with-peanut-lime-chicken.jpg?w=751",
	"like":{"$numberInt":"0"}}

}
```

## Clone the project:

```
git clone https://github.com/power88w/CookBook.git
```

### Media

Recipes and pictures updated from:
* https://www.gousto.co.uk



