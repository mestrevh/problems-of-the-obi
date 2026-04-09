from pathlib import Path
import pandas as pd

df = pd.read_csv("check_questions.csv")

output = Path("Output")

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

        print("CSV atualizado com sucesso!")
    
df = pd.read_csv("check_questions.csv")

counts = {
    "g": 0,
    "i": 0,
}

for indice, linha in df.iterrows():
    
    if linha['gabarito'] == "ok":
        counts['g'] += 1
    
    if linha['img'] == "ok":
        counts['i'] += 1

total = len(df)
print("Número de questões: ", total)
print(f"Com gabarito: {counts['g']} | Sem gabarito: {total - counts['g']}")
print(f"Com imagens: {counts['i']} | Sem imagens: {total - counts['i']}")