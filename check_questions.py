from pathlib import Path
import pandas as pd

df = pd.read_csv("check_questions.csv")

output = Path("Output")
# obi_bench = Path("obi-bench")

# list_out = []
# for question in output.glob("*"):
#     if question.is_dir():
#         list_out.append(question.name)

# list_obi_bench = []
# for question in obi_bench.glob("*"):
#     if question.is_dir():
#         list_obi_bench.append(question.name)

# for l in list_obi_bench:
#     if not (l in list_out):
#         print(l)

for question in output.glob("*"):
    if question.is_dir():
        nome = question.name
        
        gabarito = "x"
        
        test_cases = question / "test_cases"
        
        if test_cases.exists():
            gabarito = "ok"
        
        img = "x"
        imgs = question / "imgs"
        
        if imgs.exists():
            img = "ok"
        
        df.loc[df['question'] == nome, ['gabarito', 'img']] = [gabarito, img]
        df.to_csv("check_questions.csv", index=False, encoding='utf-8')

df = pd.read_csv("check_questions.csv")

counts = {
    "g": 0,
    "i": 0,
}

for indice, linha in df.iterrows():
    
    if linha['gabarito'] == "ok":
        counts['g'] += 1
    else:
        print(f"{linha['question']} sem gabarito")
    
    if linha['img'] == "ok":
        counts['i'] += 1

total = len(df)
print("Número de questões: ", total)
print(f"Com gabarito: {counts['g']} | Sem gabarito: {total - counts['g']}")
print(f"Com imagens: {counts['i']} | Sem imagens: {total - counts['i']}")