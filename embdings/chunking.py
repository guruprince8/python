import re
import PyPDF2
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tqdm import tqdm

with open("/Users/guru/Desktop/personal/US/Home Buying/Paystubs/2022/Form16_302318_2022.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    principles_of_ds = ''
    for page in tqdm(reader.pages):
        text = page.extract_text()
        print(text)
        principles_of_ds += '\n\n' + text[text.find(' ]') + 2:]


# principles_of_ds = principles_of_ds.strip()
# print(principles_of_ds)

def overlapping_chunks(text, max_tokens=500, overlapping_factor=5):
    sentences = re.split(r'[ ]', text)
    tokenizer = Tokenizer(BPE())
    print(tokenizer)
    chunks, tokens_so_far, chunk = [], 0, []
    # for sentence, token in zip(sentences, n_tokens):
    #     if tokens_so_far > max_tokens:
    #         chunks.append(". ".join(chunk) + ".")
    #         tokens_so_far = sum([len(tokenizer.encode(c)) for c in chunk])
    #     else:
    #         chunks = []
    #         tokens_so_far = 0
    #     if token > max_tokens:
    #         continue
    #     chunk.append(sentence)
    #     tokens_so_far += token + 1
    return chunks


split = overlapping_chunks(principles_of_ds, overlapping_factor=5)
#print(split)
#avg_length = sum([len(tokenizer.encode(t)) for t in split]) / len(split)
#print(f'non-overlapping chuncking approach has {len(split)} documents with average length {avg_length:.1f} tokens')
