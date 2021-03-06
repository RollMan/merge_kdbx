# merge_kdbx
# What's this?
This program merges multiple keepass 2.x databases exported in XML. The merged XML includes exclusive entries and last modified ones if two or more sources have an entry with the same title.

# Install

```
pip install merge-kdbx
```

# Usage

```
usage: merge_kdbx.py [-h] [-f] dst srcs [srcs ...]

positional arguments:
  dst          path to destination xml files.
  srcs         paths to source xml file to be merged.

optional arguments:
  -h, --help   show this help message and exit
  -f, --force  permit overwriting source file by dst.
```

Then you can import the generated XML into new and empty kdbx database. Existing entries should be removed before import as shown in the below figure.
![Empty kdbx database](https://raw.githubusercontent.com/RollMan/merge_kdbx/master/docs/_media/empty_kdbx.png "Empty database is recommended to import the generated XML.")