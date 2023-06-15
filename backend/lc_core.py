ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}


def allowed_file(filename: str) -> bool:

    """Checks if the file being uploaded has the allowed format"""
    return'.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
