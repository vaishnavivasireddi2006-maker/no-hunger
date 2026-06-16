import os
from datetime import datetime, timedelta
from app import app, db
from models import User, Donation, PickupRequest, VolunteerAssignment

def seed_database():
    print("Initializing database...")
    db.drop_all()
    db.create_all()
    print("Database tables created.")

    # --- Seed Users ---
    print("Seeding users...")
    
    # 1. Admin (your account)
    admin = User(
        username="vaishu",
        email="vaishnavivasireddi@gmail.com",
        role="admin",
        phone="9704730368",
        address="vizag"
    )
    admin.set_password("vaishu@2006")
    db.session.add(admin)

    # 2. Donors
    donor1 = User(
        username="Green Sourdough Bakery",
        email="donor@foodrescue.org",
        role="donor",
        phone="555-0101",
        address="45 Baker Street, Wheatland"
    )
    donor1.set_password("password")
    db.session.add(donor1)

    donor2 = User(
        username="Royal Curry Palace",
        email="curry@foodrescue.org",
        role="donor",
        phone="555-0102",
        address="102 Spiceland Road"
    )
    donor2.set_password("password")
    db.session.add(donor2)

    # 3. NGO
    ngo1 = User(
        username="Hope Food Bank",
        email="ngo@foodrescue.org",
        role="ngo",
        phone="555-0201",
        address="77 Community Shelter Way"
    )
    ngo1.set_password("password")
    db.session.add(ngo1)

    # 4. Volunteer
    volunteer1 = User(
        username="Alex Rider",
        email="volunteer@foodrescue.org",
        role="volunteer",
        phone="555-0301",
        address="12 Courier Lanes, Sector 5"
    )
    volunteer1.set_password("password")
    db.session.add(volunteer1)

    db.session.commit()
    print("Users seeded successfully.")

    # --- Seed Donations, Pickup Requests and Assignments ---
    print("Seeding sample rescue workflow records...")

    now = datetime.utcnow()

    d1 = Donation(
        donor_id=donor1.id,
        food_item="Fresh Sourdough Loaves",
        food_type="Bakery",
        quantity="25 loaves",
        location="45 Baker Street, Wheatland",
        expiry_time=now + timedelta(hours=8),
        image_path=None,
        status="available"
    )
    db.session.add(d1)

    d2 = Donation(
        donor_id=donor2.id,
        food_item="Vegetable Biryani Portions",
        food_type="Cooked Meal",
        quantity="30 servings",
        location="102 Spiceland Road",
        expiry_time=now + timedelta(hours=3),
        image_path=None,
        status="requested"
    )
    db.session.add(d2)
    db.session.commit()

    r2 = PickupRequest(
        donation_id=d2.id,
        ngo_id=ngo1.id,
        status="pending",
        request_notes="Urgent request for dinner distribution tonight at 7 PM."
    )
    db.session.add(r2)

    d3 = Donation(
        donor_id=donor1.id,
        food_item="Organic Fruit Baskets",
        food_type="Fruits & Veg",
        quantity="15 kg",
        location="45 Baker Street, Wheatland",
        expiry_time=now + timedelta(hours=14),
        image_path=None,
        status="assigned"
    )
    db.session.add(d3)
    db.session.commit()

    r3 = PickupRequest(
        donation_id=d3.id,
        ngo_id=ngo1.id,
        status="accepted",
        request_notes="Need fruits for children breakfast program."
    )
    db.session.add(r3)
    db.session.commit()

    a3 = VolunteerAssignment(
        donation_id=d3.id,
        pickup_request_id=r3.id,
        volunteer_id=volunteer1.id,
        status="assigned",
        assigned_at=now - timedelta(minutes=30)
    )
    db.session.add(a3)

    d4 = Donation(
        donor_id=donor1.id,
        food_item="Vanilla Cupcakes & Muffins",
        food_type="Bakery",
        quantity="50 packs",
        location="45 Baker Street, Wheatland",
        expiry_time=now - timedelta(hours=2),
        image_path=None,
        status="completed"
    )
    db.session.add(d4)
    db.session.commit()

    r4 = PickupRequest(
        donation_id=d4.id,
        ngo_id=ngo1.id,
        status="completed",
        request_notes="For community bakery distributions."
    )
    db.session.add(r4)
    db.session.commit()

    a4 = VolunteerAssignment(
        donation_id=d4.id,
        pickup_request_id=r4.id,
        volunteer_id=volunteer1.id,
        status="delivered",
        assigned_at=now - timedelta(hours=2),
        delivered_at=now - timedelta(hours=1)
    )
    db.session.add(a4)

    db.session.commit()
    print("Database seeding completed.")

if __name__ == "__main__":
    with app.app_context():
        seed_database()