# mongodb-hybrid-search-langchain


## Installation of the Repo

Make sure that you have rye installed then:
  
```bash
rye sync
```

or with pip:
  
```bash
pip install -r requirements.lock
```


## Atlas Search Setup JSONs


Create a Vector Search Index

```json
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
```json
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
```