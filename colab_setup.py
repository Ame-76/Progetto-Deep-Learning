# Codice da aggiungere all'inizio del notebook 04 in Google Colab

# 1. Monta Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Clona o sincronizza il repository
import os
import shutil

# Naviga nella directory di Drive
os.chdir('/content/drive/MyDrive')

# Se il progetto non esiste, clonalo
if not os.path.exists('Progetto-Deep-Learning'):
    # Clona da GitHub
    !git clone https://github.com/Ame-76/Progetto-Deep-Learning.git
else:
    # Aggiorna il progetto esistente
    os.chdir('Progetto-Deep-Learning')
    !git pull origin master

# Naviga nella directory del progetto
os.chdir('/content/drive/MyDrive/Progetto-Deep-Learning')

# 3. Installa le dipendenze
!pip install -r requirements.txt

# 4. Configura i path per il salvataggio
import sys
sys.path.append('/content/drive/MyDrive/Progetto-Deep-Learning/src')

# Assicurati che la directory models esista
os.makedirs('/content/drive/MyDrive/Progetto-Deep-Learning/models', exist_ok=True)
