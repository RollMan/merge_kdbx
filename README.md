# merge_kdbx
# What's this?
This program merges multiple keepass 2.x databases exported in XML. The merged XML includes exclusive entries and last modified ones if two or more sources have an entry with the same title.

# Usage

```
python -m merge_kdbx [-hf] dst  [srcs ...]
```