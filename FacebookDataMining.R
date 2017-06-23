library(Rfacebook)
library(RCurl)
#######################
# Authenticate R App with app ID and app Secret
# to get a app_id and app_secret, sign up here: https://developers.facebook.com/ and "Add a New App"
# Under settings, toggle "Client OAuth Login", "Web OAuth Login", and "Force Web OAuth Reauthentication" to YES
# Set Valid OAuth redirect URIs to: https://localhost:1410/
fb_oauth <- fbOAuth(app_id="****", app_secret="****",extended_permissions = TRUE) # Change '****' to your registered App credentials
######################

# Check autheticated users
me <- getUsers("me",token=fb_oauth, private_info=TRUE)
me$name

#Returns recent facebook likes of defined user in parameter
likes = getLikes(user="me", token = fb_oauth)
sample(likes$names, 10)

# Testing function that updates fbook status from R
updateStatus("This is a fbook status update test initiated from R...", token=fb_oauth)

#######################
#######################

# Mining facebook pages and their posts

#######################
#######################

# Search all fbook pages with defined keyword String and limit to 200 pages, return top 6 results
pages <- searchPages( string="trump", token=fb_oauth, n=200)
head(pages$name)

# Get fbook posts from a specific page within a specific timeframe
page <- getPage("bbcnews", token=fb_oauth, n=150, since='2016/06/01', until='2017/06/23')

# Get post from previous page that has the most likes
summary = page[which.max(page$likes_count),]
summary$message # prints the post

# Get post from previous page that has the most comments
summary1 = page[which.max(page$comments_count),]
summary1$message # prints the post

# Get post from previous page that was shared the most
summary2 = page[which.max(page$shares_count),]
summary2$message # prints the post

# Look at the post that got the most likes from the page and return the first 2000 users that liked it
post <- getPost(summary$id[1], token=fb_oauth, comments = FALSE, n.likes=2000)
likes <- post$likes
head(likes) # print the first 6 users that liked the post with their user IDs (encrypted for privacy)

#######################
#######################

# Facebook Comment Analysis

#######################
#######################
# Get top post from previous page and return top 1000 comments from it
post <- getPost(page$id[1], token=fb_oauth, n.comments=1000, likes=FALSE)
comments <- post$comments
# View(comments) # shows top 1000 comments from the post
comments[which.max(comments$likes_count),] # prints what comment got the most likes from the post

# Look at the most common first names from the users that made comments on the post
comments.df <- data.frame(comments)
commentNames <- data.frame(do.call('rbind', strsplit(as.character(comments.df$from_name), ' ', fixed=TRUE)))
commentNames <- subset(commentNames, select = c(X1,X2))
colnames(commentNames) <- c("First_Name", "Last_Name")
head(sort(table(commentNames$First_Name), dec=TRUE), n=3) # prints results

# Look at the first post from the previous page and return the counts of user reactions
post <- getReactions(post=page$id[1], token=fb_oauth)
colnames(post) <- c("Post_ID", "Likes_Count", "Love_Count", "Haha_Count", "Wow_Count", "Sad_Count", "Angry_Count")
print(post) # prints data

#######################
#######################

# Facebook Group Analysis

#######################
#######################

# Get a list of all facebook user groups with defined keywords
ids <- searchGroup(name="DataScience", token=fb_oauth)
head(ids) # prints top 6 facebook groups with "Data Science" in their name

# Get top 25 posts from the 2nd user group (Note: closed groups do not work)
group <- getGroup(group_id=ids[2,]$id, token=fb_oauth, n=25) 
post1 <- getPost(group$id[1], token=fb_oauth, n.comments=14, likes=FALSE)
comments2 <- post1$comments
comments2[which.max(comments2$likes_count),] # prints what comment has the most likes


