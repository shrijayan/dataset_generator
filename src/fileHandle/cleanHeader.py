class HeaderFooterCleaner:
    def remove_unwanted_lines(self, text):
        jsonl_entries = text.split('\n')
        cleaned_entries = []

        for entry in jsonl_entries:
            lines = entry.split('\n')
            
            # Remove lines from the top until it sees '{'
            while lines and '{' not in lines[0]:
                lines.pop(0)
            
            # Remove lines from the bottom until it sees '}'
            while lines and '}' not in lines[-1]:
                lines.pop()
            
            cleaned_entries.append('\n'.join(lines))
        
        return '\n'.join(cleaned_entries)