# Eksperimen_SML_Christian

Repo ini berisi eksperimen dan otomatisasi preprocessing untuk dataset transaksi bank.

## Struktur
- dataset/bank_transactions_data.csv
- preprocessing/Eksperimen_Christian.ipynb
- preprocessing/automate_christian.py
- preprocessing/dataset_processed.csv

## Menjalankan Eksperimen (Notebook)
1. Buka notebook di preprocessing/Eksperimen_Christian.ipynb
2. Jalankan cell secara berurutan sampai preprocessing selesai
3. Output akan tersimpan sebagai preprocessing/dataset_processed.csv

## Menjalankan Otomatisasi
1. Install dependency:
	- pip install -r requirements.txt
2. Jalankan script:
	- python preprocessing/automate_christian.py

## Workflow GitHub Actions
Workflow ada di .github/workflows/preprocess.yml.
Workflow akan berjalan saat ada perubahan di folder dataset/ atau preprocessing/ dan mengunggah artifact dataset-processed.
