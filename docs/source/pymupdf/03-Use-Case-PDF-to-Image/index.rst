Use Case - PDF to Image
==============================================================================
有的时候我们希望在 PDF 上进行涂画, 然后给人类看 (例如用方框将重要元素框起来). 这时我们可以先将 PDF 转化为 PNG, 然后再用 `Python pillow <https://pillow.readthedocs.io/en/stable/>`_ 对图像进行修改. 本文给出了示例代码.

Sample Document (`W2 form from IRS <https://www.irs.gov/pub/irs-pdf/fw2.pdf>`_):

.. image:: https://github.com/MacHu-GWU/learn_pylib-project/assets/6800411/25807794-fa7a-4a71-b27b-be001096a69f

.. literalinclude:: ./pdf_to_image.py
   :language: python
   :linenos:
