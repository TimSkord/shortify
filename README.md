# **Shortify**

A service for shortening links.

## **Startup Instructions:**

1. Make sure you have Docker and Docker-Compose installed correctly.
2. Clone the repository to your device and navigate to the project folder.
3. Run the command to build and run the project:
    ```bash
   sudo docker-compose up --build
   ```
4. Expect an infinitely long build load.
5. Congratulations, you are great, you can move on to the **Usage** section.

## **Usage**

### **Short link generation**
To generate a short link, just send a **POST** request in any convenient way to `http://yourhost:8000/` with the following body:
```json
{
    "full_url": "https://example.com" 
}
```

where `https://example.com` is your long link that you wish to shorten.

#### **Response**
```json
{
"id": 1,
"short_url": "c984",
"full_url": "https://example.com"
}
```

Here `"c984"` is your short link, don't lose it.

*If you request the same data again, the same shortcut will be returned to you.*

### **Redirect**
To follow your long link using a short link, you need to send a **GET** request to `http://yourhost:8000/` adding the received `short_url` to it, which would work like this:
```
http://yourhost:8000/c984/
```
This query will redirect your request to your long link.

### **Delete**
If you want to delete a link created earlier you can use the `http://yourhost:8000/c984` where `c984` is your `short_url` and send a **DELETE** request there.

## **Note**

*If you don't have time for manual testing you can use the file `test_main.http` beforehand replacing the link `https://example.com` with yours, and also replacing `c984` with the value obtained by **POST** request above.*