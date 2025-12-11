# JDF Sample Test

This project contains a minimal sample of a Job Definition Format (JDF) file and a simple Python script to validate its basic structure.

## Files

- `sample.jdf`: A sample JDF XML file describing a simple product job (e.g., a flyer), including a Resource Pool and Resource Link Pool.
- `test_jdf.py`: A Python script that parses `sample.jdf` and verifies the existence of standard JDF attributes (ID, Status, Type, Version).

## How to Run

1.  Ensure you have Python installed.
2.  Open a terminal in this directory.
3.  Run the test script:

    ```bash
    python3 test_jdf.py
    ```

## Expected Output

You should see output similar to:

```text
Testing JDF file: sample.jdf
Root Element: JDF
JDF ID: JDF_Sample_001
Status: Waiting
Type:   Product
Version:1.3
Success: JDF structure appears valid for a basic check.
```
