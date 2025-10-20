# src/core/cv_core.py
import os
import cv2
import numpy as np
from glob import glob
from joblib import dump, load
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# -------- OpenCV utils
def read_image_bgr(path: str):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"No se pudo abrir la imagen: {path}")
    return img

def bgr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def hsv_hist_features(bgr_img, h_bins=30, s_bins=32, v_bins=32):
    hsv = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0,1,2], None,
                        [h_bins, s_bins, v_bins],
                        [0,180, 0,256, 0,256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

# -------- dataset a matriz
def _list_subdirs(p):
    return [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]

def _load_matrix(data_dir: str):
    X, y, labels = [], [], []
    classes = sorted(_list_subdirs(data_dir))
    if not classes:
        raise RuntimeError(f"No hay subcarpetas de clases en {data_dir}")
    for idx, cls in enumerate(classes):
        labels.append(cls)
        paths = []
        for ext in ("*.jpg","*.jpeg","*.png","*.bmp","*.webp"):
            paths += glob(os.path.join(data_dir, cls, ext))
        for p in paths:
            try:
                img = read_image_bgr(p)
                X.append(hsv_hist_features(img))
                y.append(idx)
            except Exception as e:
                print(f"[WARN] {p}: {e}")
    return np.array(X), np.array(y), labels

# -------- Entrenar y guardar
def train_and_save(data_dir="data", model_path="models/trashorg_knn.joblib", test_size=0.2):
    X, y, labels = _load_matrix(data_dir)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=test_size, stratify=y, random_state=42)
    pipe = Pipeline([
        ("scaler", StandardScaler(with_mean=False)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ])
    pipe.fit(Xtr, ytr)
    ypred = pipe.predict(Xte)
    print(classification_report(yte, ypred, target_names=labels))
    print("Matriz de confusión:\n", confusion_matrix(yte, ypred))
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    dump({"model": pipe, "labels": labels, "type": "hsv_knn"}, model_path)
    print(f"[OK] Modelo guardado en {model_path}")

# -------- Cargar y predecir
def load_model(model_path: str):
    return load(model_path)

def classify_image_file(image_path: str, model_path: str):
    bundle = load_model(model_path)
    model = bundle["model"]; labels = bundle["labels"]
    img = read_image_bgr(image_path)
    feats = hsv_hist_features(img).reshape(1, -1)
    pred = model.predict(feats)[0]
    score = None
    if hasattr(model, "predict_proba"):
        score = float(model.predict_proba(feats)[0][pred])
    label = labels[int(pred)]
    return label, score, img
