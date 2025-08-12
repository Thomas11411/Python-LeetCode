import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    special = ["\\", " ", "@", "-", "/", "^", ","]
    special_big = [" ", "-"]

    def new_text(x):
        res = ""
        for i, v in enumerate(x):
            
            if v in special:
                res += v
            elif v.isalpha:
                if i == 0:
                    res += v.upper()
                    continue
                
                if x[i - 1] in special: 
                    if x[i - 1] in special_big:
                        res += v.upper()
                    else:
                        res += v.lower()
                    
                else: res += v.lower()
        return res

    user_content["converted_text"] = user_content["content_text"].apply(new_text)
    user_content = user_content.rename(columns = {"content_text": "original_text"})

    return user_content.rename(columns={'content_text': 'original_text'})  