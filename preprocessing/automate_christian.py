from __future__ import annotations

from pathlib import Path

import pandas as pd


def preprocess_data(input_path: Path, output_path: Path) -> None:
	df = pd.read_csv(input_path)

	# Drop duplikat
	clean_df = df.drop_duplicates().copy()

	# Isi missing numeric dengan median
	num_cols = [
		"TransactionAmount",
		"CustomerAge",
		"TransactionDuration",
		"LoginAttempts",
		"AccountBalance",
	]
	for col in num_cols:
		clean_df[col] = clean_df[col].fillna(clean_df[col].median())

	# Isi missing kategorikal dengan mode
	cat_cols = [
		"TransactionType",
		"Location",
		"DeviceID",
		"IP Address",
		"MerchantID",
		"Channel",
		"CustomerOccupation",
	]
	for col in cat_cols:
		clean_df[col] = clean_df[col].fillna(clean_df[col].mode()[0])

	# Drop baris dengan ID yang kosong
	clean_df = clean_df.dropna(subset=["TransactionID", "AccountID"]).copy()

	# Parsing tanggal
	clean_df["TransactionDate"] = pd.to_datetime(clean_df["TransactionDate"], errors="coerce")
	clean_df["PreviousTransactionDate"] = pd.to_datetime(
		clean_df["PreviousTransactionDate"], errors="coerce"
	)
	clean_df["TransactionDate"] = clean_df["TransactionDate"].fillna(
		clean_df["TransactionDate"].median()
	)
	clean_df["PreviousTransactionDate"] = clean_df["PreviousTransactionDate"].fillna(
		clean_df["PreviousTransactionDate"].median()
	)

	# One-hot encoding
	processed_df = pd.get_dummies(clean_df, columns=cat_cols, drop_first=True)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	processed_df.to_csv(output_path, index=False)


def main() -> None:
	base_dir = Path(__file__).resolve().parent
	input_path = base_dir.parent / "dataset" / "bank_transactions_data.csv"
	output_path = base_dir / "bank_transactions_data_preprocessing.csv"
	preprocess_data(input_path, output_path)


if __name__ == "__main__":
	main()
