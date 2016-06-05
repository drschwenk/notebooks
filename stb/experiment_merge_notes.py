# coding: utf-8
"""overmerged, entire page a single block




"""
merge_params = {
    'near_x': 3.0,
    'near_y': 100.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 10.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'overlap_fract': 0.4 # seems to work well
#     'overlap_fract': 1.1 # turns off
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""



overmerged, entire page a single block
start_x had little effect



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 100.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 1.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'overlap_fract': 0.4 # seems to work well
#     'overlap_fract': 1.1 # turns off
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""



overmerged, entire page a single block
start_x had little effect



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 100.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 1.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'overlap_fract': 0.4 # seems to work well
#     'overlap_fract': 1.1 # turns off
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""



mildly overmerged, 



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 5.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 1.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'overlap_fract': 0.4 # seems to work well
#     'overlap_fract': 1.1 # turns off
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""



mildly overmerged, little change



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 4.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 1.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'overlap_fract': 0.4 # seems to work well
#     'overlap_fract': 1.1 # turns off
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""



mildly overmerged, no change on discussion block



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 3.5,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 1.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'overlap_fract': 0.4 # seems to work well
#     'overlap_fract': 1.1 # turns off
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""



This seems to work well, tentatively proceeding with this 



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 2.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 1.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'starting_near_near_y': 5.0,
    'overlap_fract': 0.4 # seems to work well
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""


Seems to work much better



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 5.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 1.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'starting_near_near_y': 8.0,
    'overlap_fract': 0.01
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
"""


Best yet, catches many offset lines caused by OCR false negatives



"""
merge_params = {
    'near_x': 3.0,
    'near_y': 3.0,
    'overlap_x': 0.8,
    'overlap_y': 0.6,
    'start_x': 5.0,
    'short_length': 1,
    'char_size_ratio': 0.4,
    'starting_near_near_y': 5.0,
    'overlap_fract': 0.2
}

book_breakdowns, page_ranges = load_book_info()
dest_path = './ai2-vision-turk-data/textbook-annotation-test/merged-annotations/'
for textbook in book_breakdowns['daily_sci'][1:]:
    merging_tool.merge_single_book(textbook, page_ranges[textbook], dest_path, merge_params)
