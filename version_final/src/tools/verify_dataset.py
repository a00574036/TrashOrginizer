from pathlib import Path

IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

def find_candidate_roots(root: Path):
    roots = []
    # splits
    for split in ["TRAIN","TEST","VAL","VALID","VALIDATION","train","test","val"]:
        p = root / split
        if p.is_dir():
            roots.append(p)
    # dataset-resized
    dr = root / "dataset-resized"
    if dr.is_dir():
        for split in ["train","test","val","validation"]:
            p = dr / split
            if p.is_dir():
                roots.append(p)
    # clases directas
    if any((root / d).is_dir() for d in root.iterdir() if (root / d).is_dir()):
        roots.append(root)
    # quitar duplicados
    out, seen = [], set()
    for r in roots:
        if r not in seen:
            out.append(r)
            seen.add(r)
    return out

def count_imgs(p: Path):
    return sum(1 for x in p.rglob("*") if x.suffix.lower() in IMG_EXTS)

def main():
    repo = Path(__file__).resolve().parents[2]
    ds_root = repo / "datasets" / "waste_cls"
    print(f"[INFO] Buscando en: {ds_root}")
    if not ds_root.exists():
        print("[ERROR] Falta datasets/waste_cls (descomprime o mueve ahí el dataset)")
        return
    cands = find_candidate_roots(ds_root)
    if not cands:
        print("[ERROR] No detecté splits ni clases")
        return
    for c in cands:
        print(f"\n[CHECK] {c}")
        subdirs = [d for d in c.iterdir() if d.is_dir()]
        anyc = False
        for sd in subdirs:
            num = count_imgs(sd)
            if num > 0:
                anyc = True
                print(f"  - {sd.name:<18} imgs: {num}")
        if not anyc:
            print("  - No encontré imágenes en subcarpetas")

if __name__ == "__main__":
    main()
