from app import app
from models import db, FantasyShop


with app.app_context():
    FantasyShop.query.delete()

    fantasy_shops = []
    fs1 = FantasyShop(name="Motion Potion", category="Potion Shop", location="WaterDeep",description="cute little potion shop", in_use=True)

    fantasy_shops.append(fs1)
    
    fs2 = FantasyShop(name="Steel & Deal", category="Smithy", location="Baldur's gate",description="Cheap smith shop, decent work", in_use=True)

    fantasy_shops.append(fs2)

    db.session.add_all(fantasy_shops)
    db.session.commit()
   