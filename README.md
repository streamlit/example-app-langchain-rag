
# LangChain and Streamlit RAG

## Demo App on Community Cloud

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://st-lc-rag.streamlit.app/)


## Quickstart

### Setup Python environment

The Python version used when this was developed was 3.10.13


```bash
python -mvenv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### Setup .env file with API tokens needed.

```
OPENAI_API_KEY="<Put your token here>"
HUGGINGFACEHUB_API_TOKEN="<Put your token here>"
```

### Setup Streamlit app secrets.

#### 1. Set up the .streamlit directory and secrets file.

```bash
mkdir .streamlit
touch .streamlit/secrets.toml
chmod 0600 .streamlit/secrets.toml
```

#### 2. Edit secrets.toml

**Either edit `secrets.toml` in you favorite editor.**

```toml
OPENAI_API_KEY="<Put your token here>"
HUGGINGFACEHUB_API_TOKEN="<Put your token here>"
```

**Or, you can just reuse .env contents from above.**

```bash
cat < .env >> .streamlit/secrets.toml 
```

### Verify Environment

1. Check that LangChain dependencies are working.

```bash
python basic_chain.py
```

2. Check that Streamlit and dependencies are working.

```bash
streamlit run streamlit_app.py
```


## Example Data

* The file `nutrients_csvfile.csv` is from the Kaggle Dataset [Nutritional Facts for most common foods](https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods/) 
shared under the [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/) license.
* The file `pg65250.txt` is in the public domain, and was retrieved from Project Gutenberg at [Recipes Used in the Cooking Schools, U. S. Army by United States. Army](https://www.gutenberg.org/ebooks/65250).
* The file `healthy_meal_10_tips.pdf` was published by thes USDA, Center for Nutrition Policy and Promotion and was retrieved from Wikimedia  Commons, and is in the public domain.
[See page for author, Public domain, via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Build_a_healthy_meal_10_tips_for_healthy_meals_(IA_CAT31299650).pdf).


## Example Queries for Streamlit App

### Example 1: Metabolic Rate ###

**Question:**
If I am an 195 lb male, what should my calorie intake be to lose 1 lb a week based on what you know about my basal metabolic rate?

**Answer:**
To calculate the calorie intake for a 195 lb male to lose 1 lb per week based on their basal metabolic rate, we can use the estimated BMR values provided in the context.

For a 190 lb male, the estimated BMR is around 2,280 calories per day. To lose 1 lb per week, a general rule of thumb is to create a calorie deficit of about 500 calories per day.

Therefore, to lose 1 lb per week, a 195 lb male should aim to consume around 1,780 calories per day (2,280 calories - 500 calories). This calorie intake, combined with regular physical activity, can help achieve a sustainable weight loss goal.

### Example 2: Recipes

***Question:**
How do I make salmon croquettes according to the recipes I provided you?

**Answer:**
To make salmon croquettes based on the recipes shared, you can follow these steps:

Ingredients:

- 4 cans of salmon
- 4 pounds of cold boiled potatoes
- 2 eggs
- Salt and pepper to taste
- Cracker dust for coating
- Oil for frying

Instructions:

1. Drain the canned salmon and remove any bones or skin.
2. In a large bowl, mash the salmon and boiled potatoes together.
3. Add the eggs, salt, and pepper to the mixture and combine well.
4. Shape the mixture into small cakes about 2 inches in diameter.
5. In a separate bowl, beat the remaining eggs with a little milk to create an egg batter.
6. Dip each salmon cake into the egg batter, then coat it with cracker dust.
7. Heat oil in a pan for frying.
8. Fry the salmon croquettes in the hot oil until they are golden brown on all sides.
9. Once cooked, remove them from the oil and place them on a paper towel to drain any excess oil.
10. Serve the salmon croquettes hot and enjoy!

I hope these instructions help you make delicious salmon croquettes! Let me know if you need any more assistance.