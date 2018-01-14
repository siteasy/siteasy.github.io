{
    "date":"2017-08-24",
    "title": "Siteasy structure document"
}
# Structure

The basic structure of the siteasy looks like this

```
|_ articles                   //where you put your articles
|  |__category0
|  |  |__index.md             //define what your index of category0 looks like
|  |  |__article0.md
|  |  |__article1.md
|  |  |__article2.md
|  |__category1               //define what your index of category1 looks like
|  |  |__index.md
|  |  |__article0.md
|  |  |__article1.md
|  |  |__article2.md
|  |__index.md                //define what your index of whole site looks like
|- theme                      //can has several themes and select in config.json
|  |__default
|     |__base.html            //head and layout
|     |__detail.html          //used to parse articles
|     |__footer.html          //the footer of website. It is in every page.
|     |__header.html          //the header of website. It is in every page.
|     |__index.html           //the index of website or category
|     |__list.html            //If no index.md, then list all articles.
|     |__sider.html           //the sider of articles.
|     |__static               //static files of themes
|        |__css
|        |  |__main.css
|        |__js
|           |__main.js
|_ utils.py
|_ models.py
|_ siteasy.py
|_ config.json                //the global config file
```
Notes:  
- The index.md under articles defines the content of index of the site
- The index.md under categories defines the content of index of each category. If you don't put index.md in the category folder, then the list of articles will be the index of category.
- The category folder name can't be "index"

