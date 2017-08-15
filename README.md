# Tweet Me


Tweet Me has basic features of "Tweeter". This project is to learn and play around with Python Django framework, jQuery, and Bootstrap. This is my first Django project. Thus, below, I am attaching my daily project report so that I can share problems that I confronted and things that I learned. 



#### < TweetMe Daily Report >

##### - June 13, 2017
1. Django setup and setting

    ```ptrhon
    virtualenv -p python3 tweetme && cd tweetme
    source bin/activate
    mkdir src
    cd src
    pip freeze
    pip install django==1.10.3
    pip freeze
    django-admin.py startproject tweetme .
    ```

    -  Where manage.py is located is the root of django project
    -  https://github.com/codingforentrepreneurs/Guides/blob/master/all/Create_a_Local_Django_Project.md
    
##### - June 18, 2017
1. Django settings
    - Created settings folder under tweetme and added init, base, local, and production  files
    - local and production file basically overloads base file
    - setting.py from tweetme is copied and pasted to those newly created files (+ edit directory address) and deleted setting.py
    - add in init file. -> now runnable.

2. Serve static files
    *  https://docs.djangoproject.com/en/1.8/howto/static-files/
    *  created static-storage in the src folder
    * created static-serve file with src folder
    * edited static file setting in local.py
    * 
    ```python
    python manage.py collectstatic  
        You have requested to collect static files at the destination
        location as specified in your settings:
    
        /Users/PatriciaChun/Desktop/folder/code/tweetme/static-serve
    ```

    - Inside static-serve file, you can see admin files created.
    - when you collectstatic, it moves static files to static-serve
3. View function and templates
    * create views.py -> view convention. rendering home page.
    * change url.py and create home.html to render from views.py
4. Integrate Bootstrap
    * css, js files are static files. so we need to take care of them. 
    * files can be cached. CDN This is why storing static files is important.
    * after making changes in static files, python manage.py collect static
    * {% load static %}

