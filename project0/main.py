import argparse
import project0
#import PyPDF4

def main(url):
    # Fetch incidents data from the PDF file
    incidents_data = project0.fetchincidents(url)

    # Extract incidents from the PDF data
    incidents = project0.extractIncidents(incidents_data)

    # Create and populate the incidents table in the SQLite database
    project0.create_populateDatabase(incidents)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str,required=True,help="Incident summary url.")

    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)



