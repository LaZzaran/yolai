import http.client
import ssl

# SSL doğrulamasını devre dışı bırak
context = ssl._create_unverified_context()
conn = http.client.HTTPSConnection("linkedin-api8.p.rapidapi.com", context=context)

payload = "{\"urn\":\"7245786832909557760\",\"page\":1,\"paginationToken\":\"\"}"

headers = {
    'x-rapidapi-key': "61145145dbmsh38cdde1b99f16eap16c852jsn74192ef291ab",
    'x-rapidapi-host': "linkedin-api8.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/posts/reposts", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
