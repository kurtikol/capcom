# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TaskPulse
def paginate(items, page_size=20):
    pages = []
    for start in range(0, len(items), page_size):
        pages.append(items[start:start + page_size])
    return pages

def get_page(pages, page_index):
    if 0 <= page_index < len(pages):
        return pages[page_index]
    return []

def get_page_number(pages, page_index):
    if 0 <= page_index < len(pages):
        return page_index + 1
    return 0
