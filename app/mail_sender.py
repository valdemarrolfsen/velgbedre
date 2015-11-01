from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string

class Mail_sender:


    #This class is for sending different types of mail.

    def send_email(subject, to_email, content, html_content):
        from_email = 'Velg Bedre <valdemar@velgbedre.no>'
        msg = EmailMultiAlternatives(subject, content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    def send_no_html(subject, to_email, content):
        from_email = ''
        msg = EmailMessage(subject, content , from_email, [to_email])
        #msg.send()

    def send_wish_mail(email, to_name, from_name):
        subject = 'Dette ønsker jeg meg'
        content = 'Tull'
        html_content = render_to_string('emails/standardEmail.html', {
            'title' : 'Hei ' + to_name,
            'header' : 'Jeg ønsker meg gave fra velg bedre',
            'small_text' : "I år ønsker jeg meg en bedre verden til jul. Jeg ønsker meg et gavekort fra Velg Bedre, som lar meg velge en ting jeg trenger og bygge en bedre verden samtidig. Følg denne linken for å se hvilket gavekort jeg ønsker meg.<br><br>Med vennlig hilsen,<br>" + from_name,
            'url_link' : '/packages/'
            })
        Mail_sender.send_email(subject, email, content, html_content)


    def send_cat_request(email):
        subject = 'Noen har etterspurt katalog'
        text_content = 'Følgende har etterspurt en katalog \n Epost: ' + email
        html_content = '<h2>Følgende har etterspurt en katalog</h2><p>Epost: ' + email + '</p>'
        Mail_sender.send_email(subject, 'hei@velgbedre.no', text_content, html_content)

