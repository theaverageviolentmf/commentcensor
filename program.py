import pyperclip

# Define the exact strings to prepend
PREPEND_NORMAL = "&#x202C;&#x202D;&#x202E; "
PREPEND_NBSP = "&#x202C;&#x202D;&#x202E;&nbsp; "

def process_segment(segment):
    if segment.endswith("-nbsp-"):
        segment = segment[:-6]  # Remove the "-nbsp-"
        prepend_string = PREPEND_NBSP
    else:
        prepend_string = PREPEND_NORMAL
    
    reversed_segment = segment[::-1]
    
    if reversed_segment.endswith(" "):
        reversed_segment = reversed_segment[:-1]  # Remove trailing space from reversed string

    return f"{prepend_string}{reversed_segment}"

def reverse_segments(text):
    segments = text.split('|')
    results = []
    
    for i, segment in enumerate(segments):
        if i % 2 == 1:
            # This is a segment to be reversed
            processed_segment = process_segment(segment)
            results.append(processed_segment)
        else:
            # This is a segment to remain in original order
            results.append(segment)
    
    return ''.join(results)

# Prompt the user for input
text = input("Thy sentence: \n")

# Process the text
translated_text = reverse_segments(text)

# Print the translated text
print("Translated Text:")
print(translated_text)

# Copy the translated text to the clipboard
pyperclip.copy(translated_text)
print("\nTranslated text has been copied to the clipboard.")
