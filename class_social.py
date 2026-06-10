class SocialMedia:   

    CEO = "Mark"

    def like(self):
        print("Liked")

    def comment(self):
        print("Commented")

facebook = SocialMedia()
print( facebook.CEO )
facebook.like()
twitter = SocialMedia()
twitter.CEO = "Elon Musk"

print(facebook.CEO)
print(twitter.CEO)

Insta = SocialMedia()
LinkedIn = SocialMedia()
Twitter = SocialMedia()

print( Insta.CEO )
print( LinkedIn.CEO )
print( Twitter.CEO )