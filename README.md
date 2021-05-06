# mangadex-genre-sifter

***External modules required - bs4, openpyxl***

Note - This script was made for Mangadex v4. After Mangadex v5 comes out it will be updated.

This script searches through 10 (changeable in settings.py) pages in the given mangadex genre link and finds all manga that meet the user's criteria. Afterwards 
it stores the results in an excel document inside a new directory. 

Possible criteria include:
1. If the manga is already in the user's lists or not.
2. If it has any genre that the user wishes to exclude.
3. If the manga is of a particular nationality that the user does not want.
4. If the rating of the manga is high enough to meet the user's requirements.
5. If the series is from a particular series the user wishes to exclude. For e.g. "Touhou".

All the criteria are set from settings.py. Please change it to meet your requirements.

Please make sure to give the link in a format like these links: "https://mangadex.org/genre/5/comedy/0/2/" or "https://mangadex.org/genre/5/comedy"
You can get a complete link for a genre by going to the second (or higher) page of the genre. In the first page a redacted link like "https://mangadex.org/genre/5/"
is shown which cannot be used by the script to iterate through pages properly. The script takes the required part from the link using regex so
it will still start from the 1st page even if you give it the link for the 2nd page so no need to worry.

After running the script you can use excel_link_opener.py to open all the links in the excel document in your default browser (if you want).

Please make sure your manga lists are set to public if you want the script to get the titles already in it as otherwise it won't be able
to acquire them.
