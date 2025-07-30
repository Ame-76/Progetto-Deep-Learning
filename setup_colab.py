#!/usr/bin/env python3
"""
Script di setup per Google Colab
Esegui questo script all'inizio di ogni notebook su Colab per configurare l'ambiente
"""

import os
import sys

def setup_colab_environment():
    """Setup completo dell'ambiente Google Colab"""
    
    print("🚀 SETUP AMBIENTE GOOGLE COLAB")
    print("=" * 50)
    
    # 1. Monta Google Drive
    print("📱 1. Montaggio Google Drive...")
    try:
        from google.colab import drive
        drive.mount('/content/drive')
        print("✅ Google Drive montato!")
    except ImportError:
        print("❌ Non siamo su Google Colab")
        return False
    
    # 2. Configura path del progetto
    print("📁 2. Configurazione path progetto...")
    PROJECT_PATH = '/content/drive/MyDrive/Progetto-Deep-Learning'
    
    # 3. Clona o aggiorna repository
    print("📥 3. Sincronizzazione repository...")
    if not os.path.exists(PROJECT_PATH):
        print("   Clonazione da GitHub...")
        clone_cmd = f'git clone https://github.com/Ame-76/Progetto-Deep-Learning.git "{PROJECT_PATH}"'
        os.system(clone_cmd)
        print("✅ Repository clonato!")
    else:
        print("   Repository esistente, aggiornamento...")
        os.chdir(PROJECT_PATH)
        os.system('git pull origin master')
        print("✅ Repository aggiornato!")
    
    # 4. Cambia directory di lavoro
    os.chdir(PROJECT_PATH)
    print(f"📂 Directory corrente: {os.getcwd()}")
    
    # 5. Configura Python path
    print("🐍 4. Configurazione Python path...")
    sys.path.append(f"{PROJECT_PATH}/src")
    print("✅ Python path configurato!")
    
    # 6. Installa dipendenze
    print("📦 5. Installazione dipendenze...")
    
    # Usa il file requirements specifico per Colab se disponibile
    colab_requirements = f"{PROJECT_PATH}/requirements-colab.txt"
    if os.path.exists(colab_requirements):
        print(f"   Installando da {colab_requirements}...")
        os.system(f'pip install -q -r "{colab_requirements}"')
    else:
        # Fallback alle dipendenze manuali
        dependencies = [
            'tensorflow-datasets',
            'matplotlib',
            'seaborn', 
            'scikit-learn',
            'pandas',
            'numpy',
            'plotly',
            'opencv-python',
            'pillow',
            'tqdm',
            'GitPython'
        ]
        
        for dep in dependencies:
            print(f"   Installando {dep}...")
            os.system(f'pip install -q {dep}')
    
    print("✅ Dipendenze installate!")
    
    # 7. Crea directory necessarie
    print("📁 6. Creazione directory...")
    directories = [
        f"{PROJECT_PATH}/models",
        f"{PROJECT_PATH}/data/processed", 
        f"{PROJECT_PATH}/data/raw",
        f"{PROJECT_PATH}/data/external",
        f"{PROJECT_PATH}/reports/figures"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print("✅ Directory create!")
    
    # 8. Configurazione Git
    print("🔧 7. Configurazione Git...")
    os.system('git config --global user.email "colab-user@example.com"')
    os.system('git config --global user.name "Colab User"')
    print("✅ Git configurato!")
    
    print("\n" + "=" * 50)
    print("🎉 SETUP COMPLETATO CON SUCCESSO!")
    print("=" * 50)
    print(f"📂 Progetto configurato in: {PROJECT_PATH}")
    print("💡 Ora puoi eseguire i notebook normalmente")
    print("\n📋 PATH CONFIGURATI:")
    print(f"   MODELS: {PROJECT_PATH}/models")
    print(f"   DATA: {PROJECT_PATH}/data") 
    print(f"   NOTEBOOKS: {PROJECT_PATH}/notebooks")
    
    return True

if __name__ == "__main__":
    setup_colab_environment()
