from app import app
from db import db
from models import FantasyShop, InventoryItem


with app.app_context():
    FantasyShop.query.delete()
    InventoryItem.query.delete()

    fantasy_shops = []
    fs1 = FantasyShop(name="Motion Potion", category="Potion Shop", location="WaterDeep",description="cute little potion shop", in_use=True)

    fantasy_shops.append(fs1)
    
    fs2 = FantasyShop(name="Steel & Deal", category="Smithy", location="Baldur's gate",description="Cheap smith shop, decent work", in_use=True)
    
    fantasy_shops.append(fs2)

    fs3 = FantasyShop(name="Travelers Pack pavilion", category="General Store", location="Good Mead",description="Largest General Store in Icewind Dale", in_use=False)

    fantasy_shops.append(fs3)

    fs4 = FantasyShop(name="ArcanumRus", category="Magic item store", location="Sharn city of towers",description="Department store for Enchantments, Potion, Spell Components and more!", in_use=False)

    fantasy_shops.append(fs4)

    db.session.add_all(fantasy_shops)
    db.session.commit()

    fs1_inventory = [InventoryItem(name="Potion of Healing", category="Potion", description="Healing potion",cost=10.00, fantasy_shop_id=fs1.id), InventoryItem(name="Potion of Flying", category="Potion", description="Potion that gives you the ability to fly",cost=10.00, fantasy_shop_id=fs1.id)]
    db.session.add_all(fs1_inventory)
    db.session.commit()

    

    fs4_inventory = [InventoryItem(name="Slippers of Spider Climb", category="Potion", description="While you wear these light shoes, you can move up, down, and across vertical surfaces and upside down along ceilings, while leaving your hands free",cost=1000.00, fantasy_shop_id=fs4.id)]
    db.session.add_all(fs4_inventory)
    db.session.commit()
   
