# Guida Google Colab - Versione Semplificata

Questa guida ti mostra come usare Google Colab per addestrare modelli e scaricarli direttamente senza complicazioni.

## 🎯 **Soluzione Semplificata (RACCOMANDATO)**

**NIENTE GOOGLE DRIVE!** Download diretto dei modelli addestrati.

### ⚡ Setup Ultra-Rapido

Aggiungi questa cella all'inizio del notebook su Colab:

```python
# Setup Colab semplificato - SENZA Google Drive
import os, sys

# Clona progetto
if not os.path.exists('/content/Progetto-Deep-Learning'):
    !git clone https://github.com/Ame-76/Progetto-Deep-Learning.git /content/Progetto-Deep-Learning

# Configura ambiente
os.chdir('/content/Progetto-Deep-Learning')
sys.path.append('/content/Progetto-Deep-Learning/src')

# Installa dipendenze essenziali
!pip install -q tensorflow-datasets seaborn plotly opencv-python

print("✅ Setup completato! Inizia il training...")
```

## 🚀 **Workflow Completo**

### 1. **Training su Colab**
- Apri `04-cnn-from-scratch.ipynb` su [Google Colab](https://colab.research.google.com/)
- Aggiungi la cella di setup sopra
- Esegui tutte le celle
- **Al termine: DOWNLOAD AUTOMATICO** del modello (file ZIP)

### 2. **Uso Locale**
- Estrai il file ZIP scaricato in `models/` del progetto locale
- Esegui `05-model-evaluation.ipynb` localmente
- Il modello viene caricato automaticamente

## ✨ **Vantaggi della Soluzione Semplificata**

✅ **Niente Google Drive** - zero configurazione  
✅ **Download diretto** - un click e hai tutto  
✅ **Setup rapido** - 30 secondi invece di 5 minuti  
✅ **Niente sincronizzazione** - tutto locale dopo il download  
✅ **Compatibilità completa** - funziona sempre

## � File di Configurazione

Il progetto include diversi file per ottimizzare l'esperienza Colab:

### 📋 **requirements-colab.txt**
File requirements ottimizzato per Google Colab:
- Include solo le dipendenze non preinstallate
- Ottimizzato per tempi di installazione rapidi
- Compatibile con le versioni Colab

### 🔧 **setup_colab.py** 
Script di setup automatico:
- Monta Google Drive
- Clona/aggiorna il repository
- Installa dipendenze automaticamente
- Configura l'ambiente completo

### ⚙️ **colab_config.py**
Utility di compatibilità:
- Verifica versioni delle dipendenze
- Rileva automaticamente l'ambiente
- Garantisce compatibilità Colab-locale

## �📚 Notebook Compatibili

I seguenti notebook sono stati aggiornati per funzionare automaticamente su Colab:

### ✅ 04-cnn-from-scratch.ipynb
- **Funzione**: Addestramento modello CNN
- **Output**: Modello salvato in `models/cnn_from_scratch_YYYYMMDD_HHMMSS/`
- **Tempo stimato**: 30-60 minuti con GPU Colab

### ✅ 05-model-evaluation.ipynb  
- **Funzione**: Valutazione e analisi del modello
- **Input**: Carica automaticamente il modello più recente
- **Output**: Report e grafici di valutazione

## 🔄 Sincronizzazione Automatica

### Durante l'addestramento su Colab:
1. Il modello viene salvato automaticamente su Google Drive
2. I file vengono aggiunti al repository Git locale
3. Ricevi istruzioni per la sincronizzazione finale

### Per sincronizzare con il progetto locale:

#### Metodo 1: Git Pull (Raccomandato)
```bash
# Sul tuo computer locale
cd "path/to/Progetto-Deep-Learning"
git pull origin master
```

#### Metodo 2: Download Manuale
1. Vai su Google Drive → `MyDrive/Progetto-Deep-Learning/models/`
2. Scarica la cartella del modello più recente
3. Copiala nella cartella `models/` del progetto locale

## 🎯 Workflow Completo

### 1. Addestramento su Colab
```python
# Nel notebook 04-cnn-from-scratch.ipynb su Colab
# Il setup automatico configura tutto
# Il modello viene salvato su Drive
```

### 2. Sincronizzazione Locale
```bash
# Sul computer locale
git pull origin master
# Ora hai il modello addestrato localmente
```

### 3. Valutazione Locale
```python
# Nel notebook 05-model-evaluation.ipynb locale
# Carica automaticamente il modello sincronizzato
```

## ⚙️ Configurazione Avanzata

### Personalizzazione Git su Colab
Per personalizzare le informazioni Git, modifica la cella nel notebook:

```python
# Sostituisci con le tue informazioni
os.system('git config --global user.email "tua-email@example.com"')
os.system('git config --global user.name "Il Tuo Nome"')
```

### Ottimizzazione Tempi di Training
```python
# Nel notebook 04, modifica questi parametri:
EPOCHS = 20  # Riduci per test più veloci
BATCH_SIZE = 32  # Aumenta se hai sufficiente VRAM
```

## 🔧 Troubleshooting

### Problema: "Dataset non trovato"
**Soluzione**: Esegui prima il notebook `03-preprocessing.ipynb` su Colab

### Problema: "Modello non trovato"  
**Soluzione**: Verifica che il training sia completato e il modello sia salvato

### Problema: "Git push fallito"
**Soluzione**: Puoi sempre scaricare manualmente da Google Drive

### Problema: "Out of Memory"
**Soluzione**: 
- Riduci il `BATCH_SIZE` 
- Usa GPU Runtime su Colab
- Riduci la complessità del modello

## 📊 Monitoraggio Training

### Su Colab:
- Progress bar in tempo reale
- Callback automatici per early stopping
- Logs salvati in `models/[nome_modello]/logs/`

### Visualizzazione TensorBoard:
```python
# Su Colab, carica TensorBoard
%load_ext tensorboard
%tensorboard --logdir /content/drive/MyDrive/Progetto-Deep-Learning/models/
```

## 💡 Suggerimenti

### Per training lunghi:
- Usa GPU Runtime su Colab (Runtime → Change runtime type → GPU)
- Mantieni la tab di Colab aperta
- Configura Early Stopping per training automatico

### Per progetti collaborativi:
- Ogni membro può addestrare su Colab
- I modelli vengono sincronizzati automaticamente
- Usa branch separati per esperimenti paralleli

### Per backup sicuri:
- Google Drive backup automatico
- Git tracking delle versioni
- Export manuale dei modelli migliori

---

## 🆘 Supporto

Se incontri problemi:
1. Controlla che tutte le celle di setup siano eseguite
2. Verifica la connessione a Google Drive
3. Assicurati di avere spazio sufficiente su Drive
4. Consulta i log di errore per dettagli specifici
