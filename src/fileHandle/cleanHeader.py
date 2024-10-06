class HeaderFooterCleaner:
    def __init__(self, first_line_remove_words=None, last_line_remove_words=None):
        self.first_line_remove_words = first_line_remove_words or ['Here', 'I', 'Based','```']
        self.last_line_remove_words = last_line_remove_words or ['Let', 'Note:', 'Please', 'If', '(Note:','```']

    def remove_unwanted_lines(self, text):
        lines = text.split('\n')
        if any(lines[0].startswith(word) for word in self.first_line_remove_words):
            lines = lines[1:]
        if any(lines[-1].startswith(word) for word in self.last_line_remove_words):
            lines = lines[:-1]
        return '\n'.join(lines)
