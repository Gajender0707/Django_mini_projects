from pathlib import Path
import os

print(f"this is path: {Path(__file__).resolve().parent.parent}")


print(os.path.join(Path(__file__).resolve().parent.parent),"TEMP")