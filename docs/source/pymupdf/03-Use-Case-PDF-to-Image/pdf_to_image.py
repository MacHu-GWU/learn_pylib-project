# -*- coding: utf-8 -*-

"""
Convert PDF to Image in Python

We use `pdf2image <https://pypi.org/project/pdf2image/>`_ library.

How to install ``pdf2image``:

First, you do ``pip install pdf2image``.

Then you install the poppler CLI, ``pdf2image`` uses poppler under the hood.

Mac:

- Install `poppler for Mac <https://macappstore.org/poppler/>`_
- do ``brew install poppler``
- use ``brew list poppler`` to figure out the poppler bin folder, on my computer it is ``/opt/homebrew/Cellar/poppler/22.08.0/bin/``

Linux (Redhat):

- Install poppler for Linux ``sudo yum install poppler-utils``
- Check it is installed ``yum list poppler-utils``
"""

import typing as T
from pathlib import Path
from pdf2image import convert_from_path


def pdf_to_image(
    path_pdf: Path,
    dir_images: Path,
    dpi: int = 144,
    fmt: str = "png",
    poppler_path: T.Optional[str] = None,
) -> T.List[Path]:
    """
    :param path_pdf: the path of input PDF
    :param dir_images: the directory of output images
    """
    images = convert_from_path(
        f"{path_pdf}",
        dpi=dpi,
        fmt=fmt,
        poppler_path=str(poppler_path) if poppler_path else None,
    )
    if not dir_images.exists():
        dir_images.mkdir(parents=True)
    output_paths = list()
    for page_num, image in enumerate(images, start=1):
        path_image = dir_images / f"page-{page_num}.{fmt}"
        output_paths.append(path_image)
        image.save(f"{path_image}")
    return output_paths


if __name__ == "__main__":
    # Sample PDF, W2 form: https://www.irs.gov/pub/irs-pdf/fw2.pdf
    dir_here = Path(__file__).absolute().parent
    path_pdf = dir_here / "w2.pdf"
    dir_images = dir_here / "output"
    dpi = 150
    fmt = "png"
    poppler_path = None
    pdf_to_image(
        path_pdf=path_pdf,
        dir_images=dir_images,
        dpi=dpi,
        fmt=fmt,
        poppler_path=poppler_path,
    )