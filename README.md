# university

Програма, яка генерує випадковий пароль, шифрує його за допомогою шифрування AES-256 і зберігає у файлі.

Розберемо код по частинах:
Програма імпортує кілька модулів, включаючи os, sys, argparse, секрети та криптографію. argparse використовується для аналізу аргументів командного рядка, secrets використовується для генерації випадкових паролів, а криптографія використовується для шифрування AES-256.
Програма визначає три функції: generate_password, encrypt_password і save_password. generate_password генерує випадковий пароль вказаної довжини, encrypt_password шифрує пароль за допомогою шифрування AES-256, а save_password зберігає зашифрований пароль у файлі.
Основною функцією є точка входу в програму. Він аналізує аргументи командного рядка за допомогою argparse, зчитує ключ шифрування з файлу, генерує випадковий пароль, шифрує його, зберігає у файлі та друкує на консолі.
Програма виконується, лише якщо вона запускається як основний сценарій, перевіряючи змінну __name__.
Щоб запустити програму виконайте наступну команду в терміналі:

python3 password_gen.py -l 16 -k key.txt -o password.txt

Це створить випадковий пароль довжиною 16 символів, зашифрує його за допомогою ключа, що зберігається у файлі key.txt, і збереже його у файл password.txt. Згенерований пароль також буде надруковано на консолі.