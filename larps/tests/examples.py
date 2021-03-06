
# Basic characters and players examples

example_groups = [ "Scientists", "Doctors", "Mecanics" ]

example_characters = [ "Marie Curie", "Ada Lovelace", "Mary Jane Watson", "May Parker", "Peter Parker", "Leopold Fitz" ]
example_characters1 = [ "Marie Curie", "Ada Lovelace", "Mary Jane Watson", "May Parker" ]
example_characters2 = [ "Peter Parker", "Leopold Fitz", "Tony Stark", "Gemma Simmons" ]

example_players_complete = [
    { "username": "Ana_Garcia", "first_name": "Ana", "last_name": "Garcia", "gender":"female", "chest":90, "waist":75, "diet":"none" },
    { "username": "Pepa_Perez", "first_name": "Pepa", "last_name": "Perez", "gender":"female", "chest":95, "waist":78, "diet":"none" },
    { "username": "Manolo_Garcia", "first_name": "Manolo", "last_name": "Garcia", "gender":"male", "chest":100, "waist":90, "diet":"Vegetarian" },
    { "username": "Paco_Garcia", "first_name": "Paco", "last_name": "Garcia", "gender":"male", "chest":102, "waist":86, "diet":"none" },
]

example_players_incomplete = [
    { "username": "Maria_Gonzalez", "first_name": "Maria", "last_name": "Gonzalez", "gender":"", "chest":0, "waist":0, "diet":"" },
    { "username": "Andrea_Hernandez", "first_name": "Andrea", "last_name": "Hernandez", "gender":"", "chest":0, "waist":0, "diet":"" },
]


# Examples for testing food and diets funtionality

example_diets = [ "Vegetarian", "Vegan", "none" ]

example_players_with_diets1 = [
    { "username": "Ana_Garcia", "first_name": "Ana", "last_name": "Garcia", "gender":"female", "chest":90, "waist":75, "diet":"none", "comments":"" },
    { "username": "Pepa_Perez", "first_name": "Pepa", "last_name": "Perez", "gender":"female", "chest":95, "waist":78, "diet":"Vegan", "comments":"" },
    { "username": "Manolo_Garcia", "first_name": "Manolo", "last_name": "Garcia", "gender":"male", "chest":100, "waist":90, "diet":"none", "comments":"" },
    { "username": "Paco_Garcia", "first_name": "Paco", "last_name": "Garcia", "gender":"male", "chest":102, "waist":86, "diet":"Vegan", "comments":"" },
]

example_players_with_diets2 = [
    { "username": "Maria_Gonzalez", "first_name": "Maria", "last_name": "Gonzalez", "gender":"female", "chest":0, "waist":0, "diet":"Vegetarian", "comments":"" },
    { "username": "Andrea_Hernandez", "first_name": "Andrea", "last_name": "Hernandez", "gender":"female", "chest":0, "waist":0, "diet":"none", "comments":"" },
    { "username": "Juan_Perez", "first_name": "Juan", "last_name": "Perez", "gender":"male", "chest":100, "waist":90, "diet":"none", "comments":"" },
    { "username": "Carlos_Hernandez", "first_name": "Carlos", "last_name": "Hernandez", "gender":"male", "chest":102, "waist":86, "diet":"Vegan", "comments":"" },
]

example_diets_counts = [
    { "none" : 2, "Vegetarian": 1, "Vegan": 1 },
    { "none" : 2, "Vegetarian": 0, "Vegan": 2 },
]

example_player_food_info = [
    { "diet":"Vegetarian", "comments":"", 'allergies': "", 'food_allergies' : "", 'food_intolerances': "" },
    { "diet":"none", "comments":"", 'allergies': "polen", 'food_allergies' : "", 'food_intolerances': "lactose" },
    { "diet":"none", "comments":"", 'allergies': "", 'food_allergies' : "peanuts", 'food_intolerances': "" },
    { "diet":"Vegan", "comments":"", 'allergies': "", 'food_allergies' : "pineaple", 'food_intolerances': "lactose" },
]

