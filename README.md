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
[{"name": "Italian Rice Croquettes", "url": "https://www.allrecipes.com/recipe/221968/italian-rice-croquettes/", "category": ["Appetizer"], "author": "John Mitzewich", "summary": "Try Chef John&#39;s family recipe for fried rice croquettes (arancini) filled with Parmesan cheese and marinara sauce.", "rating": "4.5", "rating_count": "13", "review_count": 0, "ingredients": "2 pounds chicken giblets; 1 cup water; 0.5 teaspoon salt; 4 cups salted water; 2 cups long grain white rice, uncooked; 2 cups grated Parmesan cheese; 0.5 cup marinara sauce; 0.25 cup dry bread crumbs; 2 large eggs; 2 tablespoons chopped fresh parsley; salt and freshly ground black pepper to taste; 1 cup dry bread crumbs for coating; vegetable oil for frying", "directions": "Combine chicken giblets, 1 cup water, and 1/2 teaspoon salt in a pressure cooker; cook for about 20 minutes. Drain giblets and let cool, about 10 minutes. Chop giblets in a food processor or by hand; set aside. Bring rice and water to a boil in a saucepan over high heat. Reduce heat to medium-low, cover, and simmer until the rice is tender, and the liquid has been absorbed, 20 to 25 minutes. Spread cooked rice onto a baking sheet to cool, about 5 minutes. Transfer rice to a large bowl. Mix in giblets, grated Parmesan cheese, marinara sauce, 1/4 cup bread crumbs, eggs, parsley, salt, and ground pepper. Cover with plastic wrap and refrigerate for 1 hour. Remove rice and giblet mixture from refrigerator and form 2-inch, football shaped croquettes. Roll croquettes in bread crumbs and place on a baking sheet. Heat oil in a large skillet over medium-high heat; cook breaded croquettes until browned on all sides, about 10 minutes. Transfer to a plate lined with paper towels to absorb excess oil.", "prep": "PT50M", "cook": "PT50M", "total": "PT100M", "servings": ["40"], "calories": "99 kcal", "carbohydrates_g": "10 g", "fat_g": "3 g", "protein_g": "7 g", "cuisine": "italian"},
{"name": "Utica Greens and Beans", "url": "https://www.allrecipes.com/recipe/236226/utica-greens-and-beans/", "category": ["Dinner", "Side Dish"], "author": "John Mitzewich", "summary": "Escarole paired with cranberry beans and pancetta makes the perfect dish to start the New Year!", "rating": "4.7", "rating_count": "15", "review_count": 0, "ingredients": "2 heads escarole, bottoms trimmed and leaves coarsely sliced; 4 ounces pancetta bacon, diced; 2 tablespoons olive oil; 2 tablespoons chopped jalapeno pepper, or to taste; 3 cloves garlic, minced; 1 cup chicken broth; salt and ground black pepper to taste; 1 (12 ounce) can cooked cranberry beans; 0.5 cup fine bread crumbs; 1 pinch red pepper flakes, or to taste; 2 tablespoons fine bread crumbs; 0.5 cup finely grated Parmigiano-Reggiano cheese; 1 tablespoon olive oil, or as needed", "directions": "Wash escarole leaves in a large bowl in several changes of cold water until no grit remains. Bring a large pot of salted water to a boil; cook escarole in the boiling water until bright green and slightly wilted, about 2 minutes. Transfer escarole to a large bowl using a slotted spoon. Rinse greens in cold water to stop the cooking process. Drain thoroughly. Place pancetta and olive oil into a large oven-safe skillet over medium heat; cook until browned and crisp in spots, about 5 minutes. Stir jalapeno peppers into pancetta; cook and stir until peppers start to soften, about 2 minutes. Stir in garlic and cook until fragrant, about 1 minute more. Pour chicken broth over pancetta mixture, bring to a simmer, and season with salt and black pepper to taste. Gently stir beans into skillet. Mix escarole into mixture, turn off heat, and top with 1/2 cup bread crumbs. Stir until crumbs are still visible but most are incorporated. Season with red pepper flakes. Top with 2 tablespoons bread crumbs followed by Parmigiano-Reggiano cheese; drizzle top with 1 tablespoon olive oil. Set oven rack about 6 inches from the heat source and preheat the oven&#39;s broiler. Place skillet under broiler and cook until top is golden brown, 2 to 4 minutes. Serve immediately.", "prep": "PT20M", "cook": "PT15M", "total": "PT35M", "servings": ["6"], "calories": "307 kcal", "carbohydrates_g": "25 g", "fat_g": "18 g", "protein_g": "12 g", "cuisine": "Unknown"},
{"name": "Chef John&#39;s Pumpkin Bread", "url": "https://www.allrecipes.com/recipe/220494/chef-johns-holiday-pumpkin-bread/", "category": ["Bread"], "author": "John Mitzewich", "summary": "Toasted walnuts add crunch to Chef John&#39;s version of this easy quick bread.", "rating": "4.6", "rating_count": "70", "review_count": 0, "ingredients": "cooking spray; 0.5 cup unsalted butter, softened; 1 cup white sugar; 2 eggs; 1 (15 ounce) can pumpkin puree; 0.5 teaspoon ground cinnamon; 0.125 teaspoon Chinese five-spice powder; 0.125 teaspoon ground allspice; 2 cups all-purpose flour; 1 teaspoon salt; 1 teaspoon baking powder; 1 teaspoon baking soda; 0.75 cup chopped toasted walnuts", "directions": "Preheat the oven to 325 degrees F (165 degrees C). Spray a 9x5-inch loaf pan with cooking spray. Mix butter and sugar in a large bowl until light and fluffy. Whisk in eggs one at a time until combined. Whisk in the pumpkin puree, cinnamon, Chinese five-spice powder, and allspice until combined. Stir flour, salt, baking powder, and baking soda into the pumpkin mixture and mix until just combined. Stir in chopped walnuts. Pour batter into the prepared loaf pan. Bake in the preheated oven until a toothpick inserted into the center comes out clean, about 1 hour.", "prep": "PT15M", "cook": "PT60M", "total": "PT75M", "servings": ["12"], "calories": "282 kcal", "carbohydrates_g": "37 g", "fat_g": "14 g", "protein_g": "5 g", "cuisine": "chinese"},
{"name": "The Greatest Apple Crisp", "url": "https://www.allrecipes.com/recipe/260271/the-greatest-apple-crisp/", "category": ["Dessert"], "author": "ChloeMo", "summary": "Apples, brown sugar, cinnamon, and oatmeal are combined to create this simple and quick apple crisp dessert that&#39;s sure to please a crowd.", "rating": "2", "rating_count": "1", "review_count": 0, "ingredients": "cooking spray; 1.5 cups all-purpose flour; 1.5 cups brown sugar; 1 cup oats; 0.75 cup butter, melted; 1 teaspoon ground cinnamon; 6 Honey Crisp apples - peeled, cored, and sliced; 0.5 cup brown sugar; 0.5 cup white sugar; 0.25 cup all-purpose flour; 1 teaspoon ground cinnamon; 0.25 cup butter", "directions": "Preheat oven to 350 degrees F (175 degrees C). Grease a 9x13-inch baking pan with cooking spray. Combine 1 1/2 cups flour, 1 1/2 cups brown sugar, oats, melted butter, and 1 teaspooon cinnamon in a bowl; mix until well combined. Spread 1/2 of the mixture evenly in the prepared baking pan. Mix together apples, 1/2 cup brown sugar, white sugar, 1/4 cup flour, and 1 teaspoon cinnamon in a bowl; spread in the baking pan and dot with butter. Cover with the remaining oat mixture. Bake in the preheated oven until golden and crispy, 75 to 80 minutes.", "prep": "PT15M", "cook": "PT75M", "total": "PT90M", "servings": ["10"], "calories": "509 kcal", "carbohydrates_g": "84 g", "fat_g": "19 g", "protein_g": "4 g", "cuisine": "Unknown"},
{"name": "Uova in Purgatorio (Eggs in Purgatory)", "url": "https://www.allrecipes.com/recipe/265087/uova-in-purgatorio-eggs-in-purgatory/", "category": ["Brunch", "Breakfast"], "author": "linacavezza", "summary": "Eggs in purgatory is a classic southern Italian dish of poached eggs cooked in a rich and flavorsome tomato sauce for a delicious breakfast or brunch.", "rating": "4.8", "rating_count": "5", "review_count": 0, "ingredients": "2 tablespoons extra-virgin olive oil; 1 clove garlic, crushed; 3 black Italian olives, pitted and chopped, or more to taste; 1 teaspoon capers; 1 anchovy fillet in oil, drained; 7 ounces passata (crushed tomatoes); 0.5 cup water; 1 sprig chopped fresh parsley; salt to taste; 2 eggs", "directions": "Heat oil in a skillet over low heat. Add garlic, olives, capers, and anchovy; cook for 1 to 2 minutes. Add tomato sauce and water, bring to a boil, and simmer until flavors combine, about 10 minutes. Add parsley and season with salt. Gently add eggs directly into tomato sauce without breaking the yolks. Cook until eggs are just cooked, 3 to 5 minutes.", "prep": "PT5M", "cook": "PT15M", "total": "PT20M", "servings": ["2"], "calories": "245 kcal", "carbohydrates_g": "10 g", "fat_g": "20 g", "protein_g": "9 g", "cuisine": "italian"},
{"name": "Grilled Salmon", "url": "https://www.allrecipes.com/recipe/12720/grilled-salmon-i/", "category": ["Dinner"], "author": "tinamenina", "summary": "Grilled salmon with a simple soy sauce and brown sugar marinade. The sweet-salty flavors in the marinade complement the rich salmon fillets perfectly.", "rating": "4.8", "rating_count": "5605", "review_count": 0, "ingredients": "1.5 pounds salmon fillets; lemon pepper to taste; garlic powder to taste; salt to taste; 0.33333334326744 cup soy sauce; 0.33333334326744 cup brown sugar; 0.33333334326744 cup water; 0.25 cup vegetable oil", "directions": "Gather all ingredients. Season salmon fillets with lemon pepper, garlic powder, and salt. Stir soy sauce, brown sugar, water, and vegetable oil together in a small bowl until sugar is dissolved. Place fish in a large resealable plastic bag; add soy sauce mixture, seal, and turn to coat. Refrigerate for at least 2 hours. Preheat an outdoor grill for medium heat and lightly oil the grate. Place salmon on the preheated grill, and discard marinade. Cook salmon until fish flakes easily with a fork, about 6 to 8 minutes per side. Serve and enjoy!", "prep": "PT10M", "cook": "PT15M", "total": "PT145M", "servings": ["6"], "calories": "318 kcal", "carbohydrates_g": "13 g", "fat_g": "20 g", "protein_g": "21 g", "cuisine": "Unknown"},
{"name": "The Best Steak Marinade", "url": "https://www.allrecipes.com/recipe/176770/the-best-steak-marinade/", "category": ["Ingredient"], "author": "SweetCravings", "summary": "This easy steak marinade is a blend of olive oil, soy sauce, balsamic, mustard, garlic, and Worcestershire sauce. It&#39;s great for any cut of beef.", "rating": "4.8", "rating_count": "894", "review_count": 0, "ingredients": "0.25 cup olive oil; 0.25 cup balsamic vinegar; 0.25 cup Worcestershire sauce; 0.25 cup soy sauce; 2 teaspoons Dijon mustard; 2 teaspoons minced garlic; 1 pinch salt and pepper to taste", "directions": "Mix olive oil, balsamic vinegar, Worcestershire sauce, soy sauce, Dijon mustard, and garlic in a small bowl. Season with salt and pepper.", "prep": "PT5M", "cook": "", "total": "PT5M", "servings": ["4"], "calories": "156 kcal", "carbohydrates_g": "8 g", "fat_g": "14 g", "protein_g": "1 g", "cuisine": "Unknown"},
{"name": "Chef John&#39;s Roast Christmas Goose", "url": "https://www.allrecipes.com/recipe/222340/chef-johns-roast-christmas-goose/", "category": ["Dinner"], "author": "John Mitzewich", "summary": "Delicious, simple roast goose with a balsamic blackberry red wine sauce: perfect for your holiday table!", "rating": "4.8", "rating_count": "8", "review_count": 0, "ingredients": "1 whole smoked goose; 3 cups water; 0.5 cup red wine; 1 whole star anise; 0.25 cup aged balsamic vinegar; 0.25 cup blackberry jam; 0.5 teaspoon ground black pepper; salt to taste; 2 tablespoons cold butter, cut into 1/2-inch cubes; salt and ground black pepper to taste", "directions": "Preheat oven to 350 degrees F (175 degrees C). Remove top wing flat section from each wing. Place goose, breast-side up, in a baking dish or roasting pan. Combine wing sections, water, wine, and star anise in a saucepan and bring to a simmer over medium-high heat. Reduce heat to low and simmer until meat falls off the bone, about 2 hours. Remove bones and star anise; discard. Roast goose in the preheated oven until completely heated through, about 1 1/4 hours. An instant-read thermometer inserted into the thickest part of the thigh, near the bone should read 150 degrees F (66 degrees C). Stir balsamic vinegar, blackberry jam, and black pepper into red wine mixture; bring to simmer over medium heat. Simmer until reduced by three quarters, about 15 minutes. Remove from heat. Whisk in cold butter until completely incorporated. Season with salt and pepper to taste. Brush melted goose fat from bottom of pan onto the goose breast. Drizzle with sauce and serve.", "prep": "PT10M", "cook": "PT210M", "total": "PT220M", "servings": ["8"], "calories": "1108 kcal", "carbohydrates_g": "9 g", "fat_g": "78 g", "protein_g": "86 g", "cuisine": "Unknown"},
{"name": "Smoked Corn on the Cob", "url": "https://www.allrecipes.com/recipe/266330/smoked-corn-on-the-cob/", "category": ["Dinner", "Appetizer"], "author": "Elizabeth", "summary": "Smoked corn on the cob has a delicious flavor and in this recipe, the corn is brushed with a smoky lime butter. Perfect for your next BBQ party!", "rating": "5", "rating_count": "5", "review_count": 0, "ingredients": "4 ears corn on the cob, silks removed; mesquite wood chips; 2 tablespoons butter, melted; 1 tablespoon chopped fresh cilantro; 1 lime, zested; 0.5 lime, juiced; 1 teaspoon smoked paprika; salt and ground black pepper to taste", "directions": "Gather the ingredients. Place corn back in their husks in a large pot of water and soak for 2 hours. Soak wood chips in another container of water for about 30 minutes. Preheat a smoker to 250 degrees F (120 degrees C). Place corn, unstacked, onto wire racks. Place the racks into the smoker. Add wood chips according to the manufacturer&#39;s directions. Smoke until corn reaches your desired level of tenderness, 60 to 75 minutes. Combine butter, cilantro, lime zest, lime juice, and paprika in a small bowl. Peel back the husks and brush corn with butter mixture. Season with salt and pepper.", "prep": "PT10M", "cook": "PT60M", "total": "PT190M", "servings": ["4"], "calories": "141 kcal", "carbohydrates_g": "21 g", "fat_g": "7 g", "protein_g": "3 g", "cuisine": "Unknown"},
{"name": "Grilled Swordfish", "url": "https://www.allrecipes.com/recipe/75115/grilled-swordfish/", "category": ["Dinner"], "author": "BKATBSC", "summary": "Grilled swordfish, that&#39;s marinated in teriyaki sauce and basted with butter as it cooks on the grill, is a fish dish the whole family can enjoy.", "rating": "4.6", "rating_count": "66", "review_count": 0, "ingredients": "4 (8 ounce) swordfish steaks; 0.5 cup teriyaki sauce; 2 tablespoons margarine, softened; 1 teaspoon garlic powder", "directions": "Gather all ingredients. Preheat an outdoor grill for medium heat and lightly oil the grate. Meanwhile, marinate swordfish in teriyaki sauce, 5 minutes per side. Grill swordfish, basting frequently with melted butter, until fish flakes easily with a fork, 5 to 6 minutes per side. Season with garlic powder and serve.", "prep": "PT5M", "cook": "PT10M", "total": "PT25M", "servings": ["4"], "calories": "350 kcal", "carbohydrates_g": "6 g", "fat_g": "14 g", "protein_g": "46 g", "cuisine": "Unknown"},
{"name": "Quick Whole Wheat Chapati", "url": "https://www.allrecipes.com/recipe/233531/quick-whole-wheat-chapati/", "category": "uncategorized", "author": "desertdweller", "summary": "Fresh whole wheat chapati is quick, easy, and delicious; perfect with butter, as an accompaniment, or as a wrap!", "rating": "4.8", "rating_count": "21", "review_count": 0, "ingredients": "2.5 cups whole wheat flour; 0.75 teaspoon salt; 1 cup water", "directions": "Mix flour and salt together in a bowl. Stir in water to form a soft dough. Turn dough out onto a lightly floured work surface and knead several times. Divide into 8 pieces and roll each into a ball. Roll each ball into a very thin round using a rolling pin. Heat a griddle over medium-high heat. Cook each dough round on griddle until dough bubbles and blisters appear, about 2 minutes. Flip and cook until lightly browned on the other side.", "prep": "PT10M", "cook": "PT10M", "total": "PT20M", "servings": ["8"], "calories": "127 kcal", "carbohydrates_g": "27 g", "fat_g": "1 g", "protein_g": "5 g", "cuisine": "Unknown"},
{"name": "Croque Madame", "url": "https://www.allrecipes.com/recipe/282251/croque-madame-sandwich/", "category": ["Lunch"], "author": "C R Henning", "summary": "The Croque Madame isn&#39;t just any old ham and cheese sandwich! The French classic includes Gruyere cheese and Black Forest ham and is topped with bechamel and a poached egg.", "rating": "4.8", "rating_count": "4", "review_count": 0, "ingredients": "4 tablespoons salted butter, softened, divided; 1.5 tablespoons all-purpose flour; 1 cup milk; 2 ounces shredded Gruy\u00e8re cheese; 0.25 teaspoon salt, or to taste; 0.25 teaspoon ground black pepper, or to taste; 0.125 teaspoon ground nutmeg; 4 slices white bread, lightly toasted; 2 teaspoons Dijon mustard; 2 thin slices Black Forest ham; 2 large eggs; 1 tablespoon water; 1 teaspoon chopped fresh dill, or to taste", "directions": "Set an oven rack about 6 inches from the heat source and preheat the oven&#39;s broiler. Melt 1 1/2 tablespoons butter in a saucepan over medium-low heat. Whisk in flour and stir until slightly brown, about 3 minutes. Whisk in milk; bring to a boil, stirring constantly. Once boiling, reduce heat immediately and simmer for 5 minutes. Add 1/2 of the Gruy\u00e8re cheese, salt, pepper, and nutmeg; heat until cheese is melted, about 2 minutes. Remove from the heat and set aside. Spread about 1 teaspoon butter on 2 pieces of bread. Spread 1 tablespoon cheese sauce on top and layer each with a ham slice. Spread 1 teaspoon butter on the remaining 2 pieces of bread, then spread Dijon mustard on top and sprinkle with remaining Gruy\u00e8re. Transfer all 4 pieces to a baking sheet. Broil in the preheated oven until cheese is almost melted, 2 to 3 minutes. Remove from the oven, place toast slices together to make 2 sandwiches and pour remaining cheese sauce on top of each sandwich. Return to the broiler until sauce starts to brown, about 2 minutes. While the sandwiches are broiling, heat remaining butter in a nonstick skillet over medium-high heat. Crack 2 eggs into the skillet, keeping them completely separate from one another. Season with salt and pepper. Add water, cover, and baste until whites are set but yolks are still runny, about 2 minutes. Top each sandwich with an egg and sprinkle with dill, if using. Serve immediately.", "prep": "PT15M", "cook": "PT25M", "total": "PT40M", "servings": ["2"], "calories": "639 kcal", "carbohydrates_g": "37 g", "fat_g": "43 g", "protein_g": "25 g", "cuisine": "french"},
{"name": "Best Vinegar Coleslaw", "url": "https://www.allrecipes.com/recipe/59318/amish-slaw/", "category": ["Side Dish"], "author": "Christina J", "summary": "This vinegar coleslaw recipe is made with an easy vinegar-based dressing instead of mayo for a tangy sweet side that&#39;s perfect for BBQs and picnics.", "rating": "4.8", "rating_count": "523", "review_count": 0, "ingredients": "1 medium head cabbage, cored and shredded; 1 medium onion, finely chopped; 1 cup white sugar; 1 cup vinegar; 0.75 cup vegetable oil; 1 teaspoon celery seed; 1 teaspoon salt; 1 teaspoon prepared mustard; 1/4 teaspoon black pepper", "directions": "Gather the ingredients. Toss cabbage and onion together in a large bowl; set aside. Combine sugar, vinegar, oil, celery seed, salt, mustard, and pepper in a small saucepan; bring to a boil and simmer, stirring frequently, until sugar is dissolved, about 3 minutes. Let mixture cool slightly, about 5 minutes, then pour over cabbage mixture; toss well to coat. Serve and enjoy!", "prep": "PT15M", "cook": "PT5M", "total": "PT20M", "servings": ["8"], "calories": "224 kcal", "carbohydrates_g": "35 g", "fat_g": "9 g", "protein_g": "2 g", "cuisine": "Unknown"},
{"name": "Watermelon Cucumber Salad", "url": "https://www.allrecipes.com/recipe/222728/refreshing-cucumber-watermelon-salad/", "category": ["Salad"], "author": "kateroo", "summary": "This watermelon cucumber salad with feta cheese, fresh mint, and red onion is easy to make and sure to be a refreshing hit at any summer gathering.", "rating": "4.8", "rating_count": "99", "review_count": 0, "ingredients": "1 small red onion, halved and sliced into thin half-moons; 2 tablespoons lime juice, or more to taste; 2 tablespoons extra-virgin olive oil; 1 seedless watermelon, cut into cubes; 3 baby cucumbers, seeded and cut into cubes; 1 cup crumbled feta cheese; 0.5 cup mint leaves, sliced thinly", "directions": "Mix red onion with lime juice in a bowl; set aside to marinate at least 10 minutes. Stir olive oil into mixture. Toss watermelon, baby cucumbers, and feta cheese together in a large bowl. Pour red onion mixture over watermelon mixture; toss to coat. Sprinkle mint over the salad; toss.", "prep": "PT15M", "cook": "", "total": "PT25M", "servings": ["10"], "calories": "203 kcal", "carbohydrates_g": "36 g", "fat_g": "7 g", "protein_g": "5 g", "cuisine": "Unknown"}]
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
