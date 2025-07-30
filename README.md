Progetto Deep Learning
==============================

Progetto di implementazione pratiche di Deep Learning con classificazione di erbacce usando CNN.

## 🚀 Quick Start

### 💻 Ambiente Locale
```bash
git clone <repository-url>
cd Progetto-Deep-Learning
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### ☁️ Google Colab (Semplificato)
Per training su GPU gratuita senza complicazioni:

```python
# Setup ultra-rapido su Colab (SENZA Google Drive)
import os, sys

if not os.path.exists('/content/Progetto-Deep-Learning'):
    !git clone https://github.com/Ame-76/Progetto-Deep-Learning.git /content/Progetto-Deep-Learning

os.chdir('/content/Progetto-Deep-Learning')
sys.path.append('/content/Progetto-Deep-Learning/src')
!pip install -q tensorflow-datasets seaborn plotly opencv-python

print("✅ Pronto per il training!")
```

🎯 **Al termine del training**: download automatico del modello (ZIP)  
📖 **Guida completa**: [COLAB_GUIDE.md](COLAB_GUIDE.md)

### 3. Setup GPU (Opzionale ma Raccomandato)
Per accelerazione GPU, segui la guida completa: [CUDA_SETUP.md](CUDA_SETUP.md)

**Quick setup:**
- Installa [CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
- Installa [cuDNN 8.6](https://developer.nvidia.com/cudnn) 
- Verifica con: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

### 4. Esegui i Notebook
```bash
jupyter notebook notebooks/
```

**Ordine consigliato:**
1. `01-environment-setup.ipynb` - Verifica ambiente
2. `02-dataset-exploration.ipynb` - Esplorazione dataset DeepWeeds
3. `03-preprocessing.ipynb` - Preprocessing e preparazione dati
4. `04-cnn-from-scratch.ipynb` - Training CNN da zero
5. `05-model-evaluation.ipynb` - Valutazione modello

## 📊 Dataset

Utilizziamo il **DeepWeeds Dataset** per la classificazione di 9 specie di erbacce:
- 17,509 immagini etichettate
- Risoluzione 256x256 pixel
- 8 specie di erbacce + 1 classe "negative"

## 🎯 Obiettivi del Progetto

- ✅ Implementare CNN da zero con TensorFlow/Keras
- ✅ Tecniche di preprocessing avanzate
- ✅ Data augmentation e bilanciamento classi
- ✅ Monitoraggio training con callbacks
- ✅ Valutazione metriche e visualizzazioni
- ✅ Ottimizzazione performance GPU

## 📈 Performance Attese

**Con GPU (CUDA 11.8 + cuDNN 8.6):**
- Training: ~30-60 minuti (30 epoch)
- Accuratezza: >85% sul validation set

**Con CPU:**
- Training: ~2-4 ore (30 epoch)
- Stesse performance, tempi più lunghi

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
