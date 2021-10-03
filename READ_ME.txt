**Instructions**
- Install the Requirements: pip install -r requirements.txt
- change directory: cd LibraryBookManagement_site
- Then, make database migrations: python manage.py makemigrations
- python manage.py migrate
- And finally, run the application: python manage.py runserver

**RESET DATABASE TABLES**
- open fileread.py
- under create_book function
	1.uncomment DELETE SQL TABLE lines and comment other lines.
	2.run : python fileread.py
	3.uncomment CREATE SQL TABLE lines and comment other lines.
	4.uncomment INSERT INTO SQL TABLE lines and comment other lines.
	5.run : python fileread.py
		python dbwrite.py

		