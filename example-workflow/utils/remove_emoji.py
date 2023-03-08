"""
Source: https://gist.github.com/Nikitha2309/15337f4f593c4a21fb0965804755c41d
"""
import re
import argparse

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='File path to clean emojis from. Will overwrite!')
    args = parser.parse_args()
    file_path = args.filepath
    
    with open(file_path,encoding="utf-8",errors="ignore") as f_in:
        input_text = f_in.read()
        
    cleaned_input_text = remove_emoji(input_text)
    with open(file_path,"w",encoding="utf-8") as f_out:
        f_out.write(cleaned_input_text)
    