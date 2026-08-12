import contextlib
import time
from collections.abc import Generator, Iterable


def batch_generator[T](iterable: Iterable[T], batch_size: int) -> Generator[list[T]]:
    if batch_size <= 0:
        raise ValueError("El tamaño del lote debe ser mayor que cero.")

    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            print(f"Generando lote de tamaño: {len(batch)}")
            yield batch
            batch = []
    if batch:
        yield batch


@contextlib.contextmanager
def timer(label: str = "Bloque de código") -> Generator[None]:
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[{label}] Tiempo transcurrido: {elapsed:.6f} segundos")

# Simulación de una fuente de datos masiva (generador)
datos_masivos = (x for x in range(1_000_000))
tamanio_lote = 250_000

# Procesamiento por lotes temporizado
for i, lote in enumerate(batch_generator(datos_masivos, tamanio_lote), 1):
    with timer(f"Procesando Lote #{i} (Tamaño: {len(lote)})"):
        # Simulación de operación pesada (ej. guardar en base de datos o transformar)
        resultado = sum(lote)