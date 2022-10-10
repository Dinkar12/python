#download insta dp
import instaloader

ig = instaloader.Instaloader()
dp = input("Enter the username of the account : ")

ig.download_profile(dp , profile_pic_only=True)
