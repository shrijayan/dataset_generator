class Clean_Headers_Footers:
    def __init__(self, text):
        self.text = text
    def clean_up_questions(self):
        first_line_remove_words = ['Here', 'I']
        last_line_remove_words = ['Let', 'Note:', 'Please', 'If', '(Note:']
        lines = self.text.split('\n')
        if any(lines[0].startswith(word) for word in first_line_remove_words):
            lines = lines[1:]
        if any(lines[-1].startswith(word) for word in last_line_remove_words):
            lines = lines[:-1]
        return '\n'.join(lines)