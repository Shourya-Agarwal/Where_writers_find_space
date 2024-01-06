# Where_writers_find_space
1. Login or sign up for the website.
2. View other's posts or create your posters with your quotes/short stories.
3. You can download the posters made on the website and/or can post on the platform.

Working-
The quotes written go through a method called removing-stopwords where the text/quote is filtered by removing punctuations & stop-words. After this, a clear list of keywords is obtained.
This list of keywords is used for getting the emotion and image-scrapping using the web-automation tool Selenium. This brings to the user a list of images based on his/her emotions written via quote/text.
Now the user has the choice of choosing the most suitable image for his text. Moreover, the images are next cleaned via another method to remove background text and present a clean image to the user.
Further, the user has many customization options to decorate the text on the image. Lastly, the user can download/post the hence-developed poster.

The poster once posted gets stored in the backend SQLite database.