example_comments = [
    "",
    "intolerant to: lactose",
    "allergies: peanuts",
    "allergies: pineaple, intolerant to: lactose"
]

# BOOKINGS examples

example_bookings = [
    { "weapon": False, "bus": None, "accomodation": None, "sleeping_bag": False },
    { "weapon": False, "bus": "Madrid", "accomodation": "on site", "sleeping_bag": True },
]

# UNIFORMS AND SIZES EXAMPLES

example_sizes = [
         {  "gender":"female", "american_size":"S", "european_size":"38", "chest_min":"86", "chest_max":"90", "waist_min":"70", "waist_max":"74" },
         {  "gender":"female", "american_size":"M", "european_size":"40", "chest_min":"90", "chest_max":"94", "waist_min":"74", "waist_max":"78" },
         {  "gender":"female", "american_size":"M", "european_size":"42", "chest_min":"94", "chest_max":"98", "waist_min":"78", "waist_max":"82" },
         {  "gender":"male", "american_size":"M", "european_size":"46", "chest_min":"90", "chest_max":"94", "waist_min":"78", "waist_max":"82" },
         {  "gender":"male", "american_size":"M", "european_size":"48", "chest_min":"94", "chest_max":"98", "waist_min":"82", "waist_max":"86" },
         {  "gender":"male", "american_size":"L", "european_size":"50", "chest_min":"98", "chest_max":"102", "waist_min":"86", "waist_max":"90" },
     ]

example_sizes_info = [
    "female. S/38 chest(86,90) waist(70,74)",
    "female. M/40 chest(90,94) waist(74,78)",
    "female. M/42 chest(94,98) waist(78,82)",
    "male. M/46 chest(90,94) waist(78,82)",
    "male. M/48 chest(94,98) waist(82,86)",
    "male. L/50 chest(98,102) waist(86,90)"
]

correct_size_examples = [
    ["Pilots (black, red)","Pilots","black, red","women","S",38,86,90,70,74],
    ["Pilots (black, red)","Pilots","black, red","women","M",40,90,94,74,78],
    ["Pilots (black, red)","Pilots","black, red","women","M",42,94,98,78,82],
    ["Pilots (black, red)","Pilots","black, red","women","L",44,98,102,82,86],
    ["Pilots (black, red)","Pilots","black, red","women","L",46,102,107,86,91],
    ["Pilots (black, red)","Pilots","black, red","women","XL",48,107,113,91,97]
]
incorrect_size_examples = [
    ["","Pilots","","women","L",44,98,102,82,86],
    ["","","","women","L",44,98,102,82,86],
    [""," ","","women","L",44,98,102,82,86],
    ["","Pilots","","","L",44,98,102,82,86],
    ["","Pilots","","women","",44,98,102,82,86],
    ["","Pilots","","women","L","",98,102,82,86],
    ["","Pilots","","women","","",98,102,82,86],
    ["","Pilots","","women","L",44,"","","",""]
]

empty_size_info = { "gender":"", "american_size":"", "european_size":"", "chest_min":"", "chest_max":"", "waist_min":"", "waist_max" :"" }


# Datasets for CSV csv_importer

empty_data_set = ""

uniforms_data_set = '''name,group,color,gender,american_size,european_size,chest_min,chest_max,waist_min,waist_max
Pilots (black red),Pilots,black red,women,S,38,86,90,70,74
Pilots (black red),Pilots,black red,women,M,40,90,94,74,78'''

characters_data_set = '''run,player,character,group,planet,rank
1,Werner Mikolasch,Ono,agriculture teacher,Rhea,lieutenant
2,Fabio,Fuertes,artist teacher,Kepler,lieutenant'''

incorrect_data_set = '''character,group,planet,rank
1,Werner Mikolasch,Ono,agriculture teacher,Rhea,lieutenant
2,Fabio,Fuertes,artist teacher,Kepler,lieutenant'''
