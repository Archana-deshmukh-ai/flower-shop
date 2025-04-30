import sqlite3
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_shop.settings')
django.setup()

from flowers.models import Flower

# Paths to your databases
old_db_path = 'old_db.sqlite3'
old_conn = sqlite3.connect(old_db_path)
old_cursor = old_conn.cursor()

# Fetch all fields (including description and image)
old_cursor.execute("""
    SELECT name, description, price, image, is_bestseller, is_seasonal, is_new, is_budget 
    FROM shop_flower
""")
flowers = old_cursor.fetchall()

# Insert into new Django database
for flower in flowers:
    name, description, price, image, is_bestseller, is_seasonal, is_new, is_budget = flower

    # In case description or image is NULL in database
    description = description or ""
    image = image or ""

    Flower.objects.create(
        name=name,
        description=description,
        price=price,
        image=image,  # here, assuming image is a valid path relative to your media folder
        is_bestseller=is_bestseller,
        is_seasonal=is_seasonal,
        is_new=is_new,
        is_budget=is_budget
    )

old_conn.close()

print("Flowers copied successfully with description and image!")
