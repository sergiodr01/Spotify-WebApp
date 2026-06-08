import kagglehub
import shutil
import os

# Descarga el dataset
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")
print("Dataset descargado en:", path)

# Cópialo a tu carpeta data/raw
dest = "data/raw"
os.makedirs(dest, exist_ok=True)

for file in os.listdir(path):
    shutil.copy(os.path.join(path, file), dest)
    print(f"Copiado: {file}")

print("✅ Dataset listo en data/raw/")