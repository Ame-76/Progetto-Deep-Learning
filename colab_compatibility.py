# Celle da aggiungere all'inizio del notebook 04-cnn-from-scratch.ipynb

# CELLA 1: Rilevamento ambiente e setup path
import os
import sys
from pathlib import Path

# Rileva se siamo su Google Colab
try:
    import google.colab  # Only available in Colab
    IN_COLAB = True
    print("🔍 Ambiente rilevato: Google Colab")
except ImportError:
    IN_COLAB = False
    print("🔍 Ambiente rilevato: Locale")

# Configura i path in base all'ambiente
if IN_COLAB:
    # Setup per Google Colab
    from google.colab import drive
    drive.mount('/content/drive')
    
    # Path del progetto su Drive
    PROJECT_PATH = '/content/drive/MyDrive/Progetto-Deep-Learning'
    
    # Clona il progetto se non esiste
    if not os.path.exists(PROJECT_PATH):
        print("📥 Clonazione repository da GitHub...")
        !git clone https://github.com/Ame-76/Progetto-Deep-Learning.git /content/drive/MyDrive/Progetto-Deep-Learning
        print("✅ Repository clonato!")
    else:
        print("✅ Progetto trovato su Drive")
    
    # Cambia directory di lavoro
    os.chdir(PROJECT_PATH)
    
    # Aggiungi al path Python
    sys.path.append(f"{PROJECT_PATH}/src")
    
    # Installa dipendenze
    print("📦 Installazione dipendenze...")
    !pip install -q -r requirements.txt
    
else:
    # Setup per ambiente locale
    PROJECT_PATH = Path.cwd().parent  # Assumendo di essere in notebooks/
    sys.path.append(str(PROJECT_PATH / "src"))

print(f"📁 Directory progetto: {PROJECT_PATH}")

# Path comuni per entrambi gli ambienti
MODELS_DIR = f"{PROJECT_PATH}/models"
DATA_DIR = f"{PROJECT_PATH}/data"

# Crea le directory necessarie
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(f"{DATA_DIR}/processed", exist_ok=True)
