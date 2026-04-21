import re

def clean_text(text):
    # --- Remove ManualsLib header patterns ---
    text = re.sub(r"Manualslib\.com.*?\n", "", text, flags=re.IGNORECASE)
    text = re.sub(r"- The Global Manuals Library.*?\n", "", text, flags=re.IGNORECASE)

    # --- Remove navigation-like junk words ---
    text = re.sub(r"\b(Manuals|Brands|Accessories|PDF)\b", "", text, flags=re.IGNORECASE)

    # --- Normalize spacing ---
    text = re.sub(r"\n+", "\n", text)        # multiple newlines → single
    text = re.sub(r"[ \t]+", " ", text)      # multiple spaces → single

    # --- Remove weird symbol-only lines ---
    text = re.sub(r"^[\-/| ]+$", "", text, flags=re.MULTILINE)

    # --- Remove duplicate lines ---
    lines = text.split("\n")
    seen = set()
    unique_lines = []

    for line in lines:
        line = line.strip()
        if line and line not in seen:
            unique_lines.append(line)
            seen.add(line)

    # --- Remove very short useless lines ---
    cleaned_lines = []
    for line in unique_lines:
        if len(line) <= 2:
            continue
        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    return text