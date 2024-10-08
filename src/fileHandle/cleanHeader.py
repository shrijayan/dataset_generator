class HeaderFooterCleaner:
    def __init__(self, first_line_remove_words=None, last_line_remove_words=None):
        self.first_line_remove_words = first_line_remove_words or ['Here', 'I', 'Based','```']
        self.last_line_remove_words = last_line_remove_words or ['Let', 'Note:', 'Please', 'If', '(Note:','```']

    def remove_unwanted_lines(self, text):
        lines = text.split('\n')
        
        # Remove lines from the top until it sees '{'
        while lines and '{' not in lines[0]:
            lines.pop(0)
        
        # Remove lines from the bottom until it sees '}'
        while lines and '}' not in lines[-1]:
            lines.pop()
        
        return '\n'.join(lines)