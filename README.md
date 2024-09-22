# mongodb-hybrid-search-langchain


```
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": ,
      "similarity": "cosine"
    }
  ]
}
```


Create Search Index for Full Text Atlas Search

{
  "mappings": {
    "dynamic": false,
    "fields": {
      "text": [{
        "type": "string"
      }]
    }
  }
}