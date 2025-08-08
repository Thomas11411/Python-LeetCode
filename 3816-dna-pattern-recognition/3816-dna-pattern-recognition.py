import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    result = samples.copy()
    result["has_start"] = list(map(lambda x: int(x[0:3] == "ATG"), samples.dna_sequence))
    result["has_stop"] = list(map(lambda x: int(x[-3:] in {"TAA", "TAG", "TGA"}), samples.dna_sequence))
    result["has_atat"] = list(map(lambda x: int("ATAT" in x), samples.dna_sequence))
    result["has_ggg"] = list(map(lambda x: int("GGG" in x or "GGGG" in x), samples.dna_sequence))
    return result