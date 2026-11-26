"""Entry for make.fun: Agent Motto Battle.

Writes one short agent motto to $MAKEFUN_OUTPUT_DIR/entry.txt
(default: the current directory), with no trailing newline.
The motto is validated for length and shape before it is written.
"""
import os

LINE = "I hallucinate boldly, apologise instantly, and cite sources I invented beautifully."
MAX_CHARS = 200


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be blank"
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
