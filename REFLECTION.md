# Question 1. Choose one test from the provided suite and name it. In plain English, what does that test confirm about your site? Then name one thing your site could get wrong that this test would not catch.
###### def test_url_available_by_name(self). This test confirms that the vairible is named 'name" in the views.py which is what is the table to list the what tasks you have to complete. I learned that changing the code line for views.py needs to say 'return render(request, "home.html", {"tasks": name})' where name is it directs to the table

# Question 2. You built three pages that share one navigation bar. If you added a fourth link to your navigation, how many files would you edit? How many would you have edited if you had not used base.html, and why?
###### you would of have to edit them all to direct to each page so 4 pages in the templates and than include it in the config --> settings.py part also it would be a nightmare, i enjoy the convience of the base.html having it in one spot.

