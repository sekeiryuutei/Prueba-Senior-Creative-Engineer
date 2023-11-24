from email.message import EmailMessage
import smtplib

def enviar_correo():
    remitente = "sendmailphp05@gmail.com"
    destinatario = "vburbano@live.com"
    mensaje = "Hola, este es un correo de prueba desde Python."

    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Email de prueba22"
    email.set_content(mensaje)

    smtp = None

    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(remitente, "vomw ilai qqde cbzv")
        smtp.sendmail(remitente, destinatario, email.as_string())
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        if smtp:
            smtp.quit()

if __name__ == '__main__':
    enviar_correo()
