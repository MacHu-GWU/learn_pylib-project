# -*- coding: utf-8 -*-

import fitz
from pathlib import Path

def pdf_to_html(path_pdf: Path) -> Path:
	path_html = dir_here.joinpath(path_pdf.stem + ".html")
	doc = fitz.open(str(path_pdf))
	out = open(str(path_html), "wb") # create a text output
	for page in doc: # iterate the document pages
		text = page.get_text("xhtml").encode("utf8") # get plain text (is in UTF-8)
		out.write(text) # write text of page
		out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
	out.close()


if __name__ == "__main__":
	dir_here = Path(__file__).absolute().parent

	# path_pdf = dir_here / "Documentation-Best-Practices.pdf"
	path_pdf = dir_here / "PDF-to-HTML-Test.pdf"
	path_pdf = dir_here / "PyMuPDF-The-Basics.pdf"

	pdf_to_html(path_pdf)
