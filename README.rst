scribbl
=======
scribbl is a command-line python script to download image-based
documents from scribd.com. 

Installation
------------

scribbl is supported on python >=3.5. The recommended way to install scribbl
is via `pip <https://pypi.python.org/pypi/pip>`_.

.. code-block:: bash

   pip install scribbl

Alternatively, you can clone the repository and run setup.py.

.. code-block:: bash

   cd scribbl && python setup.py install

Usage
-----
``python scribbl.py [-h] --id ID [--output OUTPUT]``

Options
~~~~~~~

.. code-block:: bash

  -h, --help       show this help message and exit
	--id ID          Document id to download
	--output OUTPUT  Filename output 

License
-------

scribbl's source is provided under the `MIT License
<https://github.com/kurd/scribbl/blob/master/LICENSE>`_.
