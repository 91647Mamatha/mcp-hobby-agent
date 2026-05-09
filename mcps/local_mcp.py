def fetch_local_person(name):
    name = name.strip().lower()

    if name == "mamatha":
        return """
        [LinkedIn] Mamatha | MCA Student | Bengaluru
        Passionate learner currently pursuing MCA degree.

        [Resume] Mamatha
        Education: MCA (pursuing)
        Hobbies: Cooking new recipes, traveling to new places, watching web series and movies.

        [Instagram] @mamatha_vibes
        Posts: Trying new recipes at home  |
        | Exploring new places  | Currently watching: Mirzapur 
        | Road trips with friends 

        [Facebook] Mamatha
        Groups joined: Cooking Enthusiasts India,
        Travel Diaries India, Netflix & Series Fans
        Interests: Cooking, Traveling, Web Series, Movies

        [Portfolio] mamatha.me - About:
        When I am not studying, you will find me in the kitchen trying new recipes, planning my next trip, or binge watching
        a good series or movie.
        """

    return None