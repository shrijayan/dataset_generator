import json

class JSONLCleaner:
    def clean_entry(self, text):
        """Clean a single JSONL entry by finding valid JSON structure and ensuring it has 'question' and 'answer' keys"""
        brace_count = 0
        start_idx = -1
        end_idx = -1
        
        for i, char in enumerate(text):
            if char == '{':
                if brace_count == 0:
                    start_idx = i
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = i + 1
                    break
        
        if start_idx != -1 and end_idx != -1:
            json_str = text[start_idx:end_idx]
            try:
                json_obj = json.loads(json_str)
                if 'question' in json_obj and 'answer' in json_obj:
                    return json_str
            except json.JSONDecodeError:
                return None
        return None

    def clean_jsonl(self, text):
        """Clean entire JSONL file"""
        lines = text.splitlines()
        cleaned_lines = []
        
        for line in lines:
            if line.strip():  # Skip empty lines
                cleaned_entry = self.clean_entry(line)
                if cleaned_entry:
                    cleaned_lines.append(cleaned_entry)
        return '\n'.join(cleaned_lines)