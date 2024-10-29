from configparser import ConfigParser

"""
    function to load database configuration taking filename and section as input parameters
    returns a dictionary
    currently supported databases are postgres
"""
def load_config(filename="database.ini",section="postgres"):
    parser = ConfigParser()
    parser.read(filename)
    dbconfig = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            dbconfig[param[0]]=param[1]
    else:
        raise Exception('Section {0} is not found in filename'.format(section,filename))
    return dbconfig