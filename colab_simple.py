"""
Setup semplificato per Google Colab senza Google Drive
Download diretto dei modelli addestrati
"""

import os
import sys
import zipfile
from datetime import datetime

def setup_colab_simple():
    """Setup Google Colab senza Google Drive"""
    
    print("🚀 SETUP GOOGLE COLAB - VERSIONE SEMPLIFICATA")
    print("=" * 60)
    
    # Verifica che siamo su Colab
    try:
        import google.colab
        print("✅ Google Colab rilevato")
    except ImportError:
        print("❌ Non siamo su Google Colab")
        return False
    
    # Path del progetto
    project_path = '/content/Progetto-Deep-Learning'
    
    # Clona repository
    if not os.path.exists(project_path):
        print("📥 Clonazione repository...")
        result = os.system(f'git clone https://github.com/Ame-76/Progetto-Deep-Learning.git {project_path}')
        if result == 0:
            print("✅ Repository clonato!")
        else:
            print("❌ Errore durante la clonazione")
            return False
    else:
        print("📂 Repository già presente")
    
    # Configura ambiente
    os.chdir(project_path)
    sys.path.append(f"{project_path}/src")
    
    # Installa dipendenze essenziali
    print("📦 Installazione dipendenze...")
    essential_packages = [
        'tensorflow-datasets',
        'seaborn', 
        'plotly',
        'opencv-python'
    ]
    
    for package in essential_packages:
        print(f"   Installing {package}...")
        os.system(f'pip install -q {package}')
    
    # Crea directory
    models_dir = f"{project_path}/models"
    data_dir = f"{project_path}/data"
    
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(f"{data_dir}/processed", exist_ok=True)
    os.makedirs(f"{data_dir}/raw", exist_ok=True)
    
    print(f"\n✅ SETUP COMPLETATO!")
    print(f"📁 Progetto: {project_path}")
    print(f"📁 Models: {models_dir}")
    print(f"📁 Data: {data_dir}")
    
    return True

def download_model_from_colab(model_dir):
    """
    Download diretto del modello da Colab
    
    Args:
        model_dir: Path della directory del modello
    """
    try:
        from google.colab import files
        
        # Crea archivio ZIP
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_filename = f"cnn_model_{timestamp}.zip"
        zip_path = f"/content/{zip_filename}"
        
        print(f"📦 Creazione archivio: {zip_filename}")
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files_list in os.walk(model_dir):
                for file in files_list:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.path.dirname(model_dir))
                    zipf.write(file_path, arcname)
        
        # Info sul file
        zip_size = os.path.getsize(zip_path) / (1024 * 1024)
        print(f"✅ Archivio creato: {zip_size:.2f} MB")
        
        # Download
        print("📥 Inizio download...")
        files.download(zip_path)
        print("✅ Download completato!")
        
        return zip_path
        
    except Exception as e:
        print(f"❌ Errore download: {e}")
        return None

def print_instructions():
    """Stampa istruzioni per l'uso"""
    print("\n" + "=" * 60)
    print("📋 ISTRUZIONI D'USO")
    print("=" * 60)
    print("\n🎯 TRAINING SU COLAB:")
    print("1. Apri 04-cnn-from-scratch.ipynb su Colab")
    print("2. Esegui tutte le celle")
    print("3. Al termine, il modello verrà scaricato automaticamente")
    
    print("\n💻 USO LOCALE:")
    print("1. Estrai l'archivio ZIP in models/")
    print("2. Esegui 05-model-evaluation.ipynb localmente")
    print("3. Il modello verrà caricato automaticamente")
    
    print("\n✨ VANTAGGI:")
    print("✅ Niente Google Drive")
    print("✅ Download diretto")
    print("✅ Setup semplificato")
    print("✅ Compatibilità completa")

if __name__ == "__main__":
    print_instructions()
