from datetime import datetime

now = datetime.now()

def photo_directory_path(instance, filename):
    """
    file will be saved to MEDIA_ROOT/photos/current.year/current.month/current.day
    :param instance:
    :param filename:
    :return:
    """
    return f'photos/{now.year}/{now.month}/{now.date().day}/{filename}'

