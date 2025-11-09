# Modrinth Downloader


Config file example: <br>
```
{
  "loader": "fabric", # The mod loader (defaults to Fabric)
  "version": "1.19.2, # The minecraft version (defaults to latest)
  "location": "test", # Where to store new mods (defaults to ./output)
  "delete": true, # Delete old files in the output directory?
  "modrinth": [ # Can contain either names or slugs (or a mix!)
     "LQ3K71Q1",
     "dynamic-fps"
  ]
}
```

### Tutorial on IDs & Names<br>
[![Watch the video]()](https://files.catbox.moe/zmv9nz.mp4)


Credits
* crosby: Crosby#9153 - Helped with a lot of stuff
* tympanicblock61 - Owner of original project
* midnightdoggo19 - Forking idiot