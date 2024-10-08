class HeaderFooterCleaner:
    def remove_unwanted_lines(self, text):
        lines = text.split('\n')
        
        # Remove lines from the top until it sees '{'
        while lines and '{' not in lines[0]:
            lines.pop(0)
        
        # Remove lines from the bottom until it sees '}'
        while lines and '}' not in lines[-1]:
            lines.pop()
        
        return '\n'.join(lines)