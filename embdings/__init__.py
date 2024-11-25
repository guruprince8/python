from sentence_transformers import SentenceTransformer

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"

model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-cos-v1')
docs = [
    "Around 9 million people live in London",
   ]
doc_emb = model.encode(docs, batch_size=32, show_progress_bar=True )
# print(doc_emb[0][0])
