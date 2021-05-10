url = ["www.annauniv.edu"," www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]
def top_level_domain(url_list): 
    return url_list.split('.')[-1] 
  
sorted_url = sorted(url,key=top_level_domain) 
print(sorted_url)