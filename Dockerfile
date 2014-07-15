FROM temal/python

MAINTAINER Malte Krupa <dockerfile@nafn.de>

RUN apt-get update && apt-get install -y \
    pandoc \
    libfreetype6 \
    libfreetype6-dev \
    libatlas-base-dev \
    gfortran \
    octave \
    libzmq3-dev \
    epstool \
    xfig \
    libblas3

RUN pip install numpy scipy 
RUN pip install matplotlib Pygments oct2py ipython[notebook]

RUN groupadd -r ipython && \
    useradd -m -r -g ipython -s /sbin/nologin -c "ipython user" ipython && \
    mkdir /ipython && \
    chown -R ipython: /ipython

USER ipython
ENV HOME /home/ipython
RUN ipython profile create && \
    echo "c.FileNotebookApp.notebook_dir = u'/ipython'" >> \
    $HOME/.ipython/profile_default/ipython_notebook_config.py

RUN python -c \
    "from IPython.external import mathjax; mathjax.install_mathjax()"

VOLUME ["/ipython"]
EXPOSE 8888
WORKDIR /ipython

USER root
ADD ipython.py /ipython.py
RUN chmod +x /ipython.py

USER ipython
CMD /ipython.py
