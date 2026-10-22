"""File I/O utilities for generating and loading integer array datasets.
"""

from pathlib import Path
import random
from typing import Dict, List, Sequence


def generate_dataset_file(size: int, filepath: Path | str, seed: int | None = None) -> List[int]:
    """Generate a sorted integer array and write it to the specified file.

    Each integer is written on a new line.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    rng = random.Random(seed if seed is not None else 42 + size)
    # Generate distinct positive integers with a sensible spread
    base = rng.sample(range(1, max(1000, size * 10)), size)
    base.sort()

    with path.open("w", encoding="utf-8") as f:
        for val in base:
            f.write(f"{val}\n")

    return base


def generate_all_datasets(
    sizes: Sequence[int] = (10, 50, 100, 200),
    data_dir: Path | str = "data",
    seed: int | None = 42,
) -> Dict[int, Path]:
    """Generate dataset files for all specified input sizes if they do not exist."""
    dir_path = Path(data_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    generated_files: Dict[int, Path] = {}

    for size in sizes:
        target_file = dir_path / f"input_{size}.txt"
        generate_dataset_file(size, target_file, seed=seed)
        generated_files[size] = target_file

    return generated_files


def read_array_from_file(filepath: Path | str) -> List[int]:
    """Read integers from a file containing whitespace or newline-separated values."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        tokens = f.read().split()

    return [int(token) for token in tokens if token.strip()]


def load_datasets(
    sizes: Sequence[int] = (10, 50, 100, 200),
    data_dir: Path | str = "data",
    auto_generate: bool = True,
) -> Dict[int, List[int]]:
    """Load array datasets for all requested sizes, generating them if missing."""
    dir_path = Path(data_dir)
    datasets: Dict[int, List[int]] = {}

    for size in sizes:
        filepath = dir_path / f"input_{size}.txt"
        if not filepath.exists():
            if auto_generate:
                generate_dataset_file(size, filepath)
            else:
                raise FileNotFoundError(f"Missing dataset file: {filepath}")
        arr = read_array_from_file(filepath)
        datasets[size] = arr

    return datasets
