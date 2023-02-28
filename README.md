# Flask_blog


This is a simple Flask blog that retrieves blog posts from a JSON API and displays them on the home page. Users can click on a blog post to view its full content on a separate page.

Getting Started
To run the Flask blog, follow these steps:

Clone the repository to your local machine
Start the Flask app by running python main.py
Navigate to http://localhost:8000/ in your browser to view the home page

Usage
The home page displays a list of blog post titles and subtitles. Clicking on a post title will take you to the full post page where you can read the entire post.

Dependencies
The Flask blog requires the following dependencies:

Flask
requests
datetime
These dependencies are included in the requirements.txt file and can be installed using pip.

API

The Flask blog retrieves blog posts from a JSON API located at https://api.npoint.io/12cf49c647dc25d43d41. The API returns a list of blog post objects that include a unique ID, a title, and a subtitle. The Flask blog uses the requests library to make a GET request to the API and retrieve the blog post data.

