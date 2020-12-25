import subprocess
import codecs
import csv

START_TR = "<tr>"
END_TR = "</tr>"

START_TD = "<td>"
END_TD = "</td>" 

START_TABLE = "<table border=1>"
END_TABLE = "</table>"

CSV = "csv"
PRN = "prn"

def get_prn_file_content(file_location):
    """This is a function for prn file type. This function
    parse the prn file and converted the file as a HTML file


    Parameters
    ----------
    file_location : str, required
        file_location represents the location of a prn file        

    Raise
    ------
    FileNotFoundError
        If prn file is not located in file_location folder
    """
    
    # Trying to detect the mime type of a file
    file_stream = ""
    file_encoding = subprocess.getoutput('file -b --mime-encoding %s' % file_location)
    try:
        file_stream = codecs.open(file_location, 'r', file_encoding)
    except FileNotFoundError as e:
        return "ERROR: File not found. Check the upload file location and filename"

    column_width = [16, 38, 46, 62, 75]
    content = START_TABLE 
    try:
        for id, line in enumerate(file_stream):
            (name, address, postcode, phone, credit_limit, birthdate) = (line[:16], line[16:38], line[38:47], line[47:61], line[61: 73], line[73:])
            columns = list([name, address, postcode, phone, credit_limit, birthdate])
            content += START_TR
            for column in columns:
                content += START_TD + column.strip(' ') + END_TD
            content += END_TR
        content += END_TABLE 
        return content
    except RuntimeError as e:
        return "ERROR: Invalid prn data format"

def get_csv_file_content(file_location):
    """This is a function for csv file type. This function
    parse the csv file and converted the file as a HTML file


    Parameters
    ----------
    file_location : str, required
        file_location represents the location of a csv file        

    Raise
    ------
    FileNotFoundError
        If csv file is not located in file_location folder
    """
    
    # Trying to detect the mime type of a file
    file_encoding = subprocess.getoutput('file -b --mime-encoding %s' % file_location)
    try:
        file_stream = codecs.open(file_location, 'r', file_encoding)
    except FileNotFoundError as e:
        return "ERROR: File not found. Check the upload file location and filename"

    content = START_TABLE
    csv_reader = csv.reader(file_stream, delimiter = ',', quotechar='"')
    for line in csv_reader:
        content += START_TR
        columns = line
        for column in columns:
            content += START_TD + column + END_TD
        content += END_TR
    content += END_TABLE
    file_stream.close()
    return content

def get_file_content(file_location, filename):
    if filename.rsplit('.', 1)[1].lower() == CSV: return get_csv_file_content(file_location)
    elif filename.rsplit('.', 1)[1].lower() == PRN: return get_prn_file_content(file_location)
 
