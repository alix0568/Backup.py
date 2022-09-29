backup script med dato og zip

moduler brugt:
from datetime import datetime = Til at navngive filer til dags dato
from pathlib import Path = til flytning af filer
import zipfile = til at lave zip filer

Scriptet flytter data fra A til B, og gemmer det i en Zip fil, med datoen som navn. 
Der kan maksimum være 4 backups på samme placering, tallet kan ændres i koden 

OBJECT_TO_BACKUP = input() #Source
BACKUP_DIRECTORY = input() #Destination

Hvis Destination ikke findes, laver scriptet det i form af "mkdir"

Min Def funktion er selvfølgelig kun til illustration, men kunne være brugt til min Source, dest