##### - June 19, 2017
1. Build a TweetMe app.

    * django - easy to create user. Built-in user app.
    ```ptrhon
    python manage.py startapp tweets
    ```
    * build our own model models.py in tweets.
    * add this model ‘tweets’ in local.py (adding installed apps(installed components))
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```
    * Now you can find tweet model created in the admin with blank content fields.
2. Change fields in models

    * https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types
    * setting length limit or change model fields…etc
    * Why make migrations? because we changed models.py

3. Associate a user to a tweet with foreign keys
    * Foreign key connects different models together
    * https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types   -> find relationship fields
4. CRUD & first views
    * CRUD: create, retrieve, update, delete
    * create views for Retrieve in views.py and render with newly created html files
5. Query the database & context
    * In views.py
    * Create databases. One returns a list and one returns a single item.
    * render function combines the request, the template, and the context.
    * Context is really up to us.
    * context printed in the rendered html file using double curly brackets. {{}}
6. Template context basics
    * We are using function-based views.
    * However, class-based view is more convenient and takes out a lot of work we have to do in function-based views.
7. Class-based views

    * https://docs.djangoproject.com/en/1.11/ref/class-based-views/
    * In this video, we are replacing the function-based views with class-based views.
    * Class-based views accomplish same things.
8. Dynamic URL routing
    * This video talks about regular expression.
    * $: end of the expression
    * regular expression match a pattern or some way of how code is going to be work.
    * Regular expressions for URL
    * https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
    * function-based views doesn’t lead to 404 error if page not found. 
9. Validation
    *  Cleaning a specific field attribute
    *   https://docs.djangoproject.com/en/1.10/ref/contrib/admin/ 
10. Create view
    * CreateView & FormView
        * https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/
    * always test in incognito tab as well
    * form.user does not work. -> form.instance.user works.


##### - June 20, 2017
1. User needed & login required mixins
    * The loginrequired mixin
        * https://docs.djangoproject.com/en/1.11/topics/auth/default/
    * FormUserNeededMixin -> when not logged in, submitting a post will pop error that says you are not logged in
    * LoginRequiredMixin -> redirect to login page
2. Update view
    * Update view.
3. Delete view
    * Delete view
        * https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/
4. Reverse URLs
    * reverse
    * If there is no success_url, it automatically goes to absolute_url method in model.py
5. Advanced searching
    * complex lookups with q objects
        * https://docs.djangoproject.com/en/1.11/topics/db/queries/
6. Temperate inheritance
    * {% extends "base.html" %} simply mean parent template. 
    * {% block title %}Hello There{% endblock title %}
    * {{ block.super}}
7. Bootstrap media object for list view 
    * Media heading
        * http://getbootstrap.com/components/#media
    * CSS forms
        * http://getbootstrap.com/css/#forms
8. Bootstrap navbar
9. Bootstrap containers & columns 
    * 
    ```html
    <div class='row'>
        <div class ='col-sm-1' style='background-color:red;’>
    ```
    * 12 columns
##### - June 21, 2017

1. Tweet from Homepage
    * Redirect view
        * https://docs.djangoproject.com/en/1.11/ref/class-based-views/base/
2. Django crispy forms 
    * http://django-crispy-forms.readthedocs.io/en/latest/install.html
        * 
        ```
        pip install --upgrade django-crispy-forms
        ```
    * add installed app in base.py, local.py, and production.py so that they work at least similarly
    * add 
    ```python
    CRISPY_TEMPLATE_PACK = ‘bootstrap3’ in local.py
    ```
    * 
    ```python
    python manage.py migrate
    ```
3. Django Tests
    * test.py and then
        * 
        ```
        python manage.py test
        ```
    * joincfe.com/projects/django-test-unleashed
4. API with Django rest framework 
    * We want to make it more dynamic!
    * Ajax = asynchronized javascript request
    * for Ajax, set up APIs.
    * In our app, we have forms with validation. view that handles from validation and act as a storage. 
    * we will create serializer and another view for actual API.
    * Install django rest framework - 3rd party package. specially for API. 
    * joincfe.com/projects/django-rest-framework
    * Our goal here: we tweet, and we get the list of tweets.
    * install Django rest framework
        * 
        ```
        pip install djangorestframework
        ```
    * Add ‘rest_framework’ in installed app in local.py, base.py, production.py
5. API serializer & view 
    * ModelSerializer
        * http://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    * just like forms. 
    * but it helps us to display the data we need. also can validate the data.
    * GenericViews->ListAPIView
        * http://www.django-rest-framework.org/api-guide/generic-views/#listapiview 

##### - June 22, 2017

1. User display serializer
    * Now we have Tweet list API at api/tweet/ which is JSON data
    * goal here: create a new app
        * python manage.py startapp accounts
    * under accounts, create __init__.py and serializers.py
    *  Filling out serializers.py, add accounts app in setting files. (user serializers)
    * And then add new serializers to tweet’s serializers.
    * Then, we find updated tweet list api. (account info specified. )
##### - July 10, 2017

1. Ajax list view 
    * Jquery is a library of Javascript
        * http://api.jquery.com/jquery.ajax/
    * selector


2. jQuery search
    * https://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript/901144#901144
##### - July 11, 2017
1. Ajax & create API view 
    * CreateAPIView
        * http://www.django-rest-framework.org/api-guide/generic-views/#createapiview
    
2. Date display 
    * Now we want to change ordering. -> newest tweet on the top
    * Model manager is another way you can do.  
        * https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

3. Attach Tweet & Empty form

4. Counting characters 
    * selector
    * monitor the edit. 
    * depending on condition, we change the class. 
    * validation
    * max length. 
##### - July 17, 2017

1. Auto search 
    * timeout. last thing you type, it will release. 

2. Pagination & Ajax load more
    * disadvantage now: this list. all the tweets come up. we one small set. and ;let it load. -> pagination
    * multiple pages - pagination.
        * http://www.django-rest-framework.org/api-guide/pagination/#modifying-the-pagination-style
    * now you can check count variable.
    * updated fetch tweet function to go based off of url.
    * whatever the url in the results from the database
    * once we grab url, we do by actual button #(‘loadmore') and 

3. User detail view 
    * build user profile. 1. user name follow button and unfollow button
        * https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
    * get_slug_field()
        * https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/
##### - July 18, 2017       
1. Profile URL and API Update 
    * We are going to use UserDisplayializer to include url
    * we already did follower_count one

2. User Profile & Followers 
    * We are going to create user profile. it will include users that we are following. 
    
    
##### - July 19, 2017
1. Model Manager for Following 
    * we have to actually update 
2. Toggle Follow 
    * https://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#view
 
3. Model Manager for Follow Toggle 
    * Update model manager to have a few new method. one is checking if user is following other users.second one is doing the toggle with actual process. 
    * The reason why we created toggle_follow() and is_following() is that later we can use these in any view.
##### - July 20, 2017
1. Signals 
    * need signal that if user is created, check user profile is created. 
    * post_save: signal that is sent at the end of save method. 
        * https://docs.djangoproject.com/en/1.11/ref/signals/#post-save


2. Signal Tests 
    * We want to specifically test UserProfile function.
    * python manage.py test 

3. Display Following Tweets 
4. jQuery Hashtag 
    * We have to update our tweet list to include our own tweet. Tweets of the user is missing currently. 

5. Hashtags App 
    * we are going to create a new app for hashtag
    * python manage.py startapp hashtags  
    * python manage.py makemigrations   
    * python manage.py migrate      
##### - July 21, 2017
1. Retweet Part 1 
    * we are gonna do retweet. copy from original. 1 top tweet and a bunch of tweet below it that are coming from the top tweet. 
    * after changing model, we need to make migration and migrate.
    * create is_retweet
##### - July 22, 2017
1. Retweet Part 3 
    * prevent retweet happening if this already happened.
    * not allowing to retweet today. but after that day, you can retweet everyday.
    * pip install pytz

2. Retweet Part 4 with jQuery 
    * http://www.django-rest-framework.org/api-guide/views/

3. Parse Username & Hashtag with Python Regex 
    * Highlighting user with @.
    * Python regular expression. 
##### - July 23, 2017
1. Custom Django Signal 
    * https://docs.djangoproject.com/en/1.11/topics/signals/#defining-signals
##### - July 24, 2017
1. Tweet List Loading Everywhere 
    * update Tweet list to have our javascript located in different place.so that we can user it anywhere. 

2. User Tweets API Endpoint 

3. Like Tweet 
    * like button on out tweet
    * create the click function for it. 

4. Display Likes & Verb 
    * update serializer to show the liked account to a given model.

5. jQuery Attach Tweet Refactor 
    * create reply tweet
    
##### - July 25, 2017

1. Display Reply Tweet & Fix Likes 

bug with migration………fixed.
    * https://stackoverflow.com/questions/36053014/no-such-column-after-adding-a-field-to-the-model
2. A Form in a Bootstrap Modal 
    * Modals - live demo
      * http://getbootstrap.com/javascript/#modals
    * from id to class => $(#blah) to $(.blah)
3. Do the Reply 
4. Single Detail Tweet 
    * do fetch for individual tweet
   
##### - July 27, 2017
1. Search Tweets & Users 
    * update search. render some sort of list. 

2. Hashtag Tweet List 

3. Recommended Users & Custom Template Tags 
    * https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags

4. Registration & Auth 
    * https://docs.djangoproject.com/en/1.10/topics/auth/default/#all-authentication-views
    * getbootstrap.com/css/#forms
    * https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#formview


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
