from ..models.file import File

def upload_file(project, file):
    new_file = File.objects.create(project=project, file=file)
    return new_file

def delete_file(file_id):
    file = File.objects.get(id=file_id)
    file.delete()