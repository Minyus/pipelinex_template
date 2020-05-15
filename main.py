import sys
import os
from pathlib import Path

import pipelinex
from pipelinex import MLflowFlexibleContext


print("pipelinex version: ", pipelinex.__version__)

project_path = Path(__file__).resolve().parent

src_path = project_path / "src"
src_path_str = str(src_path)

if src_path_str not in sys.path:
    sys.path.insert(0, src_path_str)

if "PYTHONPATH" not in os.environ:
    os.environ["PYTHONPATH"] = src_path_str

print("src path: ", src_path_str)


context = MLflowFlexibleContext(project_path)
context.run()
