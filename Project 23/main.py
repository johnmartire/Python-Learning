import random
import schedule
import time
from plyer import notification
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Bible verses
bible_verses = [
    "John 3:16 - For God so loved the world that He gave His one and only Son, that whoever believes in Him shall not perish but have eternal life.",
    "Romans 8:28 - And we know that in all things God works for the good of those who love Him, who have been called according to His purpose.",
    "Matthew 6:33 - But seek first the kingdom of God and His righteousness, and all these things will be added to you.",
    "Philippians 4:13 - I can do all things through Christ who strengthens me.",
    "2 Timothy 1:7 - For God has not given us a spirit of fear, but of power, love, and a sound mind.",
    "1 Corinthians 16:14 - Let all that you do be done in love.",
    "James 1:2-3 - Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds, because you know that the testing of your faith produces perseverance.",
    "Ephesians 2:8-9 - For it is by grace you have been saved, through faith—and this is not from yourselves, it is the gift of God—not by works, so that no one can boast.",
    "Hebrews 11:1 - Now faith is the substance of things hoped for, the evidence of things not seen.",
    "1 John 4:7 - Beloved, let us love one another, for love is from God, and whoever loves has been born of God and knows God.",
    "2 Corinthians 5:7 - For we walk by faith, not by sight.",
    "Romans 12:2 - Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God's will is—His good, pleasing, and perfect will.",
    "Matthew 11:28 - Come to me, all you who are weary and burdened, and I will give you rest.",
    "Luke 6:31 - Do to others as you would have them do to you.",
    "Galatians 5:22-23 - But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, and self-control.",
    "1 Peter 5:7 - Cast all your anxiety on Him because He cares for you.",
    "Colossians 3:23 - Whatever you do, work at it with all your heart, as working for the Lord, not for human masters.",
    "John 14:27 - Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid.",
    "Acts 4:12 - Salvation is found in no one else, for there is no other name under heaven given to mankind by which we must be saved.",
    "Revelation 21:4 - He will wipe every tear from their eyes. There will be no more death or mourning or crying or pain, for the old order of things has passed away.",
    "Matthew 5:14 - You are the light of the world. A town built on a hill cannot be hidden.",
    "Matthew 5:16 - Let your light shine before others, that they may see your good deeds and glorify your Father in heaven.",
    "Matthew 7:7 - Ask, and it will be given to you; seek, and you will find; knock, and the door will be opened to you.",
    "Matthew 22:37-39 - Love the Lord your God with all your heart and with all your soul and with all your mind. This is the first and greatest commandment. And the second is like it: Love your neighbor as yourself.",
    "Mark 11:24 - Therefore I tell you, whatever you ask for in prayer, believe that you have received it, and it will be yours.",
    "Luke 1:37 - For with God nothing shall be impossible.",
    "Luke 12:31 - But seek His kingdom, and these things will be given to you as well.",
    "John 1:1 - In the beginning was the Word, and the Word was with God, and the Word was God.",
    "John 8:12 - I am the light of the world. Whoever follows me will never walk in darkness, but will have the light of life.",
    "John 14:6 - Jesus answered, 'I am the way, the truth, and the life. No one comes to the Father except through me.'",
    "John 15:5 - I am the vine; you are the branches. If you remain in me and I in you, you will bear much fruit; apart from me, you can do nothing.",
    "Acts 20:35 - It is more blessed to give than to receive.",
    "Romans 5:8 - But God demonstrates His own love for us in this: While we were still sinners, Christ died for us.",
    "Romans 10:9 - If you declare with your mouth, 'Jesus is Lord,' and believe in your heart that God raised Him from the dead, you will be saved.",
    "1 Corinthians 10:13 - No temptation has overtaken you except what is common to mankind. And God is faithful; He will not let you be tempted beyond what you can bear.",
    "2 Corinthians 12:9 - My grace is sufficient for you, for my power is made perfect in weakness.",
    "Galatians 6:9 - Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up.",
    "Ephesians 3:20 - Now to Him who is able to do immeasurably more than all we ask or imagine, according to His power that is at work within us.",
    "Ephesians 4:2 - Be completely humble and gentle; be patient, bearing with one another in love.",
    "Philippians 1:6 - Being confident of this, that He who began a good work in you will carry it on to completion until the day of Christ Jesus.",
    "Colossians 3:2 - Set your minds on things above, not on earthly things.",
    "1 Thessalonians 5:16-18 - Rejoice always, pray continually, give thanks in all circumstances; for this is God’s will for you in Christ Jesus.",
    "2 Timothy 3:16 - All Scripture is God-breathed and is useful for teaching, rebuking, correcting, and training in righteousness.",
    "Hebrews 4:12 - For the word of God is alive and active. Sharper than any double-edged sword, it penetrates even to dividing soul and spirit, joints and marrow; it judges the thoughts and attitudes of the heart.",
    "Hebrews 12:1 - Therefore, since we are surrounded by such a great cloud of witnesses, let us throw off everything that hinders and the sin that so easily entangles. And let us run with perseverance the race marked out for us.",
    "James 4:8 - Draw near to God, and He will draw near to you.",
    "1 Peter 2:9 - But you are a chosen people, a royal priesthood, a holy nation, God’s special possession, that you may declare the praises of Him who called you out of darkness into His wonderful light.",
    "1 Peter 5:8 - Be alert and of sober mind. Your enemy the devil prowls around like a roaring lion looking for someone to devour.",
    "1 John 1:9 - If we confess our sins, He is faithful and just and will forgive us our sins and purify us from all unrighteousness.",
    "Revelation 3:20 - Here I am! I stand at the door and knock. If anyone hears my voice and opens the door, I will come in and eat with that person, and they with me."
]


# Function to get a random verse
def get_random_verse():
    return random.choice(bible_verses)

# Function to send a notification
def send_notification():
    verse = get_random_verse()
    notification.notify(
        title="Daily Bible Verse",
        message=verse,
        app_name="BibleVerseApp",
        timeout=10
    )

# Schedule a daily notification at 8 AM
schedule.every().day.at("08:00").do(send_notification)

# Kivy App UI
class BibleVerseApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.verse_label = Label(text=get_random_verse(), font_size=20)
        new_verse_btn = Button(text="New Verse", size_hint=(1, 0.2))
        new_verse_btn.bind(on_press=self.update_verse)

        layout.add_widget(self.verse_label)
        layout.add_widget(new_verse_btn)

        return layout

    def update_verse(self, instance):
        self.verse_label.text = get_random_verse()

# Run background scheduler
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start the app
if __name__ == "__main__":
    BibleVerseApp().run()
