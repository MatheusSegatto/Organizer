import os
import shutil

current_dir = os.getcwd()

for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass

        elif file_ext in ('.jpg', '.png', '.gif', '.mp3'):
            shutil.move(
            os.path.join(current_dir, f'{filename}{file_ext}'),
            os.path.join(current_dir, 'Midia', f'{filename}{file_ext}'))

        elif file_ext in ('.pdf', '.docx', '.ppt', '.txt','xls', 'xlsx', 'doc'):
            shutil.move(
            os.path.join(current_dir, f'{filename}{file_ext}'),
            os.path.join(current_dir, 'Documents', f'{filename}{file_ext}'))

        elif file_ext in ('.exe'):
            if filename not in ('Organizer'):
                shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Apps', f'{filename}{file_ext}'))

        elif file_ext in ('.zip', '.rar'):
            shutil.move(
            os.path.join(current_dir, f'{filename}{file_ext}'),
            os.path.join(current_dir, 'Zip', f'{filename}{file_ext}'))

        elif file_ext in ('.epub', '.mobi'):
            shutil.move(
            os.path.join(current_dir, f'{filename}{file_ext}'),
            os.path.join(current_dir, 'Books', f'{filename}{file_ext}'))

        else:
            shutil.move(
            os.path.join(current_dir, f'{filename}{file_ext}'),
            os.path.join(current_dir, 'Others', f'{filename}{file_ext}'))

    except (FileNotFoundError, PermissionError):
        pass