import itertools

def cryptarithm_solver(equation):
    """
    Genel bir kriptaritmetik problemi çözer.
    Parametre:
        equation (str): Kriptaritmetik denklem, örneğin: "SEND + MORE == MONEY"
    Dönüş:
        list: Tüm geçerli çözümleri içeren liste.
    """
    # Harfleri tespit et
    letters = set(filter(str.isalpha, equation))
    if len(letters) > 10:
        raise ValueError("En fazla 10 farklı harf kullanılabilir.")
    
    # Tüm olası rakam eşlemelerini oluştur
    digits = range(10)
    solutions = []

    # İlk harflerin sıfır olamayacağını kontrol etmek için
    first_letters = {word[0] for word in equation.replace("==", "").replace("+", "").split() if word.isalpha()}
    
    for perm in itertools.permutations(digits, len(letters)):
        # Harfleri rakamlarla eşle
        substitution = dict(zip(letters, perm))
        
        # İlk harf sıfır ise geçersiz çözüm
        if any(substitution[letter] == 0 for letter in first_letters):
            continue
        
        # Denklemi çözmeyi dene
        translated_equation = equation
        for letter, digit in substitution.items():
            translated_equation = translated_equation.replace(letter, str(digit))
        
        # Denklemi değerlendirin
        try:
            if eval(translated_equation):
                solutions.append((translated_equation, substitution))
        except:
            continue

    return solutions

# Kullanıcıdan denklem alma
if __name__ == "__main__":
    print("Lütfen çözmek istediğiniz kriptaritmetik denklemini girin (örn: SEND + MORE == MONEY):")
    user_input = input("Denklem: ").strip()
    
    try:
        results = cryptarithm_solver(user_input)
        if results:
            print(f"{len(results)} çözüm bulundu:")
            for idx, (solution, mapping) in enumerate(results, start=1):
                print(f"{idx}. Çözüm: {solution} | Harf Eşleme: {mapping}")
        else:
            print("Hiçbir çözüm bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")
