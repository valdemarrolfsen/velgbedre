# -*- coding: UTF-8 -*-
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.core import urlresolvers


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
		msg.send()


	def send_welcome_mail(user, passord):
		subject = 'Velg Bedre - Ditt passord'
		text_content = 'Hei ' + user.firstname + '!\nDine personopplysninger er registrert! For at du senere skal kunne ha mulighet til å gå inn og redigere din ønskeliste har vi opprettet et passord du kan benytte til å logge inn.\n Ditt passord er: ' + passord + '\n For å logge inn til din profil gå til '
		html_content = '<h2>Hei ' +  user.firstname +'!</h2><h3>Dine personopplysninger er registrert!</h3><p>For at du senere skal kunne ha mulighet til å gå inn og redigere din ønskeliste har vi opprettet et passord du kan benytte til å logge inn.</p><p>Ditt passord er: <strong>' + passord + '</strong></p><p>For å logge inn til din profil gå til www.velgbedre.no/login</p>'
		Mail_sender.send_email(subject, user.email, text_content, html_content)