from pathlib import Path
from datetime import datetime

out = Path("/data/hello.txt")

with out.open("a") as f:
    f.write(f"Hello from a bind mount - {datetime.now()}\n")