import sys

def extract_exceptions(file_path):
    exceptions = []
    try:
        with open(file_path, encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            if any(keyword in lines[i] for keyword in [
                'GenericJDBCException', 
                'SQLGrammarException',
                'ConstraintViolationException'
            ]):
                # Start of exception
                exception_start = i
                exception_type = lines[i].strip()
                details = []

                # Collect up to 60 lines of the exception details
                for j in range(i, min(i + 60, len(lines))):
                    details.append(lines[j].rstrip())
                    if lines[j].strip() == "":
                        break
                exceptions.append((file_path, exception_type, details))
                i = j  # Skip ahead
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
