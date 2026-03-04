from django.core.management.base import BaseCommand
from faqs.models import FAQ, FAQCategory

class Command(BaseCommand):
    help = 'Populates the FAQ model with default content.'

    def handle(self, *args, **options):
        faqs_data = [
            {
                "question": "How much does it cost to call the helpline 116?",
                "answer": "It is completely free to call 116 — you do not need airtime. Ensure your phone is charged and you have good network coverage."
            },
            {
                "question": "In which parts of the country do you work?",
                "answer": "We work all over the country because we receive calls from all over the country."
            },
            {
                "question": "How will my case get followed up and yet you are in Kampala and I am very far (up country/village)?",
                "answer": "We work with partners — government and non-government including LCs, Community development officers (CDOs), probation and social welfare officers (PSWOs), police, and community volunteers such as para social workers and VHTs. Assistance depends on the case reported."
            },
            {
                "question": "Who can call the helpline?",
                "answer": "Anyone, whether adult or child, with a case of child abuse or GBV can call the helpline. Both males and females are assisted accordingly."
            },
            {
                "question": "What does Sauti mean or why the name Sauti?",
                "answer": "Sauti is a Kiswahili word that means voice. It is easy for children to remember and signifies being the voice of the voiceless, especially children."
            },
            {
                "question": "What language should I speak when I call?",
                "answer": "Counsellors speak a variety of local languages. They may speak English, but you can request a local language of your choice."
            },
            {
                "question": "Where are your offices located?",
                "answer": "Our offices are located in Kireka at Kireka Rehabilitation Center in Wakiso district."
            },
            {
                "question": "When is the helpline open?",
                "answer": "The helpline works 24/7/365, all year round including public holidays, day and night."
            },
            {
                "question": "What if I want to report a case to you but I do not have a telephone, what should I do?",
                "answer": "Report the case to your LC, Community Development Officer, or Probation and Social Welfare Officer. If you are a child, ask an adult or neighbor to help you call or allow you to use their phone; remember it is free."
            },
            {
                "question": "Do you pay school fees for children?",
                "answer": "No. We do not pay school fees. We may help you look for an organisation that can offer support, or direct you to probation and social welfare officers to identify such support."
            },
            {
                "question": "Do you only work on girls and women issues?",
                "answer": "No. We work on all issues of child abuse (violence against children) regardless of whether it involves boys or girls, and we also handle GBV cases for men and women."
            },
            {
                "question": "Do you provide shelter and other basic needs to vulnerable children and families?",
                "answer": "No. We do not provide shelter or basic needs, but we work with organizations that do and can refer you to them. We may also direct you to local officers to identify such support."
            },
            {
                "question": "Do you arrest perpetrators?",
                "answer": "No. Arresting perpetrators is the role of the police. We work with the police if necessary, and we also offer counselling services to perpetrators if needed."
            },
            {
                "question": "Do you have regional offices/ how many branches does the helpline have?",
                "answer": "We have one national call centre. We do not have regional offices, but work with probation officers, LCs, community development officers and the police to assist people in various districts."
            },
            {
                "question": "Is there any other way of reporting cases apart from calling 116?",
                "answer": "Yes. You can report via U-report (SMS to 8500 for free), SafePal app (Google Play Store), Facebook (Sauti 116 Uganda Child Helpline), Email (uchl@mglsd.go.ug), walk to the centre in Kireka, or Twitter (@sauti116)."
            },
            {
                "question": "Will the person I have reported know that it is I who reported them?",
                "answer": "No. The helpline values confidentiality and never discloses the identity of the reporter to the abuser."
            },
            {
                "question": "How long will it take for my case to be worked on?",
                "answer": "Cases are unique and handled based on information provided and specific needs. There is no set standard time; you will receive feedback according to your case."
            },
            {
                "question": "What happens if abuse reoccurs after a case was solved and closed?",
                "answer": "Call the helpline and provide the new information; the case will be reopened."
            },
            {
                "question": "Is UCHL an organization, CBO, NGO or government?",
                "answer": "UCHL is a project in the Ministry of Gender, Labour and Social Development, delivered through partnerships between government, private sector and NGOs."
            },
            {
                "question": "What do I do if my call does not go through 116?",
                "answer": "Try again, walk to the offices if nearby, use local reporting systems (LC, police, probation officer, CDO), or leave a voicemail and we will call you back."
            },
            {
                "question": "Do people outside Uganda call 116?",
                "answer": "No. People outside Uganda cannot call 116, but they can reach the helpline via email, Facebook, Twitter or the SafePal app."
            },
            {
                "question": "How do I become a reporting agent for SAUTI and how do I benefit?",
                "answer": "There is no need to become an agent. You can tell others about Sauti and encourage them to use it. You benefit by knowing you helped improve someone’s life."
            }
        ]

        for i, faq_data in enumerate(faqs_data):
            faq_obj, created = FAQ.objects.update_or_create(
                question=faq_data['question'],
                defaults={
                    'answer': faq_data['answer'],
                    'language': FAQ.Language.ENGLISH,
                    'order': i + 1,
                    'is_active': True,
                    'views_count': 0,
                    'category': None, # No category specified in input
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created FAQ: {faq_data['question']}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Updated FAQ: {faq_data['question']}"))
