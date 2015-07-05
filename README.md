Fitbit
======

Python/Pandas/Scikit-learn utilities and wrappers for analyzing Fitbit files

Known Issues
------------

- Point your PYTHONPATH to the project root directory in your .bashrc:

		export PYTHONPATH=/path/to/root/Fitbit:$PYTHONPATH 

- Need to use Pandas 0.16.1 or higher. There was a bug in pandas.read_csv that
failed to handle blank lines in csv files.

- To update changes to fitbittools module from notebook use these two lines

```python
%load_ext autoreload
%autoreload 2
```

After you've run this once within a cell, you can comment out the first line.
