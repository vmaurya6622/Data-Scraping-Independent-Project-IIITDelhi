import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import logging
import json

DEBUG = False
FIELDS = [
    "name",
    "url",  # Added URL
    "category",
    "author",
    "summary",
    "rating",
    "rating_count",
    "review_count",
    "ingredients",
    "directions",
    "prep",
    "cook",
    "total",
    "servings",
    "yield",
    # Nutritional information
    "calories",
    "carbohydrates_g",
    "sugars_g",
    "fat_g",
    "saturated_fat_g",
    "cholesterol_mg",
    "protein_g",
    "dietary_fiber_g",
    "sodium_mg",
    "calories_from_fat",
    # Additional nutritional info - Metals
    "calcium_mg",
    "iron_mg",
    "magnesium_mg",
    "potassium_mg",
    "zinc_mg",
    "phosphorus_mg",
    # Additional nutritional info - Vitamins
    "vitamin_a_iu_IU",
    "niacin_equivalents_mg",
    "vitamin_b6_mg",
    "vitamin_c_mg",
    "folate_mcg",
    "thiamin_mg",
    "riboflavin_mg",
    "vitamin_e_iu_IU",
    "vitamin_k_mcg",
    "biotin_mcg",
    "vitamin_b12_mcg",
    # Additional nutritional info - Fats
    "mono_fat_g",
    "poly_fat_g",
    "trans_fatty_acid_g",
    "omega_3_fatty_acid_g",
    "omega_6_fatty_acid_g",
    # Added cuisine field
    "cuisine",  # This is the new field we are adding
]

# List of valid cuisines
cuisine_list = [
    "amish-and-mennonite", "argentinian", "australian-and-new-zealander", "austrian",
    "bangladeshi", "belgian", "brazilian", "cajun-and-creole", "canadian", "chilean", 
    "chinese", "colombian", "cuban", "danish", "dutch", "filipino", "finnish", "french", 
    "german", "greek", "indian", "indonesian", "israeli", "italian", "jamaican", "japanese", 
    "jewish", "korean", "lebanese", "malaysian", "norwegian", "pakistani", "persian", 
    "peruvian", "polish", "portuguese", "puerto-rican", "russian", "scandinavian", "soul-food", 
    "south-african", "southern", "spanish", "swedish", "swiss", "tex-mex", "thai", "turkish", 
    "vietnamese"
]

def getFloat(x, index=0):
    try:
        return float(re.findall(r"[-+]?[0-9]*\.?[0-9]+", x)[index])
    except:
        return 0.0


def getText(x, index=0, toLower=False):
    try:
        tmp = re.findall(r"[a-zA-Z_]+", x)[index]
        if toLower:
            return tmp.lower()
        return tmp

    except:
        return ""


def delSpaces(x):
    if x:
        return x.translate({ord(c): None for c in "\r\n\t"}).strip()
    return ""


