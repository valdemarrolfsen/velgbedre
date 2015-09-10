from django.core.mail import EmailMultiAlternatives, EmailMessage


class Mail_sender:


    #This class is for sending different types of mail.

    def send_email(subject, to_email, content, html_content):
        from_email = ''
        msg = EmailMultiAlternatives(subject, content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    def send_no_html(subject, to_email, content):
        from_email = ''
        msg = EmailMessage(subject, content , from_email, [to_email])
        #msg.send()


    def send_cat_request(email):
        subject = 'Noen har etterspurt katalog'
        text_content = 'Følgende har etterspurt en katalog \n Epost: ' + email
        html_content = '<h2>Følgende har etterspurt en katalog</h2><p>Epost: ' + email + '</p>'
        Mail_sender.send_email(subject, 'hei@velgbedre.no', text_content, html_content)

