"""Generate TP3 report PDF from a markdown-like text source."""

from pathlib import Path

from fpdf import FPDF


class ReportPDF(FPDF):
    """Simple PDF renderer with footer page numbers."""

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Helvetica", size=9)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")


def add_wrapped_line(pdf: ReportPDF, text: str) -> None:
    """Render one input line while preserving simple heading/list style."""
    stripped = text.strip()
    if stripped.startswith("# "):
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 16)
        pdf.multi_cell(170, 8, stripped[2:])
        pdf.ln(1)
        return
    if stripped.startswith("## "):
        pdf.ln(1)
        pdf.set_font("Helvetica", "B", 13)
        pdf.multi_cell(170, 7, stripped[3:])
        pdf.ln(0.5)
        return
    if stripped.startswith("### "):
        pdf.set_font("Helvetica", "B", 11)
        pdf.multi_cell(170, 6, stripped[4:])
        return
    if stripped == "---":
        pdf.ln(1)
        return

    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(170, 5.3, text)


def main() -> None:
    """Load report markdown and produce PDF in the same directory."""
    base = Path(__file__).resolve().parent
    source = base / "rapport_tp3.md"
    target = base / "rapport_tp3.pdf"

    content = source.read_text(encoding="utf-8")

    pdf = ReportPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_margins(18, 15, 18)

    for line in content.splitlines():
        add_wrapped_line(pdf, line)

    pdf.output(str(target))
    print(f"Generated: {target}")


if __name__ == "__main__":
    main()
