#download insta dp
import instaloader

ig = instaloader.Instaloader()
dp = input("Enter username account : ")

ig.download_profile(dp , profile_pic_only=True)
