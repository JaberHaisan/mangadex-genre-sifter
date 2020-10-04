# mangadex_sifter.py - Sifts through a certain number of pages of a mangadex 
# genre and finds all the mangas that meets all of the criteria 
# saves the results in an excel file.
# Possible Criteria - Rating, Genres, Already in user's list, Nationality.

import threading
import sifter_functions
import settings

# Base link to sift through.
base_link = input("Link of genre to sift through: ")

base_link, genre = sifter_functions.format_link(base_link)	
	
print("Getting manga titles already in user's lists...")
already_checked = sifter_functions.checked_set(settings.user_id)

print("Getting mangas from given link...\n")
manga_elems = sifter_functions.all_manga_elem(base_link, settings.max_page)

mangas = {}

num = 1
def check_elems(manga_elems, dictionary=mangas):
	"""Checks each manga elem to see if it meets all of user's requirements.
	If it does then it is added to the given dictionary"""
	global num, already_checked
	
	for elem in manga_elems:
		manga_name = elem.getText()
		manga_link = 'https://mangadex.org/' + elem.get('href')
		
		# Removing mangas already checked by user.
		if manga_name in already_checked:
			verdict = "Rejected (Already in user's lists)"
		
		# Removing mangas from series excluded by user.
		elif any(name in manga_name for name in settings.not_needed):
			verdict = "Rejected (Series excluded by user)"
		
		else: 
			manga_obj = sifter_functions.Manga(manga_link)
			
			# Removing manga that have a rejected genre.
			if manga_obj.has_rejected_genre(settings.rejected_genres):
				verdict = "Rejected (Contains a rejected genre)"
				
			# Removing manga if it's from an excluded country.
			elif manga_obj.nationality() == settings.excluded_nationality:
				verdict = "Rejected (Is %s)" % settings.excluded_nationality

			# Checking if rating is high enough.
			elif manga_obj.is_rating_higher(settings.min_rating):
				verdict = 'Accepted (Meets all criteria)'
				
				dictionary[manga_name] = {}
				dictionary[manga_name]['rating'] = manga_obj.rating()
				dictionary[manga_name]['link'] = manga_link
				
			else:
				verdict = "Rejected (Low Rating)"
				
		print("%s) %s - %s" % (num, manga_name, verdict))
		num += 1
	
threads = []
threads_no = 15
segment_length = len(manga_elems) // threads_no

n = 0
for i in range(threads_no - 1):
	segment = manga_elems[n: n + segment_length]
	thread = threading.Thread(target=check_elems, args=(segment,))
	threads.append(thread)
	n += segment_length
else:
	segment = manga_elems[n:]
	thread = threading.Thread(target=check_elems, args=(segment,))
	threads.append(thread)
	
sifter_functions.start_and_join(threads)	

# Saving results in an excel document.
sifter_functions.save_mangas(mangas, genre)

print("\nTask Completed. Results have been stored in an excel file inside Output folder.")