class RecipeSpider(CrawlSpider):
    name = "recipespider"
    allowed_domains = ["allrecipes.com"]
    start_urls = [
        "https://www.allrecipes.com/recipes",
        "https://www.allrecipes.com/recipes/76/appetizers-and-snacks",
        "https://www.allrecipes.com/recipes/88/bbq-grilling",
        "https://www.allrecipes.com/recipes/156/bread",
        "https://www.allrecipes.com/recipes/78/breakfast-and-brunch",
        "https://www.allrecipes.com/recipes/79/desserts",
        "https://www.allrecipes.com/recipes/17562/dinner",
        "https://www.allrecipes.com/recipes/1642/everyday-cooking",
        "https://www.allrecipes.com/recipes/84/healthy-recipes",
        "https://www.allrecipes.com/recipes/85/holidays-and-events",
        "https://www.allrecipes.com/recipes/17567/ingredients",
        "https://www.allrecipes.com/recipes/17561/lunch",
        "https://www.allrecipes.com/recipes/80/main-dish",
        "https://www.allrecipes.com/recipes/92/meat-and-poultry",
        "https://www.allrecipes.com/recipes/95/pasta-and-noodles",
        "https://www.allrecipes.com/recipes/96/salad",
        "https://www.allrecipes.com/recipes/93/seafood",
        "https://www.allrecipes.com/recipes/81/side-dish",
        "https://www.allrecipes.com/recipes/94/soups-stews-and-chili",
        "https://www.allrecipes.com/recipes/236/us-recipes",
        "https://www.allrecipes.com/recipes/86/world-cuisine",
    ]

    custom_settings = {
        "FEED_EXPORT_FIELDS": FIELDS,
        "FEEDS": {
            "./export/recipes.jsonl": {
                "format": "jsonlines",
                "encoding": "utf8",
            },
            "./export/recipes.csv": {"format": "csv"},
        },
    }

    rule_next = Rule(
        LinkExtractor(restrict_css=".category-page-list-related-nav-next-button"),
        follow=True,
    )

    rule_recipe = Rule(
        LinkExtractor(allow=(r".+\/recipe\/.+\/$"), unique=True),
        callback="parse_item",
        follow=True,
    )
    rules = (rule_recipe, rule_next)

    def parse_item(self, response):
        json_ld = response.xpath('//script[@type="application/ld+json"]/text()').get()
        recipe = {}
        if json_ld:
            try:
                data = json.loads(json_ld)
                recipe = next((item for item in data if "@type" in item and "Recipe" in item["@type"]), {})
            except json.JSONDecodeError as e:
                self.logger.warning(f"JSON decoding error for {response.url}: {e}")
        else:
            self.logger.warning(f"No JSON-LD found for {response.url}")

        name = recipe.get("name") or response.css("h1.headline.heading-content::text").get()
        author = (
            recipe.get("author", [{}])[0].get("name") if "author" in recipe else
            response.css(".author-name-title .authorName::text").get()
        )
        description = recipe.get("description") or response.css("meta[name='description']::attr(content)").get()
        category = recipe.get("recipeCategory", "uncategorized")
        
        # Extract ingredients and description to match cuisine
        ingredients = recipe.get("recipeIngredient") or response.css(".ingredients-item-name::text").getall()
        description_text = delSpaces(description or "")
        
        # Priority: check URL for cuisine match
        cuisine = "Unknown"
        for c in cuisine_list:
            if c in response.url.lower():
                cuisine = c
                break
        # If no cuisine found in the URL, check the ingredients or description
        if cuisine == "Unknown":
            for c in cuisine_list:
                if c in " ".join(ingredients).lower() or c in description_text.lower():
                    cuisine = c
                    break
        # Check the directions for cuisine match
        directions = [
        step.get("text") for step in recipe.get("recipeInstructions", [])
        if isinstance(step, dict)
    ] or response.css(".instructions-section-item p::text").getall()

        if cuisine == "Unknown":
            directions_text = " ".join(directions).lower() if directions else ""
            for c in cuisine_list:
                if c in directions_text:
                    cuisine = c
                    break


        # Log if cuisine is found
        self.logger.debug(f"Cuisine found: {cuisine}")

        nutrition = recipe.get("nutrition", {})
        calories = nutrition.get("calories")
        carbohydrates_g = nutrition.get("carbohydrateContent")
        protein_g = nutrition.get("proteinContent")
        fat_g = nutrition.get("fatContent")

        directions = [
            step.get("text") for step in recipe.get("recipeInstructions", [])
            if isinstance(step, dict)
        ] or response.css(".instructions-section-item p::text").getall()

        aggregate_rating = recipe.get("aggregateRating", {})
        rating = aggregate_rating.get("ratingValue")
        rating_count = aggregate_rating.get("ratingCount")

        prep = response.css(".prep-time span::text").get() or recipe.get("prepTime", "")
        cook = response.css(".cook-time span::text").get() or recipe.get("cookTime", "")
        total = response.css(".total-time span::text").get() or recipe.get("totalTime", "")
        servings = response.css(".recipe-servings span::text").get() or recipe.get("recipeYield", "")

        # Data for CSV export
        data = {
            "name": name,
            "url": response.url,
            "category": category,
            "author": author,
            "summary": description,
            "rating": rating,
            "rating_count": rating_count,
            "review_count": response.css(".review-headline-count::text").get() or 0,
            "ingredients": "; ".join(ingredients),
            "directions": " ".join(directions),
            "prep": prep,
            "cook": cook,
            "total": total,
            "servings": servings,
            "calories": calories,
            "carbohydrates_g": carbohydrates_g,
            "protein_g": protein_g,
            "fat_g": fat_g,
            "cuisine": cuisine,  # Added cuisine field to data
        }

        # Log the data for debugging
        self.logger.debug(f"Data being scraped: {json.dumps(data, indent=4)}")

        if not data["name"]:
            self.logger.warning(f"Missing recipe name for {response.url}")

        yield data
