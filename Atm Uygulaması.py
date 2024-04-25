class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Yeni bakiyeniz: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Yetersiz bakiye!"
        else:
            self.balance -= amount
            return f"Yeni bakiyeniz: {self.balance}"

    def check_balance(self):
        return f"{self.owner} adlı kullanıcının bakiyesi: {self.balance}"


def main():
    # Örnek bir hesap oluşturalım
    account = BankAccount("Önder", 1000)

    while True:
        print("\nATM Uygulamasına Hoş Geldiniz!")
        print("1. Bakiye Sorgulama")
        print("2. Para Yatırma")
        print("3. Para Çekme")
        print("4. Çıkış")

        choice = input("Lütfen bir işlem seçin (1/2/3/4): ")

        if choice == "1":
            print(account.check_balance())
        elif choice == "2":
            amount = float(input("Yatırmak istediğiniz tutarı girin: "))
            print(account.deposit(amount))
        elif choice == "3":
            amount = float(input("Çekmek istediğiniz tutarı girin: "))
            print(account.withdraw(amount))
        elif choice == "4":
            print("Güle güle!")
            break
        else:
            print("Geçersiz işlem! Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()

