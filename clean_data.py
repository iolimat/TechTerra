import re

def remove_extra_spaces_and_lines(text):
    """Remove extra spaces and lines from the text"""
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = re.sub(r'[\r\n]+', ' ', cleaned_text)
    return cleaned_text

def remove_escape_characters(text):
    """Remove escape characters from the text"""
    escape_char_pattern = re.compile(r'[\n\r\t\b\f\v]')
    cleaned_text = escape_char_pattern.sub('', text)
    return cleaned_text

def clean_text(text):
    """Complete text cleaning pipeline"""
    cleaned_text = remove_extra_spaces_and_lines(text)
    cleaned_text = remove_escape_characters(cleaned_text)
    return cleaned_text