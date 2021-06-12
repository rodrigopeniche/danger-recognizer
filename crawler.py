import requests

# retrieves subreddit all posts within the provided time range from Pushshift API
def getSubPosts(sub, time_range):
    url = 'https://api.pushshift.io/reddit/search/submission/?subreddit=' + sub + '&sort=desc&sort_type=created_utc&after=' + time_range[0]  + '&before=' + time_range[1] + '&size=1000'
    r = requests.get(url).json()
    print(sub, len(r))
    return r

# retrieves all posts images urls given a Pushshift api response object
def getSubImgUrls(json):
    imgs = []
    data = json['data']
    for element in data:
        try:
            imgs.append(element['preview']['images'][0]['source']['url'].replace('amp;s', 's'))
        except:
            pass
    return imgs

# write urls into text files
def writeUrlsIntoFile(imgs, flag):
    pos_name = 'pos_imgs.txt'
    neg_name = 'neg_imgs.txt'
    with open(pos_name if flag else neg_name, "a") as text_file:
        for element in imgs:
            text_file.write(element + "\n")

# positive subreddits
pos_subs = []
# negative subreddits
neg_subs = []

# list of 2 elements lists, both a unix timestamp for start and end date respectively
time_ranges = []
time_ranges.append(['1590642436', '1622178436'])
time_ranges.append(['1527544336', '1559080336'])
time_ranges.append(['1496008336', '1527544336'])
time_ranges.append(['1464472336', '1496008336'])
time_ranges.append(['1432849936', '1464472336'])
time_ranges.append(['1401563041', '1433099041'])
time_ranges.append(['1370047436', '1401563041'])
time_ranges.append(['1338511436', '1370047436'])
time_ranges.append(['1306889036', '1338511436'])
time_ranges.append(['1275353036', '1306889036'])


with open('pos_subreddits.txt') as file:
    pos_subs = file.readlines()

with open('neg_subreddits.txt') as file:
    neg_subs = file.readlines()

# iterates over all time ranges, so every subreddit in the subreddit's list will be queried for every time range
for range in time_ranges:
    for (p_sub, n_sub) in zip(pos_subs, neg_subs):
        p_data = getSubPosts(p_sub.replace('\n', ''), range)
        p_imgs = getSubImgUrls(p_data)
        try:
            writeUrlsIntoFile(p_imgs, True)
        except:
            pass
        n_data = getSubPosts(n_sub.replace('\n', ''), range)
        n_imgs = getSubImgUrls(n_data)
        try:
            writeUrlsIntoFile(n_imgs, False)
        except:
            pass
