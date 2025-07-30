# 🚀 Guida Installazione CUDA 11.8 e cuDNN 8.6

Questa guida spiega come installare CUDA Toolkit 11.8 e cuDNN 8.6 per l'accelerazione GPU con TensorFlow e PyTorch.

## 📋 Prerequisiti

- **GPU NVIDIA** compatibile con CUDA (GTX 10xx series o più recente)
- **Driver NVIDIA** aggiornati (versione 522.06 o superiore)
- **Windows 10/11** (64-bit)

## 🔧 Installazione CUDA Toolkit 11.8

### 1. Download CUDA Toolkit 11.8
1. Vai su [NVIDIA CUDA Downloads](https://developer.nvidia.com/cuda-11-8-0-download-archive)
2. Seleziona:
   - Operating System: **Windows**
   - Architecture: **x86_64**
   - Version: **10** o **11** (a seconda del tuo Windows)
   - Installer Type: **exe (local)**

### 2. Installazione
1. Esegui il file `.exe` scaricato come **Amministratore**
2. Scegli **Custom (Advanced)** installation
3. Assicurati che siano selezionati:
   - ✅ CUDA Toolkit 11.8
   - ✅ CUDA Samples 11.8
   - ✅ CUDA Documentation 11.8
   - ✅ CUDA Runtime 11.8
   - ✅ CUDA Development 11.8

### 3. Verifica Installazione
Apri PowerShell/CMD e esegui:
```powershell
nvcc --version
```
Dovresti vedere output simile a:
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:41:10_Pacific_Daylight_Time_2022
Cuda compilation tools, release 11.8, V11.8.89
```

## 🧠 Installazione cuDNN 8.6

### 1. Download cuDNN 8.6
1. Vai su [NVIDIA cuDNN Downloads](https://developer.nvidia.com/cudnn)
2. **Registrati/Login** con account NVIDIA (gratuito)
3. Scarica **cuDNN v8.6.0 for CUDA 11.x**
4. Scegli: **cuDNN Library for Windows (x86)**

### 2. Installazione
1. Estrai il file ZIP scaricato
2. Copia i file nelle cartelle CUDA:
   ```
   Copia da cuDNN\bin\*.dll     → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin\
   Copia da cuDNN\include\*.h   → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include\
   Copia da cuDNN\lib\x64\*.lib → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib\x64\
   ```

### 3. Variabili d'Ambiente
Aggiungi alle variabili d'ambiente di sistema:
- **CUDA_PATH**: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8`
- **PATH**: Aggiungi `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin`

## ✅ Verifica Setup Completo

### 1. Verifica TensorFlow con GPU
```python
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("GPU disponibili:", tf.config.list_physical_devices('GPU'))
print("CUDA build:", tf.test.is_built_with_cuda())

# Test veloce di calcolo GPU
if tf.config.list_physical_devices('GPU'):
    print("\n🚀 Test GPU:")
    with tf.device('/GPU:0'):
        a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
        b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
        c = tf.matmul(a, b)
        print("Calcolo GPU riuscito:", c.numpy())
else:
    print("⚠️ GPU non disponibile, usando CPU")
```

## 🐛 Risoluzione Problemi

### Errore: "Could not load dynamic library 'cudart64_110.dll'"
- Reinstalla CUDA Toolkit 11.8
- Verifica che le variabili d'ambiente siano corrette

### Errore: "Could not load dynamic library 'cudnn64_8.dll'"
- Verifica che cuDNN sia installato correttamente
- Controlla che i file DLL siano nella cartella bin di CUDA

### GPU non rilevata
- Aggiorna i driver NVIDIA all'ultima versione
- Riavvia il computer dopo l'installazione
- Verifica compatibilità GPU con CUDA

## 📚 Link Utili

- [CUDA Compatibility Guide](https://docs.nvidia.com/deploy/cuda-compatibility/index.html)
- [TensorFlow GPU Support](https://www.tensorflow.org/install/gpu)
- [TensorFlow Build Configurations](https://www.tensorflow.org/install/source#gpu)

## 🎯 Test Performance

Dopo l'installazione, esegui il notebook `04-cnn-from-scratch.ipynb` per verificare l'accelerazione GPU!
