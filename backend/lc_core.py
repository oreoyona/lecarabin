from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}


def save_to_db(dbs: SQLAlchemy, data: Model):
    """Saves the model data to the databse"""
    
    dbs.session.add(data)
    
    dbs.session.commit()


def write_log(e: Exception):
    
    """ Writes an exception to the log file"""
    
    with open('./lc_contents/data_logs/', 'a') as log_file:
        
        log_file.write(f"An error occured: ")
        
        log_file.write(f"{e}")


def save_new_data(model: Model, dbs: SQLAlchemy):
    """ Saves the data from a form to the databse"""
    
    try:
        save_to_db(dbs, model)
    
    except Exception as e:
        
        write_log(e)


def delete_from_db(dbs: SQLAlchemy, model: Model):
    
    """ Deletes the model from the databse"""
    
    dbs.session.delete(model)
    
    dbs.session.commit()
    
    dbs.session.close()