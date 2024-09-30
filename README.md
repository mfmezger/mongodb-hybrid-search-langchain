# mongodb-hybrid-search-langchain


```
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 384, # you need to pick the right number of dimensions for your embeddings
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
