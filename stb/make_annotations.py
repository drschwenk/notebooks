import pdfextraction.ocr_pipeline
import pickle

with open('breakdowns.pkl', 'r') as f:
    book_breakdowns = pickle.load(f)

with open('pdfs/page_ranges.csv') as f:
    ranges = f.readlines()
range_lookup = {line.split(' ')[0]:[int(num) for num in line.strip().split(' ')[1:]] for line in ranges}

for tbt in book_breakdowns['daily_sci'][4:5]:
    pdfextraction.ocr_pipeline.perform_ocr(tbt, 'annotations', range_lookup[tbt])
