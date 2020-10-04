# settings.py - Set search criteria.
# Possible Criteria - Rating, Series, Genres, Already in user's list, Nationality.
# User's mangadex lists need to be public in order for the script to 
# get the mangas already in them.
# Excluded Tags and Nationality should have the same capitalization and
# spelling as their mangadex counterparts.
# If you don't want any tags or genres to be excluded, change not_needed
# and rejected genres to an empty list.
# Change excluded_nationality to an empty string if you don't want to exclude any
# nationality.

# User id. 
user_id = "532463"

# Minimum rating for manga to be accepted.
min_rating = 7.5

# Names of series that the user wants to exclude.
not_needed = ["Haikyuu!!", "Love Live!", "Touhou", "Kantai Collection", "Danganronpa",
"BanG Dream!", "Promo"]

# Genres that the user wants to exclude. 
rejected_genres = ["Yuri", "Yaoi", "Shoujo Ai", "Shounen Ai"]

# Nationality of manga that the user wants to exclude. 
excluded_nationality = "Korean"

# Number of pages to look through.
max_page = 10

