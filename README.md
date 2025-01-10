<div align="center">
<h1> AllRecipes.com Scraper </h1>
Scrapy spider to scrape recipe and nutritional data from <code>www.allrecipes.com</code>. <strong>35,516 recipes</strong> scraped, found in <code>/export</code>. 
<br>
Data was used to provide insight of the nutritional value of various recipes.
</div>

<br>

Data scraped for each recipe includes:

```python
# Recipe and related information 
'name', 'url', 'category', 'author', 'summary', 'rating', 'rating_count', 'review_count', 'ingredients', 'directions', 'prep', 'cook', 'total', 'Servings', 'Yield', 
# Nutritional information
'calories', 'carbohydrates_g', 'sugars_g', 'fat_g', 'saturated_fat_g', 'cholesterol_mg', 'protein_g', 'dietary_fiber_g', 'sodium_mg', 'calories_from_fat',
# Additional nutritional info - Metals
'calcium_mg', 'iron_mg', 'magnesium_mg', 'potassium_mg', 'zinc_mg', 'phosphorus_mg',
# Additional nutritional info - Vitamins
'vitamin_a_iu_IU', 'niacin_equivalents_mg', 'vitamin_b6_mg', 'vitamin_c_mg', 'folate_mcg', 'thiamin_mg', 'riboflavin_mg', 'vitamin_e_iu_IU', 'vitamin_k_mcg', 'biotin_mcg', 'vitamin_b12_mcg',
# Additional nutritional info - Fats
'mono_fat_g', 'poly_fat_g', 'trans_fatty_acid_g', 'omega_3_fatty_acid_g', 'omega_6_fatty_acid_g'
```

> *Note:* Many recipes do not list most of the nutrients from the 'Additional nutritional info'. A few nutrients aren't scraped and have been omitted from 'Additional nutritional info' due to its listing being extremely scarce.

### Example data
```json
[
  {
    "name": "Italian Rice Croquettes",
    "url": "https://www.allrecipes.com/recipe/221968/italian-rice-croquettes/",
    "category": ["Appetizer"],
    "author": "John Mitzewich",
    "summary": "Try Chef John's family recipe for fried rice croquettes (arancini) filled with Parmesan cheese and marinara sauce.",
    "rating": "4.5",
    "rating_count": "13",
    "review_count": 0,
    "ingredients": "2 pounds chicken giblets; 1 cup water; 0.5 teaspoon salt; 4 cups salted water; 2 cups long grain white rice, uncooked; 2 cups grated Parmesan cheese; 0.5 cup marinara sauce; 0.25 cup dry bread crumbs; 2 large eggs; 2 tablespoons chopped fresh parsley; salt and freshly ground black pepper to taste; 1 cup dry bread crumbs for coating; vegetable oil for frying",
    "directions": "Combine chicken giblets, 1 cup water, and 0.5 teaspoon salt in a pressure cooker; cook for about 20 minutes. Drain giblets and let cool, about 10 minutes. Chop giblets in a food processor or by hand; set aside. Bring rice and water to a boil in a saucepan over high heat. Reduce heat to medium-low, cover, and simmer until the rice is tender, and the liquid has been absorbed, 20 to 25 minutes. Spread cooked rice onto a baking sheet to cool, about 5 minutes. Transfer rice to a large bowl. Mix in giblets, grated Parmesan cheese, marinara sauce, 0.25 cup bread crumbs, eggs, parsley, salt, and ground pepper. Cover with plastic wrap and refrigerate for 1 hour. Remove rice and giblet mixture from refrigerator and form 2-inch, football-shaped croquettes. Roll croquettes in bread crumbs and place on a baking sheet. Heat oil in a large skillet over medium-high heat; cook breaded croquettes until browned on all sides, about 10 minutes. Transfer to a plate lined with paper towels to absorb excess oil.",
    "prep": "PT50M",
    "cook": "PT50M",
    "total": "PT100M",
    "servings": ["40"],
    "calories": "99 kcal",
    "carbohydrates_g": "10 g",
    "fat_g": "3 g",
    "protein_g": "7 g",
    "cuisine": "italian"
  },
  {
    "name": "Utica Greens and Beans",
    "url": "https://www.allrecipes.com/recipe/236226/utica-greens-and-beans/",
    "category": ["Dinner", "Side Dish"],
    "author": "John Mitzewich",
    "summary": "Escarole paired with cranberry beans and pancetta makes the perfect dish to start the New Year!",
    "rating": "4.7",
    "rating_count": "15",
    "review_count": 0,
    "ingredients": "2 heads escarole, bottoms trimmed and leaves coarsely sliced; 4 ounces pancetta bacon, diced; 2 tablespoons olive oil; 2 tablespoons chopped jalapeno pepper, or to taste; 3 cloves garlic, minced; 1 cup chicken broth; salt and ground black pepper to taste; 1 (12 ounce) can cooked cranberry beans; 0.5 cup fine bread crumbs; 1 pinch red pepper flakes, or to taste; 2 tablespoons fine bread crumbs; 0.5 cup finely grated Parmigiano-Reggiano cheese; 1 tablespoon olive oil, or as needed",
    "directions": "Wash escarole leaves in a large bowl in several changes of cold water until no grit remains. Bring a large pot of salted water to a boil; cook escarole in the boiling water until bright green and slightly wilted, about 2 minutes. Transfer escarole to a large bowl using a slotted spoon. Rinse greens in cold water to stop the cooking process. Drain thoroughly. Place pancetta and olive oil into a large oven-safe skillet over medium heat; cook until browned and crisp in spots, about 5 minutes. Stir jalapeno peppers into pancetta; cook and stir until peppers start to soften, about 2 minutes. Stir in garlic and cook until fragrant, about 1 minute more. Pour chicken broth over pancetta mixture, bring to a simmer, and season with salt and black pepper to taste. Gently stir beans into skillet. Mix escarole into mixture, turn off heat, and top with 0.5 cup bread crumbs. Stir until crumbs are still visible but most are incorporated. Season with red pepper flakes. Top with 2 tablespoons bread crumbs followed by Parmigiano-Reggiano cheese; drizzle top with 1 tablespoon olive oil. Set oven rack about 6 inches from the heat source and preheat the oven's broiler. Place skillet under broiler and cook until top is golden brown, 2 to 4 minutes. Serve immediately.",
    "prep": "PT20M",
    "cook": "PT15M",
    "total": "PT35M",
    "servings": ["6"],
    "calories": "307 kcal",
    "carbohydrates_g": "25 g",
    "fat_g": "18 g",
    "protein_g": "12 g",
    "cuisine": "Unknown"
  }
]

```


## Run
First run `pip install scrapy`
### Run the spider:

- Set `DEBUG = False` in `recipescrape/spiders/recipes.py`
- Run `scrapy crawl recipes`

### Run the spider w/ minimal logs with count of items scraped and pause/resume-ability:

- Set `DEBUG = True` in `recipescrape/spiders/recipes.py`
- Run `scrapy crawl recipes -L WARN --logfile=scrapelog.txt -s JOBDIR=recipes/spider-1`

## Extras

### Spider to extract all the nutrient names:

- Run `pip install pandas`
- Make sure `DEBUG = True` in `nutrient_list.py`
- Run `scrapy crawl nutrients -o nutrients.csv -L WARN -s JOBDIR=nutrients/spider-1`
- Outputs 'items_count', 'nutri_count', 'nutri_list', 'url' in `output.json` in which the last row contains the unified list of nutritients found so far.
