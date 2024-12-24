# sv-parser
Demo repository for SystemVerilog parser based on tree-sitter-systemverilog

## Installation

Open the Linux bash terminal and type:

```bash
git submodule update --init --recursive

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install ./tree-sitter-systemverilog
```

## Usage

```bash
python3 parse-sv.py
```
