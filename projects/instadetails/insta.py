
# Import instaloader package
'''import instaloader

# creating an Instaloader() object
ig=instaloader.Instaloader()

# Taking the instagram username as input from user
usrname=input("Enter username:")

#Fetching the details of provided useraname using instaloder object
profile=instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details and storing the profile pic of that account
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username+" is having " + str(profile.followers)+' followers.')
print(profile.username+" is following " + str(profile.followees)+' people')
print("Bio: ", profile.biography)
instaloader.Instaloader().download_profile(usrname,profile_pic_only=True)# Import instaloader package'''
import instaloader

# Create an Instaloader() object
ig = instaloader.Instaloader()

# Taking the Instagram username as input from user
usrname = input("Enter username: ")

try:
    # Fetching the details of the provided username using instaloader object
    profile = instaloader.Profile.from_username(ig.context, usrname)

    # Printing the fetched details
    print("Username: ", profile.username)
    print("Number of Posts Uploaded: ", profile.mediacount)
    print(profile.username + " is having " + str(profile.followers) + ' followers.')
    print(profile.username + " is following " + str(profile.followees) + ' people')
    print("Bio: ", profile.biography)

    # Downloading the profile picture of the account
    ig.download_profile(usrname, profile_pic_only=True)
    print("Profile picture downloaded successfully.")

except instaloader.exceptions.ProfileNotExistsException:
    print("The profile does not exist.")
except instaloader.exceptions.ConnectionException:
    print("Failed to connect to Instagram. Please check your internet connection.")
except Exception as e:
    print(f"An error occurred: {e}")
