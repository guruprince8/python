from transformers import pipelines
from transformers import pipeline

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"

def classify_text(email):
    classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
    labels = ['spam', 'not spam']
    hypothesis_template = 'This email is {}'
    results = classifier(email, labels, hypothesis_template=hypothesis_template)
    print(results)
    return results['labels'][0]


text = "Please send the address ship to goods"
email_classification = classify_text(text)
print(email_classification)
