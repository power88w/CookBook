< div class="custom-control">
    <input class="custom-control-input" id="customCheck1">
        <label type="checkbox" class="custom-control-label" for="customCheck1">
            {{prescription.pcs_01}} {{prescription.uom_01}} {{prescription.ing_01}}</label>
</div>

< option
value = "1" > All
Receipies
Categories < / option >
{ %
for prescription in prescription %}
< option > {{prescription.ingredients_name}} < / option >
{ % endfor %}
