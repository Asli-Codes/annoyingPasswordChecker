import re
import string

forbiddenWords =[
    "password",
    "sifre",
    "şifre",
    "ŞİFRE",
    "Şifre"
    "Sifre"
    "qwerty",
    "admin",
    "123456",
    "2026"
]

easySequences = [
    "123",
    "234",
    "345",
    "456",
    "567",
    "678",
    "789",
    "abc",
    "bcd",
    "cde",
    "xyz"
]

def hasRepeatedPattern(password):
    passwordLower = password.lower()

    #Örnek: sifresifre,abcabc
    for patternLength in range(2, (len(passwordLower)// 2) + 1):
        pattern = passwordLower[:patternLength]

        if pattern * (len(passwordLower) // patternLength) == passwordLower:
            return True

    # Şifrenin herhangi bir yerinde 3+ karakterlik bir bölüm arka arkaya tekrar ediyor mu?
    repeatedPattern = re.search(r"(.{3,)\1", passwordLower)

    return repeatedPattern is not None

def hasUppercase(password):
    return any(character.isupper() for character in password)

def hasLowercase(password):
    return any(character.islower() for character in password)

def hasDigit(password):
    return any(character.isdigit() for character in password)

def hasSpecialCharacter(password):
    return any(character in string.punctuation  for character in password)

def containsEasySequence(password):
    passwordLower = password.lower()

    return any(word in passwordLower for word in forbiddenWords)

def hasTripleCharacter(password):
    for index in range(len(password) - 2):
        if(
            password[index]
            == password[index + 1]
            == password[index + 2]
        ):
            return True
    return False

def calculateDigitSum(password):
    return sum(
        int(character)
        for character in password
        if character.isdigit()
    )


def getDifferentSpecialCharacters(password):
    specialCharacters = {
        character
        for character in password
        if character in string.punctuation
    }

    return len(specialCharacters)


def hasRepeatedNonAdjacentLetter(password):
    passwordLower = password.lower()

    for index, character in enumerate(passwordLower):
        if not character.isalpha():
            continue

        for secondIndex in range(index + 2, len(passwordLower)):
            if passwordLower[secondIndex] == character:
                return True

    return False


def containsForbiddenWord(password):
    pass


def validatePassword(password):

    # 1
    if len(password) < 10:
        return False, (
            "🤏 **Bu kadar mı?**\n\n"
            "Ben şifre istedim, Wi-Fi adı değil.\n\n"
            "**En az 10 karakter kullanmalısın.**"
        )

    # 2
    if hasRepeatedPattern(password):
        return False, (
            "🔁 **Aynı şeyi tekrar yazınca daha güvenli olmuyor.**\n\n"
            "`sifresifre` taktiğini gördüm. Güzel deneme."
        )

    # 3
    if not hasUppercase(password):
        return False, (
            "🔠 **Büyük harfler sana ne yaptı?**\n\n"
            "En az **1 büyük harf** ekle."
        )

    # 4
    if not hasLowercase(password):
        return False, (
            "🔡 Tamamen büyük harfle bağırmana gerek yok.\n\n"
            "En az **1 küçük harf** kullan."
        )

    # 5
    if not hasDigit(password):
        return False, (
            "🔢 Sayıları unutmuşuz.\n\n"
            "En az **1 rakam** ekle."
        )

    # 6
    if not hasSpecialCharacter(password):
        return False, (
            "✨ Biraz karakter katalım.\n\n"
            "En az **1 özel karakter** kullan: `! @ # $ %` gibi."
        )

    # 7
    if containsForbiddenWord(password):
        return False, (
            "🚨 **Çok tahmin edilebilir.**\n\n"
            "`password`, `sifre`, `qwerty`, `admin`, `2026` "
            "gibi ifadeler burada yasak."
        )

    # 8
    if containsEasySequence(password):
        return False, (
            "🧐 `123`, `456`, `abc` falan mı?\n\n"
            "Ben görmeyeceğim sandın galiba.\n\n"
            "**Kolay sıralamalar kullanamazsın.**"
        )

    # 9
    if hasTripleCharacter(password):
        return False, (
            "😐 Aynı karakteri üç kere yazmak biraz fazla.\n\n"
            "`aaa`, `111`, `!!!` gibi tekrarlar yasak."
        )

    # 10
    if password[0].isdigit():
        return False, (
            "☝️ Yeni bir isteğim var.\n\n"
            "**Şifren rakamla başlayamaz.**"
        )

    # 11
    if password[-1] in string.punctuation:
        return False, (
            "🙂 Tam oluyordu...\n\n"
            "Ama şifren **özel karakterle bitemez.**"
        )

    # 12
    digitSum = calculateDigitSum(password)

    if digitSum <= 10:
        return False, (
            f"➕ Şifrendeki rakamların toplamı **{digitSum}**.\n\n"
            "Ben en az **11** istiyorum.\n\n"
            "Evet, bunu da kontrol ediyorum."
        )

    # 13
    differentSpecialCharacters = getDifferentSpecialCharacters(password)

    if differentSpecialCharacters < 2:
        return False, (
            "🎭 Tek bir özel karakter bana yetmedi.\n\n"
            "En az **2 farklı özel karakter** kullan.\n\n"
            "Örneğin: `!` ve `#`."
        )

    # 14
    if password[0].lower() == password[-1].lower():
        return False, (
            "👀 İlk ve son karakterinin aynı olduğunu gördüm.\n\n"
            "**Onları da farklı yap.**"
        )

    # 15
    if not hasRepeatedNonAdjacentLetter(password):
        return False, (
            "🧩 Son bir şey...\n\n"
            "Şifrende aynı harften en az **iki tane** olsun,\n"
            "ama **yan yana olmasınlar**.\n\n"
            "Neden mi? Çünkü öyle istiyorum."
        )

    return True, (
        "✅ **TAMAM.**\n\n"
        "Gerçekten başardın.\n\n"
        "Şifren tüm gereksiz derecede zor kuralları geçti.\n\n"
        "**Şimdi bunu hatırlamak senin problemin.** 😌"
    )