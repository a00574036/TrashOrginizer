from pathlib import Path
from src.core.cv_core import train_and_save

if __name__ == "__main__":
    # Carpeta del dataset
    dataset_path = Path(__file__).resolve().parents[2] / "datasets" / "garbage10"

    # Dónde guardar el modelo entrenado
    model_path = Path(__file__).resolve().parents[2] / "models" / "trashorg_garbage10.joblib"

    print(f"📦 Entrenando con datos en: {dataset_path}")
    print(f"🧠 Guardando modelo en: {model_path}")

    # Entrenamiento (usa 80% train / 20% test)
    train_and_save(data_dir=str(dataset_path), model_path=str(model_path), test_size=0.2)

    print("✅ Entrenamiento completo.")
