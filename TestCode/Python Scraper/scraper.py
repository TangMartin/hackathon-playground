from recipe_scrapers import scrape_me
import json

#sample code to learn
"""
recipe = {
    
    "example": {
        "title": scraper.title(),
    },
    "recipe2": {
        "title": "carrots",
    }
}
json.dump(recipe, outfile, indent = 6)
recipe.update({'recipe3': {'title': 23, 'shirt': 34}})
"""

# json file where the output will be sorted
outfile = open("/Users/martintang/Desktop/testcode/Python Scraper/scraper.json", "w")

# array of urls of recipes
urls = ["https://tasty.co/recipe/one-pot-garlic-parmesan-pasta"
        ]

# dictionary of recipe
recipe = {
    "layout": {
        "recipename": "recipename",
        "totaltime": "totaltime",
        "ingredients": "ingredients",
        "instructions": "instructions",
        "nutrients": "nutrients",
    },
}

for x in urls:
    scraper = scrape_me(x)
    recipe.update({scraper.title(): {'recipename': scraper.title(), 'totaltime': scraper.total_time(), 'ingredients': scraper.ingredients(), "instructions": scraper.instructions(), "nutrients": scraper.nutrients()}})

json.dump(recipe, outfile, indent = 6)

outfile.close()
