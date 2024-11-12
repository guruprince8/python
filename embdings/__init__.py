from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-cos-v1')
docs = [
    "Around 9 million people live in London",
   ]
doc_emb = model.encode(docs, batch_size=32, show_progress_bar=True )
# print(doc_emb[0][0])
