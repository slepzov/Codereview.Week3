import json
import smtplib
from email.message import EmailMessage
import ssl


def send_email(json_file: json) -> None:

    try:
        data = json.load(json_file)
        name = data["name"]
        result = data["result"]
        email_receiver = data["email"]

        email_sender = "test.python.viktor@gmail.com"
        email_password = "tlzhwjzkgdvzlqbu"

        subject = "Результат вашего теста"
        body = f"Привет, {name}, твой результат: {result}"

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    except Exception as ex:
        print(ex)
        print("Не удалось отправить письмо")


if __name__ == "__main__":

    # создаем json-файл
    dictData = {"name": "Артем",
                "email": "slepzov@yandex.ru",
                "result": 24.5}
    jsonData = json.dumps(dictData)

    with open("data.json", "w") as file:
        file.write(jsonData)

    # открываем json-файл и вызываем нашу функцию
    with open("data.json", "r", encoding="UTF-8") as file:
        send_email(file)
