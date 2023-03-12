## Project Description
I am Sujata Sahu and in this project my main aim was to extract the incident data from the  Norman, Oklahoma police department , creata a SQLite database, insert the data in the database and print the nature and the number of times it appeared.
## Packages used
To do the above I first imported the following packages :
1. urllib
2. tempfile
3. re
4. sqlite3
5. PyPDF4
## process to install package
The installation of above packages was done using pip install. Below is the complete explanation of installation process:

1. Having Python and pip installed on your system prior is required.
2. Create a new directory for the project using the mkdir command and change to that directory using cd.
3. Change to the project0 directory using cd.
4. Install the pipenv package by running the command pip install pipenv.
5. Install all the dependencies listed in the requirements.txt file by running the command pipenv install -r requirements.txt.
6. To run the  tests for the project, use the command pipenv run python -m pytest.
7. To run the main.py file, use the command pipenv run python project0/main.py --incidents <url>, where <url> is the URL of the PDF file    containing the incident data.
 
## Functions and its definations

The following are the 3 functions I created to carry out the required operation:
1. fetchincidents()
2. extractIncidents()
3. create_populateDatabase()

### fetchincident()- 
This function will get the data from the website and at the end it will return the data.
<img width="701" alt="image" src="https://user-images.githubusercontent.com/120352925/223577833-305c7a99-648e-4159-9aa9-928bd0ec4db7.png">

### extractIncident() - 
This function, extractIncidents, takes in incident_data, which is a PDF file containing incident reports, as its argument. The function attempts to read the PDF file, extract the text from each page, and parse the incident reports from the text. If successful, the function returns a list of incidents, where each incident is a list containing 5 elements: the incident number, the date and time of the incident, the location of the incident, a brief description of the incident, and the status of the incident.If there is an error in the process, the function prints an error message indicating that there was an "error in extracting incidents from the PDF file".The function uses the tempfile module to create a temporary file to store the incident data, and the PyPDF2 module to read the PDF file and extract its content. It also uses regular expressions (re.split()) to split the text into incident reports based on their formatting. Overall, this function can be used to automate the process of extracting incident reports from a PDF file and processing them for further analysis or storage.
<img width="686" alt="image" src="https://user-images.githubusercontent.com/120352925/223578052-2b6fe9cd-f036-43aa-a8ad-24615b00d908.png">

### create_populateDatabase()-
Instead of writing the separate function for each task (creating a database, inserting data into the data base, using SQL query to get the required analysed data)  i wrote a single function which performs all the three tasks and at the end gives me the desired output.It takes in a list of incidents as its argument and performs several tasks related to creating and populating a SQLite database with the incident data. First, the function connects to the SQLite database named   'incident.db' using the sqlite3 module. It then creates a table named 'incidents' with five columns: date_time, incident_number, location, nature, and ori. Next, the function populates the 'incidents' table with the data from the incidents list using the executemany method of the SQLite cursor object. Each incident in the list is a tuple containing the values for the five columns in the 'incidents' table. After populating the table, the function executes a SQL query to count the number of incidents by their nature, and orders the results by the count in descending order and then by the nature in ascending order. The results are then printed to the console. Finally, the function closes the connection to the database.
Overall, this function can be used to automate the process of creating and populating a SQLite database with incident data,    and then analyzing the data to provide insights about the nature of the incidents.
<img width="704" alt="image" src="https://user-images.githubusercontent.com/120352925/223578141-b60bd8b3-eef9-45da-8e3f-a8a15d69959d.png">
 
## main.py
All the above functions are called in main.py file and a url is passed as an argument
 <img width="687" alt="image" src="https://user-images.githubusercontent.com/120352925/223579786-3362581f-ac78-45b6-973d-f3f32fa197e3.png">

## Test
Test files are created to test the function since I have three functions so three test files were created in order to test them and the package used was pytest
### To test the fetchincident():
 <img width="689" alt="image" src="https://user-images.githubusercontent.com/120352925/223580268-ffb44bb9-9bb8-49fc-ae21-57f594d8382c.png">
 
### To test the extractIncidents():
 <img width="694" alt="image" src="https://user-images.githubusercontent.com/120352925/223580344-0cc8aaa6-ae1d-44b3-9d63-5aa192f4eed3.png">
 
### To test the create_populateDatabase():
 <img width="672" alt="image" src="https://user-images.githubusercontent.com/120352925/223580723-a508eb74-179f-45b5-9c42-e4e9619e934e.png">
 
## Bugs faced :
I wrote the program where I created the table and for the first time it gave me the correct value but when I was running again and again the value of nature appeared was getting doubled and then i added drop_table='''drop TABLE incidents'''  to my code which solved the issue. Now my functions works perfectly.
## Video my code executing, using the pipenv run command and pipenv run python -m pytest is below

https://user-images.githubusercontent.com/120352925/223597034-cb5bf5a8-7579-493c-92dc-a91b220385d3.mp4

