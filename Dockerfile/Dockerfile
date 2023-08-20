# Set the base image
FROM conda/miniconda3
# Dockerfile author / maintainer 
MAINTAINER William H Thompson <hedley@startmail.com> 

RUN mkdir -p /app
WORKDIR /app

ENV DISPLAY :0
# Install tvc_benchmarker (and dependencies)
RUN conda install -c conda-forge cxx-compiler theano pygpu
RUN pip install "teneto==0.2.7b"
RUN pip install "seaborn==0.7.0"
RUN pip install tvc_benchmarker
RUN pip install "pybids==0.4.2"
RUN mkdir -p /root/.config/matplotlib
RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc 


CMD ["python","-m","tvc_benchmarker"]
