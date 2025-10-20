from src.core.cv_core import train_and_save
from pathlib import Path

if __name__ == "__main__":
    dataset_path = Path(__file__).resolve().parents[2] / "datasets" / "waste_cls" / "TRAIN"
    model_path = Path(__file__).resolve().parents[2] / "models" / "trashorg_knn.joblib"

    print(f"📦 Entrenando modelo con datos de: {dataset_path}")
    print(f"🧠 Guardando modelo en: {model_path}")

    train_and_save(data_dir=str(dataset_path), model_path=str(model_path), test_size=0.2)

    print("✅ Entrenamiento completo.")