"""
Configurazione di compatibilità per Google Colab e ambiente locale
"""

# Versioni minime compatibili tra Colab e locale
COMPATIBLE_VERSIONS = {
    'tensorflow': '2.13.0',
    'numpy': '1.24.0', 
    'pandas': '2.0.0',
    'matplotlib': '3.7.0',
    'seaborn': '0.12.0',
    'scikit-learn': '1.3.0',
    'tensorflow-datasets': '4.9.0',
    'opencv-python': '4.8.0',
    'pillow': '9.0.0',
    'plotly': '5.0.0'
}

# Pacchetti preinstallati su Google Colab (potrebbero non richiedere installazione)
COLAB_PREINSTALLED = [
    'tensorflow',
    'numpy', 
    'pandas',
    'matplotlib',
    'scikit-learn',
    'pillow'
]

# Pacchetti che richiedono installazione esplicita su Colab
COLAB_INSTALL_REQUIRED = [
    'tensorflow-datasets',
    'seaborn',
    'opencv-python', 
    'plotly',
    'tqdm',
    'GitPython',
    'scipy'
]

def check_environment():
    """Rileva se siamo su Google Colab"""
    try:
        import google.colab
        return 'colab'
    except ImportError:
        return 'local'

def get_install_command(environment='local'):
    """Restituisce il comando di installazione appropriato per l'ambiente"""
    if environment == 'colab':
        return 'pip install -q -r requirements-colab.txt'
    else:
        return 'pip install -r requirements.txt'

def verify_versions():
    """Verifica che le versioni installate siano compatibili"""
    import importlib
    from packaging import version
    
    print("🔍 Verifica compatibilità versioni...")
    
    for package, min_version in COMPATIBLE_VERSIONS.items():
        try:
            if package == 'opencv-python':
                import cv2
                installed_version = cv2.__version__
                package_name = 'OpenCV'
            elif package == 'scikit-learn':
                import sklearn
                installed_version = sklearn.__version__
                package_name = 'scikit-learn'
            elif package == 'tensorflow-datasets':
                import tensorflow_datasets as tfds
                installed_version = tfds.__version__
                package_name = 'TensorFlow Datasets'
            else:
                module = importlib.import_module(package.replace('-', '_'))
                installed_version = module.__version__
                package_name = package
            
            if version.parse(installed_version) >= version.parse(min_version):
                print(f"✅ {package_name}: {installed_version} (>= {min_version})")
            else:
                print(f"⚠️ {package_name}: {installed_version} (richiesta >= {min_version})")
                
        except ImportError:
            print(f"❌ {package_name}: NON INSTALLATO")
        except Exception as e:
            print(f"❓ {package_name}: Errore verifica - {e}")

if __name__ == "__main__":
    env = check_environment()
    print(f"Ambiente rilevato: {env}")
    print(f"Comando installazione: {get_install_command(env)}")
    verify_versions()
