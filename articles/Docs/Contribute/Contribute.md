{
    "date":"2017-09-05",
    "title": "Contribute to siteasy"
}
# Function description
The base function of siteasy is to generate a context and use it to render the static html files with theme.

The context need to include,
- logo 
```json
    {"logo":text}
```
- header 
```json
    {"header":[{"text":cate_text, "url":cate_url},{"text":cate_text, "url":cate_url}...]}
```
- site_map
```json
    {"site_map": [{"id":cate_id, "text":cate_text, "url":cate_url, "selected":true/false, "sub": sub_site_map}]}
```
- md_content
```json
    {"md_content":md_content}
```

