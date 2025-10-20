# src/core/ingest.py
import os, shutil
from pathlib import Path

IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

def _norm(name: str) -> str:
    return name.strip().upper().replace(" ", "_")

def _is_img(p: Path) -> bool:
    return p.suffix.lower() in IMG_EXTS

def _copy_class(src_dir: Path, dst_dir: Path):
    dst_dir.mkdir(parents=True, exist_ok=True)
    for p in src_dir.rglob("*"):
        if _is_img(p):
            out = dst_dir / p.name
            base = p.stem
            i = 1
            while out.exists():
                out = dst_dir / f"{base}_{i}{p.suffix}"
                i += 1
            shutil.copy2(p, out)

def ingest_waste_dataset(src_root: str, dst_root: str):
    """
    Acepta:
      - src/dataset-resized/{train,test,val}/<clase>/*
      - src/{TRAIN,TEST,VAL}/<clase>/*
      - src/<clase>/*
    Copia todo a: dst_root/<CLASE>/*
    """
    src = Path(src_root)
    dst = Path(dst_root)
    dst.mkdir(parents=True, exist_ok=True)

    # 1) dataset-resized con splits
    dr = src / "dataset-resized"
    if dr.is_dir():
        for split in ["train","test","val","validation"]:
            sp = dr / split
            if sp.is_dir():
                for cls_dir in sp.iterdir():
                    if cls_dir.is_dir():
                        cls_name = _norm(cls_dir.name)
                        print(f"[INGEST] {cls_dir} -> {dst/cls_name}")
                        _copy_class(cls_dir, dst/cls_name)
        print(f"[OK] Ingesta completa en {dst}")
        return

    # 2) splits TRAIN/TEST/VAL en raíz
    splits = []
    for s in ["TRAIN","TEST","VAL","VALID","VALIDATION","train","test","val"]:
        p = src / s
        if p.is_dir(): splits.append(p)
    if splits:
        for sp in splits:
            for cls_dir in sp.iterdir():
                if cls_dir.is_dir():
                    cls_name = _norm(cls_dir.name)
                    print(f"[INGEST] {cls_dir} -> {dst/cls_name}")
                    _copy_class(cls_dir, dst/cls_name)
        print(f"[OK] Ingesta completa en {dst}")
        return

    # 3) clases directamente en raíz
    class_dirs = [d for d in src.iterdir() if d.is_dir()]
    if class_dirs:
        for cls_dir in class_dirs:
            cls_name = _norm(cls_dir.name)
            print(f"[INGEST] {cls_dir} -> {dst/cls_name}")
            _copy_class(cls_dir, dst/cls_name)
        print(f"[OK] Ingesta completa en {dst}")
        return

    raise RuntimeError("No se detectaron clases ni splits. Revisa la ruta al dataset.")
