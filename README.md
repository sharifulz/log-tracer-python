<<<<<<< HEAD

# Log Exception Extractor

This Python utility reads multiple log files, searches for exceptions, and generates a structured exception report.

---

## 📂 Project Structure

```
.
├── exception_log_report.py     # Main Python script
├── log_report_file.txt         # Output report (generated)
├── README.md                   # Documentation
├── *.log                       # Your log files
```

---

## ⚙️ Features

- Accepts multiple log file names via command-line arguments.
- Searches for lines containing `Exception`.
- Extracts the first line as exception type.
- Includes up to 20 lines of detailed context.
- Writes a formatted report for all files.

---

## 🔧 Prerequisites

- Python 3.x installed
- Log files present in the working directory

---

## 🧾 Get Matching Log Files

To list up to N log files matching a specific **prefix** and **extension**:

```bash
ls -1 trace-*.log | head -n 5
```

If no files appear, try loosening the pattern:

```bash
ls -1 *trace**.log | head -n 5
```

Or use `find`:

```bash
find . -maxdepth 1 -type f -name "trace-*.log" | head -n 5
```

---

## 🐍 Python Script Usage

### ✨ 1. Run the script:

```bash
python exception_log_report.py log1.log log2.log log3.log
```

You can pass up to N matching files from the previous step.

### 📦 Output:

- A `log_report_file.txt` is generated with structured exception info:
  ```
  File Name: log1.log
  Exception Type: java.lang.NullPointerException
  ----------------------------------------
  ----------------------------------------
  Details:
  ... (20 lines of stack trace)
  ```

---

## 🧠 Example Bash Execution

```bash
python exception_log_report.py $(ls -1 trace-*.log | head -n 5)
```

Make sure that:
- Filenames are correct
- You're in the right directory

---

## 🛠 Python Script Overview

### `exception_log_report.py`

```python
import sys

def extract_exceptions(file_path):
    exceptions = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        i = 0
        while i < len(lines):
            if 'Exception' in lines[i]:
                exception_start = i
                exception_type = lines[i].strip()
                details = []
                for j in range(i, min(i + 20, len(lines))):
                    details.append(lines[j].rstrip())
                    if lines[j].strip() == "":
                        break
                exceptions.append((file_path, exception_type, details))
                i = j
            else:
                i += 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return exceptions

def generate_report(exceptions, output_file="log_report_file.txt"):
    with open(output_file, 'w') as f:
        for file_name, exception_type, details in exceptions:
            f.write(f"File Name: {file_name}\n")
            f.write(f"Exception Type: {exception_type}\n")
            f.write("-" * 40 + "\n")
            f.write("-" * 40 + "\n")
            f.write("Details:\n")
            f.write("\n".join(details) + "\n")
            f.write("=" * 60 + "\n\n")
    print(f"Report written to {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python exception_log_report.py log1.txt log2.txt ...")
        sys.exit(1)

    all_exceptions = []
    for file_name in sys.argv[1:]:
        all_exceptions.extend(extract_exceptions(file_name))

    generate_report(all_exceptions)

if __name__ == "__main__":
    main()
```

---

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first to discuss.
=======
# log-tracer-python
>>>>>>> parent of 483f066 (use python to analyse log file)
