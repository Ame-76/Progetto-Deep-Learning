# ========================================
# TEMPLATE COLAB SEMPLIFICATO
# Copia e incolla questa cella all'inizio 
# del notebook su Google Colab
# ========================================

import os
import sys

# Verifica ambiente
try:
    import google.colab  # type: ignore
    print("🔍 Google Colab rilevato")
    IN_COLAB = True
except ImportError:
    print("🔍 Ambiente locale")
    IN_COLAB = False

if IN_COLAB:
    # Setup Colab SENZA Google Drive
    PROJECT_PATH = '/content/Progetto-Deep-Learning'
    
    # Clona repository
    if not os.path.exists(PROJECT_PATH):
        print("📥 Clonazione repository...")
        os.system(f'git clone https://github.com/Ame-76/Progetto-Deep-Learning.git {PROJECT_PATH}')
        print("✅ Repository clonato!")
    
    # Configura ambiente
    os.chdir(PROJECT_PATH)
    sys.path.append(f'{PROJECT_PATH}/src')
    
    # Installa dipendenze essenziali
    print("📦 Installazione dipendenze...")
    packages = ['tensorflow-datasets', 'seaborn', 'plotly', 'opencv-python']
    for pkg in packages:
        os.system(f'pip install -q {pkg}')
    
    # Definisci variabili globali
    MODELS_DIR = f'{PROJECT_PATH}/models'
    DATA_DIR = f'{PROJECT_PATH}/data'
    
    # Crea directory
    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(f'{DATA_DIR}/processed', exist_ok=True)
    os.makedirs(f'{DATA_DIR}/raw', exist_ok=True)
    
    print("✅ Setup Colab completato!")
    print(f"📁 Progetto: {PROJECT_PATH}")
    
else:
    # Setup locale
    from pathlib import Path
    PROJECT_PATH = str(Path.cwd().parent)
    MODELS_DIR = f'{PROJECT_PATH}/models'
    DATA_DIR = f'{PROJECT_PATH}/data'
    sys.path.append(f'{PROJECT_PATH}/src')
    print("✅ Setup locale completato!")

print("\n🚀 Pronto per l'esecuzione!")

# ========================================
# FINE TEMPLATE - INIZIA IL TUO CODICE
# ========================================
