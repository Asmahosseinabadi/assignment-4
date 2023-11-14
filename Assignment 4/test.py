import instaloader 
import getpass

f=open("follower.txt","r")
old_followers=[]
for line in f:
    old_followers.append(line)

f.close()

f=open("instagram_new_follower.txt","r")
new_followers=[]
for line in f:
    new_followers.append(line)

f.close()



l=instaloader.Instaloader()

username=input("enter username:")
password=getpass.getpass("enter password")
l.login(username,password)
print("login successfully")

profile=instaloader.Profile.from_username(l.context,"asma")

new_followers=[]
for follower in profile.get_followers():
    new_followers.append(follower)


for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)

for instagram_new_follower in new_followers:
    if instagram_new_follower not in old_followers:
        print(instagram_new_follower)



f=open("followers.txt","w")
for follower in new_followers:
    f.write(follower + "\n")

f.close()


