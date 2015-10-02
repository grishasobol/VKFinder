#coding=utf-8
import vk_auth
import vkontakte
import json
import time

(token,user_id) = vk_auth.auth('vk.finder@mail.ru', '123456789', '5054584', "photos")
vk = vkontakte.API(token=token)
print "Hello from VK API , server time is ",vk.getServerTime()

NUMBER_OF_GROUPS = 100
groupsFile = open("../groups.txt", "a")

groups = vk.get('groups.get', 
        extended = 0,
        count=NUMBER_OF_GROUPS
        )
print(groups)
time.sleep(0.3)

for group in range(len(groups)):
    print(groups[group])
    isAdded = 0
    howManyTimes = 0
    for num in range(10):
        try:
            message = vk.get('wall.search',
                owner_id = "-"+str(groups[group]),
                query = "репост подарки",
                count = 1, 
                offset = num
                )
            print(group, num)
            if len(message) > 1:
                print(message[1]["text"])
                isAdded += 1;
            if isAdded == 1 and howManyTimes < 1:
                groupsFile.write(str(groups[group])+"\n")
                print("writing done")
                howManyTimes = 1;
        except Exception as exc:
            print("Something wrong ", type(exc))
        

        time.sleep(0.35)

groupsFile.close()
