FROM python:3.8-slim

# Install
RUN pip install --no-cache-dir spacy ginza pandas ja_ginza

WORKDIR /MyMorphologicalAnalysis

COPY setup.sh /setup.sh
RUN chmod +x /setup.sh

COPY . /MyMorphologicalAnalysis

ENTRYPOINT ["/setup.sh"]
CMD ["/bin/bash"]