from datetime import datetime
from pathlib import Path
import zipfile

def Ada_isnotproud():
    print ("Har ikke brugt en Def så effektivt (mangel på kreativitet)")


OBJECT_TO_BACKUP = input("stien til din data? :O\n")  #bruger input til den fulde sti

BACKUP_DIRECTORY = input("Destination?????\n")  #hvor vil vi gemme Dataen
MAX_BACKUP_AMOUNT = 4  # Hvor mange backups kan vi lave



object_to_backup_path = Path(OBJECT_TO_BACKUP)
backup_directory_path = Path(BACKUP_DIRECTORY)
assert object_to_backup_path.exists()  # tjekker om vores objekter findes

# Tjekker at mappen findes, ellers så laver den en ny
backup_directory_path.mkdir(parents=True, exist_ok=True)

#Tjekker efter hvor mange backups der er lavet i forevejen
existing_backups = []
for x in backup_directory_path.iterdir():
    if x.is_file() and x.suffix == '.zip' and x.name.startswith('NSA-'):
        existing_backups.append(x)


#Laver en zipfil, med dato som navn
backup_file_name = f'NSA-{datetime.now().strftime("%d-%m-%Y")}.zip'
zip_file = zipfile.ZipFile(str(backup_directory_path / backup_file_name), mode='w')
if object_to_backup_path.is_file():
    # hvis det er en fil,skriv en fil
    zip_file.write(
        object_to_backup_path.absolute(),
        arcname=object_to_backup_path.name,
        compress_type=zipfile.ZIP_DEFLATED
    )
elif object_to_backup_path.is_dir():
    # hvis det er en mappe, skriv alle filerne
    for file in object_to_backup_path.glob('**/*'):
        if file.is_file():
            zip_file.write(
                file.absolute(),
                arcname=str(file.relative_to(object_to_backup_path)),
                compress_type=zipfile.ZIP_DEFLATED
            )
Ada_isnotproud()
# lukker og slukker
zip_file.close()