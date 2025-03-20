import random

data = {
    "person1": {"name": "Cristiano Ronaldo", "instagram_followers": 600000000, "description": "Football superstar", "country": "Portugal"},
    "person2": {"name": "Kylie Jenner", "instagram_followers": 400000000, "description": "Entrepreneur and reality TV star", "country": "USA"},
    "person3": {"name": "Lionel Messi", "instagram_followers": 500000000, "description": "World-renowned footballer", "country": "Argentina"},
    "person4": {"name": "Dwayne 'The Rock' Johnson", "instagram_followers": 390000000, "description": "Hollywood actor and former wrestler", "country": "USA"},
    "person5": {"name": "Selena Gomez", "instagram_followers": 430000000, "description": "Singer and actress", "country": "USA"},
    "person6": {"name": "Kim Kardashian", "instagram_followers": 360000000, "description": "Reality TV star and businesswoman", "country": "USA"},
    "person7": {"name": "Beyoncé", "instagram_followers": 320000000, "description": "Music icon", "country": "USA"},
    "person8": {"name": "Justin Bieber", "instagram_followers": 290000000, "description": "Pop singer", "country": "Canada"},
    "person9": {"name": "Taylor Swift", "instagram_followers": 270000000, "description": "Singer-songwriter", "country": "USA"},
    "person10": {"name": "Elon Musk", "instagram_followers": 180000000, "description": "Tech billionaire", "country": "USA"},
    "person11": {"name": "Ariana Grande", "instagram_followers": 300000000, "description": "Pop singer and actress", "country": "USA"},
    "person12": {"name": "Billie Eilish", "instagram_followers": 110000000, "description": "Grammy-winning singer", "country": "USA"},
    "person13": {"name": "Drake", "instagram_followers": 140000000, "description": "Rapper and singer", "country": "Canada"},
    "person14": {"name": "Zendaya", "instagram_followers": 180000000, "description": "Actress and fashion icon", "country": "USA"},
    "person15": {"name": "Virat Kohli", "instagram_followers": 260000000, "description": "Cricket legend", "country": "India"},
}

def get_random_person(exclude=None):
    """Returns a random person from data, excluding a specified person."""
    persons = list(data.values())  # Get all persons as a list
    if exclude:
        persons = [p for p in persons if p["name"] != exclude]  # Remove excluded person
    return random.choice(persons)

def game():
    print("""
        __        ___  __      __   __           __        ___  __  
  |__| | / _` |__| |__  |__)    /  \ |__)    |    /  \ |  | |__  |__) 
  |  | | \__> |  | |___ |  \    \__/ |  \    |___ \__/ |/\| |___ |  \                                                                
    """)

    score = 0
    person_A = get_random_person()  # Select first random person

    while True:
        person_B = get_random_person(exclude=person_A["name"])  # Ensure B is different

        print(f"\nCompare A: {person_A['name']}, {person_A['description']}, {person_A['country']}")
        print("     VS    ")
        print(f"Compare B: {person_B['name']}, {person_B['description']}, {person_B['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if (guess == "A" and person_A["instagram_followers"] > person_B["instagram_followers"]) or \
           (guess == "B" and person_B["instagram_followers"] > person_A["instagram_followers"]):
            score += 1
            print(f"That's right! Current score: {score}")
            person_A = person_B  # B becomes the new A
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break  # End game if wrong

game()
